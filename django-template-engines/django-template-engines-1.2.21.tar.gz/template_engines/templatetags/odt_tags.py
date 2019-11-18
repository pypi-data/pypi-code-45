import base64
import logging
import secrets
import random
import re
import requests

from bs4 import BeautifulSoup
from django import template
from django.utils.safestring import mark_safe

from template_engines.backends.utils_odt import ODT_IMAGE
from .utils import parse_tag, resize

register = template.Library()

logger = logging.getLogger(__name__)


def parse_p(soup):
    """ Replace p tags with text:p """
    paragraphs = soup.find_all("p")

    for p_tag in paragraphs:
        p_tag.name = 'text:p'
    return soup


def parse_italic(soup):
    """ Replace i tags with text:span with autmotatic style """
    italic_tags = soup.find_all("em")
    for i_tag in italic_tags:
        i_tag.name = 'text:span'
        i_tag.attrs['text:style-name'] = "ITALIC"
    return soup


def parse_strong(soup):
    """ Replace strong tags with text:span with autmotatic style """
    strong_tags = soup.find_all("strong")
    for s_tag in strong_tags:
        s_tag.name = 'text:span'
        s_tag.attrs['text:style-name'] = "BOLD"
    return soup


def parse_underline(soup):
    """ Replace u tags with text:span with automatic style """
    u_tags = soup.find_all("u")
    for u_tag in u_tags:
        u_tag.name = 'text:span'
        u_tag.attrs['text:style-name'] = "UNDERLINE"
    return soup


def fix_li(soup, tag):
    tag.name = 'text:list-item'
    contents = ''
    for e in tag.contents:
        # get tag content formatted (keep nested tags)
        contents = f'{contents}{e}'
    tag.string = ''
    content = soup.new_tag('text:p')
    content.attrs['text:style-name'] = "Standard"
    content.append(BeautifulSoup(contents, 'html.parser'))
    tag.append(content)


def parse_ul(soup):
    """ Replace ul / li tags text:list and text:list-item """
    ul_tags = soup.find_all("ul")

    for ul_tag in ul_tags:
        ul_tag.name = 'text:list'
        ul_tag.attrs['xml:id'] = f'list{str(random.randint(100000000000000000, 900000000000000000))}'
        ul_tag.attrs['text:style-name'] = "L1"
        li_tags = ul_tag.findChildren(recursive=False)

        for li in li_tags:
            fix_li(soup, li)

    return soup


def parse_ol(soup):
    """ Replace ol / li tags text:list and text:list-item """
    ol_tags = soup.find_all("ol")
    for ol_tag in ol_tags:
        ol_tag.name = 'text:list'
        ol_tag.attrs['xml:id'] = f'list{str(random.randint(100000000000000000, 900000000000000000))}'
        ol_tag.attrs['text:style-name'] = "L2"
        ol_tag.attrs['text:level'] = "1"
        li_tags = ol_tag.findChildren(recursive=False)

        for li in li_tags:
            fix_li(soup, li)
    return soup


def parse_a(soup):
    # replace a
    a_tags = soup.find_all("a")
    for a_tag in a_tags:
        a_tag.name = 'text:a'
        new_attrs = {
            'xlink:type': 'simple',
            'xlink:href': a_tag.attrs['href']
        }
        a_tag.attrs = new_attrs

    return soup


def parse_h(soup):
    # replace h*
    h_tags = soup.find_all(re.compile("^h[0-3]"))
    for h_tag in h_tags:
        num = h_tag.name[1]
        h_tag.name = 'text:h'
        new_attrs = {
            'text:outline-level': num
        }
        h_tag.attrs = new_attrs
    return soup


def parse_br(soup):
    # replace br
    br_tags = soup.find_all("br")
    for br_tag in br_tags:
        br_tag.name = 'text:line-break'
    return soup


@register.filter()
def from_html(value, is_safe=True):
    """ Convert HTML from rte fields to odt compatible format """
    soup = BeautifulSoup(value, "html.parser")
    soup = parse_p(soup)
    soup = parse_strong(soup)
    soup = parse_italic(soup)
    soup = parse_underline(soup)
    soup = parse_ul(soup)
    soup = parse_ol(soup)
    soup = parse_a(soup)
    soup = parse_h(soup)
    soup = parse_br(soup)
    return mark_safe(str(soup))


class ImageLoaderNodeURL(template.Node):
    def __init__(self, url, data=None, request=None, max_width=None,
                 max_height=None, anchor=None):
        # saves the passed obj parameter for later use
        # this is a template.Variable, because that way it can be resolved
        # against the current context in the render method
        self.url = url
        self.data = data
        self.request = request
        self.max_width = max_width
        self.max_height = max_height
        self.anchor = anchor

    def render(self, context):
        url, type_request, max_width, max_height, anchor, data = self.get_value_context(context)
        name = secrets.token_hex(15)
        response = self.get_content_url(url, type_request or "get", data)
        if not response:
            return ""
        width, height = resize(response.content, max_width, max_height, odt=True)
        context.setdefault('images', {})
        context['images'].update({name: response.content})
        return mark_safe(ODT_IMAGE.format(name, width, height, anchor or "paragraph"))

    def get_value_context(self, context):
        final_url = self.url.resolve(context)
        final_request = "get" if not self.request else self.request.resolve(context)
        final_max_width = None if not self.max_width else self.max_width.resolve(context)
        final_max_height = None if not self.max_height else self.max_height.resolve(context)
        final_anchor = "paragraph" if not self.anchor else self.anchor.resolve(context)
        final_data = "" if not self.data else self.data.resolve(context)
        return final_url, final_request, final_max_width, final_max_height, final_anchor, final_data

    def get_content_url(self, url, type_request, data):
        try:
            response = getattr(requests, type_request.lower())(url, data=data)
        except requests.exceptions.ConnectionError:
            logger.warning("Connection Error, check the url given")
            return
        except AttributeError:
            logger.warning("Type of request specified not allowed")
            return
        if response.status_code != 200:
            logger.warning("The picture is not accessible (Error: %s)" % response.status_code)
            return
        return response


@register.tag
def image_url_loader(parser, token):
    """
    Replace a tag by an image from the url you specified.
    The necessary key is url
    - url : Url where you want to get your picture
    Other keys : data, max_width, max_height, request
    - data : Use it only with post request
    - max_width : Width of the picture rendered
    - max_heigth : Height of the picture rendered
    - request : Type of request, post or get. Get by default.
    - anchor : Type of anchor, paragraph, as-char, char, frame, page
    """
    tag_name, args, kwargs = parse_tag(token, parser)
    usage = '{{% {tag_name} [url] max_width="5000" max_height="5000" ' \
            'request="GET" data="{{"data": "example"}}" anchor="as-char" %}}'.format(tag_name=tag_name)
    if len(args) > 1 or not all(key in ['max_width', 'max_height', 'request', 'data', 'anchor'] for key in kwargs.keys()):
        raise template.TemplateSyntaxError("Usage: %s" % usage)
    return ImageLoaderNodeURL(*args, **kwargs)


class ImageLoaderNode(template.Node):
    def __init__(self, object, max_width=None, max_height=None, anchor=None):
        # saves the passed obj parameter for later use
        # this is a template.Variable, because that way it can be resolved
        # against the current context in the render method
        self.object = object
        self.max_width = max_width
        self.max_height = max_height
        self.anchor = anchor

    def base64_to_binary(self, picture):
        if isinstance(picture, str) and 'base64' in picture:
            picture = base64.b64decode(picture.split(';base64,')[1])
        return picture

    def render(self, context):
        # Evaluate the arguments in the current context
        name = self.object
        picture, max_width, max_height, anchor = self.get_value_context(context)
        picture = self.base64_to_binary(picture)
        if not picture or not isinstance(picture, bytes):
            logger.warning("{object} is not a valid picture".format(object=name))
            return ""

        name = secrets.token_hex(15)
        width, height = resize(picture, max_width, max_height, odt=True)
        context.setdefault('images', {})
        context['images'].update({name: picture})
        return mark_safe(ODT_IMAGE.format(name, width, height, anchor))

    def get_value_context(self, context):
        final_object = self.object.resolve(context)
        final_max_width = None if not self.max_width else self.max_width.resolve(context)
        final_max_height = None if not self.max_height else self.max_height.resolve(context)
        final_anchor = "paragraph" if not self.anchor else self.anchor.resolve(context)
        return final_object, final_max_width, final_max_height, final_anchor


@register.tag
def image_loader(parser, token):
    """
    Replace a tag by an image you specified.
    You must add an entry to the ``context`` var that is a dict with at least a ``content`` key
    whose value is a byte object. You can also specify ``width`` and ``height``, otherwise it will
    automatically resize your image.
    The necessary key is image
    - image : content of your picture in binary or base64
    Other keys : max_width, max_height, anchor
    - max_width : Width of the picture rendered
    - max_heigth : Height of the picture rendered
    - anchor : Type of anchor, paragraph, as-char, char, frame, page
    """
    tag_name, args, kwargs = parse_tag(token, parser)
    usage = '{{% {tag_name} [image] max_width="5000" max_height="5000" anchor="as-char" %}}'.format(tag_name=tag_name)
    if len(args) > 1 or not all(key in ['max_width', 'max_height', 'anchor']
                                for key in kwargs.keys()):
        raise template.TemplateSyntaxError("Usage: %s" % usage)
    return ImageLoaderNode(*args, **kwargs)
