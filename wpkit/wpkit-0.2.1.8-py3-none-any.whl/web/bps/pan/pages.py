# import wpkit
# from wpkit.web import bps
# app=wpkit.web.get_default_app(__name__)
# app.register_blueprint(bps.bp_pan.bp_pan(app,url_prefix='/pan'))


from wpkit.node import *
from wpkit.node import components
from wpkit.node.Q import *
from wpkit.node.components import *

# body=Body(style="background-color:#ffffff;")(
#     Div(_class="row",style="width:300px;height:300px;background-color:#fafafa"),
#     Div(_class="row",style="width:300px;height:300px;background-color:yellow;")
# )
post_script = Text("var data={cmd:{op:1,params:[2]}};console.log(data);res=postJson('/pan/data',data);console.log(res)")
body = Div(style=StyleAttr(height="100%", width="100%"))(
    QBox().css(height='{{h1}}%'),
    QBox()(
        QBox(style=StyleAttr(float="left", width="calc({{w}}%)", background_color="#eeeeee"))(
            QButton(onclick=post_script)("Click Me")
        ),
        QBox(id=3)(
            QCell()("Hello")
        ).css(float="right", width="calc({{100-w}}%)")
    ).css(height='{{100-h1}}%')
)

body = Div(_class='container')(
    QRow()(

    ),
    QRow(id='1')(
        QCol()(
            "hi"
        ).cls('bg-danger'),
        QCol()(
            "hi"
        )
    ).cls('bg-info')
)
panpage = components.Sitebase().render(body=body)
# testobj=body
# panpage["body"].css(padding=0, margin=0,background="black",color="white")
panpage["body"].css(padding=0, margin=0)
testobj = body
panpage = panpage.compile().render(h1=8, w=8)
