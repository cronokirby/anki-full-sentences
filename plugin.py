from collections import namedtuple
import csv
import MeCab
import os

SIMPLE_ACCENT_WORDS = [
    'です'
]

Morpheme = namedtuple('Morpheme', ['raw', 'reading'])
NHKEntry = namedtuple('NHKEntry', ['reading', 'accent'])


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


class NHKDict:
    def __init__(self, relpath='nhk.tsv'):
        path = os.path.join(os.path.dirname(__file__), relpath)
        self.dict = dict()
        with open(path) as fp:
            reader = csv.reader(fp, delimiter='\t')
            for row in reader:
                self.dict[row[0]] = NHKEntry(
                    reading=row[1], accent=int(row[2]))

    def lookup(self, word):
        return self.dict.get(word)


def simple_accent(word):
    if len(word.reading) == 1:
        return True
    if word.raw in SIMPLE_ACCENT_WORDS:
        return True
    return False
