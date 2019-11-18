# -*- coding: utf-8 -*-
#
# Copyright (c), 2016-2019, SISSA (International School for Advanced Studies).
# All rights reserved.
# This file is distributed under the terms of the MIT License.
# See the file 'LICENSE' in the root directory of the present
# distribution, or http://opensource.org/licenses/MIT.
#
# @author Davide Brunato <brunato@sissa.it>
#
import os.path
import re
import codecs
from elementpath import iter_select, Selector, XPath1Parser

from .compat import (
    PY3, StringIO, BytesIO, string_base_type, urlopen, urlsplit, urljoin, urlunsplit,
    pathname2url, URLError, uses_relative
)
from .exceptions import XMLSchemaTypeError, XMLSchemaValueError, XMLSchemaURLError, XMLSchemaOSError
from .namespaces import get_namespace
from .qnames import XSI_SCHEMA_LOCATION, XSI_NONS_SCHEMA_LOCATION
from .etree import ElementTree, PyElementTree, SafeXMLParser, etree_tostring


DEFUSE_MODES = ('always', 'remote', 'never')


XML_RESOURCE_XPATH_SYMBOLS = {
    'position', 'last', 'not', 'and', 'or', '!=', '<=', '>=', '(', ')', 'text',
    '[', ']', '.', ',', '/', '|', '*', '=', '<', '>', ':', '(end)', '(name)',
    '(string)', '(float)', '(decimal)', '(integer)'
}


class XmlResourceXPathParser(XPath1Parser):
    symbol_table = {k: v for k, v in XPath1Parser.symbol_table.items() if k in XML_RESOURCE_XPATH_SYMBOLS}
    SYMBOLS = XML_RESOURCE_XPATH_SYMBOLS


XmlResourceXPathParser.build_tokenizer()


def is_remote_url(url):
    return isinstance(url, string_base_type) and urlsplit(url).scheme not in ('', 'file')


def url_path_is_directory(url):
    return os.path.isdir(urlsplit(url).path)


def url_path_is_file(url):
    return os.path.isfile(urlsplit(url).path)


def normalize_url(url, base_url=None, keep_relative=False):
    """
    Returns a normalized URL doing a join with a base URL. URL scheme defaults to 'file' and
    backslashes are replaced with slashes. For file paths the os.path.join is used instead of
    urljoin.

    :param url: a relative or absolute URL.
    :param base_url: the reference base URL for construct the normalized URL from the argument. \
    For compatibility between "os.path.join" and "urljoin" a trailing '/' is added to not empty paths.
    :param keep_relative: if set to `True` keeps relative file paths, which would not strictly \
    conformant to URL format specification.
    :return: A normalized URL.
    """
    def add_trailing_slash(x):
        return urlunsplit((x[0], x[1], x[2] + '/' if x[2] and x[2][-1] != '/' else x[2], x[3], x[4]))

    def filter_url(x):
        x = x.strip().replace('\\', '/')
        while x.startswith('//'):
            x = x.replace('//', '/', 1)
        while x.startswith('file:////'):
            x = x.replace('file:////', 'file:///', 1)
        if urlsplit(x).scheme in {'', 'file'}:
            x = x.replace('#', '%23')
        return x

    url = filter_url(url)

    if base_url is not None:
        base_url = filter_url(base_url)
        base_url_parts = urlsplit(base_url)
        base_url = add_trailing_slash(base_url_parts)
        if base_url_parts.scheme not in uses_relative:
            base_url_parts = urlsplit('file:///{}'.format(base_url))
        else:
            base_url_parts = urlsplit(base_url)

        if base_url_parts.scheme not in ('', 'file'):
            url = urljoin(base_url, url)
        else:
            url_parts = urlsplit(url)
            if url_parts.scheme not in ('', 'file'):
                url = urljoin(base_url, url)
            elif not url_parts.netloc or base_url_parts.netloc == url_parts.netloc:
                # Join paths only if host parts (netloc) are equal, using the os.path.join
                # instead of urljoin for path normalization.
                url = urlunsplit((
                    '',
                    base_url_parts.netloc,
                    os.path.normpath(os.path.join(base_url_parts.path, url_parts.path)),
                    url_parts.query,
                    url_parts.fragment,
                ))

                # Add 'file' scheme if '//' prefix is added
                if base_url_parts.netloc and not url.startswith(base_url_parts.netloc) and url.startswith('//'):
                    url = 'file:' + url

    url_parts = urlsplit(url, scheme='file')
    if url_parts.scheme not in uses_relative:
        normalized_url = 'file:///{}'.format(url_parts.geturl())  # Eg. k:/Python/lib/....
    elif url_parts.scheme != 'file':
        normalized_url = urlunsplit((
            url_parts.scheme,
            url_parts.netloc,
            pathname2url(url_parts.path),
            url_parts.query,
            url_parts.fragment,
        ))
    elif os.path.isabs(url_parts.path):
        normalized_url = url_parts.geturl()
    elif keep_relative:
        # Can't use urlunsplit with a scheme because it converts relative paths to absolute ones.
        normalized_url = 'file:{}'.format(urlunsplit(('',) + url_parts[1:]))
    else:
        normalized_url = urlunsplit((
            url_parts.scheme,
            url_parts.netloc,
            os.path.abspath(url_parts.path),
            url_parts.query,
            url_parts.fragment,
        ))
    return filter_url(normalized_url)


def fetch_resource(location, base_url=None, timeout=30):
    """
    Fetch a resource trying to accessing it. If the resource is accessible
    returns the URL, otherwise raises an error (XMLSchemaURLError).

    :param location: an URL or a file path.
    :param base_url: reference base URL for normalizing local and relative URLs.
    :param timeout: the timeout in seconds for the connection attempt in case of remote data.
    :return: a normalized URL.
    """
    if not location:
        raise XMLSchemaValueError("'location' argument must contains a not empty string.")

    url = normalize_url(location, base_url)
    try:
        resource = urlopen(url, timeout=timeout)
    except URLError as err:
        # fallback joining the path without a base URL
        url = normalize_url(location)
        try:
            resource = urlopen(url, timeout=timeout)
        except URLError:
            raise XMLSchemaURLError(reason=err.reason)
        else:
            resource.close()
            return url
    else:
        resource.close()
        return url


def fetch_schema_locations(source, locations=None, **resource_options):
    """
    Fetches the schema URL for the source's root of an XML data source and a list of location hints.
    If an accessible schema location is not found raises a ValueError.

    :param source: an Element or an Element Tree with XML data or an URL or a file-like object.
    :param locations: a dictionary or dictionary items with Schema location hints.
    :param resource_options: keyword arguments for providing :class:`XMLResource` class init options.
    :return: A tuple with the URL referring to the first reachable schema resource, a list \
    of dictionary items with normalized location hints.
    """
    base_url = resource_options.pop('base_url', None)
    timeout = resource_options.pop('timeout', 30)
    if not isinstance(source, XMLResource):
        resource = XMLResource(source, base_url, timeout=timeout, **resource_options)
    else:
        resource = source

    base_url = resource.base_url
    namespace = resource.namespace
    locations = resource.get_locations(locations)
    if not locations:
        msg = "the XML data resource {!r} does not contain any schema location hint."
        raise XMLSchemaValueError(msg.format(source))

    for ns, url in sorted(locations, key=lambda x: x[0] != namespace):
        try:
            return fetch_resource(url, base_url, timeout), locations
        except XMLSchemaURLError:
            pass

    raise XMLSchemaValueError("not found a schema for XML data resource {!r}.".format(source))


def fetch_schema(source, locations=None, **resource_options):
    """
    Fetches the schema URL for the source's root of an XML data source.
    If an accessible schema location is not found raises a ValueError.

    :param source: An an Element or an Element Tree with XML data or an URL or a file-like object.
    :param locations: A dictionary or dictionary items with schema location hints.
    :param resource_options: keyword arguments for providing :class:`XMLResource` class init options.
    :return: An URL referring to a reachable schema resource.
    """
    return fetch_schema_locations(source, locations, **resource_options)[0]


def fetch_namespaces(source, **resource_options):
    """
    Extracts namespaces with related prefixes from the XML data source. If the source is
    an lxml's ElementTree/Element returns the nsmap attribute of the root. If a duplicate
    prefix declaration is encountered then adds the namespace using a different prefix,
    but only in the case if the namespace URI is not already mapped by another prefix.

    :param source: a string containing the XML document or file path or an url \
    or a file like object or an ElementTree or Element.
    :param resource_options: keyword arguments for providing :class:`XMLResource` init options.
    :return: A dictionary for mapping namespace prefixes to full URI.
    """
    timeout = resource_options.pop('timeout', 30)
    return XMLResource(source, timeout=timeout, **resource_options).get_namespaces()


def load_xml_resource(source, element_only=True, **resource_options):
    """
    Load XML data source into an Element tree, returning the root Element, the XML text and an
    url, if available. Usable for XML data files of small or medium sizes, as XSD schemas.

    :param source: an URL, a filename path or a file-like object.
    :param element_only: if True the function returns only the root Element of the tree.
    :param resource_options: keyword arguments for providing :class:`XMLResource` init options.
    :return: a tuple with three items (root Element, XML text and XML URL) or \
    only the root Element if 'element_only' argument is True.
    """
    lazy = resource_options.pop('lazy', False)
    source = XMLResource(source, lazy=lazy, **resource_options)
    if element_only:
        return source.root
    else:
        source.load()
        return source.root, source.text, source.url


class XMLResource(object):
    """
    XML resource reader based on ElementTree and urllib.

    :param source: a string containing the XML document or file path or an URL or a file like \
    object or an ElementTree or an Element.
    :param base_url: is an optional base URL, used for the normalization of relative paths when \
    the URL of the resource can't be obtained from the source argument.
    :param defuse: set the usage of SafeXMLParser for XML data. Can be 'always', 'remote' or 'never'. \
    Default is 'remote' that uses the defusedxml only when loading remote data.
    :param timeout: the timeout in seconds for the connection attempt in case of remote data.
    :param lazy: if set to `False` the source is fully loaded into and processed from memory. \
    Default is `True` that means that only the root element of the source is loaded. This is \
    ignored if *source* is an Element or an ElementTree.
    """
    def __init__(self, source, base_url=None, defuse='remote', timeout=300, lazy=True):
        if base_url is not None and not isinstance(base_url, string_base_type):
            raise XMLSchemaValueError(u"'base_url' argument has to be a string: {!r}".format(base_url))

        self._root = self._text = self._url = None
        self._base_url = base_url
        self.defuse = defuse
        self.timeout = timeout
        self._lazy = lazy
        self.source = source

    def __str__(self):
        # noinspection PyCompatibility,PyUnresolvedReferences
        return unicode(self).encode("utf-8")

    def __unicode__(self):
        return self.__repr__()

    if PY3:
        __str__ = __unicode__

    def __repr__(self):
        if self._root is None:
            return u'%s()' % self.__class__.__name__
        elif self._url is None:
            return u'%s(tag=%r)' % (self.__class__.__name__, self._root.tag)
        else:
            return u'%s(tag=%r, basename=%r)' % (
                self.__class__.__name__, self._root.tag, os.path.basename(self._url)
            )

    def __setattr__(self, name, value):
        if name == 'source':
            self._root, self._text, self._url = self._fromsource(value)
        elif name == 'defuse' and value not in DEFUSE_MODES:
            raise XMLSchemaValueError(u"'defuse' attribute: {!r} is not a defuse mode.".format(value))
        elif name == 'timeout' and (not isinstance(value, int) or value <= 0):
            raise XMLSchemaValueError(u"'timeout' attribute must be a positive integer: {!r}".format(value))
        elif name == 'lazy' and not isinstance(value, bool):
            raise XMLSchemaValueError(u"'lazy' attribute must be a boolean: {!r}".format(value))
        super(XMLResource, self).__setattr__(name, value)

    def _fromsource(self, source):
        url = None
        if hasattr(source, 'tag') and hasattr(source, 'attrib'):
            self._lazy = False
            return source, None, None  # Source is already an Element --> nothing to load

        elif isinstance(source, string_base_type):
            _url, self._url = self._url, None
            try:
                if self._lazy:
                    # check if source is a string containing a valid XML root
                    for _, root in self.iterparse(StringIO(source), events=('start',)):
                        return root, source, None
                else:
                    return self.fromstring(source), source, None
            except (ElementTree.ParseError, PyElementTree.ParseError, UnicodeEncodeError):
                if '\n' in source:
                    raise
            finally:
                self._url = _url

            url = normalize_url(source) if '\n' not in source else None

        elif isinstance(source, StringIO):
            _url, self._url = self._url, None
            try:
                if self._lazy:
                    for _, root in self.iterparse(source, events=('start',)):
                        return root, source.getvalue(), None
                else:
                    return self.parse(source).getroot(), source.getvalue(), None
            finally:
                self._url = _url

        elif hasattr(source, 'read'):
            try:
                # Save remote urls for open new resources (non seekable)
                if is_remote_url(source.url):
                    url = source.url
            except AttributeError:
                pass

            _url, self._url = self._url, url
            try:
                if self._lazy:
                    for _, root in self.iterparse(source, events=('start',)):
                        return root, None, url
                else:
                    return self.parse(source).getroot(), None, url
            finally:
                self._url = _url

        else:
            # Try ElementTree object at last
            try:
                root = source.getroot()
            except (AttributeError, TypeError):
                pass
            else:
                if hasattr(root, 'tag'):
                    self._lazy = False
                    return root, None, None

        if url is None:
            raise XMLSchemaTypeError(
                "wrong type %r for 'source' attribute: an ElementTree object or an Element instance or a "
                "string containing XML data or an URL or a file-like object is required." % type(source)
            )
        else:
            resource = urlopen(url, timeout=self.timeout)
            _url, self._url = self._url, url
            try:
                if self._lazy:
                    for _, root in self.iterparse(resource, events=('start',)):
                        return root, None, url
                else:
                    return self.parse(resource).getroot(), None, url
            finally:
                self._url = _url
                resource.close()

    @property
    def root(self):
        """The XML tree root Element."""
        return self._root

    @property
    def text(self):
        """The XML text source, `None` if it's not available."""
        return self._text

    @property
    def url(self):
        """The source URL, `None` if the instance is created from an Element tree or from a string."""
        return self._url

    @property
    def base_url(self):
        """The base URL for completing relative locations."""
        return os.path.dirname(self._url) if self._url else self._base_url

    @property
    def document(self):
        """
        The resource as ElementTree XML document. It's `None` if the instance
        is lazy or if it's an lxml Element.
        """
        if isinstance(self.source, ElementTree.ElementTree):
            return self.source
        elif hasattr(self.source, 'getroot') and hasattr(self.source, 'parse'):
            return self.source  # lxml's _ElementTree
        elif not self._lazy and not hasattr(self.root, 'nsmap'):
            return ElementTree.ElementTree(self.root)

    @property
    def namespace(self):
        """The namespace of the XML resource."""
        return get_namespace(self._root.tag) if self._root is not None else None

    @staticmethod
    def defusing(source):
        """
        Defuse an XML source, raising an `ElementTree.ParseError` if the source contains entity
        definitions or remote entity loading.

        :param source: a filename or file object containing XML data.
        """
        parser = SafeXMLParser(target=PyElementTree.TreeBuilder())
        try:
            for _, _ in PyElementTree.iterparse(source, ('start',), parser):
                break
        except PyElementTree.ParseError as err:
            raise ElementTree.ParseError(str(err))

    def parse(self, source):
        """
        An equivalent of *ElementTree.parse()* that can protect from XML entities attacks.
        When protection is applied XML data are loaded and defused before building the
        ElementTree instance. The protection applied is based on value of *defuse*
        attribute and *base_url* property.

        :param source: a filename or file object containing XML data.
        :returns: an ElementTree instance.
        """
        if self.defuse == 'always' or self.defuse == 'remote' and \
                hasattr(source, 'read') and is_remote_url(self.base_url):

            if hasattr(source, 'read'):
                text = source.read()
            else:
                with open(source) as f:
                    text = f.read()

            if isinstance(text, bytes):
                self.defusing(BytesIO(text))
                return ElementTree.parse(BytesIO(text))
            else:
                self.defusing(StringIO(text))
                return ElementTree.parse(StringIO(text))
        else:
            return ElementTree.parse(source)

    def iterparse(self, source, events=None):
        """
        An equivalent of *ElementTree.iterparse()* that can protect from XML entities attacks.
        When protection is applied the iterator yields pure-Python Element instances.
        The protection applied is based on resource *defuse* attribute and *base_url* property.

        :param source: a filename or file object containing XML data.
        :param events: a list of events to report back. If omitted, only “end” events are reported.
        """
        if self.defuse == 'always' or self.defuse == 'remote' and \
                hasattr(source, 'read') and is_remote_url(self.base_url):

            parser = SafeXMLParser(target=PyElementTree.TreeBuilder())
            try:
                return PyElementTree.iterparse(source, events, parser)
            except PyElementTree.ParseError as err:
                raise ElementTree.ParseError(str(err))
        else:
            return ElementTree.iterparse(source, events)

    def fromstring(self, text):
        """
        An equivalent of *ElementTree.fromstring()* that can protect from XML entities attacks.
        The protection applied is based on resource *defuse* attribute and *base_url* property.

        :param text: a string containing XML data.
        :returns: the root Element instance.
        """
        if self.defuse == 'always' or self.defuse == 'remote' and is_remote_url(self.base_url):
            self.defusing(StringIO(text))
        return ElementTree.fromstring(text)

    def tostring(self, indent='', max_lines=None, spaces_for_tab=4, xml_declaration=False):
        """Generates a string representation of the XML resource."""
        elem = self._root
        namespaces = self.get_namespaces()
        return etree_tostring(elem, namespaces, indent, max_lines, spaces_for_tab, xml_declaration)

    def copy(self, **kwargs):
        """Resource copy method. Change init parameters with keyword arguments."""
        obj = type(self)(
            source=self.source,
            base_url=kwargs.get('base_url', self.base_url),
            defuse=kwargs.get('defuse', self.defuse),
            timeout=kwargs.get('timeout', self.timeout),
            lazy=kwargs.get('lazy', self._lazy)
        )
        if obj._text is None and self._text is not None:
            obj._text = self._text
        return obj

    def open(self):
        """
        Returns a opened resource reader object for the instance URL. If the
        source attribute is a seekable file-like object rewind the source and
        return it.
        """
        if self.seek(0) == 0:
            return self.source
        elif self._url is None:
            raise XMLSchemaValueError("can't open, the resource has no URL associated.")
        try:
            return urlopen(self._url, timeout=self.timeout)
        except URLError as err:
            raise XMLSchemaURLError(reason="cannot access to resource %r: %s" % (self._url, err.reason))

    def seek(self, position):
        """
        Change stream position if the XML resource was created with a seekable
        file-like object. In the other cases this method has no effect.
        """
        if not hasattr(self.source, 'read'):
            return

        try:
            if not self.source.seekable():
                return
        except AttributeError:
            pass
        else:
            return self.source.seek(position)

        try:
            value = self.source.seek(position)
        except AttributeError:
            pass
        else:
            return value if PY3 else position

        try:
            value = self.source.fp.seek(position)
        except AttributeError:
            pass
        else:
            return value if PY3 else position

    def close(self):
        """
        Close the XML resource if it's created with a file-like object.
        In other cases this method has no effect.
        """
        try:
            self.source.close()
        except (AttributeError, TypeError):
            pass

    def load(self):
        """
        Loads the XML text from the data source. If the data source is an Element
        the source XML text can't be retrieved.
        """
        if self._url is None and not hasattr(self.source, 'read'):
            return  # Created from Element or text source --> already loaded

        resource = self.open()
        try:
            data = resource.read()
        except (OSError, IOError) as err:
            raise XMLSchemaOSError("cannot load data from %r: %s" % (self._url, err))
        finally:
            # We don't want to close the file obj if it wasn't originally
            # opened by `XMLResource`. That is the concern of the code
            # where the file obj came from.
            if resource is not self.source:
                resource.close()

        if isinstance(data, bytes):
            try:
                text = data.decode('utf-8') if PY3 else data.encode('utf-8')
            except UnicodeDecodeError:
                if PY3:
                    text = data.decode('iso-8859-1')
                else:
                    with codecs.open(urlsplit(self._url).path, mode='rb', encoding='iso-8859-1') as f:
                        text = f.read().encode('iso-8859-1')
        else:
            text = data

        self._text = text

    def is_lazy(self):
        """Returns `True` if the XML resource is lazy."""
        return self._lazy

    def is_loaded(self):
        """Returns `True` if the XML text of the data source is loaded."""
        return self._text is not None

    def iter(self, tag=None):
        """XML resource tree iterator."""
        if not self._lazy:
            for elem in self._root.iter(tag):
                yield elem
            return
        elif self.seek(0) == 0:
            resource = self.source
        elif self._url is not None:
            resource = urlopen(self._url, timeout=self.timeout)
        else:
            resource = StringIO(self._text)

        # Note: lazy iteration change the order (top level element is the last)
        try:
            for event, elem in self.iterparse(resource, events=('end',)):
                if tag is None or elem.tag == tag:
                    yield elem
                elem.clear()
        finally:
            if resource is not self.source:
                resource.close()

    def iterfind(self, path=None, namespaces=None):
        """XML resource tree iterfind selector."""
        if not self._lazy:
            if path is None:
                yield self._root
            else:
                for e in iter_select(self._root, path, namespaces, strict=False):
                    yield e
            return
        elif self.seek(0) == 0:
            resource = self.source
        elif self._url is not None:
            resource = urlopen(self._url, timeout=self.timeout)
        else:
            self.load()
            resource = StringIO(self._text)

        try:
            if path is None:
                level = 0
                for event, elem in self.iterparse(resource, events=('start', 'end')):
                    if event == "start":
                        if level == 0:
                            self._root.clear()
                            self._root = elem
                        level += 1
                    else:
                        level -= 1
                        if level == 0:
                            yield elem
                            elem.clear()
            else:
                selector = Selector(path, namespaces, strict=False, parser=XmlResourceXPathParser)
                path = path.replace(' ', '').replace('./', '')
                path_level = path.count('/') + 1 if path != '.' else 0
                select_all = '*' in path and set(path).issubset({'*', '/'})

                level = 0
                for event, elem in self.iterparse(resource, events=('start', 'end')):
                    if event == "start":
                        if level == 0:
                            self._root.clear()
                            self._root = elem
                        level += 1
                    else:
                        level -= 1
                        if level == path_level and \
                                (select_all or elem in selector.select(self._root)):
                            yield elem
                            elem.clear()
                        elif level == 0:
                            elem.clear()
        finally:
            if self.source is not resource:
                resource.close()

    def iter_location_hints(self):
        """Yields schema location hints from the XML tree."""
        for elem in self.iter():
            try:
                locations = elem.attrib[XSI_SCHEMA_LOCATION]
            except KeyError:
                pass
            else:
                locations = locations.split()
                for ns, url in zip(locations[0::2], locations[1::2]):
                    yield ns, url

            try:
                locations = elem.attrib[XSI_NONS_SCHEMA_LOCATION]
            except KeyError:
                pass
            else:
                for url in locations.split():
                    yield '', url

    def get_namespaces(self):
        """
        Extracts namespaces with related prefixes from the XML resource. If a duplicate
        prefix declaration is encountered then adds the namespace using a different prefix,
        but only in the case if the namespace URI is not already mapped by another prefix.

        :return: A dictionary for mapping namespace prefixes to full URI.
        """
        def update_nsmap(prefix, uri):
            if prefix not in nsmap and (prefix or not local_root):
                nsmap[prefix] = uri
            elif not any(uri == ns for ns in nsmap.values()):
                if not prefix:
                    try:
                        prefix = re.search(r'(\w+)$', uri.strip()).group()
                    except AttributeError:
                        return

                while prefix in nsmap:
                    match = re.search(r'(\d+)$', prefix)
                    if match:
                        index = int(match.group()) + 1
                        prefix = prefix[:match.span()[0]] + str(index)
                    else:
                        prefix += '2'
                nsmap[prefix] = uri

        local_root = self.root.tag[0] != '{'
        nsmap = {}

        if self._url is not None or hasattr(self.source, 'read'):
            resource = self.open()
            try:
                for event, node in self.iterparse(resource, events=('start-ns', 'end')):
                    if event == 'start-ns':
                        update_nsmap(*node)
                    else:
                        node.clear()
            except (ElementTree.ParseError, PyElementTree.ParseError, UnicodeEncodeError):
                pass
            finally:
                # We don't want to close the file obj if it wasn't
                # originally opened by `XMLResource`. That is the concern
                # of the code where the file obj came from.
                if self.source is not resource:
                    resource.close()
        elif isinstance(self._text, string_base_type):
            try:
                for event, node in self.iterparse(StringIO(self._text), events=('start-ns', 'end')):
                    if event == 'start-ns':
                        update_nsmap(*node)
                    else:
                        node.clear()
            except (ElementTree.ParseError, PyElementTree.ParseError, UnicodeEncodeError):
                pass
        else:
            # Warning: can extracts namespace information only from lxml etree structures
            try:
                for elem in self._root.iter():
                    for k, v in elem.nsmap.items():
                        update_nsmap(k if k is not None else '', v)
            except (AttributeError, TypeError):
                pass  # Not an lxml's tree or element

        return nsmap

    def get_locations(self, locations=None):
        """
        Returns a list of schema location hints. The locations are normalized using the
        base URL of the instance. The *locations* argument can be a dictionary or a list
        of namespace resources, that are inserted before the schema location hints extracted
        from the XML resource.
        """
        base_url = self.base_url
        location_hints = []
        if locations is not None:
            try:
                for ns, value in locations.items():
                    if isinstance(value, list):
                        location_hints.extend([(ns, normalize_url(url, base_url)) for url in value])
                    else:
                        location_hints.append((ns, normalize_url(value, base_url)))
            except AttributeError:
                location_hints.extend([(ns, normalize_url(url, base_url)) for ns, url in locations])

        location_hints.extend([(ns, normalize_url(url, base_url)) for ns, url in self.iter_location_hints()])
        return location_hints
