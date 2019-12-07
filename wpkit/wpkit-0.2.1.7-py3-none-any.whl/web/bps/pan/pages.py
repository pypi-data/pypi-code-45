# import wpkit
# from wpkit.web import bps
# app=wpkit.web.get_default_app(__name__)
# app.register_blueprint(bps.bp_pan.bp_pan(app,url_prefix='/pan'))


from wpkit.node import *
from wpkit.node import components
body=Body(style="background-color:#ffffff;")(
    Div(_class="row",style="width:300px;height:300px;background-color:#fafafa"),
    Div(_class="row",style="width:300px;height:300px;background-color:yellow;")
)
post_script=Text("var data={cmd:{op:1,params:[2]}};console.log(data);res=postJson('/pan/data',data);console.log(res)")
body=Div(style=StyleAttr(height="100%",width="100%"))(
    components.PlaceHolder(height="calc({{h1}}% - 1px)",border_bottom="1px gray solid"),
    Div(style=StyleAttr(float="left",height="{{100-h1}}%",width="calc({{w}}% - 1px)",background_color="#eeeeee",border_right="1px gray solid"))(
        Button(onclick=post_script)("Click Me")
    )
)
panpage=components.Sitebase().render(body=body)
panpage["body"].style(padding=0,margin=0)
panpage=panpage.compile().render(h1=8,w=8)