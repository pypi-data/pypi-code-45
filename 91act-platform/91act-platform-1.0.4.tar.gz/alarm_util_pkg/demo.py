# -*- coding: utf-8 -*-
from core import SimpleCronControl, NormalTools
import core

cron_control = SimpleCronControl("Your Address", "2").cron_control()
wx_txt = "<font color=\"comment\">Crossing Void - Global OnlineCNT Alarm</font>\n"
wx_txt = wx_txt + "<font color=\"warning\">测试</font>\n"
body = {
    "msgtype": "markdown",
    "markdown": {
        "content": wx_txt
    }
}
cron_control.send(2, body)

from flask import Flask, jsonify

app = Flask(__name__)
Core = core
Core.build(project_id="PROJECT_ID", server="AUTH_SERVER_ADDRESS", app=app, secret_key="Secret_key")


@app.route('/heartbeat', methods=['GET'])
@Core.login_required
def heartbeat():
    """
    心跳
    :return:
    """
    return jsonify(code=200)


app.config['JSON_AS_ASCII'] = False
app.run(host="0.0.0.0", debug=True, threaded=True)

# conn = NormalTools().mysql_connector("HOST",3306,"USER","PASSWD","DATABASE")
