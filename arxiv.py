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

    abstract = fields['abstract']
    link = fields['arXiv_id']

    if (abstract is None
            or len(abstract) <10
            or link is None):
        return False
    if isinstance(link, str):
        link = [link]
    for v in link:
        if arxiv.match(v):
            fields['arXiv_id'] = v
            fields['abstract'] = abstract.lstrip('Summary: ')
            return True
    return False


run(
    # max_records=10,
    outfile="arxiv.csv",
    row_filter=row_filter,
    fieldnames=fieldnames,
    field_map=field_map,
    endpoint='https://oai.portal.mardi4nfdi.de/oai/OAIHandler'
)
