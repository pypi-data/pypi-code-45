from flask import Flask, request, Blueprint, abort, send_file
from wpkit.web import resources,utils
from wpkit.pan import Pan
from wpkit.web.bps.myblueprint import MyBlueprint
from wpkit.web.resources import env
import wpkit
class BluePan(MyBlueprint):
    def __init__(self,import_name=None,name='pan',datapath='./data/pan',url_prefix='/pan',**kwargs):
        super().__init__(name=name,import_name=import_name,url_prefix=url_prefix,**kwargs)
        self.datapath = wpkit.basic.DirPath(datapath)
        self.db=wpkit.piu.Piu(path=self.datapath.db)
        self.usman=wpkit.web.utils.UserManager(dbpath=self.datapath.usman.db,home_url=self.url_prefix)
        usman = self.usman
        self.route('/login', methods=['post'])(usman.login)
        self.route('/signup', methods=['post'])(usman.signup)
        @self.route('/', methods=['get'])
        @usman.login_required
        def do_pan_get():
            return env.get_template('pan.html').render()
        @self.route('/', methods=['POST'])
        def do_pan_post():
            pass
