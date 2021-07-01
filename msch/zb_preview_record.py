from csv import DictWriter

from sickle.models import Record


class ZbPreviewRecord(Record):
    fieldnames = ['de', 'msc', 'keyword', 'title', 'text', 'refs']

    def get_de(self) -> int:
        return self.get_metadata()['document_id'][0]

    def get_msc(self):
        return self.get_metadata()['classification']

    def get_keywords(self):
        try:
            return self.get_metadata()['keyword']
        except KeyError:
            return ""

    def get_title(self):
        return self.get_metadata()['document_title'][0]

    def get_text(self) -> str:
        return self.get_metadata()['review_text'][0]

    def get_refs(self):
        try:
            refs = self.get_metadata()['ref_classification']
            return refs
        except KeyError:
            return ""

    def writerow(self, writer: DictWriter):
        writer.writerow({
            'de': self.get_de(),
            'msc': self.get_msc(),
            'keyword': self.get_keywords(),
            'title': self.get_title(),
            'text': self.get_text(),
            'refs': self.get_refs(),
        })


