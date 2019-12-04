from wpkit.node import *
import copy
class script:
    class jquery(Script):__node_type__='script';src = '/pkg-resource/js/jquery-3.4.1.js'
    class propper(Script):__node_type__='script';src='/pkg-resource/js/popper.min.js'
    class boostrap(Script):__node_type__='script';src='/pkg-resource/js/bootstrap.min.js'
    class vue(Script):__node_type__='script';src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"
    class myjs(Script):__node_type__='script';src="/pkg-resource/js/my.js"

class link:
    class csslink(Link): rel = "stylesheet";__node_type__='link'
class meta:
    boostrap=lambda :Text('<meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">')

class Htmlbase(Html):
    __node_type__='html'
    def __init__(self):
        super().__init__()
        self(
            Head()(Meta(charset=Var(charset='utf-8')),Title()(Var(title='Home')),Var(head_items=None)),
            Body()(Var(body=None))
        )
class Loginform(Form):
    __node_type__='form'
    def __init__(self):
        super().__init__(method=Var(method='get'), action=Var(action='/login'))
        self(Input(name='email', type='email'),
        Input(name='password', type='password'),
        Button(name='submit', type='submit')('Submit'))
class Loginpage(Htmlbase):
    __node_type__='html'
    def __init__(self):
        super().__init__()
        self.render(body=Loginform())
class Sitebase(Htmlbase):
    __node_type__ = 'html'
    def __init__(self):
        super().__init__()
        self.render(head_items=NodeList([
            meta.boostrap(),
            link.csslink(),
            script.jquery(),
            script.propper(),
            script.boostrap(),
            script.vue(),
            script.myjs()
        ]))
def site_base():
    return Htmlbase().render(
    head_items=NodeList([
        Text('<meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">'),
        Text('''<link href="/pkg-resource/css/bootstrap.min.css" rel="stylesheet">
    <script src="/pkg-resource/js/jquery-3.4.1.js"></script>
    <script src="/pkg-resource/js/popper.min.js"></script>
    <script src="/pkg-resource/js/bootstrap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src="/pkg-resource/js/my.js"></script>''')
        ])
    )


