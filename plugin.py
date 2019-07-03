from collections import namedtuple
import MeCab


Morpheme = namedtuple('Morpheme', ['raw', 'reading'])


class Tagger:
    def __init__(self):
        self.mecab = MeCab.Tagger('-Ochasen')

    def tag(self, sentence):
        acc = []
        mecab_out = self.mecab.parse(sentence)
        for line in mecab_out.split('\n'):
            if line == 'EOS':
                break
            parts = line.split('\t')
            acc.append(Morpheme(raw=parts[0], reading=parts[1]))
        return acc
