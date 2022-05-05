from main import run
import re

fieldnames = ["doi", "msc", "zbl_id"]
full_id = re.compile(r'\d+\.\d')


def row_filter(fields):
    for k, v in fields.items():
        if v == "":
            return False
        if k == "zbl_id" and not full_id.match(v):
            return False
    fields['msc']=fields['msc'][0]
    return True


run(
    max_records=10000000,
    outfile="springer.csv",
    log_interval=1000,
    row_filter=row_filter,
    fieldnames=fieldnames,
)
