from main import run
import re

fieldnames = ["arXiv_id", "abstract"]
full_id = re.compile(r'\d+\.\d')


def row_filter(fields):
    for k, v in fields.items():
        if v == "":
            return False
        if k == "zbl_id" and not full_id.match(v):
            return False
    if isinstance(fields['msc'], list):
        fields['msc'] = fields['msc'][0]
    return True


run(
    max_records=10,
    outfile="arxiv.csv",
    log_interval=1,
    # row_filter=row_filter,
    # fieldnames=fieldnames,
    endpoint='https://oai.portal.mardi4nfdi.de/oai/OAIHandler'
)
