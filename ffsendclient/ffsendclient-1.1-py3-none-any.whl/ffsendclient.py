# -*- coding: utf-8 -*-

#         __.|.__
#     .-"'..':`..`"-.
#   .' .' .  :  . `. `.
#  / .  FFSENDCLIENT . \
# /_ _._ _.._:_.._ _._ _\
#   '   '    |    '   '
#            |
#            |
#            |
#         \  |  /
#          \ | /
#           \ /
#            '


"""
Firefox Send API Client
~~~~~~~~~~~~~~~~~~~~~

ffsendclient is a library for interfacing with Firefox Send
<https://send.firefox.com/> or your own instance of it. Basic file upload
usage:

    >>> import os
    >>> from ffsendclient.ffsendclient import SendClient
    >>> send = SendClient('send.firefox.com')
    >>> up_data = os.urandom(1024)
    >>> fid, owner_token, url = send.upload('ffsendclient.bin', up_data)
    >>> fid
    'eb99746752a74975'
    >>> owner_token
    'fc8a7a910688869021be'
    >>> url
    'https://send.firefox.com/download/eb99746752a74975/#xsKqVUcdh_Dp6GDn2zUVLg'

... and continue to download:

    >>> secret = url.split('#')[1]
    >>> secret
    'xsKqVUcdh_Dp6GDn2zUVLg'
    >>> file_name, down_data = send.download(fid, secret)
    >>> file_name
    'ffsendclient.bin'
    >>> up_data == down_data
    True

Passwords, download limits and time limits are also supported. Full
documentation is at <https://gitlab.com/skorov/ffsendclient>.

Not yet supported:
 - Multi-file upload/download
 - Firefox authentication

:copyright: (c) 2019 by Alexei Doudkine.
:license: Apache 2.0, see LICENSE for more details.
"""


import asyncio
import os
import mimetypes
import base64
import json
import hmac
import requests
import websockets
from typing import Tuple, Dict, Optional
from hashlib import sha256
from io import BytesIO
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

# region Constants
NONCE_LENGTH = 12
TAG_LENGTH = 16
KEY_LENGTH = 16
ECE_RECORD_SIZE = 1024 * 64
# endregion


# region Helpers
def b64encode(s):
    return base64.urlsafe_b64encode(s).decode().rstrip('=')


def b64decode(s):
    # accept unicode (py2), str (py2) and str (py3) inputs
    s = str(s)
    s += '==='[(len(s) + 3) % 4:]
    return base64.urlsafe_b64decode(s)


def rshift(val, n):
    """Equivilant to javascript's >>> operator"""
    return val >> n if val >= 0 else (val+0x100000000) >> n
# endregion


class CryptoCurrencyIsAScam:
    def __init__(self, secret=os.urandom(KEY_LENGTH), salt=os.urandom(KEY_LENGTH), rs=ECE_RECORD_SIZE):
        self.secret = secret
        self.salt = salt
        self.file_key = self._derive_file_key(self.secret, self.salt)
        self.auth_key = self.derive_auth_key(self.secret)
        self.meta_key = self._derive_meta_key(self.secret)
        self.nonce_base = self._derive_nonce_base(self.secret, self.salt)
        self.rs = rs  # Record size

    def encrypt_metadata(self, metadata):
        meta_cipher = AES.new(self.meta_key, AES.MODE_GCM, b'\x00' * 12, mac_len=KEY_LENGTH)
        encrypted = meta_cipher.encrypt(metadata)
        encrypted += meta_cipher.digest()
        return encrypted

    def decrypt_metadata(self, metadata_enc):
        meta_cipher = AES.new(self.meta_key, AES.MODE_GCM, b'\x00' * 12, mac_len=KEY_LENGTH)
        metadata = metadata_enc[:-TAG_LENGTH]
        digest = metadata_enc[-TAG_LENGTH:]
        metadata = meta_cipher.decrypt_and_verify(metadata, digest)
        return metadata

    def encrypt_file(self, file):
        header = self.salt + self.rs.to_bytes(4, byteorder='big', signed=True) + b'\x00'  # This is the header. It is always sent as 21 byte chunk
        yield header
        seq = 0
        is_last = False
        chunk_itr = self._chopchop(file)
        prev_chunk, record = None, None
        chunk = next(chunk_itr)
        while not is_last:
            try:
                prev_chunk = chunk
                chunk = next(chunk_itr)
                record = self._pad(prev_chunk, is_last)
            except StopIteration:
                is_last = True
                record = self._pad(prev_chunk, is_last)
            finally:
                file_cipher = AES.new(self.file_key, AES.MODE_GCM, self._generate_nonce(seq), mac_len=KEY_LENGTH)
                seq += 1
                encrypted = file_cipher.encrypt(record)
                encrypted += file_cipher.digest()
                yield encrypted

    def decrypt_file(self, encrypted):
        encrypted = BytesIO(encrypted)

        # Read header (21 bytes)
        self.salt = encrypted.read(KEY_LENGTH)
        self.rs = int.from_bytes(encrypted.read(4), byteorder='big', signed=True)
        encrypted.read(1)  # Last 0x00 from header

        self.file_key = self._derive_file_key(self.secret, self.salt)
        self.nonce_base = self._derive_nonce_base(self.secret, self.salt)
        seq = 0
        chunk = encrypted.read(self.rs)
        file = BytesIO()
        while chunk:
            file_cipher = AES.new(self.file_key, AES.MODE_GCM, self._generate_nonce(seq), mac_len=KEY_LENGTH)
            file_chunk = file_cipher.decrypt_and_verify(chunk[:-TAG_LENGTH], chunk[-TAG_LENGTH:])
            file.write(file_chunk[:-1])
            seq += 1
            chunk = encrypted.read(self.rs)

        file.seek(0)
        return file.read()

    def derive_auth_key(self, secret, password=None, url=None):
        if password is None:
            return self._hkdf(64, secret, info=b'authentication')
        return PBKDF2(password.encode('utf8'), url.encode('utf8'), 64, 100,
                      lambda x, y: hmac.new(x, y, sha256).digest())

    def _derive_file_key(self, secret, salt):
        return self._hkdf(KEY_LENGTH, secret, salt=salt, info=b'Content-Encoding: aes128gcm\x00')

    def _derive_meta_key(self, secret):
        return self._hkdf(KEY_LENGTH, secret, info=b'metadata')

    # nonce is the same as IV for enc/dec. Crypto is hard
    # We make a BASE (all your base are belong to me), then we make a nonce for each "record"
    def _derive_nonce_base(self, secret, salt):
        return self._hkdf(NONCE_LENGTH, secret, salt=salt, info=b'Content-Encoding: nonce\x00')

    # This is the nonce for the current "record". We make a new nonce each ECE_RECORD_SIZE bytes
    def _generate_nonce(self, seq):
        m = self.nonce_base[len(self.nonce_base) - 4:][:4]
        xor = rshift(int.from_bytes(m, 'big') ^ seq, 0).to_bytes(4, byteorder='big', signed=False)
        nonce = self.nonce_base[:len(self.nonce_base) - 4] + xor + self.nonce_base[len(self.nonce_base) - 4 + len(xor):]
        return nonce

    def _pad(self, chunk, is_last):
        chunk_length = len(chunk)
        if chunk_length > self.rs - (KEY_LENGTH + 1):
            raise ValueError(f'Chunk is too big to pad: {chunk_length} bytes')

        delimiter = b'\x02' if is_last else b'\x01'
        return chunk + delimiter

    def _chopchop(self, data):
        chunk_size = self.rs - (TAG_LENGTH + 1)
        data = BytesIO(data)
        while True:
            chunk = data.read(chunk_size)
            if len(chunk) == 0:
                break
            yield chunk

    @staticmethod
    def _hkdf(length, ikm, hashfunc=sha256, salt=b"", info=b""):
        prk = hmac.new(salt, ikm, hashfunc).digest()
        t = b""
        i = 0
        okm = bytearray()
        while len(okm) < length:
            i += 1
            t = hmac.new(prk, t + info + bytes(bytearray([i])), hashfunc).digest()
            okm += t
        return bytes(okm[:length])


class SendClient:
    def __init__(self, hostname: str, http_scheme: Optional[str] = 'https', websocket_scheme: Optional[str] = 'wss') -> None:
        """
        Create a new SendClient object giving the hostname

        :param hostname: Hostname of the Send server (e.g. "send.firefox.com")
        :param http_scheme: Use either "http" or "https". Defaults to the secure one ;)
        :param websocket_scheme: Use either "ws" or "wss". Defaults to the secure one.
        """
        self.hostname = hostname
        self.http_scheme = http_scheme
        self.websocket_scheme = websocket_scheme

    def upload(self, filename: str, file_data: bytes, password: Optional[str] = None, download_limit: Optional[int] = 1, time_limit: Optional[int] = 86400) -> Tuple[str, str, str]:
        """
        Uploads a file-like byte array to Send. Optionally sets a password if supplied

        :param filename: The name of the file uploading to Send
        :param file_data: Byte array containing for the file data
        :param password: (Optional) Password to set for the file
        :param download_limit: How many times the file is allowed to be downloaded
        :param time_limit: How many seconds until the file expires
        :return: Returns a tuple of "File ID", "Owner Token" and "URL"
        """
        crypto_service = CryptoCurrencyIsAScam()
        mimetype = mimetypes.guess_type(filename, strict=False)[0] or 'application/octet-stream'

        metadata = {"name": filename, "size": len(file_data), "type": mimetype, "manifest": {"files": [{"name": filename, "size": len(file_data), "type": mimetype}]}}
        metadata_enc = crypto_service.encrypt_metadata(json.dumps(metadata).encode('utf8'))
        filedata_enc = crypto_service.encrypt_file(file_data)

        data = {'authorization': 'send-v1 ' + b64encode(crypto_service.auth_key), 'dlimit': download_limit, 'fileMetadata': b64encode(metadata_enc), 'timeLimit': time_limit}
        responses = asyncio.run(self._send_recv_ws(json.dumps(data), filedata_enc))
        url_response = json.loads(responses[0])
        status = json.loads(responses[1])
        assert status['ok']

        url = url_response['url'] + '#' + b64encode(crypto_service.secret)
        owner_token = url_response['ownerToken']
        fid = url_response['id']

        if password is not None:
            new_auth_key = crypto_service.derive_auth_key(crypto_service.secret, password, url)
            self._set_password(fid, owner_token, new_auth_key)

        return fid, owner_token, url

    def download(self, fid: str, secret: str, password: Optional[str] = None, url: Optional[str] = None) -> Tuple[str, bytes]:
        """
        Download a file hosted on the Send server

        :param fid: The file ID of the file we are downloading
        :param secret: The secret key, in base64 encoded format. The part after the "#" in the URL.
        :param password: (Optional) The password for the file we are downloading
        :param url: (Optional) The full URL (including the secret key part) of where the file is stored. Must be supplied if a password is given
        :return: A Tuple containing: The file name, bytes array of the file data
        """
        assert (password is None and url is None) or (password is not None and url is not None)
        metadata, nonce = self.get_metadata(fid, secret, password, url)

        secret = b64decode(secret)
        crypto_service = CryptoCurrencyIsAScam(secret)
        auth_key = crypto_service.derive_auth_key(secret, password, url)
        sig = hmac.new(auth_key, nonce, sha256).digest()

        resp = requests.get(f'{self.http_scheme}://{self.hostname}/api/download/{fid}',
                            headers={'Authorization': f'send-v1 {b64encode(sig)}'}, stream=True)
        resp.raise_for_status()
        file = crypto_service.decrypt_file(resp.content)
        return metadata['name'], file

    def get_info(self, fid: str, owner_token: str) -> Tuple[int, int, int]:
        """
        Get the info for the file in Send

        :param fid: The file ID of the file we are getting info for
        :param owner_token: The owner token supplied during upload
        :return: A tuple of values: Download limit, Download total, Time to live (in seconds)
        """
        resp = requests.post(f'{self.http_scheme}://{self.hostname}/api/info/{fid}',
                             headers={'Content-Type': 'application/json'},
                             json={'owner_token': owner_token})
        resp.raise_for_status()
        info = resp.json()
        return info['dlimit'], info['dtotal'], int(info['ttl'] / 1000)  # Convert back into seconds from milliseconds

    def get_metadata(self, fid: str, secret: str, password: Optional[str] = None, url: Optional[str] = None) -> Tuple[Dict, bytes]:
        """
        Get the metadata for a file in Send

        :param fid: The file ID of the file we are getting metadata for
        :param secret: The secret key, in base64 encoded format. The part after the "#" in the URL.
        :param password: (Optional) The password for the file we are downloading
        :param url: (Optional) The full URL (including the secret key part) of where the file is stored. Must be supplied if a password is given
        :return: Returns 2 things: 1. A Dict containing the file's metadata values (name, size, mimetype, manifest). 2. A bytes array with the next nonce (needed for download)
        """
        secret = b64decode(secret)
        crypto_service = CryptoCurrencyIsAScam(secret)
        resp = requests.get(f'{self.http_scheme}://{self.hostname}/download/{fid}')
        resp.raise_for_status()
        nonce = base64.b64decode(resp.headers['WWW-Authenticate'].split()[1])
        sig = hmac.new(crypto_service.derive_auth_key(secret, password, url), nonce, sha256).digest()

        resp = requests.get(f'{self.http_scheme}://{self.hostname}/api/metadata/{fid}',
                            headers={'Authorization': f'send-v1 {b64encode(sig)}'})
        resp.raise_for_status()
        next_nonce = base64.b64decode(resp.headers['WWW-Authenticate'].split()[1])
        metadata_enc = resp.json()['metadata']
        metadata = crypto_service.decrypt_metadata(b64decode(metadata_enc))
        return json.loads(metadata), next_nonce

    def delete(self, fid: str, owner_token: str) -> None:
        """
        Deletes a file that is stored in Send

        :param fid: The file ID of the file we are deleting
        :param owner_token: The owner token supplied during upload
        """
        resp = requests.get(f'{self.http_scheme}://{self.hostname}/api/delete/{fid}',
                            json={'owner_token': owner_token})
        resp.raise_for_status()

    def _set_password(self, fid, owner_token, new_auth_key):
        """Private method to set the password on a file during upload"""
        resp = requests.post(f'{self.http_scheme}://{self.hostname}/api/password/{fid}',
                             headers={'Content-Type': 'application/json'},
                             json={'auth': b64encode(new_auth_key), 'owner_token': owner_token})
        resp.raise_for_status()

    async def _send_recv_ws(self, init_data, file_cipher):
        """This method does the websocket part of the file upload"""
        async with websockets.connect(f'{self.websocket_scheme}://{self.hostname}/api/ws', ssl=(self.websocket_scheme == 'wss')) as ws:
            await ws.send(init_data)
            url_data = await ws.recv()
            resp_json = json.loads(url_data)
            assert 'error' not in resp_json

            await ws.send(file_cipher)
            await ws.send('\x00')
            status = await ws.recv()
            return url_data, status
