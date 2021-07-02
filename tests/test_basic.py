from zbsickle.app import ZbPreviewSickle
from zbsickle.models import ZbPreviewRecord


def test_get_client():
    s = ZbPreviewSickle()
    row = s.GetRecord(de=6675366)
    assert len(row.get_refs()) == 36
    assert row.get_text() == ''
