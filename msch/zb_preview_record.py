from sickle.models import Record


class ZbPreviewRecord(Record):
    def get_de(self) -> int:
        return self.get_metadata()['document_id'][0]
