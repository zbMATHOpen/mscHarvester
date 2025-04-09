from main import run
import re

fieldnames = ["arXiv_id", "abstract"]
field_map =  {
        "arXiv_id": "link",
        "abstract": "review_text",
    }
# https://arxiv.org/abs/1402.1748
arxiv = re.compile(r'https?://arxiv\.org')


def row_filter(fields):
    for k, v in fields.items():
        if v is None: # Remove articles without abstract
            return False
        if k == "abstract" and len(v) < 10:
            return False
        if k=="arXiv_id" and not arxiv.search(v):
            return False
    fields['abstract'] = fields['abstract'].lstrip('Summary: ')
    return True


run(
    max_records=10,
    outfile="arxiv.csv",
    row_filter=row_filter,
    fieldnames=fieldnames,
    field_map=field_map,
    endpoint='https://oai.portal.mardi4nfdi.de/oai/OAIHandler'
)
