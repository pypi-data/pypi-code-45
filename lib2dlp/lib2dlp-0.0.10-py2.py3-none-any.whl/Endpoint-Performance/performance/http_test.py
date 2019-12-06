#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys,os
import getopt
import httplib
import urllib
import urllib2
import time
import base64
#_DEBUG=True


def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            L.append(os.path.join(root, file))
    return L

#模拟HTTP提交file
def post_http_file(ip,port,filename):
    ret=True
    #if _DEBUG == True:
    #    import pdb
    #    pdb.set_trace()
    try:
        data = []
        boundary = '----------%s' % hex(int(time.time() * 1000))
        data.append('--%s' % boundary)

        url = "http://%s:%s/upload_file.php" % (ip, port)

        data.append('Content-Disposition: form-data; name="%s"\r\n' % 'args')
        data.append(base64.b64encode(filename))
        data.append('--%s' % boundary)


        fr=open(filename,'rb')
        data.append('Content-Disposition: form-data; name="%s"; filename="%s"' % ('file', filename))
        data.append('Content-Type: %s\r\n' % 'application/octet-stream')
        data.append(fr.read())
        fr.close()
        data.append('--%s--\r\n' % boundary)

        http_body='\r\n'.join(data)
        #   print http_body
        #buld http request
        req=urllib2.Request(url, data=http_body)
        #header
        req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
        req.add_header('User-Agent','Mozilla/5.0')
        req.add_header('Referer','http://%s/' % ip)
        #post data to server
        resp = urllib2.urlopen(req, timeout=5)
        #get response
        qrcont=resp.read()
        #print qrcont
        print "http upload file OK"
        return ret
    except Exception as e:
        print(": unable to send URL: {0}".format(e))
        print "http upload file False"
        return False
    return

def http_test():
    ip = "10.95.41.15"
    port = "8000"
    #filename = file_name("test\\leixing")
    filename = "data\\test\\SN.txt"
    print filename
    post_http_file(ip,port,filename)

#end--------------------------------------------------------
if __name__ == "__main__":

    http_test()
    '''
    def usage():
        print(u'\
        -h or --help：显示帮助信息\n\
        -t:测试HTTP上传文件\n\
        -v or --version：显示版本\
        ')
    if len(sys.argv) == 1:
        usage()
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "htpclTv", ["help", "output="])
    except getopt.GetoptError:
        usage()        

    for cmd, arg in opts:
        if cmd in ("-h", "--help"):
            usage()
        if cmd in ("-t", ""):
            http_test()
        elif cmd in ("-v", "--version"):
            print("version 1.0")
    '''