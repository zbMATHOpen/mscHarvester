# run pip install sickle

from zbsickle.app import ZbPreviewSickle
from zbsickle.models import ZbPreviewRecord
import time
import csv
import math


def log(m):
    print(m)


def run(
    max_records=math.inf,
    outfile="out.csv",
    log_interval=1000,
    only_complete=False,
    fieldnames=ZbPreviewRecord.fieldnames,
):
    t0 = time.time()
    s = ZbPreviewSickle()
    r = s.ListRecords()
    i = 0
    w: csv.DictWriter
    with open(outfile, "w") as csvfile:
        w = csv.DictWriter(csvfile, fieldnames)
        w.writeheader()
        for row in r:
            row.fieldnames = fieldnames
            added = row.writerow(w, only_complete)
            if i > max_records:
                return
            elif added:
                i += 1
            if i % log_interval == 0:
                current_time = time.time()
                log(f"{i / (current_time - t0)} records per second")


if __name__ == "__main__":
    run()
