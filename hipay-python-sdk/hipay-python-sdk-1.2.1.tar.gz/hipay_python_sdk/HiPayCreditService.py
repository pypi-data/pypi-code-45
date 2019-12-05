import zeep


class HiPayCreditService:
    def __init__(self, ws_login, ws_password, callback_email, url_callback, url_decline, url_cancel, url_logo,
                 wsdl='https://test-ws.hipay.com/soap/payment-v2?wsdl'):
        self.client = zeep.Client(wsdl=wsdl)
        self.ws_login = ws_login
        self.ws_password = ws_password
        self.callback_email = callback_email
        self.url_callback = url_callback
        self.url_decline = url_decline
        self.url_cancel = url_cancel
        self.url_logo = url_logo

    def generate_payment(self, website_id, category_id, amount, customer_email, currency="EUR", rating="ALL",
                         locale="pt_PT", customer_ip_address="127.0.0.1", description="Default description",
                         manual_capture="0"):
        generated_page = self.client.service.generate(
            websiteID=website_id,
            categoryID=category_id,
            currency=currency,
            amount=amount,
            rating=rating,
            locale=locale,
            costumerIpAddress=customer_ip_address,
            description=description,
            manualCapture=manual_capture,
            customerEmail=customer_email,
            emailCallback=self.callback_email,
            urlCallback=self.url_callback,
            urlDecline=self.url_decline,
            urlCancel=self.url_cancel,
            urlLogo=self.url_logo,
            wsLogin=self.ws_login,
            wsPassword=self.ws_password
        )

        return generated_page

    def generate_refund(self):
        pass
