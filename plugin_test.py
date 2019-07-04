import unittest
from plugin import get_info, Morpheme, NHKDict, NHKEntry, Tagger, WordInfo

NEKO = Morpheme('猫', 'ネコ', '猫')


class TestTagger(unittest.TestCase):

    def test_simple_sentences(self):
        tagger = Tagger()
        sentence = '猫が見た。'
        expected = [
            NEKO,
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


class TestWordInfo(unittest.TestCase):

    def test_words(self):
        nhk = NHKDict()
        neko_expected = WordInfo('猫', 'ネコ', 1)
        self.assertEqual(get_info(NEKO, nhk), neko_expected)
        desu = Morpheme('です', 'デス', 'です')
        desu_expected = WordInfo('です', None, None)
        self.assertEqual(get_info(desu, nhk), desu_expected)


if __name__ == '__main__':
    unittest.main()
