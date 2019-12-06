#coding:utf-8
"""
´°¿Ú²Ù×÷×Ô¶¯»¯·½·¨
"""
import autoutil, autoinput
import ctypes
import re
import win32con, win32gui, win32api
import time
import subprocess

#´°¿Ú»ùÀà
class Window:
    @staticmethod
    def parseClickConfig(clkCfg):
        if clkCfg == None:
            return None, None, autoinput.CLICK_MOUSE
        if type(clkCfg) == int:
            return None, None, clkCfg
        if len(clkCfg) == 2:
            return clkCfg[0], clkCfg[1], autoinput.CLICK_MOUSE
        return clkCfg

    @staticmethod
    def parseTitleConfig(titleCfg):
        if type(titleCfg) == str:
            return titleCfg, None, False
        if len(titleCfg) == 2:
            if type(titleCfg[1]) == bool:
                return titleCfg[0], None, titleCfg[1]
            return titleCfg[0], titleCfg[1], False
        return titleCfg

    def __init__(self, hwnd):
        self.hwnd = hwnd

    #clkCfg:mode|(x,y)|(x,y,mode)
    def click(self, clkCfg = None):
        clickWindow(self.hwnd, clkCfg)

    #timeout:timeout|(timeout,interval)
    #clkCfg:mode|(x,y)|(x,y,mode)
    def clickFor(self, timeout, cond, clkCfg = None):
        return clickWindowFor(self.hwnd, timeout, cond, clkCfg)

    #timeout:timeout|(timeout,interval)
    #clkCfg:mode|(x,y)|(x,y,mode)
    def clickForClose(self, timeout, hwnd, clkCfg = None):
        return clickWindowForClose(self.hwnd, timeout, hwnd, clkCfg)

    #timeout:timeout|(timeout,interval)
    #clkCfg:mode|(x,y)|(x,y,mode)
    def clickForCloseSelf(self, timeout, clkCfg = None):
        return clickWindowForCloseSelf(self.hwnd, timeout, clkCfg)

    #timeout:timeout|(timeout,interval)
    #titleCfg:title|(title,parentTitle)|(title,isRaw)|(title,parentTitle,isRaw)
    #clkCfg:mode|(x,y)|(x,y,mode)
    def clickForFind(self, timeout, titleCfg, clkCfg = None):
        hwnd = clickWindowForFind(self.hwnd, timeout, titleCfg, clkCfg)
        if hwnd:
            return Window(hwnd)

    #timeout:timeout|(timeout,interval)
    #titleCfg:title|(title,isRaw)
    #clkCfg:mode|(x,y)|(x,y,mode)
    def clickForFindChild(self, timeout, titleCfg, clkCfg = None):
        hwnd = clickWindowForFindChild(self.hwnd, timeout, titleCfg, clkCfg)
        if hwnd:
            return Window(hwnd)

    #timeout:timeout|(timeout,interval)
    #clkCfg:mode|(x,y)|(x,y,mode)
    def clickForHidden(self, timeout, hwnd, clkCfg = None):
        return clickWindowForHidden(self.hwnd, timeout, hwnd, clkCfg)

    #timeout:timeout|(timeout,interval)
    #clkCfg:mode|(x,y)|(x,y,mode)
    def clickForHiddenSelf(self, timeout, clkCfg = None):
        return clickWindowForHiddenSelf(self.hwnd, timeout, clkCfg)

    #timeout:timeout|(timeout,interval)
    #clkCfg:mode|(x,y)|(x,y,mode)
    def clickForMd5(self, timeout, hwnd, x, y, md5, clkCfg = None):
        return clickWindowForMd5(self.hwnd, timeout, hwnd, x, y, md5, clkCfg)

    #timeout:timeout|(timeout,interval)
    #clkCfg:mode|(x,y)|(x,y,mode)
    def clickForMd5Self(self, timeout, x, y, md5, clkCfg = None):
        return clickWindowForMd5Self(self.hwnd, timeout, x, y, md5, clkCfg)

    def getClass(self):
        return getWindowClass(self.hwnd)

    def getParent(self):
        hwnd = getParentWindow(self.hwnd)
        if hwnd:
            return Window(hwnd)

    def getRect(self):
        return getWindowRect(self.hwnd)

    def getText(self):
        return getWindowText(self.hwnd)

    def findChild(self, title, isRaw = False):
        hwnd = findWindow(title, self.hwnd, isRaw)
        if hwnd:
            return Window(hwnd)

    def findChilds(self, title, isRaw = False):
        hwndList = findWindows(title, self.hwnd, isRaw)
        return [Window(hwnd) for hwnd in hwndList]        

    def max(self):
        return maxWindow(self.hwnd)

    def min(self):
        return minWindow(self.hwnd)

    def setText(self, text):
        return setWindowText(self.hwnd, text)

    def show(self):
        showWindow(self.hwnd)

    def top(self):
        return topWindow(self.hwnd)

    def isVisible(self):
        return win32gui.IsWindowVisible(self.hwnd)

    def isEnabled(self):
        return win32gui.IsWindowEnabled(self.hwnd)

    def isDisabled(self):
        if not win32gui.IsWindowVisible(self.hwnd):
            return True
        if not win32gui.IsWindowEnabled(self.hwnd):
            return True

#µã»÷´°¿Ú
#clkCfg:mode|(x,y)|(x,y,mode)
def clickWindow(hwnd, clkCfg = None):
##    if isRawWindow(hwnd):
##        return
    topWindow(hwnd)
    rect = getWindowRect(hwnd)
    if not rect:
        return
    x, y, mode = Window.parseClickConfig(clkCfg)
    if x == None:
        x = (rect[0] + rect[2]) / 2
    elif x < 0:
        x += rect[2]
    else:
        x += rect[0]
    if y == None:
        y = (rect[1] + rect[3]) / 2
    elif y < 0:
        y += rect[3]
    else:
        y += rect[1]
    autoinput.clickMouse(x, y, False, mode)

#µã»÷´°¿ÚµÈ´ýÌõ¼þÂú×ã
#timeout:timeout|(timeout,interval)
#clkCfg:mode|(x,y)|(x,y,mode)
def clickWindowFor(hwnd, timeout, cond, clkCfg = None):
    def __clickWindowFor__(hwnd, cond, clkCfg):
        rst = cond.do()
        if not rst or autoutil.isExcept(rst):
            clickWindow(hwnd, clkCfg)
        return rst
    return autoutil.handleTimeout(__clickWindowFor__, timeout, hwnd, cond, clkCfg)

#µã»÷´°¿ÚµÈ´ýÄ³´°¿Ú¹Ø±Õ
#timeout:timeout|(timeout,interval)
#clkCfg:mode|(x,y)|(x,y,mode)
def clickWindowForClose(hwnd, timeout, tgtHwnd, clkCfg = None):
    cond = autoutil.Condition(autoutil.negative, win32gui.IsWindow, tgtHwnd)
    return clickWindowFor(hwnd, timeout, cond, clkCfg)

#µã»÷´°¿ÚµÈ´ý¸Ã´°¿Ú¹Ø±Õ
#timeout:timeout|(timeout,interval)
#clkCfg:mode|(x,y)|(x,y,mode)
def clickWindowForCloseSelf(hwnd, timeout, clkCfg = None):
    return clickWindowForClose(hwnd, timeout, hwnd, clkCfg)

#µã»÷´°¿ÚµÈ´ýÕÒµ½Ä³´°¿Ú
#timeout:timeout|(timeout,interval)
#titleCfg:title|(title,isRaw)|(title,parentTitle)|(title,parentTitle,isRaw)
#clkCfg:mode|(x,y)|(x,y,mode)
def clickWindowForFind(hwnd, timeout, titleCfg, clkCfg = None):
    title, parentTitle, isRaw = Window.parseTitleConfig(titleCfg)
    cond = autoutil.Condition(findWindow, title, parentTitle, isRaw)
    return clickWindowFor(hwnd, timeout, cond, clkCfg)

#µã»÷´°¿ÚµÈ´ýÕÒµ½¸Ã´°¿ÚµÄÄ³×Ó´°¿Ú
#timeout:timeout|(timeout,interval)
#titleCfg:title|(title,isRaw)
#clkCfg:mode|(x,y)|(x,y,mode)
def clickWindowForFindChild(hwnd, timeout, titleCfg, clkCfg = None):
    if type(titleCfg) == tuple:
        titleCfg = titleCfg[0], hwnd, titleCfg[1]
    else:
        titleCfg = titleCfg, hwnd
    return clickWindowForFind(hwnd, timeout, titleCfg, clkCfg)

#µã»÷´°¿ÚµÈ´ýÄ³´°¿Ú²»¿É¼û
#timeout:timeout|(timeout,interval)
#clkCfg:mode|(x,y)|(x,y,mode)
def clickWindowForHidden(hwnd, timeout, tgtHwnd, clkCfg = None):
    cond = autoutil.Condition(autoutil.negative, win32gui.IsWindowVisible, tgtHwnd)
    return clickWindowFor(hwnd, timeout, cond, clkCfg)

#µã»÷´°¿ÚµÈ´ý¸Ã´°¿Ú²»¿É¼û
#timeout:timeout|(timeout,interval)
#clkCfg:mode|(x,y)|(x,y,mode)
def clickWindowForHiddenSelf(hwnd, timeout, clkCfg = None):
    return clickWindowForHidden(hwnd, timeout, hwnd, clkCfg)

#µã»÷´°¿ÚµÈ´ýÄ³´°¿ÚÇøÓòµÄÏñËØÆ¥Åämd5
#timeout:timeout|(timeout,interval)
#clkCfg:mode|(x,y)|(x,y,mode)
def clickWindowForMd5(hwnd, timeout, tgtHwnd, x, y, md5, clkCfg = None):
    def __clickWindowForMd5__(hwnd, x, y, md5):
        if isRawWindow(hwnd):
            return False
        if not topWindow(hwnd):
            return False
        rect = getWindowRect(hwnd)
        if not rect:
            return False
        if x < 0:
            x += rect[2]
        else:
            x += rect[0]
        if y < 0:
            y += rect[3]
        else:
            y += rect[1]
##        grabStr = autoio.grab(x - 5, y - 5, x + 6, y + 6).tostring()
        return autoutil.md5(grabStr) == md5
    cond = autoutil.Condition(__clickWindowForMd5__, tgtHwnd, x, y, md5)
    return clickWindowFor(hwnd, timeout, cond, clkCfg)

#µã»÷´°¿ÚµÈ´ý¸Ã´°¿ÚÇøÓòµÄÏñËØÆ¥Åämd5
#timeout:timeout|(timeout,interval)
#clkCfg:mode|(x,y)|(x,y,mode)
def clickWindowForMd5Self(hwnd, timeout, x, y, md5, clkCfg = None):
    return clickWindowForMd5(hwnd, timeout, hwnd, x, y, md5, clkCfg)

#²éÕÒµÚÒ»¸ö´°¿Ú£¨°üº¬²»¿É¼û¡¢²»¿ÉÓÃ¡¢×èÈû£©
#title:text,class,ctrlid
#parentTitle:None,hwnd,text,class
def findRawWindow(title, parentTitle = None):
    return findWindows(title, parentTitle, True, True)

#²éÕÒ´°¿Ú£¨°üº¬²»¿É¼û¡¢²»¿ÉÓÃ¡¢×èÈû£©
#title:text,class,ctrlid
#parentTitle:None,hwnd,text,class
def findRawWindows(title, parentTitle = None):
    return findWindows(title, parentTitle, True)

#²éÕÒµÚÒ»¸ö´°¿Ú
#title:text,class,ctrlid
#parentTitle:None,hwnd,text,class
def findWindow(title, parentTitle = None, isRaw = False):
    return findWindows(title, parentTitle, isRaw, True)

#²éÕÒ´°¿Ú
#title:text,class,ctrlid
#parentTitle:None,hwnd,text,class
def findWindows(title, parentTitle = None, isRaw = False, returnFirst = False):
    def __fillWindowAttrs__(hwnd, rst):
        if not returnFirst:
            rst.add(hwnd)
        elif __matchWindow__(hwnd, title):
            rst.add(hwnd)
    def __enumChildWindows__(hwnd, hwnds):
        hwnds.add(hwnd)
        rst = set()
        if not hwnd:
            autoutil.tryExcept(win32gui.EnumWindows, __fillWindowAttrs__, rst)
        else:
            autoutil.tryExcept(win32gui.EnumChildWindows, hwnd, __fillWindowAttrs__, rst)
            crst = set()
            for hcwnd in rst:
                if hcwnd not in hwnds:
                    crst.update(__enumChildWindows__(hcwnd, hwnds))
            rst.update(crst)
        return rst
    def __findChildWindows__(hwnd, hwnds):
        hwnds.add(hwnd)
        rst = set()
        hcwnd = autoutil.tryExcept(win32gui.FindWindowEx, hwnd, None, None, None)
        while hcwnd and not autoutil.isExcept(hcwnd) and hcwnd not in hwnds:
            __fillWindowAttrs__(hcwnd, rst)
            if hwnd:
                rst.update(__findChildWindows__(hcwnd, hwnds))
            hcwnd = autoutil.tryExcept(win32gui.FindWindowEx, hwnd, hcwnd, None, None)
        return rst
    def __getChildWindows__(hwnd, hwnds):
        hwnds.add(hwnd)
        rst = set()
        hcwnd = autoutil.tryExcept(win32gui.GetWindow, hwnd or win32gui.GetDesktopWindow(), win32con.GW_CHILD)
        while hcwnd and not autoutil.isExcept(hcwnd) and hcwnd not in hwnds:
            __fillWindowAttrs__(hcwnd, rst)
            if hwnd:
                rst.update(__getChildWindows__(hcwnd, hwnds))
            hcwnd = autoutil.tryExcept(win32gui.GetWindow, hcwnd, win32con.GW_HWNDNEXT)
        return rst
    def __matchWindow__(hwnd, title):
        if not isRaw and isRawWindow(hwnd):
            return False
        if type(title) == int:
            return win32gui.GetDlgCtrlID(hwnd) == title
        text = re.split('(\r|\n)+', getWindowText(hwnd))[0].strip()
        if text == title or re.match('^' + title + '$', text, re.S):
            return True
        clazz = getWindowClass(hwnd).strip()
        if clazz == title or re.match('^' + title + '$', clazz, re.S):
            return True
        return False
    if not parentTitle:
        hpwndList = [None]
    elif type(parentTitle) == int:
        hpwndList = [parentTitle]
    else:
        hpwndList = findRawWindows(parentTitle)
    rst = set()
    for hpwnd in hpwndList:
        rst.update(__enumChildWindows__(hpwnd, set()))
        if returnFirst and rst:
            return rst.pop()
        rst.update(__findChildWindows__(hpwnd, set()))
        if returnFirst and rst:
            return rst.pop()
        rst.update(__getChildWindows__(hpwnd, set()))
        if returnFirst and rst:
            return rst.pop()
    if returnFirst:
        return 0
    else:
        lst = []
        for hwnd in rst:
            if __matchWindow__(hwnd, title):
                lst.append(hwnd)
        return lst

#»ñÈ¡×ÀÃæ³ß´ç
def getDesktopRect():
    return getWindowRect(win32gui.GetDesktopWindow())

#»ñÈ¡¸¸´°¿Ú
def getParentWindow(hwnd):
    hwnd = autoutil.tryExcept(win32gui.GetParent, hwnd)
    if not autoutil.isExcept(hwnd):
        return hwnd


#»ñÈ¡´°¿ÚÀàÃû
def getWindowClass(hwnd, buf = ctypes.create_string_buffer(1024)):
    size = ctypes.sizeof(buf)
    ctypes.memset(buf, 0, size)
    ctypes.windll.user32.GetClassNameA(hwnd, ctypes.addressof(buf), size)
    return buf.value.strip()

#»ñµÃ´°¿Ú³ß´ç
def getWindowRect(hwnd):
    rect = autoutil.tryExcept(win32gui.GetWindowRect, hwnd)
    if not autoutil.isExcept(rect):
        return rect
#»ñÈ¡´°¿Ú´óÐ¡
def getWindowSize(hwnd):
    rect = getWindowRect(hwnd)
    if not rect:
        return None
    return (rect[2]-rect[0], rect[3]-rect[1])
def findWindowWithSize(title ,size, parentTitle = None, isRaw = False):
    hs = findWindows(title, parentTitle, isRaw = isRaw)
    hs = filter(lambda h : getWindowSize(h) == size, hs)
    if hs:
        return hs[0]
    else:
        return None
#»ñÈ¡´°¿ÚÎÄ×Ö
def getWindowText(hwnd, buf = ctypes.create_string_buffer(1024)):
    #if ctypes.windll.kernel32.GetUserDefaultUILanguage() in 1081:# hindi  Ó¡¶ÈÓï»·¾³,²»Ö§³Ö·Çunicode
    ##if ctypes.windll.kernel32.GetUserDefaultUILanguage() in [1081,1028,3076,1066,2070,1025]:
    import auto360
    if auto360.getTSInstallPath():#Èç¹ûµ±Ç°»·¾³Îª¹ú¼Ê°æÎÀÊ¿£¬ÔòÍ³Ò»Ê¹ÓÃunicode±àÂë
        return getWindowTextW(hwnd)    
    size = ctypes.sizeof(buf)
    ctypes.memset(buf, 0, size)
    autoutil.tryExcept(win32gui.SendMessageTimeout, hwnd, win32con.WM_GETTEXT, size, buf, win32con.SMTO_ABORTIFHUNG, 30)
    return buf.value.strip()

#»ñÈ¡´°¿ÚÎÄ×Ö£¬²ÉÓÃutf-8±àÂë
def getWindowTextW(hwnd):
    #size = ctypes.windll.user32.GetWindowTextLengthW(hwnd) 
    #if size == 0:  # edit »ñÈ¡²»µ½³¤¶È
        #size = 1024
    #buf = ctypes.create_unicode_buffer(size +1 )
    #res = ctypes.windll.user32.GetWindowTextW(hwnd,buf,size+1)
    #if res:
        #return buf.value.encode('utf-8')
    size = 1024
    buf2 = ctypes.create_unicode_buffer(size +1 )
    autoutil.tryExcept(ctypes.windll.user32.SendMessageTimeoutW,hwnd,win32con.WM_GETTEXT,size + 1, buf2,win32con.SMTO_ABORTIFHUNG,20,None)
    return buf2.value.encode('utf-8')


#ÉèÖÃ´°¿ÚÎÄ×Ö
def setWindowText(hwnd, text):
    rst = autoutil.tryExcept(win32gui.SendMessageTimeout, hwnd, win32con.WM_SETTEXT, 0, text, win32con.SMTO_ABORTIFHUNG, 30)
    return not autoutil.isExcept(rst)

#ÅÐ¶ÏÊÇ·ñÎª·ÇÕý³£´°¿Ú
def isRawWindow(hwnd):
    return not win32gui.IsWindowVisible(hwnd) or not win32gui.IsWindowEnabled(hwnd) or ctypes.windll.user32.IsHungAppWindow(hwnd)

#»¹Ô­´°¿Ú
def normalWindow(hwnd):
    try:
        win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
    except:
        pass
        
#×î´ó»¯´°¿Ú
def maxWindow(hwnd):
    return win32gui.ShowWindow(hwnd, win32con.SW_SHOWMAXIMIZED) and topWindow(hwnd)

#×îÐ¡»¯´°¿Ú
def minWindow(hwnd):
    return win32gui.ShowWindow(hwnd, win32con.SW_SHOWMINIMIZED)

#ÏÔÊ¾Ä¬ÈÏ´°¿Ú
def showWindow(hwnd):
    return win32gui.ShowWindow(hwnd, win32con.SW_SHOWDEFAULT) and topWindow(hwnd)

#ÖÃ¶¥´°¿Ú
def topWindow(hwnd):
    ret = win32gui.GetWindowLong(hwnd,win32con.GWL_EXSTYLE)
    if ret & win32con.WS_EX_TOPMOST:
        return True
    hwndList = [hwnd]
    while True:
        hwnd = getParentWindow(hwnd)
        if not hwnd:
            break
        hwndList.append(hwnd)
    topHwnd = None
    while len(hwndList) > 0:
        hwnd = hwndList.pop()
        if not isRawWindow(hwnd):
            topHwnd = hwnd
            break
    if not topHwnd:
        return False
    place = autoutil.tryExcept(win32gui.GetWindowPlacement, topHwnd)
    if autoutil.isExcept(place):
        return False
    if place[1] == win32con.SW_SHOWMINIMIZED and not showWindow(topHwnd):
        return False
    hwnd = win32gui.GetForegroundWindow()
    if hwnd == topHwnd:
        return True
    rst = autoutil.tryExcept(win32gui.SetForegroundWindow, topHwnd)
    if not autoutil.isExcept(rst):
        return True
    return getWindowClass(hwnd) == 'Progman' and getWindowText(hwnd) == 'Program Manager'

def moveWindow(hwnd, x, y):
    left, top, right, bottom = getWindowRect(hwnd)
    w = right - left
    h = bottom - top
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x, y, w, h, 0)
    return True

def moveWindowByClick(hwnd, x, y):
    topWindow(hwnd)
    a = 10
    while a:
        left, top, right, bottom = getWindowRect(hwnd)
        if left == x and right == y:
            break
        pos = left+(right-left)/2, top+10
        autoinput.moveMouse(pos[0], pos[1])
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        autoinput.moveMouse(x+(right-left)/2, y)
        time.sleep(0.1)
        a -= 1
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

#ÏÔÊ¾ÏûÏ¢¿ò
def alertMessage(msg, text = '', style = win32con.MB_ICONINFORMATION):
    return win32gui.MessageBox(None, msg, text, style|win32con.MB_SYSTEMMODAL)

#ÏÔÊ¾´íÎó¿ò
def alertError(error, text = ''):
    return alertMessage(error, text, win32con.MB_ICONERROR)

#ÏÔÊ¾Ñ¡Ôñ¿ò
def alertChoice(choice, text = ''):
    return alertMessage(choice, text, win32con.MB_YESNO|win32con.MB_ICONQUESTION) == win32con.IDYES

def ClickOnMenuItemByText(text, button = "LEFT"):
    hwnd = win32gui.FindWindow("#32768", None)
    MN_GETHMENU = 0x01E1
    hmenu = win32gui.SendMessage(hwnd, MN_GETHMENU, 0, 0)
    icount = win32gui.GetMenuItemCount(hmenu)
    for i in xrange(icount):
        t = GetMenuItemString(i).decode("gbk").encode("UTF-8")
        #        print text, t
        if text == t:
            rect = rect = win32gui.GetMenuItemRect(hwnd, hmenu, i)[1]
            x = (rect[2] - rect[0]) / 2 + rect[0]
            y = (rect[3] - rect[1]) / 2 + rect[1]
            MouseClick(x, y, button)
            return True

    return False
def MouseClick(x, y, button = "LEFT"):
    SCREENRANGE = 65536
    cx = 1366
    cy = 768
    x = x * SCREENRANGE / cx
    y = y * SCREENRANGE / cy

    if "RIGHT" == button:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN + win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP + win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, x, y)
    else:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN + win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP + win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, x, y)
def ClickOnMenuItem(idx, button = "LEFT"):
    hwnd = win32gui.FindWindow("#32768", None)
    MN_GETHMENU = 0x01E1
    hmenu = win32gui.SendMessage(hwnd, MN_GETHMENU, 0, 0)
    icount = win32gui.GetMenuItemCount(hmenu)
    if idx < 0:
        idx += icount
    rect = win32gui.GetMenuItemRect(hwnd, hmenu, idx)[1]
    x = (rect[2] - rect[0]) / 2 + rect[0]
    y = (rect[3] - rect[1]) / 2 + rect[1]

    MouseClick(x, y, button)
def GetMenuItemCount():
    hwnd = win32gui.FindWindow("#32768", None)
    MN_GETHMENU = 0x01E1
    hmenu = win32gui.SendMessage(hwnd, MN_GETHMENU, 0, 0)
    icount = win32gui.GetMenuItemCount(hmenu)
    return icount

if __name__ == "__main__":
    #t = findWindow("WTL_TabbedMDICommandBar", "RegWorkshopWndClass")
    ##topWindow(t)
    #l, t, r, b = getWindowRect(t)
    #print l, t
    #autoinput.moveMouse(l+25, t+15)
    #autoinput.clickMouse(l+25, t+15)
    #time.sleep(1)
    ##autoinput.clickMouse(l+25, t+15)
    #clickWindow(l+25, t+25)
    #print normalWindow(0x22B4E)
    hwnds = findWindows('CabinetWClass')

    subprocess.Popen(r"explorer /select," + r"C:\www.txt")
    time.sleep(5)
    hwnds_2 = findWindows('CabinetWClass')

    hwnds_find = list(set(hwnds_2).difference(set(hwnds)))
    if len(hwnds_find) == 1:

        print 'right'
        target_wnd = hwnds_find[0]
        print target_wnd

        topWindow(target_wnd)
        clickWindow(target_wnd,(40,15))

        win32api.keybd_event(0xA0,0,0,0)
        win32api.keybd_event(0x79,0,0,0)
        time.sleep(0.05)

        win32api.keybd_event(0xA0, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(0x79, 0, win32con.KEYEVENTF_KEYUP, 0)

        
        for _ in range(16):
            win32api.keybd_event(0x28,0,0,0)
            win32api.keybd_event(0x28,0,win32con.KEYEVENTF_KEYUP,0)
            time.sleep(0.05)
        
        
        win32api.keybd_event(0x27, 0, 0, 0)
        win32api.keybd_event(0x27, 0, win32con.KEYEVENTF_KEYUP, 0)

        time.sleep(3)
        
        for _ in range(8):
            win32api.keybd_event(0x28,0,0,0)
            win32api.keybd_event(0x28,0,win32con.KEYEVENTF_KEYUP,0)
            time.sleep(0.05)
        
        win32api.keybd_event(0x0D, 0, 0, 0)
        win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)