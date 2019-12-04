import os
from . import AESCipher

LOCK_TEXT = 'nanome-vault-lock'

FILES_DIR = os.path.expanduser('~/Documents/nanome-vault')
if not os.path.exists(os.path.join(FILES_DIR, 'shared')):
    os.makedirs(os.path.join(FILES_DIR, 'shared'))

class VaultManager:
    def is_safe_path(self, base_path, sub_path):
        safe = os.path.realpath(base_path)
        path = os.path.realpath(os.path.join(base_path, sub_path))
        common = os.path.commonprefix((safe, path))
        return os.path.exists(path) and common == safe

    def get_vault_path(self, path):
        path = FILES_DIR if path is None else os.path.join(FILES_DIR, path)
        if not self.is_safe_path(FILES_DIR, path):
            raise Exception("Invalid path")
        return path

    def get_locked_path(self, path):
        if os.path.commonpath(FILES_DIR, path) == FILES_DIR:
            path = path[len(FILES_DIR):]

        path = os.path.normpath(path)
        parts = path.split(os.path.sep)
        subpath = ''
        for part in parts:
            subpath = os.path.join(subpath, part)
            if os.path.exists(os.path.join(FILES_DIR, subpath, '.locked')):
                return subpath
        return None

    def is_path_locked(self, path):
        return self.get_locked_path(path) != None

    def is_key_valid(self, path, key):
        path = self.get_locked_path(path)
        if path is None:
            return True

        try:
            lock = os.path.join(path, '.locked')
            result = AESCipher.decrypt(lock, key)
            return result == LOCK_TEXT
        except:
            return False

    def list_path(self, path=None):
        path = self.get_vault_path(path)

        result = dict()
        result['locked_path'] = self.get_locked_path(path)
        result['locked_folders'] = []
        result['folders'] = []
        result['files'] = []

        items = [item for item in os.listdir(path) if not item.startswith('.')]
        for item in sorted(items):
            is_dir = os.path.isdir(os.path.join(path, item))
            if is_dir and os.path.exists(os.path.join(path, item, '.locked')):
                result['locked_folders'].append(item)
            result['folders' if is_dir else 'files'].append(item)

        return result

    def decrypt_file(self, path, out_file, key=None):
        path = self.get_vault_path(path)

        if not self.is_key_valid(path, key):
            raise Exception("Invalid key")

        with open(path, 'rb') as f:
            data = AESCipher.decrypt(f.read())
        return data
