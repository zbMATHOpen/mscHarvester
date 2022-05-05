from main import run

fieldnames = ["doi", "msc"]


def filter(fields):
    for k, v in fields.items():
        if v == "":
            return False
    return True


run(
    max_records=10000000,
    outfile="springer.csv",
    log_interval=1000,
    row_filter=filter,
    fieldnames=fieldnames,
)
