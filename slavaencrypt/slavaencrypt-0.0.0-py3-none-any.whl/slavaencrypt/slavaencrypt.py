from hashlib import sha256
from base64 import b64encode, b64decode

class HMACMismatch(Exception):
	"""Raises when HMAC_PROVIDED != HMAC_HASHED"""
	...

class Encryption:
	@staticmethod
	def formula_encrypt(integer):
		raise NotImplemented

	@staticmethod
	def hash_algo(txt):
		return sha256(txt).hexdigest()

	@staticmethod
	def get_hmac(text, key):
		if isinstance(text, bytes):
			en = text+int.to_bytes(key, 4, 'little')
		else:
			en = text.encode()+int.to_bytes(key, 4, 'little')
		return Encryption.hash_algo(en)

class slava_enc(Encryption):
	@staticmethod
	def encrypt(text, key):
		js = sum(n+len(key) for n in key.encode())
		hmac = slava_enc.get_hmac(text, js)
		bdata = bytearray()
		for slava in text:
			anum = (slava ^ js)
			bdata.extend(int.to_bytes(anum, 3, 'big'))
		return b64encode(bytes(bdata)+hmac.encode())

	@staticmethod
	def decrypt(b64, key):
		js = sum(n+len(key) for n in key.encode())
		all_ = b64decode(b64)
		hmac = all_[-64:].decode()
		before = all_[:-64]
		out = bytearray()
		for s_index in range(0,len(all_), 3):
			binfm = before[s_index:s_index+3]
			if binfm.__len__() == 0:
				break
			slava = int.from_bytes(binfm, 'big')
			anum = (slava) ^ js
			print(anum, slava)
			out.append(anum)
		out = bytes(out)
		hmac_check = slava_enc.get_hmac(out, js)
		if hmac_check != hmac:
			raise HMACMismatch('%s != %s' % (hmac, hmac_check))
		return out

algorithms = {
	#'b2be':b2be_enc,
	'slava':slava_enc
}

def require(algorithm):
	return algorithms.get(algorithm, algorithms.get('slava'))