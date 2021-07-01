from sickle import Sickle

from msch.zb_preview_record import ZbPreviewRecord

# URL = 'https://oai.zbmath.org/v1/'
URL = 'https://zboai.formulasearchengine.com/v1'


def get_client():
    s = Sickle(URL, retry_status_codes=[429], max_retries=1000)
    s.class_mapping['GetRecord'] = ZbPreviewRecord
    s.class_mapping['ListRecords'] = ZbPreviewRecord
    return s
