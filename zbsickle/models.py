from csv import DictWriter

from sickle.models import Record


class ZbPreviewRecord(Record):
    fieldnames = ["de", "doi", "msc", "keyword", "title", "text", "refs"]
    metadata = None

    def get_attrib(self, attrib):
        if self.metadata is None:
            self.metadata = self.get_metadata()
        try:
            data = self.metadata[attrib]
            if len(data) == 0:
                data = ""
            if len(data) == 1:
                data = data[0]
            if (
                data == "zbMATH Open Web Interface contents unavailable due "
                "to conflicting licenses."
            ):
                return ""
            else:
                return data
        except KeyError:
            return ""

    def get_de(self) -> int:
        return self.get_attrib("document_id")

    def get_doi(self) -> int:
        return self.get_attrib("doi")

    def get_msc(self) -> []:
        return self.get_attrib("classification")

    def get_keywords(self) -> []:
        return self.get_attrib("keyword")

    def get_title(self) -> str:
        return self.get_attrib("document_title")

    def get_text(self) -> str:
        return self.get_attrib("review_text")

    def get_refs(self) -> []:
        return self.get_attrib("ref_classification")

    def writerow(self, writer: DictWriter, only_complete=False) -> bool:
        fields = {
            "de": self.get_de(),
            "doi": self.get_doi(),
            "msc": self.get_msc(),
            "keyword": self.get_keywords(),
            "title": self.get_title(),
            "text": self.get_text(),
            "refs": self.get_refs(),
        }
        if only_complete:
            for k, v in fields.items():
                if v == "":
                    return False
        writer.writerow(fields)
        return True
