from .base_provider import BaseProvider
from ..parser import Parser


class _PrimaryDefinitionProvider(Parser):

    def val_pos(self):
        return self.select('td.posList > a', one=False)

    def val_exp(self):
        return self.select("td > div.def").replace(f"{self.val_pos()} ", "")


class _FullDefinitionItemProvider(Parser):

    def val_pos(self):
        return self.select("h3.definition > a")

    def val_exp(self):
        return self.select("h3.definition").lstrip(self.val_pos()).strip()

    def val_examples(self):
        sentences = self.select("div.example", one=False)
        sentence_highlight = self.select("div.example > strong", one=False)
        return [
            {
                "sentence": s,
                "highlight": w
            } for s, w in zip(sentences, sentence_highlight)
        ]


class _FullDefinitionGroupProvider(Parser):

    def val_items(self):
        return self.provider_to_list(_FullDefinitionItemProvider, 'div.ordinal')


class _DefinitionsProvider(Parser):
    def val_primary(self):
        return self.provider_to_list(_PrimaryDefinitionProvider, ('tr', {}))

    def val_full(self):
        return self.provider_to_list(
            _FullDefinitionItemProvider, 'div.group > div.ordinal'
        )


class Vocabulary(BaseProvider):

    @property
    def url(self):
        return f"https://www.vocabulary.com/dictionary/{self.word}"

    def __init__(self, word: str, seg=''):
        super(Vocabulary, self).__init__(word, seg)
        self.seg = seg

    @property
    def head_word(self):
        return self.select("h1.dynamictext")

    @property
    def val_audio(self):
        audio_id = self.select("h1.dynamictext", text=False).a['data-audio']
        if audio_id:
            return f'https://audio.vocab.com/1.0/us/{audio_id}.mp3'

    @property
    def val_short_def(self):
        return self.select("p.short")

    @property
    def val_long_def(self):
        return self.select("p.long")

    # @property
    # def val_sentences(self):
    #     try:
    #         return [
    #             sd['sentence'] for sd in
    #             requests.get(f'https://corpus.vocabulary.com/api/1.0/examples.json'
    #                          f'?query={self.head_word}&maxResults=24').json()
    #             ['result']['sentences']
    #         ]
    #     except KeyError:
    #         return None

    @property
    def val_defs(self):
        return _DefinitionsProvider(
            self.bs.find('div', class_='definitions')
        ).to_dict()
