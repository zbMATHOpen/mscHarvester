from sickle.models import Record
from csv import DictWriter


class ZbPreviewRecord(Record):
    def get_de(self) -> int:
        return self.get_metadata()['document_id'][0]

    def writerow(self, writer: DictWriter):
        writer.writerow({
            'de': self.get_de()
        })
