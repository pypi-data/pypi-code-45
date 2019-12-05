import requests
from hashlib import sha512
import urllib.parse
import hmac


class DefaultCodeErrorException(Exception):
    pass


class WalletException(Exception):
    pass


class ConnectionErrorException(Exception):
    pass


class WalletConnectionErrorException(Exception):
    pass


class BrokerConnectionErrorException(Exception):
    pass


class ValidationErrorException(Exception):
    pass


class Google2faErrorException(Exception):
    pass


class AuthTokenErrorException(Exception):
    pass


class ApiTokenErrorException(Exception):
    pass


class LimitErrorException(Exception):
    pass


class BadSignException(Exception):
    pass


class ForbiddenException(Exception):
    pass


class PayBillErrorException(Exception):
    pass


class PayPairNotFoundException(Exception):
    pass


class DefaulCodeErrorException(Exception):
    pass


class BrokerConnectionErrorException(Exception):
    pass


class BrokerException(Exception):
    pass


class CoinNotFoundException(Exception):
    pass


class WalletNotFoundException(Exception):
    pass


class AccountNotFoundException(Exception):
    pass


class InsufficientFundsException(Exception):
    pass


class InsufficientUnspentsException(Exception):
    pass


class TransactionFailedException(Exception):
    pass


class PermissionDeniedException(Exception):
    pass


class InvalidAddressException(Exception):
    pass


class InvalidPrivateKeyException(Exception):
    pass


class TransactionNotFoundException(Exception):
    pass


class InvalidAddressException(Exception):
    pass


class InvalidPrivateKeyException(Exception):
    pass


class TransactionNotFoundException(Exception):
    pass


class ConnectionNodesErrorException(Exception):
    pass


class AddressException(Exception):
    pass


class Address(object):
    def __init__(self, api_token, secret_token, base_url='https://api.address.so/api/'):
        self.api_token = api_token
        self.secret_token = secret_token
        self.urls = self._get_url_templates()
        self.errors = self._get_exceptions()
        self.base_url = base_url

    @staticmethod
    def _get_url_templates():
        coins = 'coins'
        coin = 'coins/{}/'
        wallets = 'wallets/'
        wallet = '{}/'
        accounts = 'accounts/'
        account = '{}/'
        transactions = 'transactions/'
        send = 'send/'
        permissions = 'permissions/'
        archive = 'archive/'
        return {
            'coin': {
                'all': {
                    'url': coins,
                    'method': 'GET'
                },
                'read': {
                    'url': coin,
                    'method': 'GET'
                },
            },
            'wallet': {
                'all': {
                    'url': coin + wallets,
                    'method': 'GET'
                },
                'create': {
                    'url': coin + wallets,
                    'method': 'POST'
                },
                'read': {
                    'url': coin + wallets + wallet,
                    'method': 'GET'
                },
                'update': {
                    'url': coin + wallets + wallet,
                    'method': 'PUT'
                },
                'delete': {
                    'url': coin + wallets + wallet,
                    'method': 'DELETE'
                },
                'send': {
                    'url': coin + wallets + wallet + send,
                    'method': 'POST'
                },
                'permissions': {
                    'url': coin + wallets + wallet + permissions,
                    'method': 'GET'
                },
                'transactions': {
                    'url': coin + wallets + wallet + transactions,
                    'method': 'GET'
                },
            },
            'account': {
                'all': {
                    'url': coin + wallets + wallet + accounts,
                    'method': 'GET'
                },
                'create': {
                    'url': coin + wallets + wallet + accounts,
                    'method': 'POST'
                },
                'read': {
                    'url': coin + wallets + wallet + accounts + account,
                    'method': 'GET'
                },
                'delete': {
                    'url': coin + wallets + wallet + accounts + account,
                    'method': 'DELETE'
                },
                'archive': {
                    'url': coin + wallets + wallet + accounts + archive,
                    'method': 'DELETE'
                },
                'send': {
                    'url': coin + wallets + wallet + accounts + account + send,
                    'method': 'POST'
                },
                'transactions': {
                    'url': coin + wallets + wallet + accounts + account + transactions,
                    'method': 'GET'
                },
            }
        }

    @staticmethod
    def _get_exceptions():
        return {
            -3000: DefaulCodeErrorException,
            -2999: WalletException,
            -3001: ConnectionErrorException,
            -3002: WalletConnectionErrorException,
            -3003: BrokerConnectionErrorException,
            -3005: ValidationErrorException,
            -3057: Google2faErrorException,
            -3058: AuthTokenErrorException,
            -3059: ApiTokenErrorException,
            -3060: LimitErrorException,
            -3061: BadSignException,
            -3062: ForbiddenException,
            -3070: PayBillErrorException,
            -3071: PayPairNotFoundException,
            -2000: DefaulCodeErrorException,
            -1000: BrokerConnectionErrorException,
            -1999: BrokerException,
            -2401: CoinNotFoundException,
            -2402: WalletNotFoundException,
            -2403: AccountNotFoundException,
            -2500: InsufficientFundsException,
            -2501: InsufficientUnspentsException,
            -2560: TransactionFailedException,
            -2011: PermissionDeniedException,
            -3000: InvalidAddressException,
            -3005: InvalidPrivateKeyException,
            -4001: TransactionNotFoundException,
            -1095: InvalidAddressException,
            -1094: InvalidPrivateKeyException,
            -1004: TransactionNotFoundException,
            -1010: ConnectionNodesErrorException
        }

    def request_builder(self, entity, method, *args):
        return {
            'url': self.urls[entity][method]['url'].format(*args),
            'method': self.urls[entity][method]['method']
        }

    def get_coins(self):
        return self.request(**self.request_builder('coin', 'all'))

    def get_coin(self, coin):
        return self.request(**self.request_builder('coin', 'read', coin))

    def get_wallets(self, coin):
        return self.request(**self.request_builder('wallet', 'all', coin))

    def get_wallet(self, coin, wallet):
        return self.request(**self.request_builder('wallet', 'read', coin, wallet))

    def create_wallet(self, coin, wallet_name):
        return self.request(**self.request_builder('wallet', 'create', coin), params={'label': wallet_name})

    def update_wallet(self, coin, wallet_id, wallet_name):
        return self.request(**self.request_builder('wallet', 'update', coin, wallet_id), params={'label': wallet_name})

    def delete_wallet(self, coin, wallet_id):
        return self.request(**self.request_builder('wallet', 'delete', coin, wallet_id))
        pass

    def get_wallet_transactions(self, coin, wallet_id, limit=100):
        return self.request(**self.request_builder('wallet', 'transactions', coin, wallet_id), params={'limit': limit})

    def send_from_wallet(self, coin, wallet_id, amount, recipient, payment_password, odd_address=None,
                         token_label=None):
        return self.request(**self.request_builder('wallet', 'send', coin, wallet_id),
                            params={'amount': amount, 'recipient': recipient, 'payment_password': payment_password,
                                    'odd_address': odd_address, 'token_label': token_label}, sign=True)

    def get_account(self, coin, wallet_id, account_id):
        return self.request(**self.request_builder('account', 'read', coin, wallet_id, account_id))

    def get_accounts(self, coin, wallet_id):
        return self.request(**self.request_builder('account', 'all', coin, wallet_id))

    def create_account(self, coin, wallet_id, account_id):
        return self.request(**self.request_builder('account', 'create', coin, wallet_id, account_id))

    def delete_account(self, coin, wallet_id, account_id):
        return self.request(**self.request_builder('account', 'delete', coin, wallet_id, account_id))

    def archive_accounts(self, coin, wallet_id, accounts):
        return self.request(**self.request_builder('account', 'archive', coin, wallet_id),
                            params={'accounts', accounts})

    def get_account_transactions(self, coin, wallet_id, account_id, limit=100):
        return self.request(**self.request_builder('account', 'transactions', coin, wallet_id, account_id),
                            params={'limit': limit})

    def send_from_account(self, coin, wallet_id, account_id, amount, recipient, payment_password, odd_address=None,
                          token_label=None):
        return self.request(**self.request_builder('account', 'send', coin, wallet_id, account_id),
                            params={'amount': amount, 'recipient': recipient, 'payment_password': payment_password,
                                    'odd_address': odd_address, 'token_label': token_label}, sign=True)

    def set_permissions(self, coin, wallet_id, user_id, permissions):
        return self.request(**self.request_builder('wallet', 'permissions', coin, wallet_id),
                            params={'user_id': user_id, 'permissions': permissions})

    def remove_all_permissions(self, coin, wallet_id, user_id):
        return self.request(**self.request_builder('wallet', 'permissions', coin, wallet_id),
                            params={'user_id': user_id, 'permissions': ['0']})

    def request(self, url, method, params=None, sign=False):
        methods = {
            'GET': requests.get,
            'POST': requests.post,
            'DELETE': requests.delete,
            'PUT': requests.put
        }
        headers = {'X-Api-Token': self.api_token}

        if params is not None:
            params = {k: v for k, v in params.items() if v}

        if sign:
            params.update({'sign': self.sign_params(params)})

        response = methods[method](self.base_url + url, params=params, headers=headers)
        content = response.json()

        if not ('result' in content.keys()):
            raise AddressException('msg: {} , http code: {}'.format(content, response.status_code))
        elif 'errors' in content.keys() and content['errors'] is not None:
            error_code = content['errors']['code']
            message = content['errors']['message']
            if error_code not in self.errors.keys():
                raise AddressException(message)
            else:
                raise self.errors[error_code](message)
        return content['result']

    def sign_params(self, params):
        secret = sha512(self.secret_token.encode()).hexdigest()
        return hmac.new(secret.encode(), urllib.parse.urlencode(params).encode(), sha512).hexdigest()
