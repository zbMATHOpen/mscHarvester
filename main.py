# run pip install sickle
from typing import Iterator

from sickle import Sickle
from msch.zb_preview_record import ZbPreviewRecord
import time
import csv

MAX_RECORDS = 10

METADATA_PREFIX = 'oai_zb_preview'
# METADATA_PREFIX = 'oai_dc'

URL = 'https://oai.zbmath.org/v1/'


def log(m):
    print(m)


def run():
    t0 = time.time()
    s = Sickle(URL, retry_status_codes=[429], max_retries=1000)
    s.class_mapping['GetRecord'] = ZbPreviewRecord
    s.class_mapping['ListRecords'] = ZbPreviewRecord
    r: Iterator[ZbPreviewRecord] = s.ListRecords(
        metadataPrefix=METADATA_PREFIX)
    i = 0
    w: csv.DictWriter
    with open('out.csv', 'w') as csvfile:
        fieldnames = ['de']
        w = csv.DictWriter(csvfile, fieldnames)
        w.writeheader()
        for row in r:
            row.writerow(w)
            if i > MAX_RECORDS:
                return
            else:
                i += 1
            if i % 100 == 0:
                current_time = time.time()
                log(f"{i / (current_time - t0)} records per second")


if __name__ == '__main__':
    run()
