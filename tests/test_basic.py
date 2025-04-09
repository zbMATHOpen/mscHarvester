from zbsickle.app import ZbPreviewSickle
from zbsickle.models import ZbPreviewRecord


def test_get_client():
    s = ZbPreviewSickle()
    row = s.GetRecord(de=6675366)
    assert len(row.get_refs()) == 45
    assert row.get_text() == ""
    assert row.get_doi() == "10.1515/math-2016-0103"

def test_get_arxiv():
    s = ZbPreviewSickle()
    row = s.GetRecord(de=6377771)
    assert row.get_attrib("link") == "https://arxiv.org/abs/1402.1748"