# run pip install sickle
from sickle import Sickle
import time

MAX_RECORDS = 10

METADATA_PREFIX = 'oai_zb_preview'
# METADATA_PREFIX = 'oai_dc'

URL = 'https://oai.zbmath.org/v1/'


def log(m):
    print(m)


def run():
    t0 = time.time()
    s = Sickle(URL, retry_status_codes=[429], max_retries=1000)
    r = s.ListRecords(metadataPrefix=METADATA_PREFIX)
    i = 0
    for row in r:
        if i > MAX_RECORDS:
            return
        else:
            i += 1
        if i % 100 == 0:
            current_time = time.time()
            log(f"{i / (current_time - t0)} records per second")


if __name__ == '__main__':
    run()
