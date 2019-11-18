import abc
import datetime
import email
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from typing import Sequence, Union, Dict, List

from mailables.exceptions import BadHeaderError


class BaseAttachment(abc.ABC):
    def __init__(
            self,
            mime_type: str = 'application/octet-stream',
            charset: str = None,
            disposition: str = 'attachment',
            content_id: str = None,
            headers: Dict[str, str] = None,
    ):
        self.mime_type = mime_type
        self.charset = charset
        self.disposition = disposition
        self.content_id = content_id
        self.headers = headers or {}

        if content_id:
            self.headers['Content-ID'] = f'<{content_id}>'
            self.headers['X-Attachment-ID'] = content_id

    @abc.abstractmethod
    def build(self) -> MIMEBase:  # pragma: nocover
        raise NotImplementedError()

    def as_string(self) -> str:
        return self.build().as_string()

    def __str__(self):
        return self.as_string()


class Attachment(BaseAttachment):
    def __init__(
            self,
            file_name: str,
            contents: str,
            mime_type: str = 'application/octet-stream',
            disposition: str = 'attachment',
            charset: str = None,
            content_id: str = None,
            headers: Dict[str, str] = None,

    ):
        self.file_name = file_name
        self.contents = contents
        super().__init__(
            mime_type=mime_type,
            charset=charset,
            disposition=disposition,
            content_id=content_id,
            headers=headers,
        )

    def read(self) -> Union[str, bytes]:
        return self.contents

    def build(self) -> MIMEBase:
        main_type, subtype = self.mime_type.split('/')
        part = MIMEBase(main_type, subtype)
        part.add_header('Content-Disposition', self.disposition, filename=self.file_name)
        part.set_payload(self.read(), self.charset)
        for header_name, header_value in self.headers.items():
            part.add_header(header_name, header_value)
        return part


def _ensure_list(value: Union[str, Sequence[str]]) -> List[str]:
    if value is None:
        return []

    if isinstance(value, (str,)):
        return [value]
    return list(value)


def _create_address(address: str, name: str = None):
    if name:
        return f'{name} <{address}>'
    return address


def _forbid_new_lines(value: str):
    if value is not None:
        if '\n' in value or '\r' in value:
            raise BadHeaderError(f'Header value "{value}" contains new line characters.')
    return value


class EmailMessage:
    _to: List[str]
    _cc: List[str]
    _bcc: List[str]
    _reply_to: List[str]

    def __init__(
            self,
            to: Union[str, Sequence[str]] = None,
            subject: str = None,
            text_body: str = None,
            from_address: str = None,
            cc: Union[str, Sequence[str]] = None,
            bcc: Union[str, Sequence[str]] = None,
            reply_to: Union[str, Sequence[str]] = None,
            html_body: str = None,
            attachments: Sequence[Attachment] = None,
            headers: Dict[str, str] = None,
            date: datetime.datetime = None,
            boundary: str = None,
            charset: str = None,
            parts: Sequence[MIMEBase] = None,
            encoding: str = 'quoted-printable',
    ):
        self.to = to
        self.cc = cc
        self.bcc = bcc
        self.reply_to = reply_to

        self.subject = subject
        self.from_address = from_address
        self.text_body = text_body
        self.html_body = html_body
        self.attachments = attachments or []
        self.boundary = boundary
        self.charset = charset
        self.headers = headers or {}
        self.parts = parts or []
        self.encoding = encoding
        self.date = date or datetime.datetime.today()

    @property
    def to(self) -> List[str]:
        return self._to

    @to.setter
    def to(self, value: Union[str, Sequence[str]]):
        self._to = _ensure_list(value)

    @property
    def cc(self) -> List[str]:
        return self._cc

    @cc.setter
    def cc(self, value: Union[str, Sequence[str]]):
        self._cc = _ensure_list(value)

    @property
    def bcc(self) -> List[str]:
        return self._bcc

    @bcc.setter
    def bcc(self, value: Union[str, Sequence[str]]):
        self._bcc = _ensure_list(value)

    @property
    def reply_to(self) -> List[str]:
        return self._reply_to

    @reply_to.setter
    def reply_to(self, value: Union[str, Sequence[str]]):
        self._reply_to = _ensure_list(value)

    @property
    def date(self) -> datetime.datetime:
        return self.headers.get('Date', None)

    @date.setter
    def date(self, date: datetime.datetime):
        self.headers['Date'] = date.isoformat()

    def add_to(self, address: str, name: str = None) -> 'EmailMessage':
        self._to.append(_create_address(address, name))
        return self

    def add_cc(self, address: str, name: str = None) -> 'EmailMessage':
        self._cc.append(_create_address(address, name))
        return self

    def add_bcc(self, address: str, name: str = None) -> 'EmailMessage':
        self._bcc.append(_create_address(address, name))
        return self

    def add_reply_to(self, address: str, name: str = None) -> 'EmailMessage':
        self._reply_to.append(_create_address(address, name))
        return self

    def add_part(self, part: MIMEBase) -> 'EmailMessage':
        self.parts.append(part)
        return self

    def add_attachment(self, attachment: Attachment) -> 'EmailMessage':
        self.attachments.append(attachment)
        return self

    def attach(
            self,
            contents: Union[str, bytes],
            file_name: str,
            mime_type: str = 'application/octet-stream',
            charset: str = None,
            content_id: str = None,
            headers: Dict[str, str] = None,
            disposition: str = 'attachment',
    ) -> 'EmailMessage':
        self.add_attachment(
            Attachment(
                file_name=file_name,
                contents=contents,
                mime_type=mime_type,
                charset=charset,
                content_id=content_id,
                headers=headers,
                disposition=disposition,
            )
        )
        return self

    def build_message(self) -> MIMEMultipart:
        envelope = MIMEMultipart(boundary=self.boundary)

        envelope.preamble = 'This is a multi-part message in MIME format.'
        envelope.add_header('Subject', self.subject)
        envelope.add_header('From', _forbid_new_lines(self.from_address))
        envelope.add_header('To', _forbid_new_lines(', '.join(self._to)))
        envelope.add_header('Content-Transfer-Encoding', self.encoding)

        if len(self._cc):
            envelope.add_header('Cc', ', '.join(self._cc))

        if len(self._bcc):
            envelope.add_header('Bcc', ', '.join(self._bcc))

        if len(self._reply_to):
            envelope.add_header('Reply-to', ', '.join(self._reply_to))

        for name, value in self.headers.items():
            envelope.add_header(name, value)

        # create content parts
        main_message = MIMEMultipart('alternative')
        envelope.attach(main_message)

        if self.text_body:
            text_part = MIMEText(self.text_body, 'plain', self.charset)
            main_message.attach(text_part)

        if self.html_body:
            html_part = MIMEText(self.html_body, 'html', self.charset)
            main_message.attach(html_part)

        # add custom parts and attachments at the end to prevent their content
        # be used as preview message in GMail.
        for part in self.parts:
            envelope.attach(part)

        for attachment in self.attachments:
            part = attachment.build()
            email.encoders.encode_base64(part)
            envelope.attach(part)

        return envelope

    def as_string(self) -> str:
        return self.build_message().as_string()

    def __str__(self) -> str:
        return self.as_string()
