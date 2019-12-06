#coding:utf-8
import compress
import copyfile
import ftpupload
import IEOpen
import install
import runapp
import processinfo
import time
import wgetfile

def case_compress(i):
    logpath = 'log\\compress_%s.txt' %i
    processinfo.logname = logpath
    processinfo.endtag = False

    processlist = ['360entclient.exe','360tray.exe']
    watch = processinfo.begin_watch(processlist,processinfo.endtag)
    watch.start()

    decompress_time = compress.test_decompress(r'E:\python\performance\performance\data\mutifile.rar')
    time.sleep(1)
    compress_time = compress.test_compress(r'E:\python\performance\performance\data\download')
    time.sleep(1)
    processinfo.endtag = True
    f = open(logpath,'a+')
    f.write('decompress_time:\t%s\tcompress_time:\t%s\ttotal:\t%s\r\n' %(decompress_time,compress_time,decompress_time+compress_time))
    f.close()
    return decompress_time,compress_time
    
def case_ftpupload(i):
    logpath = 'log\\ftpupload_%s.txt' %i
    processinfo.logname = logpath
    processinfo.endtag = False

    processlist = ['360entclient.exe','360tray.exe']
    watch = processinfo.begin_watch(processlist,processinfo.endtag)
    watch.start()

    ftpupload_time = ftpupload.uploadsftp()
    processinfo.endtag = True
    f = open(logpath,'a+')
    f.write('ftpupload_time:\t%s\r\n' %ftpupload_time)
    f.close()
    return ftpupload_time

def case_copyfile(i):

    logpath = 'log\\copyfile_%s.txt' %i
    processinfo.logname = logpath
    processinfo.endtag = False

    processlist = ['360entclient.exe','360tray.exe']
    watch = processinfo.begin_watch(processlist,processinfo.endtag)
    watch.start()

    copyfile_time = copyfile.copy_dir(r'E:\python\performance\performance\data\download',r'E:\python\performance\performance\data\download2')
    processinfo.endtag = True
    f = open(logpath,'a+')
    f.write('copyfile_time:\t%s\r\n' %copyfile_time)
    f.close()
    return copyfile_time

def case_IEOpen(i):
    logpath = 'log\\IEOpen_%s.txt' %i
    processinfo.logname = logpath
    processinfo.endtag = False

    processlist = ['360entclient.exe','360tray.exe']
    watch = processinfo.begin_watch(processlist,processinfo.endtag)
    watch.start()

    IEOpen_time = IEOpen.getallurl(IEOpen.urls)
    processinfo.endtag = True
    f = open(logpath,'a+')
    f.write('IEOpen:\t%s\r\n' %IEOpen_time)
    f.close()
    return IEOpen_time

def case_Runapp(i):
    logpath = 'log\\Runapp_%s.txt' %i
    processinfo.logname = logpath
    processinfo.endtag = False

    processlist = ['360entclient.exe','360tray.exe']
    watch = processinfo.begin_watch(processlist,processinfo.endtag)
    watch.start()

    excel_time = runapp.case_open_excel()
    word_time = runapp.case_open_word()
    pdf_time = runapp.case_open_pdf()
    ppt_time = runapp.case_open_ppt()
    processinfo.endtag = True
    f = open(logpath,'a+')
    f.write('excel_time:\t%s\tword_time:\t%s\tpdf_time:\t%s\tppt_time:\t%s\t\r\n' %(excel_time,word_time,pdf_time,ppt_time))
    f.close()
    return excel_time,word_time,pdf_time,ppt_time

def case_install(i):
    logpath = 'log\\install_%s.txt' %i
    processinfo.logname = logpath
    processinfo.endtag = False

    processlist = ['360entclient.exe','360tray.exe']
    watch = processinfo.begin_watch(processlist,processinfo.endtag)
    watch.start()

    adobe_time = install.case_install_adobereader()
    qq_time = install.install_QQ()
    chrome_time = install.insatall_chorme()
    vc_time = install.case_install_vc()
    processinfo.endtag = True
    f = open(logpath,'a+')
    f.write('adobe_time:\t%s\tqq_time:\t%s\tchrome_time:\t%s\tvc_time:\t%s\r\n' %(adobe_time,qq_time,chrome_time,vc_time))
    f.close()
    return adobe_time,qq_time,chrome_time,vc_time

def case_uninstall(i):
    logpath = 'log\\uninstall_%s.txt' %i
    processinfo.logname = logpath
    processinfo.endtag = False

    processlist = ['360entclient.exe','360tray.exe']
    watch = processinfo.begin_watch(processlist,processinfo.endtag)
    watch.start()

    un_adobe_time = install.case_uninstall_adobereader()
    un_qq_time = install.uninstall_QQ()
    un_chrome_time = install.uninsatall_chorme()
    un_vc_time = install.case_unstall_vc()
    processinfo.endtag = True
    f = open(logpath,'a+')
    f.write('un_adobe_time:\t%s\tun_qq_time:\t%s\tun_chrome_time:\t%s\tun_vc_time:\t%s\r\n' %(un_adobe_time,un_qq_time,un_chrome_time,un_vc_time))
    f.close()
    return un_adobe_time,un_qq_time,un_chrome_time,un_vc_time

def case_http_download(i):
    logpath = 'log\\download_%s.txt' %i
    processinfo.logname = logpath
    processinfo.endtag = False

    processlist = ['360entclient.exe','360tray.exe']
    watch = processinfo.begin_watch(processlist,processinfo.endtag)
    watch.start()

    download_time = wgetfile.downWget(r'http://10.74.121.45/download/setup/360skylarsetup.exe',r'data\test.exe')

    processinfo.endtag = True

    f = open(logpath,'a+')
    f.write('download_time:\t%s\r\n' %download_time)
    f.close()
    return download_time

for i in range(1,200):
    '''
    case_compress(i)
    time.sleep(3)
    case_ftpupload(i)
    time.sleep(3)
    case_copyfile(i)
    time.sleep(3)
    

    case_IEOpen(i)
    time.sleep(3)
    case_install(i)
    time.sleep(3)
    case_Runapp(i)
    time.sleep(3)
    case_uninstall(i)
    time.sleep(4)   
    '''
    case_http_download(i)
