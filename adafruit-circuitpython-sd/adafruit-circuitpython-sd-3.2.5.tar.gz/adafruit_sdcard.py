# The MIT License (MIT)
#
# Copyright (c) 2014-2016 Damien George, Peter Hinch and Radomir Dopieralski
# Copyright (c) 2017 Scott Shawcroft for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_sdcard` - SD card over SPI driver
====================================================

CircuitPython driver for SD cards using SPI bus.

Requires an SPI bus and a CS pin.  Provides readblocks and writeblocks
methods so the device can be mounted as a filesystem.

* Author(s): Scott Shawcroft

Implementation Notes
--------------------

**Hardware:**

* Adafruit `MicroSD card breakout board+
  <https://www.adafruit.com/product/254>`_ (Product ID: 254)

* Adafruit `Assembled Data Logging shield for Arduino
  <https://www.adafruit.com/product/1141>`_ (Product ID: 1141)

* Adafruit `Feather M0 Adalogger
  <https://www.adafruit.com/product/2796>`_ (Product ID: 2796)

* Adalogger `FeatherWing - RTC + SD Add-on For All Feather Boards
  <https://www.adafruit.com/product/2922>`_ (Product ID: 2922)

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the ESP8622 and M0-based boards:
  https://github.com/adafruit/circuitpython/releases
* Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
"""

import time
from micropython import const
from adafruit_bus_device import spi_device

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_SD.git"

_CMD_TIMEOUT = const(200)

_R1_IDLE_STATE = const(1 << 0)
#R1_ERASE_RESET = const(1 << 1)
_R1_ILLEGAL_COMMAND = const(1 << 2)
#R1_COM_CRC_ERROR = const(1 << 3)
#R1_ERASE_SEQUENCE_ERROR = const(1 << 4)
#R1_ADDRESS_ERROR = const(1 << 5)
#R1_PARAMETER_ERROR = const(1 << 6)
_TOKEN_CMD25 = const(0xfc)
_TOKEN_STOP_TRAN = const(0xfd)
_TOKEN_DATA = const(0xfe)

#pylint: disable-msg=superfluous-parens
class SDCard:
    """Controls an SD card over SPI.

        :param ~busio.SPI spi: The SPI bus
        :param ~digitalio.DigitalInOut cs: The chip select connected to the card
        :param int baudrate: The SPI data rate to use after card setup

        Example usage:

        .. code-block:: python

            import busio
            import storage
            import adafruit_sdcard
            import os
            import board

            spi = busio.SPI(SCK, MOSI, MISO)
            sd = adafruit_sdcard.SDCard(spi, board.SD_CS)
            vfs = storage.VfsFat(sdcard)
            storage.mount(vfs, '/sd')
            os.listdir('/')

        """
    def __init__(self, spi, cs, baudrate=1320000):
        # This is the init baudrate.
        # We create a second device with the target baudrate after card initialization.
        self._spi = spi_device.SPIDevice(spi, cs, baudrate=250000, extra_clocks=8)

        self._cmdbuf = bytearray(6)
        self._single_byte = bytearray(1)

        # Card is byte addressing, set to 1 if addresses are per block
        self._cdv = 512

        # initialise the card and switch to high speed
        self._init_card(baudrate)

    def _clock_card(self, cycles=8):
        """
        Clock the bus a minimum of `cycles` with the chip select high.

        :param int cycles: The minimum number of clock cycles to cycle the bus.
        """
        while not self._spi.spi.try_lock():
            pass
        self._spi.spi.configure(baudrate=self._spi.baudrate)
        self._spi.chip_select.value = True

        self._single_byte[0] = 0xff
        for _ in range(cycles // 8 + 1):
            self._spi.spi.write(self._single_byte)
        self._spi.spi.unlock()

    def _init_card(self, baudrate):
        """Initialize the card in SPI mode."""
        # clock card at least cycles with cs high
        self._clock_card(80)

        with self._spi as card:
            # CMD0: init card; should return _R1_IDLE_STATE (allow 5 attempts)
            for _ in range(5):
                if self._cmd(card, 0, 0, 0x95) == _R1_IDLE_STATE:
                    break
            else:
                raise OSError("no SD card")

            # CMD8: determine card version
            rb7 = bytearray(4)
            r = self._cmd(card, 8, 0x01aa, 0x87, rb7, data_block=False)
            if r == _R1_IDLE_STATE:
                self._init_card_v2(card)
            elif r == (_R1_IDLE_STATE | _R1_ILLEGAL_COMMAND):
                self._init_card_v1(card)
            else:
                raise OSError("couldn't determine SD card version")

            # get the number of sectors
            # CMD9: response R2 (R1 byte + 16-byte block read)
            csd = bytearray(16)
            if self._cmd(card, 9, 0, 0xaf, response_buf=csd) != 0:
                raise OSError("no response from SD card")
            #self.readinto(csd)
            csd_version = (csd[0] & 0xc0) >> 6
            if csd_version >= 2:
                raise OSError("SD card CSD format not supported")

            if csd_version == 1:
                self._sectors = ((csd[8] << 8 | csd[9]) + 1) * 1024
            else:
                block_length = 2 ** (csd[5] & 0xf)
                c_size = ((csd[6] & 0x3) << 10) | (csd[7] << 2) | ((csd[8] & 0xc) >> 6)
                mult = 2 ** (((csd[9] & 0x3) << 1 | (csd[10] & 0x80) >> 7) + 2)
                self._sectors = block_length // 512 * mult * (c_size + 1)

            # CMD16: set block length to 512 bytes
            if self._cmd(card, 16, 512, 0x15) != 0:
                raise OSError("can't set 512 block size")

        # set to high data rate now that it's initialised
        self._spi = spi_device.SPIDevice(self._spi.spi, self._spi.chip_select,
                                         baudrate=baudrate, extra_clocks=8)

    def _init_card_v1(self, card):
        """Initialize v1 SDCards which use byte addressing."""
        for _ in range(_CMD_TIMEOUT):
            self._cmd(card, 55, 0, 0)
            if self._cmd(card, 41, 0, 0) == 0:
                #print("[SDCard] v1 card")
                return
        raise OSError("timeout waiting for v1 card")

    def _init_card_v2(self, card):
        """Initialize v2 SDCards which use 512-byte block addressing."""
        ocr = bytearray(4)
        for _ in range(_CMD_TIMEOUT):
            time.sleep(.050)
            self._cmd(card, 58, 0, 0xfd, response_buf=ocr, data_block=False)
            self._cmd(card, 55, 0, 0x65)
            # On non-longint builds, we cannot use 0x40000000 directly as the arg
            # so break it into bytes, which are interpreted by self._cmd().
            if self._cmd(card, 41, b'\x40\x00\x00\x00', 0x77) == 0:
                self._cmd(card, 58, 0, 0xfd, response_buf=ocr, data_block=False)

                # Check for block addressing
                if (ocr[0] & 0x40) != 0:
                    self._cdv = 1
                #print("[SDCard] v2 card")
                return
        raise OSError("timeout waiting for v2 card")

    def _wait_for_ready(self, card, timeout=0.3):
        """
        Wait for the card to clock out 0xff to indicate its ready.

        :param busio.SPI card: The locked SPI bus.
        :param float timeout: Maximum time to wait in seconds.
        """
        start_time = time.monotonic()
        self._single_byte[0] = 0x00
        while time.monotonic() - start_time < timeout and self._single_byte[0] != 0xff:
            card.readinto(self._single_byte, write_value=0xff)

    # pylint: disable-msg=too-many-arguments
    # pylint: disable=no-member
    # no-member disable should be reconsidered when it can be tested
    def _cmd(self, card, cmd, arg=0, crc=0, response_buf=None, data_block=True, wait=True):
        """
        Issue a command to the card and read an optional data response.

        :param busio.SPI card: The locked SPI bus.
        :param int cmd: The command number.
        :param int|buf(4) arg: The command argument
        :param int crc: The crc to allow the card to verify the command and argument.
        :param bytearray response_buf: Buffer to read a data block response into.
        :param bool data_block: True if the response data is in a data block.
        """
        # create and send the command
        buf = self._cmdbuf
        buf[0] = 0x40 | cmd
        if isinstance(arg, int):
            buf[1] = (arg >> 24) & 0xff
            buf[2] = (arg >> 16) & 0xff
            buf[3] = (arg >> 8) & 0xff
            buf[4] = arg & 0xff
        elif len(arg) == 4:
            # arg can be a 4-byte buf
            buf[1:5] = arg
        else:
            raise ValueError()

        if (crc == 0):
            buf[5] = calculate_crc(buf[:-1])
        else:
            buf[5] = crc

        if wait:
            self._wait_for_ready(card)

        card.write(buf)

        # wait for the response (response[7] == 0)
        for _ in range(_CMD_TIMEOUT):
            card.readinto(buf, end=1, write_value=0xff)
            if not (buf[0] & 0x80):
                if response_buf:
                    if data_block:
                        # Wait for the start block byte
                        buf[1] = 0xff
                        while buf[1] != 0xfe:
                            card.readinto(buf, start=1, end=2, write_value=0xff)
                    card.readinto(response_buf, write_value=0xff)
                    if data_block:
                        # Read the checksum
                        card.readinto(buf, start=1, end=3, write_value=0xff)
                return buf[0]
        return -1
    #pylint: enable-msg=too-many-arguments

    # pylint: disable-msg=too-many-arguments
    def _block_cmd(self, card, cmd, block, crc, response_buf=None):
        """
        Issue a command to the card with a block argument.

        :param busio.SPI card: The locked SPI bus.
        :param int cmd: The command number.
        :param int block: The relevant block.
        :param int crc: The crc to allow the card to verify the command and argument.
        """
        if self._cdv == 1:
            return self._cmd(card, cmd, block, crc, response_buf=response_buf)

        # create and send the command
        buf = self._cmdbuf
        buf[0] = 0x40 | cmd
        # We address by byte because cdv is 512. Instead of multiplying, shift
        # the data to the correct spot so that we don't risk creating a long
        # int.
        buf[1] = (block >> 15) & 0xff
        buf[2] = (block >> 7) & 0xff
        buf[3] = (block << 1) & 0xff
        buf[4] = 0

        if (crc == 0):
            buf[5] = calculate_crc(buf[:-1])
        else:
            buf[5] = crc

        result = -1
        self._wait_for_ready(card)

        card.write(buf)

        # wait for the response (response[7] == 0)
        for _ in range(_CMD_TIMEOUT):
            card.readinto(buf, end=1, write_value=0xff)
            if not (buf[0] & 0x80):
                result = buf[0]
                break

        # pylint: disable=singleton-comparison
        # Disable should be removed when refactor can be tested.
        if response_buf != None and result == 0:
            self._readinto(card, response_buf)

        return result
    # pylint: enable-msg=too-many-arguments

    def _cmd_nodata(self, card, cmd, response=0xff):
        """
        Issue a command to the card with no argument.

        :param busio.SPI card: The locked SPI bus.
        :param int cmd: The command number.
        """
        buf = self._cmdbuf
        buf[0] = cmd
        buf[1] = 0xff

        card.write(buf, end=2)
        for _ in range(_CMD_TIMEOUT):
            card.readinto(buf, end=1, write_value=0xff)
            if buf[0] == response:
                return 0    # OK
        return 1 # timeout

    def _readinto(self, card, buf, start=0, end=None):
        """
        Read a data block into buf.

        :param busio.SPI card: The locked SPI bus.
        :param bytearray buf: The buffer to write into
        :param int start: The first index to write data at
        :param int end: The index after the last byte to write to.
        """
        if end is None:
            end = len(buf)

        # read until start byte (0xfe)
        buf[start] = 0xff #busy
        while buf[start] != 0xfe:
            card.readinto(buf, start=start, end=start+1, write_value=0xff)

        card.readinto(buf, start=start, end=end, write_value=0xff)

        # read checksum and throw it away
        card.readinto(self._cmdbuf, end=2, write_value=0xff)

    # pylint: disable-msg=too-many-arguments
    def _write(self, card, token, buf, start=0, end=None):
        """
        Write a data block to the card.

        :param busio.SPI card: The locked SPI bus.
        :param int token: The start token
        :param bytearray buf: The buffer to write from
        :param int start: The first index to read data from
        :param int end: The index after the last byte to read from.
        """
        cmd = self._cmdbuf
        if end is None:
            end = len(buf)

        self._wait_for_ready(card)

        # send: start of block, data, checksum
        cmd[0] = token
        card.write(cmd, end=1)
        card.write(buf, start=start, end=end)
        cmd[0] = 0xff
        cmd[1] = 0xff
        card.write(cmd, end=2)

        # check the response
        # pylint: disable=no-else-return
        # Disable should be removed when refactor can be tested
        for _ in range(_CMD_TIMEOUT):
            card.readinto(cmd, end=1, write_value=0xff)
            if not (cmd[0] & 0x80):
                if (cmd[0] & 0x1f) != 0x05:
                    return -1
                else:
                    break

        # wait for write to finish
        card.readinto(cmd, end=1, write_value=0xff)
        while cmd[0] == 0:
            card.readinto(cmd, end=1, write_value=0xff)

        return 0 # worked
    # pylint: enable-msg=too-many-arguments

    def count(self):
        """
        Returns the total number of sectors.

        :return: The number of 512-byte blocks
        :rtype: int
        """
        return self._sectors

    def readblocks(self, start_block, buf):
        """
        Read one or more blocks from the card

        :param int start_block: The block to start reading from
        :param bytearray buf: The buffer to write into. Length must be multiple of 512.
        """
        nblocks, err = divmod(len(buf), 512)
        assert nblocks and not err, 'Buffer length is invalid'
        with self._spi as card:
            if nblocks == 1:
                # CMD17: set read address for single block
                # We use _block_cmd to read our data so that the chip select line
                # isn't toggled between the command, response and data.
                if self._block_cmd(card, 17, start_block, 0, response_buf=buf) != 0:
                    return 1
            else:
                # CMD18: set read address for multiple blocks
                if self._block_cmd(card, 18, start_block, 0) != 0:
                    return 1
                offset = 0
                while nblocks:
                    self._readinto(card, buf, start=offset, end=(offset + 512))
                    offset += 512
                    nblocks -= 1
                ret = self._cmd(card, 12, 0, 0x61, wait=False)
                # return first status 0 or last before card ready (0xff)
                while ret != 0:
                    card.readinto(self._single_byte, write_value=0xff)
                    if self._single_byte[0] & 0x80:
                        return ret
                    ret = self._single_byte[0]
        return 0

    def writeblocks(self, start_block, buf):
        """
        Write one or more blocks to the card

        :param int start_block: The block to start writing to
        :param bytearray buf: The buffer to write into. Length must be multiple of 512.
        """
        nblocks, err = divmod(len(buf), 512)
        assert nblocks and not err, 'Buffer length is invalid'
        with self._spi as card:
            if nblocks == 1:
                # CMD24: set write address for single block
                if self._block_cmd(card, 24, start_block, 0) != 0:
                    return 1

                # send the data
                self._write(card, _TOKEN_DATA, buf)
            else:
                # CMD25: set write address for first block
                if self._block_cmd(card, 25, start_block, 0) != 0:
                    return 1
                # send the data
                offset = 0
                while nblocks:
                    self._write(card, _TOKEN_CMD25, buf, start=offset, end=(offset + 512))
                    offset += 512
                    nblocks -= 1
                self._cmd_nodata(card, _TOKEN_STOP_TRAN, 0x0)
        return 0

def _calculate_crc_table():
    """Precompute the table used in calculate_crc."""
    # Code converted from https://github.com/hazelnusse/crc7/blob/master/crc7.cc by devoh747
    # With permission from Dale Lukas Peterson <hazelnusse@gmail.com>
    # 8/6/2019

    crc_table = bytearray(256)
    crc_poly = const(0x89)  # the value of our CRC-7 polynomial

    # generate a table value for all 256 possible byte values
    for i in range(256):
        if (i & 0x80):
            crc_table[i] = i ^ crc_poly
        else:
            crc_table[i] = i
        for _ in range(1, 8):
            crc_table[i] = crc_table[i] << 1
            if (crc_table[i] & 0x80):
                crc_table[i] = crc_table[i] ^ crc_poly
    return crc_table

CRC_TABLE = _calculate_crc_table()

def calculate_crc(message):
    """
    Calculate the CRC of message[0:5], using a precomputed table in CRC_TABLE.
    :param bytearray message: Where each index is a byte
    """

    crc = 0
    # All messages in _cmd are 5 bytes including the cmd.. The 6th byte is the crc value.
    for i in range(0, 5):
        crc = CRC_TABLE[(crc << 1) ^ message[i]]

    return ((crc << 1) | 1)
