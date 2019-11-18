#!/usr/bin/env python
"""
areaDetector Display

"""
import os
import sys
import time
import json
from functools import partial
from collections import namedtuple

import numpy as np
import matplotlib.cm as colormap

import wx
import wx.lib.mixins.inspection

from wxmplot.plotframe import PlotFrame

import epics
from epics import get_pv
from epics.wx import (DelayedEpicsCallback, EpicsFunction)

from ..utils import MoveToDialog, normalize_pvname, get_pvdesc

from wxutils import (GridPanel, SimpleText, MenuItem, OkCancel, Popup,
                     FileOpen, SavedParameterDialog, Font, FloatSpin)

try:
    from epicsscan.scandb import ScanDB, InstrumentDB
except ImportError:
    ScanDB = InstrumentDB = None

from .contrast_control import ContrastControl
from .xrd_integrator import XRD_Integrator
from .imagepanel import ADMonoImagePanel, ThumbNailImagePanel
from .pvconfig import PVConfigPanel
from .ad_config import ADConfig, CONFFILE, get_default_configfile
from ..utils import SelectWorkdir, get_icon

labstyle = wx.ALIGN_LEFT|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL
rlabstyle = wx.ALIGN_RIGHT|wx.RIGHT|wx.TOP|wx.EXPAND
txtstyle = wx.ALIGN_LEFT|wx.ST_NO_AUTORESIZE|wx.TE_PROCESS_ENTER

class ADFrame(wx.Frame):
    """
    AreaDetector Display Frame
    """
    def __init__(self, configfile=None, prompt=False, calibration_callback=None):
        wx.Frame.__init__(self, None, -1, 'AreaDetector Viewer',
                          style=wx.DEFAULT_FRAME_STYLE)

        if configfile is None:
            configfile = get_default_configfile(CONFFILE)
        if prompt or configfile is None:
            default_file = configfile or CONFFILE
            fpath, fname = os.path.split(default_file)
            wcard = 'Detector Config Files (*.yaml)|*.yaml|All files (*.*)|*.*'
            configfile = FileOpen(self, "Read Detector Configuration File",
                                  default_file=fname,
                                  default_dir=fpath,
                                  wildcard=wcard)
        if configfile is None:
            sys.exit()

        self.read_config(fname=configfile)
        try:
            os.chdir(self.config.get('workdir', os.getcwd()))
        except:
            pass

        if prompt:
            ret = SelectWorkdir(self)
            if ret is None:
                self.Destroy()
            os.chdir(ret)

        self.SetTitle(self.config['title'])

        self.calib = None
        self.ad_img = None
        self.ad_cam = None
        self.lineplotter = None
        self.integrator = None
        self.int_panel = None
        self.int_lastid = None
        self.contrast_levels = None
        self.thumbnail = None

        self.buildMenus()
        self.buildFrame()

    def read_config(self, fname=None):
        "read config file"
        self.configfile = ADConfig(fname=fname)
        cnf = self.config = self.configfile.config
        if 'general' in cnf:
            for key, val in cnf['general'].items():
                cnf[key] = val
        self.prefix = cnf['prefix']
        self.fname = cnf['name']
        self.fsaver = cnf['filesaver']
        self.colormode = cnf['colormode'].lower()
        self.cam_attrs = cnf['camera_attributes']
        self.img_attrs = cnf['image_attributes']
        self.epics_controls = cnf.get('epics_controls', [])
        self.scandb_instname = cnf.get('scandb_instrument', None)
        self.connect_scandb()

    def connect_scandb(self):
        self.scandb_choices = []
        if self.scandb_instname is not None:
            self.scandb = self.instdb = None
            try:
                self.scandb = ScanDB()
            except:
                self.scandb_instname = None
                return

        self.instdb = InstrumentDB(self.scandb)
        try:
            poslist = self.instdb.get_positionlist(self.scandb_instname)
            self.scandb_choices = poslist
        except:
            pass

    def buildFrame(self):
        self.SetFont(Font(10))

        sbar = self.CreateStatusBar(3, wx.CAPTION)
        self.SetStatusWidths([-1, -1, -1])
        self.SetStatusText('',0)

        sizer = wx.GridBagSizer(3, 3)
        panel = self.panel = wx.Panel(self)
        pvpanel = PVConfigPanel(panel, self.prefix, self.epics_controls)

        wsize = (100, -1)
        lsize = (250, -1)

        start_btn = wx.Button(panel, label='Start',    size=wsize)
        stop_btn  = wx.Button(panel, label='Stop',     size=wsize)
        start_btn.Bind(wx.EVT_BUTTON, partial(self.onButton, key='start'))
        stop_btn.Bind(wx.EVT_BUTTON,  partial(self.onButton, key='stop'))

        self.contrast = ContrastControl(panel, callback=self.set_contrast_level)
        self.imagesize = wx.StaticText(panel, label='? x ?',
                                       size=(150, 30), style=txtstyle)


        def lin(len=200, wid=2, style=wx.LI_HORIZONTAL):
            return wx.StaticLine(panel, size=(len, wid), style=style)

        irow = 0
        sizer.Add(start_btn, (irow, 0), (1, 1), labstyle)
        sizer.Add(stop_btn,  (irow, 1), (1, 1), labstyle)
        if self.config.get('show_free_run', False):
            free_btn  = wx.Button(panel, label='Free Run', size=wsize)
            free_btn.Bind(wx.EVT_BUTTON,  partial(self.onButton, key='free'))
            irow += 1
            sizer.Add(free_btn,  (irow, 0), (1, 2), labstyle)

        irow += 1
        sizer.Add(pvpanel,  (irow, 0), (1, 3), labstyle)

        if self.scandb_instname is not None and len(self.scandb_choices) > 1:
            irow += 1
            self.scandb_sel = wx.Choice(panel, size=(80, -1),
                                           choices=self.scandb_choices)
            self.scandb_sel.SetSelection(0)
            scandb_btn = wx.Button(panel, label='Go To',  size=(55, -1))
            scandb_btn.Bind(wx.EVT_BUTTON, self.onInstrumentGo)
            sizer.Add(SimpleText(panel, " %s:" % self.scandb_instname),
                      (irow, 0), (1, 1), labstyle)
            sizer.Add(self.scandb_sel, (irow, 1), (1, 1), labstyle)
            sizer.Add(scandb_btn,      (irow, 2), (1, 1), labstyle)


        irow += 1
        sizer.Add(lin(200, wid=4),  (irow, 0), (1, 3), labstyle)

        irow += 1
        sizer.Add(self.imagesize, (irow, 0), (1, 3), labstyle)

        if self.colormode.startswith('mono'):
            self.cmap_choice = wx.Choice(panel, size=(80, -1),
                                         choices=self.config['colormaps'])
            self.cmap_choice.SetSelection(0)
            self.cmap_choice.Bind(wx.EVT_CHOICE,  self.onColorMap)
            self.cmap_reverse = wx.CheckBox(panel, label='Reverse', size=(60, -1))
            self.cmap_reverse.Bind(wx.EVT_CHECKBOX,  self.onColorMap)

            irow += 1
            sizer.Add(wx.StaticText(panel, label='Color Map: '),
                      (irow, 0), (1, 1), labstyle)

            sizer.Add(self.cmap_choice,  (irow, 1), (1, 1), labstyle)
            sizer.Add(self.cmap_reverse, (irow, 2), (1, 1), labstyle)

        irow += 1
        sizer.Add(self.contrast.label,  (irow, 0), (1, 1), labstyle)
        sizer.Add(self.contrast.choice, (irow, 1), (1, 1), labstyle)

        if self.config['show_1dintegration']:
            self.show1d_btn = wx.Button(panel, label='Show 1D Integration',
                                         size=(200, -1))
            self.show1d_btn.Bind(wx.EVT_BUTTON, self.onShowIntegration)
            self.show1d_btn.Disable()
            irow += 1
            sizer.Add(self.show1d_btn, (irow, 0), (1, 2), labstyle)

        if self.config['show_thumbnail']:
            t_size=self.config.get('thumbnail_size', 100)

            tnail = ThumbNailImagePanel(panel, imgsize=t_size,
                                        size=(300, 300),
                                        motion_writer=partial(self.write, panel=0))

            self.thumbnail = tnail
            label = wx.StaticText(panel, label='Thumbnail size (pixels): ',
                                       size=(200, -1), style=txtstyle)

            self.thumbsize = FloatSpin(panel, value=100, min_val=10, increment=5,
                                       action=self.onThumbSize,
                                       size=(150, -1), style=txtstyle)

            irow += 1
            sizer.Add(label,          (irow, 0), (1, 1), labstyle)
            sizer.Add(self.thumbsize, (irow, 1), (1, 1), labstyle)
            irow += 1
            sizer.Add(self.thumbnail, (irow, 0), (1, 2), labstyle)

        panel.SetSizer(sizer)
        sizer.Fit(panel)

        # image panel
        self.image = ADMonoImagePanel(self, prefix=self.prefix,
                                      rot90=self.config['default_rotation'],
                                      size=(750, 750),
                                      writer=partial(self.write, panel=1),
                                      thumbnail=self.thumbnail,
                                      motion_writer=partial(self.write, panel=2))

        mainsizer = wx.BoxSizer(wx.HORIZONTAL)
        mainsizer.Add(panel, 0, wx.LEFT|wx.GROW|wx.ALL)
        mainsizer.Add(self.image, 1, wx.CENTER|wx.GROW|wx.ALL)
        self.SetSizer(mainsizer)
        mainsizer.Fit(self)
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.SetAutoLayout(True)
        iconfile = self.config.get('iconfile', None)
        if not os.path.exists(iconfile):
            iconfile = get_icon('camera')
        try:
            self.SetIcon(wx.Icon(iconfile, wx.BITMAP_TYPE_ICO))
        except:
            pass
        self.connect_pvs()

    def onThumbSize(self, event=None):
        self.thumbnail.imgsize = int(self.thumbsize.GetValue())

    def onColorMap(self, event=None):
        cmap_name = self.cmap_choice.GetStringSelection()
        if self.cmap_reverse.IsChecked():
            cmap_name = cmap_name + '_r'
        self.image.colormap = getattr(colormap, cmap_name)
        self.image.Refresh()

    def onCopyImage(self, event=None):
        "copy bitmap of canvas to system clipboard"
        bmp = wx.BitmapDataObject()
        bmp.SetBitmap(wx.Bitmap(self.image.GrabWxImage()))
        wx.TheClipboard.Open()
        wx.TheClipboard.SetData(bmp)
        wx.TheClipboard.Close()
        wx.TheClipboard.Flush()

    def onReadCalibFile(self, event=None):
        "read calibration file"
        wcards = "Poni Files(*.poni)|*.poni|All files (*.*)|*.*"
        dlg = wx.FileDialog(None, message='Read Calibration File',
                            defaultDir=os.getcwd(),
                            wildcard=wcards,
                            style=wx.FD_OPEN)
        ppath = None
        if dlg.ShowModal() == wx.ID_OK:
            ppath = os.path.abspath(dlg.GetPath())

        if os.path.exists(ppath) and HAS_PYFAI:
            self.integrator = XRD_Integrator(ppath,
                                 calibration_callback=calibration_callback)
            self.show1d_btn.Enable(self.integrator.enabled)

    def onShowIntegration(self, event=None):
        if self.calib is None or self.integrator is None:
            return
        shown = False
        try:
            self.int_panel.Raise()
            shown = True
        except:
            self.int_panel = None
        if not shown:
            self.int_panel = PlotFrame(self)
        self.show_1dpattern(init=(not shown))

    def show_1dpattern(self, init=False):
        if self.calib is None or self.integrator is None:
            return

        img = self.ad_img.PV('ArrayData').get()

        h, w = self.image.GetImageSize()
        img.shape = (w, h)

        # may need to trim outer pixels (int1d_trimx/int1d_trimy in config)
        xstride = 1
        if self.config.get('int1d_flipx', False):
            xstride = -1

        xslice = slice(None, None, xstride)
        trimx = int(self.config.get('int1d_trimx', 0))
        if trimx != 0:
            xslice = slice(trimx*xstride, -trimx*xstride, xstride)

        ystride = 1
        if self.config.get('int1d_flipy', True):
            ystride = -1

        yslice = slice(None, None, ystride)
        trimy = int(self.config.get('int1d_trimy', 0))
        if trimy > 0:
            yslice = slice(trimy*ystride, -trimy*ystride, ystride)

        img = img[yslice, xslice]

        img_id = self.ad_cam.ArrayCounter_RBV
        title = 'Image %d' % img_id
        q, xi = self.integrator.integrate1d(img, 2048)
        if init:
            self.int_panel.plot(q, xi, xlabel=r'$Q (\rm\AA^{-1})$',
                                marker='+', title=title)
            self.int_panel.Raise()
            self.int_panel.Show()
        else:
            self.int_panel.update_line(0, q, xi, draw=True)
            self.int_panel.set_title(title)

    @EpicsFunction
    def onSaveImage(self, event=None):
        "prompts for and save image to file"
        defdir = os.getcwd()
        self.fname = "Image_%i.tiff"  % self.ad_cam.ArrayCounter_RBV
        dlg = wx.FileDialog(None, message='Save Image as',
                            defaultDir=os.getcwd(),
                            defaultFile=self.fname,
                            style=wx.FD_SAVE)
        path = None
        if dlg.ShowModal() == wx.ID_OK:
            path = os.path.abspath(dlg.GetPath())


        root, fname = os.path.split(path)
        epics.caput("%s%sFileName" % self.prefix, self.fsaver, fname)
        epics.caput("%s%sFileWriteMode" % self.prefix, self.fsaver, 0)
        time.sleep(0.05)
        epics.caput("%s%sWriteFile" % self.prefix, self.fsaver, 1)
        time.sleep(0.05)

        file_pv = "%s%sFullFileName_RBV" % (self.prefix, self.prefix)
        print("Saved image File ", epics.caget(file_pv,  as_string=True))

    def onSaveConf(self, event=None):
        fname = self.configfile.write(config=self.config, defaultfile=True)
        print("wrote %s" % fname)

    def onClose(self, event=None):
        ret = Popup(self, "Really Quit?", "Exit AreaDetector Viewer?",
                    style=wx.YES_NO|wx.NO_DEFAULT|wx.ICON_QUESTION)
        if wx.ID_YES == ret:
            self.config['workdir'] = os.path.abspath(os.getcwd())
            self.configfile.write(config=self.config)
            try:
                wx.Yield()
            except:
                pass
            self.Destroy()

    def onAbout(self, event=None):
        msg =  """areaDetector Display version 0.2
Matt Newville <newville@cars.uchicago.edu>"""

        dlg = wx.MessageDialog(self, msg, "About areaDetector Display",
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def buildMenus(self):
        fmenu = wx.Menu()
        MenuItem(self, fmenu, "&Save\tCtrl+S", "Save Image", self.onSaveImage)
        MenuItem(self, fmenu, "&Copy\tCtrl+C", "Copy Image to Clipboard",
                 self.onCopyImage)
        MenuItem(self, fmenu, "Read Calibration File", "Read PONI Calibration",
                 self.onReadCalibFile)
        MenuItem(self, fmenu, "&Save Configuration\tCtrl+E",
                 "Save Configuration as Default", self.onSaveConf)
        fmenu.AppendSeparator()
        MenuItem(self, fmenu, "E&xit\tCtrl+Q",  "Exit Program", self.onClose)

        omenu = wx.Menu()
        MenuItem(self, omenu,  "&Rotate CCW\tCtrl+R", "Rotate Counter Clockwise", self.onRot90)
        MenuItem(self, omenu,  "Flip Up/Down\tCtrl+T", "Flip Up/Down", self.onFlipV)
        MenuItem(self, omenu,  "Flip Left/Right\tCtrl+F", "Flip Left/Right", self.onFlipH)
        MenuItem(self, omenu,  "Reset Rotations and Flips", "Reset", self.onResetRotFlips)
        omenu.AppendSeparator()

        hmenu = wx.Menu()
        MenuItem(self, hmenu, "About", "About areaDetector Display", self.onAbout)

        mbar = wx.MenuBar()
        mbar.Append(fmenu, "File")
        mbar.Append(omenu, "Options")

        mbar.Append(hmenu, "&Help")
        self.SetMenuBar(mbar)

    def onResetRotFlips(self, event):
        self.image.rot90 = 0
        self.image.flipv = self.image.fliph = False

    def onRot90(self, event):
        self.image.rot90 = (self.image.rot90 - 1) % 4

    def onFlipV(self, event):
        self.image.flipv= not self.image.flipv

    def onFlipH(self, event):
        self.image.fliph = not self.image.fliph

    def set_contrast_level(self, contrast_level=0):
        self.image.contrast_levels = [contrast_level, 100.0-contrast_level]
        self.image.Refresh()

    def write(self, s, panel=0):
        """write a message to the Status Bar"""
        self.SetStatusText(text=s, number=panel)

    def onInstrumentGo(self, event=None):
        posname = self.scandb_sel.GetStringSelection()
        instname = self.scandb_instname

        # pre-load to make sure the PVs are connected
        for pv in self.instdb.get_instrument(instname).pv:
            pvname = normalize_pvname(pv.name)
            get_pv(pvname)
            get_pvdesc(pvname)

        pos = self.instdb.get_position(instname, posname)
        time.sleep(0.005)

        pvdata = {}
        for pvpos in pos.pv:
            pvname = normalize_pvname(pvpos.pv.name)
            save_val = pvpos.value
            curr_val = get_pv(pvname).get(as_string=True)
            desc = get_pvdesc(pvname)
            pvdata[pvname] = (desc, save_val, curr_val)

        def GoCallback(pvdata):
            for pvname, sval in pvdata.items():
                get_pv(pvname).put(sval)
        m2d = MoveToDialog(self, pvdata, instname, posname,
                           callback=GoCallback)
        m2d.Raise()

    @EpicsFunction
    def onButton(self, event=None, key='free'):
        key = key.lower()
        if key.startswith('free'):
            ftime = self.config['free_run_time']
            self.image.restart_fps_counter()
            self.ad_cam.AcquireTime   = ftime
            self.ad_cam.AcquirePeriod = ftime
            self.ad_cam.NumImages = int((3*86400.)/ftime)
            self.ad_cam.Acquire = 1
        elif key.startswith('start'):
            self.image.restart_fps_counter()
            self.ad_cam.Acquire = 1
        elif key.startswith('stop'):
            self.ad_cam.Acquire = 0

    @EpicsFunction
    def connect_pvs(self, verbose=True):
        if self.prefix is None or len(self.prefix) < 2:
            return
        self.write('Connecting to areaDetector %s' % self.prefix)

        self.ad_img = epics.Device(self.prefix + 'image1:', delim='',
                                   attrs=self.img_attrs)
        self.ad_cam = epics.Device(self.prefix + 'cam1:', delim='',
                                   attrs=self.cam_attrs)

        if self.config['use_filesaver']:
            epics.caput("%s%sEnableCallbacks" % (self.prefix, self.fsaver), 1)
            epics.caput("%s%sAutoSave" % (self.prefix, self.fsaver), 0)
            epics.caput("%s%sAutoIncrement" % (self.prefix, self.fsaver), 0)
            epics.caput("%s%sFileWriteMode" % (self.prefix, self.fsaver), 0)

        time.sleep(0.002)
        if not self.ad_img.PV('UniqueId_RBV').connected:
            epics.poll()
            if not self.ad_img.PV('UniqueId_RBV').connected:
                self.write('Warning: detector seems to not be connected!')
                return
        if verbose:
            self.write('Connected to detector %s' % self.prefix)

        self.SetTitle("Epics areaDetector Display: %s" % self.prefix)

        sizex = self.ad_cam.MaxSizeX_RBV
        sizey = self.ad_cam.MaxSizeY_RBV

        sizelabel = 'Image Size: %i x %i pixels'
        try:
            sizelabel = sizelabel  % (sizex, sizey)
        except:
            sizelabel = sizelabel  % (0, 0)

        self.imagesize.SetLabel(sizelabel)

        self.ad_cam.add_callback('DetectorState_RBV',  self.onDetState)
        self.contrast.set_level_str('0.01')

    @DelayedEpicsCallback
    def onDetState(self, pvname=None, value=None, char_value=None, **kw):
        self.write(char_value, panel=0)

class areaDetectorApp(wx.App, wx.lib.mixins.inspection.InspectionMixin):
    def __init__(self, configfile=None, prompt=False, **kws):
        self.configfile = configfile
        self.prompt = prompt
        wx.App.__init__(self, **kws)

    def createApp(self):
        frame = ADFrame(configfile=self.configfile, prompt=self.prompt)
        frame.Show()
        self.SetTopWindow(frame)

    def OnInit(self):
        self.createApp()
        return True
