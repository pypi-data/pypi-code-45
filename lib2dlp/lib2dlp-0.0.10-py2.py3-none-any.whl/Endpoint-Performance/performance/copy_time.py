#coding:gbk
import ConfigParser
import time,win32api,os
import win32api,win32file
import ctypes

def _listFile_(path, isDeep=True):
    _list = []
    if isDeep:
        try:
            for root, dirs, files in os.walk(path):
                for fl in files:
                    _list.append('%s\%s' % (root, fl))
        except:
            pass
    else:
        for fn in glob.glob(path + os.sep + '*'):
            if not os.path.isdir(fn):
                _list.append('%s' % path + os.sep + fn[fn.rfind('\\') + 1:])
    return _list


def copy_dir(dir1, dir2):
    flist1 = _listFile_(dir1)

    flist2, dirlist2 = [], []
    for fname1 in flist1:
        fname2 = fname1.replace(dir1, dir2)
        flist2.append(fname2)
        dirlist2.append(os.path.dirname(fname2))

    for dir in sorted(list(set(dirlist2))):
        os.system('mkdir "%s" >NUL 2>NUL' % dir)

    b_t = Winmm.timeGetTime()
    for index, value in enumerate(flist1):
        ##        log.debug('拷贝文件【%s】到【%s】' % (flist1[index], flist2[index]))
        ##        os.system(r'copy /y "%s" "%s" >nul 2>nul' % (flist1[index], flist2[index]))
        try:
            win32file.CopyFile(flist1[index], flist2[index], 0)
        except Exception, e:
            print 'copy_dir', e
            pass
        if not os.path.exists(flist2[index]):
            print flist2[index]
    ret = Winmm.timeGetTime() - b_t
    # os.system(r'rd "%s" /S /Q >NUL 2>NUL' % dir2)
    return ret


def get_Conf():
    try:
        config = ConfigParser.ConfigParser()
        config.readfp(open('perfconf.ini'))
        sourcepath = config.get("copy", "sourcepath")
        destpath = config.get("copy", "destpath")
        return sourcepath,destpath
    except Exception as e:
        print(e)


Winmm = ctypes.WinDLL('Winmm.dll')
sourcepath,destpath = get_Conf()
logpath = 'log\\copyfile.txt'
copyfile_time = copy_dir(sourcepath,destpath)
f = open(logpath,'a+')
f.write('copyfile_time:\t%s\r\n' %copyfile_time)
f.close()
print ('copyfile_time:\t%s' %copyfile_time)
#os.system('pause')
