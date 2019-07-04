import unittest
from plugin import Morpheme, NHKDict, NHKEntry, Tagger


class TestTagger(unittest.TestCase):

    def test_simple_sentences(self):
        tagger = Tagger()
        sentence = '猫が見た。'
        expected = [
            Morpheme('猫', 'ネコ', '猫'),
            Morpheme('が', 'ガ', 'が'),
            Morpheme('見', 'ミ', '見る'),
            Morpheme('た', 'タ', 'た'),
            Morpheme('。', '。', '。')
        ]
        self.assertEqual(tagger.tag(sentence), expected)


class TestNHKDict(unittest.TestCase):

    def test_simple_lookups(self):
        nhk = NHKDict()
        neko_expected = NHKEntry('ネコ', 1)
        self.assertEqual(nhk.lookup('猫'), neko_expected)
        aka_expected = NHKEntry('アカ', 1)
        self.assertEqual(nhk.lookup('赤'), aka_expected)


if __name__ == '__main__':
    unittest.main()
