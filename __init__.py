from anki.hooks import addHook
from aqt import mw
from aqt.qt import *
from .plugin import SentenceTagger

SRC_FIELDS = {'Expression'}
DST_FIELDS = {'Reading'}

TAGGER = SentenceTagger()


def on_focus_lost(flag, n, fidx):
    if 'japanese' not in n.model()['name'].lower():
        return flag
    src = None
    srcIdx = None
    dst = None
    for c, name in enumerate(mw.col.models.fieldNames(n.model())):
        if name in SRC_FIELDS:
            src = name
            srcIdx = c
        if name in DST_FIELDS:
            dst = name
    if not src or not dst:
        return flag
    if n[dst]:
        return flag
    if fidx != srcIdx:
        return flag
    srcTxt = mw.col.media.strip(n[src])
    if not srcTxt:
        return flag
    n[dst] = TAGGER.html_out(n[src])
    return True


addHook('editFocusLost', on_focus_lost)
