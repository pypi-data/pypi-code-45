import time
from njtest.serial import nj_serial
from njtest.common import nj_file, nj_email


class Ser_Email(nj_serial.Ser):
    def __init__(self, email_name):
        super().__init__()
        self.email_name = email_name
        self.email = nj_email.Email()

    def while_err(self):
        while True:
            if super().get_email_sum() == 0:
                self.email.send_email(self.email_name, "串口松动了", "读取串口数据报错")
                super().set_email_sum(-1)  # 保证只发送一次邮件
            else:
                time.sleep(30)


if __name__ == '__main__':
    nj_ser = Ser_Email("ssssssss")
    nj_ser.while_err()
