import unittest
from plugin import Morpheme, Tagger


class TestTagger(unittest.TestCase):

    def test_simple_sentences(self):
        tagger = Tagger()
        sentence = '猫が大好き。'
        expected = [
            Morpheme('猫', 'ネコ'),
            Morpheme('が', 'ガ'),
            Morpheme('大好き', 'ダイスキ'),
            Morpheme('。', '。')
        ]
        self.assertEqual(tagger.tag(sentence), expected)


if __name__ == '__main__':
    unittest.main()
