from main import run

fieldnames = ["doi", "msc"]
run(
    max_records=10000000,
    outfile="springer.csv",
    log_interval=1000,
    only_complete=True,
    fieldnames=fieldnames,
)
