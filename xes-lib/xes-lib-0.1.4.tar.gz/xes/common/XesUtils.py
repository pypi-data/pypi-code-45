#coding=utf-8
import json
import sys, getopt
import time

# Information Transfer Protocol
# Information exchange Protocol
# 信息交换输出工具函数
def InfoTransferAndExchange(data):
	time.sleep(0.01)
	jsonStr = json.dumps(data)
	print("#xzeysx#" + jsonStr + "#xzeysx#")

'''
	// 提示信息
    data = { 'type':'msg','value': "识别前图片："+img_src } 
    XesUtils.InfoTransferAndExchange(data)

	// 结果信息
	data = { 'type':'result','desc':'识别后图片','value' : imgurl }
    XesUtils.InfoTransferAndExchange(data)
'''


# 命令行参数获取方法
# 例:
# img_src = 'http://wx2.sinaimg.cn/mw690/ac38503ely1fesz8m0ov6j20qo140dix.jpg'
# img_src = XesUtils.GetArgByName('i','file',img_src)
# 对应命令行  python3 t.py  -i http:xyz   OR  --file=http:xyz
def GetArgByName(shortArgName,fullArgName,default):
	value = default
	try:
		opts, args = getopt.getopt(sys.argv[1:],shortArgName+":", [fullArgName+'='])
	except getopt.GetoptError:
		print('获取参数遇到错误！')
		return value
	for opt, arg in opts:
		if opt in ("-" + shortArgName, "--" + fullArgName):
			value = arg
	# print('参数 = ' + value+ '  '+sys.argv[1])
	return value

# 文件存取路径获取方法
def GetPath():
	filePath = sys.argv[0]
	pathArr = filePath.split('/')
	pathArr[len(pathArr) - 1] = ''
	dirPath = '/'.join(pathArr)
	return dirPath


# excepthook 异常钩子，告知程序是否出错
class ExitHooks(object):
    def __init__(self):
        self.exit_code = None
        self.exception = None

    def hook(self):
        self._orig_exit = sys.exit
        sys.exit = self.exit
        sys.excepthook = self.exc_handler

    def exit(self, code=0):
        self.exit_code = code
        self._orig_exit(code)

    def exc_handler(self, exc_type, exc, *args):
        self.exception = exc
        sys.__excepthook__(exc_type,exc,*args)