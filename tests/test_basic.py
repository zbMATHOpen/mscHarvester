from msch.client import get_client
from msch.zb_preview_record import ZbPreviewRecord


def test_get_client():
    s = get_client()
    row: ZbPreviewRecord = s.GetRecord(identifier="oai:zbmath.org:6675366",
                                       metadataPrefix="oai_zb_preview",
                                       )
    assert len(row.get_refs()) == 31
