# run pip install sickle
from typing import Iterator

from sickle import Sickle

from msch.client import get_client
from msch.zb_preview_record import ZbPreviewRecord
import time
import csv

MAX_RECORDS = 1000

METADATA_PREFIX = 'oai_zb_preview'
# METADATA_PREFIX = 'oai_dc'



def log(m):
    print(m)


def run():
    t0 = time.time()
    s = get_client()
    r: Iterator[ZbPreviewRecord] = s.ListRecords(
        metadataPrefix=METADATA_PREFIX)
    i = 0
    w: csv.DictWriter
    with open('out.csv', 'w') as csvfile:
        w = csv.DictWriter(csvfile, ZbPreviewRecord.fieldnames)
        w.writeheader()
        for row in r:
            row.writerow(w,True)
            if i > MAX_RECORDS:
                return
            else:
                i += 1
            if i % 100 == 0:
                current_time = time.time()
                log(f"{i / (current_time - t0)} records per second")





if __name__ == '__main__':
    run()
