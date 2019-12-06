#coding:gbk

import ConfigParser
import time,win32api,os
import ctypes
def test_decompress(rarfile, outpath,bin=os.path.realpath(r'tool\WinRAR\Rar.exe')):
    #outpath = getToPath(os.path.dirname(rarfile))
    #outpath = rarfile[0:-4]
    if not os.path.exists(outpath):
        os.mkdir(outpath)
    b_t = Winmm.timeGetTime()
    cmd = bin
    cmd += ' x "%s" "%s"' % (rarfile, outpath)
    os.system(cmd)
    #createProcess(cmd, True)
    ret = Winmm.timeGetTime()- b_t
    os.system('rd /S /Q "%s" >NUL 2>NUL' % outpath)
    return ret


def get_Conf():
    try:
        config = ConfigParser.ConfigParser()
        config.readfp(open('perfconf.ini'))
        zippath = config.get("unzip", "zippath")
        output = config.get("unzip", "output")
        return zippath,output
    except Exception as e:
        print e

Winmm = ctypes.WinDLL('Winmm.dll')
zippath,output = get_Conf()
logpath = 'log\\compress.txt'
decompress_time = test_decompress(zippath,output)
f = open(logpath,'a+')
f.write('decompress_time:\t%s\r\n' %decompress_time )
f.close()
print ('decompress_time:\t%s' %decompress_time )
#os.system('pause')