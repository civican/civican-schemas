from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Chamber(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHAMBER_UNSPECIFIED: _ClassVar[Chamber]
    CHAMBER_HOUSE: _ClassVar[Chamber]
    CHAMBER_SENATE: _ClassVar[Chamber]

class SortField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SORT_FIELD_UNSPECIFIED: _ClassVar[SortField]
    SORT_FIELD_NUMBER: _ClassVar[SortField]
    SORT_FIELD_LATEST_EVENT_DATE: _ClassVar[SortField]
    SORT_FIELD_SPONSOR: _ClassVar[SortField]
    SORT_FIELD_STATUS: _ClassVar[SortField]
    SORT_FIELD_TITLE: _ClassVar[SortField]

class SortDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SORT_DIRECTION_UNSPECIFIED: _ClassVar[SortDirection]
    SORT_DIRECTION_ASC: _ClassVar[SortDirection]
    SORT_DIRECTION_DESC: _ClassVar[SortDirection]

class PendingBillType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PENDING_BILL_TYPE_UNSPECIFIED: _ClassVar[PendingBillType]
    PENDING_BILL_TYPE_STAGE: _ClassVar[PendingBillType]
    PENDING_BILL_TYPE_METADATA: _ClassVar[PendingBillType]
CHAMBER_UNSPECIFIED: Chamber
CHAMBER_HOUSE: Chamber
CHAMBER_SENATE: Chamber
SORT_FIELD_UNSPECIFIED: SortField
SORT_FIELD_NUMBER: SortField
SORT_FIELD_LATEST_EVENT_DATE: SortField
SORT_FIELD_SPONSOR: SortField
SORT_FIELD_STATUS: SortField
SORT_FIELD_TITLE: SortField
SORT_DIRECTION_UNSPECIFIED: SortDirection
SORT_DIRECTION_ASC: SortDirection
SORT_DIRECTION_DESC: SortDirection
PENDING_BILL_TYPE_UNSPECIFIED: PendingBillType
PENDING_BILL_TYPE_STAGE: PendingBillType
PENDING_BILL_TYPE_METADATA: PendingBillType

class ListSessionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSessionsResponse(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, sessions: _Optional[_Iterable[str]] = ...) -> None: ...

class BillFilters(_message.Message):
    __slots__ = ("session", "chamber", "sponsor", "sponsor_affiliation", "status", "latest_activity", "number", "date_after", "date_before", "search_query", "has_text", "committee_only")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    CHAMBER_FIELD_NUMBER: _ClassVar[int]
    SPONSOR_FIELD_NUMBER: _ClassVar[int]
    SPONSOR_AFFILIATION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LATEST_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    DATE_AFTER_FIELD_NUMBER: _ClassVar[int]
    DATE_BEFORE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_QUERY_FIELD_NUMBER: _ClassVar[int]
    HAS_TEXT_FIELD_NUMBER: _ClassVar[int]
    COMMITTEE_ONLY_FIELD_NUMBER: _ClassVar[int]
    session: str
    chamber: Chamber
    sponsor: str
    sponsor_affiliation: str
    status: str
    latest_activity: str
    number: str
    date_after: str
    date_before: str
    search_query: str
    has_text: bool
    committee_only: bool
    def __init__(self, session: _Optional[str] = ..., chamber: _Optional[_Union[Chamber, str]] = ..., sponsor: _Optional[str] = ..., sponsor_affiliation: _Optional[str] = ..., status: _Optional[str] = ..., latest_activity: _Optional[str] = ..., number: _Optional[str] = ..., date_after: _Optional[str] = ..., date_before: _Optional[str] = ..., search_query: _Optional[str] = ..., has_text: bool = ..., committee_only: bool = ...) -> None: ...

class ListBillsRequest(_message.Message):
    __slots__ = ("filters", "sort_field", "sort_direction", "limit", "offset")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    filters: BillFilters
    sort_field: SortField
    sort_direction: SortDirection
    limit: int
    offset: int
    def __init__(self, filters: _Optional[_Union[BillFilters, _Mapping]] = ..., sort_field: _Optional[_Union[SortField, str]] = ..., sort_direction: _Optional[_Union[SortDirection, str]] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListBillsResponse(_message.Message):
    __slots__ = ("bills", "total_count")
    BILLS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    bills: _containers.RepeatedCompositeFieldContainer[BillSummary]
    total_count: int
    def __init__(self, bills: _Optional[_Iterable[_Union[BillSummary, _Mapping]]] = ..., total_count: _Optional[int] = ...) -> None: ...

class GetBillRequest(_message.Message):
    __slots__ = ("session", "bill_number")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    BILL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    session: str
    bill_number: str
    def __init__(self, session: _Optional[str] = ..., bill_number: _Optional[str] = ...) -> None: ...

class GetBillResponse(_message.Message):
    __slots__ = ("bill",)
    BILL_FIELD_NUMBER: _ClassVar[int]
    bill: BillDetail
    def __init__(self, bill: _Optional[_Union[BillDetail, _Mapping]] = ...) -> None: ...

class GetBillTextRequest(_message.Message):
    __slots__ = ("session", "bill_number", "stage_slug", "format")
    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORMAT_UNSPECIFIED: _ClassVar[GetBillTextRequest.Format]
        FORMAT_MARKDOWN: _ClassVar[GetBillTextRequest.Format]
        FORMAT_XML: _ClassVar[GetBillTextRequest.Format]
    FORMAT_UNSPECIFIED: GetBillTextRequest.Format
    FORMAT_MARKDOWN: GetBillTextRequest.Format
    FORMAT_XML: GetBillTextRequest.Format
    SESSION_FIELD_NUMBER: _ClassVar[int]
    BILL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STAGE_SLUG_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    session: str
    bill_number: str
    stage_slug: str
    format: GetBillTextRequest.Format
    def __init__(self, session: _Optional[str] = ..., bill_number: _Optional[str] = ..., stage_slug: _Optional[str] = ..., format: _Optional[_Union[GetBillTextRequest.Format, str]] = ...) -> None: ...

class GetBillTextResponse(_message.Message):
    __slots__ = ("bill_number", "session", "stage_slug", "content", "format")
    BILL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    STAGE_SLUG_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    bill_number: str
    session: str
    stage_slug: str
    content: str
    format: str
    def __init__(self, bill_number: _Optional[str] = ..., session: _Optional[str] = ..., stage_slug: _Optional[str] = ..., content: _Optional[str] = ..., format: _Optional[str] = ...) -> None: ...

class BillSummary(_message.Message):
    __slots__ = ("number", "session", "title_en", "title_fr", "sponsor_name", "status", "latest_event_date")
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    TITLE_EN_FIELD_NUMBER: _ClassVar[int]
    TITLE_FR_FIELD_NUMBER: _ClassVar[int]
    SPONSOR_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LATEST_EVENT_DATE_FIELD_NUMBER: _ClassVar[int]
    number: str
    session: str
    title_en: str
    title_fr: str
    sponsor_name: str
    status: str
    latest_event_date: str
    def __init__(self, number: _Optional[str] = ..., session: _Optional[str] = ..., title_en: _Optional[str] = ..., title_fr: _Optional[str] = ..., sponsor_name: _Optional[str] = ..., status: _Optional[str] = ..., latest_event_date: _Optional[str] = ...) -> None: ...

class BillStage(_message.Message):
    __slots__ = ("slug", "name", "date", "source_type")
    SLUG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    slug: str
    name: str
    date: str
    source_type: str
    def __init__(self, slug: _Optional[str] = ..., name: _Optional[str] = ..., date: _Optional[str] = ..., source_type: _Optional[str] = ...) -> None: ...

class BillDetail(_message.Message):
    __slots__ = ("number", "session", "title_en", "title_fr", "sponsor_name", "sponsor_email", "status", "latest_event_date", "stages")
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    TITLE_EN_FIELD_NUMBER: _ClassVar[int]
    TITLE_FR_FIELD_NUMBER: _ClassVar[int]
    SPONSOR_NAME_FIELD_NUMBER: _ClassVar[int]
    SPONSOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LATEST_EVENT_DATE_FIELD_NUMBER: _ClassVar[int]
    STAGES_FIELD_NUMBER: _ClassVar[int]
    number: str
    session: str
    title_en: str
    title_fr: str
    sponsor_name: str
    sponsor_email: str
    status: str
    latest_event_date: str
    stages: _containers.RepeatedCompositeFieldContainer[BillStage]
    def __init__(self, number: _Optional[str] = ..., session: _Optional[str] = ..., title_en: _Optional[str] = ..., title_fr: _Optional[str] = ..., sponsor_name: _Optional[str] = ..., sponsor_email: _Optional[str] = ..., status: _Optional[str] = ..., latest_event_date: _Optional[str] = ..., stages: _Optional[_Iterable[_Union[BillStage, _Mapping]]] = ...) -> None: ...

class StagePendingBill(_message.Message):
    __slots__ = ("session", "bill_number", "author_name", "author_email", "metadata_xml_path", "summary_md_path", "slug", "stage_name", "stage_date", "stage_xml_path", "stage_md_path", "type")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    BILL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    METADATA_XML_PATH_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_MD_PATH_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    STAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    STAGE_DATE_FIELD_NUMBER: _ClassVar[int]
    STAGE_XML_PATH_FIELD_NUMBER: _ClassVar[int]
    STAGE_MD_PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    session: str
    bill_number: str
    author_name: str
    author_email: str
    metadata_xml_path: str
    summary_md_path: str
    slug: str
    stage_name: str
    stage_date: str
    stage_xml_path: str
    stage_md_path: str
    type: str
    def __init__(self, session: _Optional[str] = ..., bill_number: _Optional[str] = ..., author_name: _Optional[str] = ..., author_email: _Optional[str] = ..., metadata_xml_path: _Optional[str] = ..., summary_md_path: _Optional[str] = ..., slug: _Optional[str] = ..., stage_name: _Optional[str] = ..., stage_date: _Optional[str] = ..., stage_xml_path: _Optional[str] = ..., stage_md_path: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class MetadataPendingBill(_message.Message):
    __slots__ = ("session", "bill_number", "author_name", "author_email", "metadata_xml_path", "summary_md_path", "event_date", "restore_xml_path", "restore_md_path", "type")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    BILL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    METADATA_XML_PATH_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_MD_PATH_FIELD_NUMBER: _ClassVar[int]
    EVENT_DATE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_XML_PATH_FIELD_NUMBER: _ClassVar[int]
    RESTORE_MD_PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    session: str
    bill_number: str
    author_name: str
    author_email: str
    metadata_xml_path: str
    summary_md_path: str
    event_date: str
    restore_xml_path: str
    restore_md_path: str
    type: str
    def __init__(self, session: _Optional[str] = ..., bill_number: _Optional[str] = ..., author_name: _Optional[str] = ..., author_email: _Optional[str] = ..., metadata_xml_path: _Optional[str] = ..., summary_md_path: _Optional[str] = ..., event_date: _Optional[str] = ..., restore_xml_path: _Optional[str] = ..., restore_md_path: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class ScrapeResult(_message.Message):
    __slots__ = ("success", "updated_stages", "author_name", "author_email", "stage_pending_commits", "metadata_pending_commits")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_STAGES_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    STAGE_PENDING_COMMITS_FIELD_NUMBER: _ClassVar[int]
    METADATA_PENDING_COMMITS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    updated_stages: _containers.RepeatedScalarFieldContainer[str]
    author_name: str
    author_email: str
    stage_pending_commits: _containers.RepeatedCompositeFieldContainer[StagePendingBill]
    metadata_pending_commits: _containers.RepeatedCompositeFieldContainer[MetadataPendingBill]
    def __init__(self, success: bool = ..., updated_stages: _Optional[_Iterable[str]] = ..., author_name: _Optional[str] = ..., author_email: _Optional[str] = ..., stage_pending_commits: _Optional[_Iterable[_Union[StagePendingBill, _Mapping]]] = ..., metadata_pending_commits: _Optional[_Iterable[_Union[MetadataPendingBill, _Mapping]]] = ...) -> None: ...

class BillIndexData(_message.Message):
    __slots__ = ("title", "status", "activity", "stages", "last_checked")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    STAGES_FIELD_NUMBER: _ClassVar[int]
    LAST_CHECKED_FIELD_NUMBER: _ClassVar[int]
    title: str
    status: str
    activity: str
    stages: _containers.RepeatedScalarFieldContainer[str]
    last_checked: str
    def __init__(self, title: _Optional[str] = ..., status: _Optional[str] = ..., activity: _Optional[str] = ..., stages: _Optional[_Iterable[str]] = ..., last_checked: _Optional[str] = ...) -> None: ...

class SessionInfo(_message.Message):
    __slots__ = ("name", "status", "updated")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    name: str
    status: str
    updated: str
    def __init__(self, name: _Optional[str] = ..., status: _Optional[str] = ..., updated: _Optional[str] = ...) -> None: ...

class DocViewerLinks(_message.Message):
    __slots__ = ("xml_links", "html_links")
    class XmlLinksEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class HtmlLinksEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    XML_LINKS_FIELD_NUMBER: _ClassVar[int]
    HTML_LINKS_FIELD_NUMBER: _ClassVar[int]
    xml_links: _containers.ScalarMap[str, str]
    html_links: _containers.ScalarMap[str, str]
    def __init__(self, xml_links: _Optional[_Mapping[str, str]] = ..., html_links: _Optional[_Mapping[str, str]] = ...) -> None: ...
