import json
import re

from .base_provider import BaseProvider


class SpanishDict(BaseProvider):

    @property
    def url(self):
        return f'https://www.spanishdict.com/translate/{self.word}'

    def __init__(self, word: str, seg='es-en'):
        super(SpanishDict, self).__init__(word, seg)
        self.seg = seg

    @property
    def json(self) -> dict:
        return json.loads(re.search(
            'SD_DICTIONARY_RESULTS_PROPS\s?=(?P<c>.+);.+global.SD_WORD_ROOT_PROPS.+',
            self.rsp.content.decode().replace("\n", ""), re.MULTILINE
        ).group(1))['es']['entry']

    @property
    def head_word(self):
        return self.select("div#headword-es")

    @property
    def val_audio(self):
        return f'http://audio1.spanishdict.com/audio?lang=es&text={self.head_word}'

    @property
    def val_neodict(self):
        return self.json['neodict']
