#!/usr/bin/env python3
# The MIT License (MIT)
# Copyright (c) 2019 ezflash
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.


__version__ = "0.1-dev"


import logging 
import sys
from pathlib import Path

from ezFlashCLI.ezFlash.pyjlink import *
from ezFlashCLI.ezFlash.smartbond.smartbondDevices import *

import argparse


class ezFlashCLI():


    def __init__(self):

        # parse the command line arguments
        self.argument_parser()

        # load the flash database
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'flash_database.json')) as json_file:
            self.flash_db = json.load(json_file)

            json_file.close()
        

        # set the verbosity
        if self.args.verbose:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)
            

        #list the jlink interfaces
        if self.args.version:
            logging.info("{}".format(__version__))
            sys.exit(0)

        #using JLINK for operations
        if not self.args.port:
            self.link = pyjlink()
            self.link.init()
            self.rawdevicelist = self.link.browse()

            if self.rawdevicelist is None:
                logging.error("No JLink device found")
                return
            self.devicelist = []
            for device in self.rawdevicelist:
                if device.SerialNumber != 0:
                    self.devicelist.append(device)



            if len(self.devicelist) > 1 and not self.args.jlink and self.args.operation != 'list':
                logging.error("JLink interface must be selected using -j option")
                self.display_jlink_devices()
                sys.exit(1)

        #list the jlink interfaces
        if self.args.operation == 'list':
            self.display_jlink_devices()

        elif self.args.operation == 'probe':
            self.probeDevice()

            print("Smartbond chip: {}".format(SMARTBOND_PRETTY_IDENTIFIER[self.deviceType]))


            print('Flash information:')
            self.probeFlash()
            if  not self.flashid is None:
                print("  - Device Id: {}".format(self.flashid['name']))
            else:
                print("  - Device Id: {}".format("Not Found"))

            # # check the flash header
            # if self.flashid:
            #     print("  - Product header programmed: {}".format(self.flashProductHeaderIsCorrect()))


        elif self.args.operation == 'erase_flash':
            self.probeDevice()
            da =  eval(self.deviceType)()
            da.connect(self.args.jlink)
            if da.flash_erase():
                print("Flash erase success")

            else:
                logging.error("Flash erase failed")
        
        elif self.args.operation == 'write_flash':

            with open(self.args.filename,'rb') as fp:
                fileData = fp.read()
                logging.info('Program file size {}'.format(len(fileData)))
                self.probeDevice()
                da =  eval(self.deviceType)()
                da.connect(self.args.jlink)
                da.link.reset()
                da.flash_program_data(fileData,self.args.addr)
                fp.close()


        elif self.args.operation ==  'image_flash':

            try: 
                fp  = open(self.args.filename,'rb')
            except:
                logging.error("Failed to open {}".format(self.args.filename))
                return

            self.probeDevice()
            self.probeFlash()
            self.da =  eval(self.deviceType)()
            self.da.connect(self.args.jlink)
            fileData = fp.read()
            fp.close()
            self.da.flash_program_image(fileData,self.flashid)
                
        elif self.args.operation == 'product_header_check':
            ''' Performs sanity check on the product header
                it will verify the content is consistent with the probed flash

                Args:
                    None
                    
                Returns:
                    True if the Header is consistent with the attached flash

            '''

            self.probeDevice()
            self.probeFlash()
            da =  eval(self.deviceType)()

            productHeaderCalculated = self.calculateProductHeader()

            self.da.connect(self.args.jlink)
            self.da.flash_configure_controller(self.flashid)
            productHeader = self.da.read_product_header()
            

            # print(productHeader,productHeaderCalculated)
            if productHeaderCalculated == productHeader:
                logging.info("Product header OK")
            else:
                logging.error("Product header mismatch")

        else:
            self.parser.print_help(sys.stderr)
        sys.exit(0)

    def probeDevice(self):
        try:
            self.deviceType = SMARTBOND_IDENTIFIER[self.link.connect(self.args.jlink)]
            self.link.close()

        except Exception as inst:
            logging.error("Device not responding: {}".format(inst))
            sys.exit(1)
    
    def probeFlash(self):
        # look for attached flash
        try:
            self.da =  eval(self.deviceType)()
            self.da.connect(self.args.jlink)
            self.da.flash_init()
            dev = self.da.flash_probe()
            self.flashid = self.da.get_flash(dev,self.flash_db)
            self.da.link.close()
            return self.flashid
        except Exception as inst:
            logging.error("No Flash detected {}".format(inst))

        return None
        

    def calculateProductHeader(self):
        return(self.da.make_product_header(self.flashid['flash_burstcmda_reg_value'], \
            self.flashid['flash_burstcmdb_reg_value'], \
            self.flashid['flash_write_config_command'] ))

    def display_jlink_devices(self):
        print('JLink devices:')
        for device in self.devicelist:
            if device.SerialNumber != 0:
                print("  - {}".format(device.SerialNumber))

    def argument_parser(self):
        """ Initializes the arguments passed from the command line 
        
        """    
        self.parser = argparse.ArgumentParser(description='Smartbond tool v%s - Dialog Smartbond devices flash management tool' % __version__,prog='ezFlashCLI')


        self.parser.add_argument('-c','--chip', 
                        help='Smartbond chip version',
                        choices=['auto','DA14531', 'DA14580', 'DA14585', 'DA14681',  'DA14683', 'DA1469x' ],
                        default=os.environ.get('SMARTBOND_CHIP', 'auto'))

        self.parser.add_argument('-p','--port', 
                        help='Serial port device',
                        default=os.environ.get('SMARTBOND_PORT', None))

        self.parser.add_argument('-j','--jlink', 
                        help='JLink device identifier',
                        default=os.environ.get('SMARTBOND_JLINK_ID', None))

        self.parser.add_argument("-v","--verbose", help="increase verbosity",action='store_true')
        self.parser.add_argument("--version", help="return version number",action='store_true')

        self.subparsers = self.parser.add_subparsers(dest='operation',help='Run  {command} -h for additional help')

        self.subparsers.add_parser('list',help="list JLink interfaces")
        self.subparsers.add_parser('probe',help='Perform Chip detection and its associated flash')

        self.subparsers.add_parser('erase_flash',help='Perform Chip Erase on SPI/QSPI flash')

        flash_parser = self.subparsers.add_parser('write_flash',help='Write binary file at specified address')

        flash_parser.add_argument('addr',type=lambda x: int(x,0), help='Address in the flash area')
        flash_parser.add_argument('filename', help='Binary file path')

        flash_parser = self.subparsers.add_parser('image_flash',help='Write the flash binary')
        flash_parser.add_argument('filename', help='Binary file path')

        flash_parser = self.subparsers.add_parser('product_header_check',help='Read the product header and check')


        self.args = self.parser.parse_args()


if __name__ == "__main__":
    
    ezFlashCLI()
    
    pass
