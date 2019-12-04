import json
import unittest

from web_dict.core.factory import VocabularyDictionary


class VocabularyTest(unittest.TestCase):

    def setUp(self) -> None:
        self.c = VocabularyDictionary(word='python')

    def test_basic(self):
        self.assertIsNotNone(self.c.en(), )
        self._p(self.c.en())

    def _p(self, c):
        print(json.dumps(c, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    unittest.main()
