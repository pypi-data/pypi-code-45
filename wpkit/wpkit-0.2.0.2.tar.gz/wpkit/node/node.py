import re
from collections import deque

class NodeMetaClass(type):
    __not_found__='not_found'
    def __new__(cls, name, bases, attrs):
        if attrs.get('__open_node__',cls.__not_found__)==cls.__not_found__:
            attrs['__open_node__']=bases[-1].__open_node__
        if attrs.get('__node_type__',cls.__not_found__)==cls.__not_found__:
            attrs['__node_type__']=name.lower()
        return type.__new__(cls, name, bases, attrs)

def parse_selector(sel):
    s=sel
    # s = '.div.blue[name=big]  #test,div'
    res={}
    pos = 0
    while True:
        if pos >= len(s) - 1:
            break
        reg_el = re.compile("[a-zA-Z0-9]+")
        match = reg_el.match(s, pos=pos)
        if match:
            pos += len(match.group())
            res['__node_type__']=match.group()
            continue

        reg_cls = re.compile('\.[a-zA-Z0-9_\-]+')
        match = reg_cls.match(s, pos=pos)
        if match:
            pos += len(match.group())
            if '_class' in res.keys():res['_class']+=' '+match.group().lstrip('.')
            else:res['_class']=match.group().lstrip('.')
            continue

        reg_id = re.compile('#[a-zA-Z0-9_\-]+')
        match = reg_id.match(s, pos=pos)
        if match:
            pos += len(match.group())
            res['id']=match.group().lstrip('#')
            continue

        reg_attr = re.compile('\[[a-zA-Z0-9_\-]+=[a-zA-Z0-9_\-]+\]')
        match = reg_attr.match(s, pos=pos)
        if match:
            pos += len(match.group())
            k,v=match.group().lstrip('[').rstrip(']').split('=')
            res[k.strip()]=v.strip()
            continue
    return res
class Node(metaclass=NodeMetaClass):
    __indent__=' '*4
    __open_node__=True
    def __init__(self,**kwargs):
        self.__dict__['__children__'] = deque([])
        self.__dict__['__attrs__']=kwargs
        self.seta(parent=None)
    def attrs(self):
        return self.__dict__['__attrs__']
    def parent(self):
        return self.geta('parent')
    def children(self):
        return self.__dict__['__children__']
    def append(self,x):
        x.seta(parent=self)
        self.__dict__['__children__'].append(x)
    def appendleft(self,x):
        x.seta(parent=self)
        return self.__dict__['__children__'].appendleft(x)
    def count(self, x):
        return self.__dict__['__children__'].count(x)
    def extend(self,iterable):
        for x in iterable:x.seta(parent=self)
        return self.__dict__['__children__'].extend(iterable)
    def extendleft(self,iterable):
        for x in iterable: x.seta(parent=self)
        return self.__dict__['__children__'].extendleft(iterable)
    def insert(self,i,x):
        x.seta(parent=self)
        return self.__dict__['__children__'].insert(i,x)
    def index(self,x,start=0,stop=None):
        stop=len(self.children()) if stop is None else stop
        return self.__dict__['__children__'].index(x,start,stop)
    def pop(self,i):
        return self.__dict__['__children__'].pop(i)
    def popleft(self):
        return self.__dict__['__children__'].popleft()
    def remove(self,value):
        return self.__dict__['__children__'].remove(value)
    def reverse(self):
        return self.__dict__['__children__'].reverse()
    def rotate(self, n: int) -> None:
        return self.__dict__['__children__'].rotate(n)
    def replace(self,v1,v2):
        index=self.index(v1)
        self.remove(v1)
        self.insert(index,v2)
    def replacewith(self,node):
        return self.parent().replace(self,node)
    def __getitem__(self, item):
        if isinstance(item,str):
            return self.find(sel=item)[0]
        return self.children()[item]
    def __setitem__(self, key, value):
        value.seta(parent=self)
        return self.__dict__['__children__'].__setitem__(key,value)
    def __call__(self, *args):
        if not len(args):return self.children()
        args=list(args)
        for i in range(len(args)):
            if isinstance(args[i],str):
                s=args[i].strip()
                if s.startswith('<!--') and s.endswith('-->'):
                    args[i]=Comment(s.lstrip('<!--').rstrip('-->'))
                else:
                    args[i]=Text(s)
        self.__dict__['__children__'] = deque(args)
        for i in self.children():
            i.seta(parent=self)
        return self

    def __getattr__(self, key):
        return self.__dict__['__attrs__'].get(key, None)

    def __setattr__(self, key, value):
        self.__dict__['__attrs__'][key] = value

    def set_attribute(self, key, value):
        self.__dict__[key] = value

    def get_attribute(self, *args, **kwargs):
        return self.__dict__.get(*args, **kwargs)

    def seta(self, **kwargs):
        for k, v in kwargs.items():
            self.set_attribute('__%s__' % (k), v)

    def geta(self, key, *args, **kwargs):
        return self.get_attribute('__%s__' % (key), *args, **kwargs)
    def match(self,**kwargs):
        if '__node_type__' in kwargs.keys():
            if not self.__node_type__==kwargs['__node_type__']:return False
            kwargs.pop('__node_type__')
        if '_class' in kwargs.keys():
            if (not self._class) or (not set(kwargs['_class'].split()).issubset(set(self._class.split()))):return False
            kwargs.pop('_class')
        for k,v in kwargs.items():
            if not self.__getattr__(k)==v:return False
        return True
    def find(self, sel=None,kws=None, res_list=None):
        if sel:kws=parse_selector(sel);
        if not res_list:res_list={'list':FindResult()}
        if self.match(**kws):res_list['list'].append(self)
        for ch in self.children():
            ch.find(kws=kws,res_list=res_list)
        return res_list['list']
    def __str__(self):
        return self.to_string()
    def get_children_string(self,depth=0):
        def to_string(ch,depth=0):
           return ch.to_string(depth=depth) if isinstance(ch,Node) else '\n'+self.__indent__*depth+str(ch)

        mid = '\n' + self.__indent__ * depth if len(self.__dict__['__children__']) else ''
        content = ''.join([to_string(ch, depth=depth + 1) for ch in self.__dict__['__children__']])
        return content+mid
    def to_string(self, depth=0):
        def to_string(ch,depth=0):
           return ch.to_string(depth=depth) if isinstance(ch,Node) else '\n'+self.__indent__*depth+str(ch)

        attrs = ' '.join(['%s="%s"' % ('class' if k == '_class' else k, v) for k, v in self.attrs().items()])
        attrs = ' ' + attrs if len(attrs) else attrs
        if self.__open_node__:
            mid='\n'+self.__indent__ * depth if len(self.__dict__['__children__']) else ''
            content=''.join([to_string(ch,depth=depth + 1) for ch in self.__dict__['__children__']])
            return '\n%s<%s%s>%s%s</%s>' % (self.__indent__ * depth,self.__node_type__,attrs,
                                               content,mid,self.__node_type__)
        else:
            return '\n%s<%s %s/>' % (self.__indent__ * depth,self.__node_type__,attrs)
    def compile(self):
        return Text(self.to_string())
    def render(self,**kwargs):
        for k,v in kwargs.items():
            ns = self.find('var[name=%s]'%(k))
            for n in ns:n.replacewith(v)
        return self
    def print(self,depth=0):
        print(self.to_string(depth=depth))

class FindResult(list):
    pass


class CloseNode(Node):
    __open_node__=False

class Text(Node):
    def __init__(self,content='',**kwargs):
        self.seta(content=content)
        super().__init__(**kwargs)
    def to_string(self, depth=0):
        return '\n'+self.__indent__*depth+str(self.geta('content'))
    def render(self,**kwargs):
        from jinja2 import Environment
        tem = Environment().from_string(self.geta('content'))
        return Text(tem.render(**kwargs))


class Comment(Node):
    def __init__(self, content='', **kwargs):
        self.__dict__['content'] = content
        super().__init__(**kwargs)
    def to_string(self, depth=0):
        return '\n'+self.__indent__*depth+'<!--'+str(self.__dict__['content'])+'-->'

class Html(Node):pass
class Head(Node):pass
class Title(Node):pass
class Meta(CloseNode):pass
class Link(CloseNode):pass
class Style(Node):pass
class Script(Node):pass
class Body(Node):pass
class Div(Node):pass
class Span(Node):pass
class H(Node):pass
class P(Node):pass
class A(Node):pass
class Img(CloseNode):pass
class Form(Node):pass
class Input(CloseNode):pass
class Button(Node):pass

# ---------more tags ---------

class Address(Node):pass
class Article(Node):pass
class Aside(Node):pass
class Footer(Node):pass
class Header(Node):pass
class H1(Node):pass
class H2(Node):pass
class H3(Node):pass
class H4(Node):pass
class H5(Node):pass
class H6(Node):pass
class Hgroup(Node):pass
class Main(Node):pass
class Nav(Node):pass
class Section(Node):pass
class Blackquote(Node):pass
class Dd(Node):pass
class Dir(Node):pass
class Dl(Node):pass
class Dt(Node):pass
class Figure(Node):pass
class Hr(Node):pass
class Li(Node):pass
class Ol(Node):pass
class Ul(Node):pass
class Pre(Node):pass
class Abbr(Node):pass
class B(Node):pass
class Br(Node):pass
class Cite(Node):pass
class Code(Node):pass
class Data(Node):pass
class Em(Node):pass
class I(Node):pass
class Kbd(Node):pass
class Mark(Node):pass
class Q(Node):pass
class Small(Node):pass
class Strong(Node):pass
class Sub(Node):pass
class Sup(Node):pass
class Time(Node):pass
class Area(Node):pass
class Audio(Node):pass
class Map(Node):pass
class Video(Node):pass
class Track(Node):pass
class Embed(Node):pass
class Iframe(Node):pass
class Object(Node):pass
class Param(Node):pass
class Picture(Node):pass
class Sourcecanvas(Node):pass
class Noscript(Node):pass
class Del(Node):pass
class Ins(Node):pass
class Caption(Node):pass
class Col(Node):pass
class Table(Node):pass
class Tbody(Node):pass
class Td(Node):pass
class Tfoot(Node):pass
class Th(Node):pass
class Thead(Node):pass
class Tr(Node):pass
class Fieldset(Node):pass
class Datalist(Node):pass
class Label(Node):pass
class Legend(Node):pass
class Meter(Node):pass
class Optgroup(Node):pass
class Option(Node):pass
class Output(Node):pass
class Progress(Node):pass
class Select(Node):pass
class Textarea(Node):pass
class Details(Node):pass
class Dialog(Node):pass
class Menu(Node):pass
class Menuitem(Node):pass
class Summary(Node):pass
class Element(Node):pass
class Shadow(Node):pass
class Slot(Node):pass
class Template(Node):pass
class Big(Node):pass
class Blink(Node):pass
class Center(Node):pass
class Bgsound(Node):pass
class Command(Node):pass

taglist=\
    'address article aside footer header h1 h2 h3 h4 h5 h6 ' \
    'hgroup main nav section ' \
    'blackquote dd dir dl dt figure hr li ol ul pre ' \
    'abbr b br cite code data em i kbd mark q small strong sub sup ' \
    'time var area audio map video track embed iframe object param picture source' \
    'canvas noscript del ins caption col table tbody td tfoot th thead tr ' \
    'button fieldset datalist form input label legend meter optgroup option ' \
    'output progress select textarea details dialog menu menuitem summary ' \
    'comment element shadow slot template ' \
    'big blink center bgsound center command '.split()


# ----------------------------------------------------
class Tem(Node):pass
class Var(Node):
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name
class Jvar(Node):
    def __init__(self,name,**kwargs):
        self.seta(name=name)
        super().__init__(**kwargs)
    def __str__(self):
        return self.to_string()
    def to_string(self, depth=0):
        return '{{%s}}' % (self.geta('name'))
class For(Node):
    def __init__(self,forwhat,**kwargs):
        self.seta(forwhat=forwhat)
        super().__init__(**kwargs)
    def to_string(self, depth=0):
        return '\n'+self.__indent__*depth+'{%for '+self.geta('forwhat')+'%}'+self.get_children_string(depth=depth)+'{%endfor%}'

class If(Node):
    def __init__(self, condition, **kwargs):
        self.seta(condition=condition)
        super().__init__(**kwargs)
    def to_string(self, depth=0):
        return '\n'+self.__indent__*depth+'{%if '+self.geta('condition')+'%}'+self.get_children_string(depth=depth)+'{%endif%}'
class Elif(Node):
    def __init__(self, condition, **kwargs):
        self.seta(condition=condition)
        super().__init__(**kwargs)
    def to_string(self, depth=0):
        return '\n'+self.__indent__*depth+'{%elif '+self.geta('condition')+'%}'+self.get_children_string(depth=depth)
class Else(Node):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def to_string(self, depth=0):
        return '\n'+self.__indent__*depth+'{%else%}'+self.get_children_string(depth=depth)

