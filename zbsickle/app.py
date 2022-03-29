from typing import Iterator

from sickle import Sickle
from sickle.iterator import OAIItemIterator
from sickle.models import Header, Set, MetadataFormat, Identify

from zbsickle.models import ZbPreviewRecord


class ZbPreviewSickle(Sickle):
    METADATA_PREFIX = "oai_zb_preview"
    DEFAULT_ENDPOINT = "https://oai.zbmath.org/v1"
    DEFAULT_CLASS_MAP = {
        "GetRecord": ZbPreviewRecord,
        "ListRecords": ZbPreviewRecord,
        "ListIdentifiers": Header,
        "ListSets": Set,
        "ListMetadataFormats": MetadataFormat,
        "Identify": Identify,
    }

    def __init__(
        self,
        endpoint=DEFAULT_ENDPOINT,
        http_method="GET",
        protocol_version="2.0",
        iterator=OAIItemIterator,
        max_retries=1000,
        retry_status_codes=None,
        default_retry_after=60,
        class_mapping=None,
        encoding=None,
        **request_args,
    ):
        if class_mapping is None:
            class_mapping = self.DEFAULT_CLASS_MAP
        super().__init__(
            endpoint,
            http_method,
            protocol_version,
            iterator,
            max_retries,
            retry_status_codes,
            default_retry_after,
            class_mapping,
            encoding,
            **request_args,
        )

    # noinspection PyPep8Naming
    def ListRecords(
        self, ignore_deleted=False, metadataPrefix=METADATA_PREFIX, **kwargs
    ) -> Iterator[ZbPreviewRecord]:
        return super().ListRecords(
            ignore_deleted, metadataPrefix=metadataPrefix, **kwargs
        )

    def GetRecord(self, de: int, **kwargs) -> ZbPreviewRecord:
        """
        :param de DE number without the prefix DE.
        :type de: int
        """
        de = f"oai:zbmath.org:{int(de)}"
        return super().GetRecord(
            identifier=de, metadataPrefix=self.METADATA_PREFIX, **kwargs
        )
