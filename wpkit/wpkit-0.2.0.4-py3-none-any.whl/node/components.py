from wpkit.node import *

html_base=Html()(
    Head()(
        Meta(charset=Var(charset='utf-8')),
        Title()(Var(title='Home')),
        Var(head_items=None)
    ),
    Body()(
        Var(body=None)
    )
)

login_form=Form(method=Var(method='get'),action=Var(action='/login'))(
    Input(name='email',type='email'),
    Input(name='password',type='password'),
    Button(name='submit',type='submit')('Submit')
)



