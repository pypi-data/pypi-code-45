import moyasar
import json


class Capture:
    def capture_url(self, id):
        return f'{moyasar.resource_url(self.__class__.__name__)}/{id}/capture'.lower()

    def capture(self, amount=None):
        data = None
        if amount is not None:
            data = {'amount': amount}

        response = moyasar.request('POST', self.capture_url(self.id), data)
        response = json.loads(response.text)
        moyasar.fill_object(self, response)
