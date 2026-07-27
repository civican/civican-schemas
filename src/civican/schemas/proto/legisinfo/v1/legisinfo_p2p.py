# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 7.35.1 
# Pydantic Version: 2.13.4 
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
import typing

class Chamber(IntEnum):
    CHAMBER_UNSPECIFIED = 0
    CHAMBER_HOUSE = 1
    CHAMBER_SENATE = 2


class SortField(IntEnum):
    SORT_FIELD_UNSPECIFIED = 0
    SORT_FIELD_NUMBER = 1
    SORT_FIELD_LATEST_EVENT_DATE = 2
    SORT_FIELD_SPONSOR = 3
    SORT_FIELD_STATUS = 4
    SORT_FIELD_TITLE = 5


class SortDirection(IntEnum):
    SORT_DIRECTION_UNSPECIFIED = 0
    SORT_DIRECTION_ASC = 1
    SORT_DIRECTION_DESC = 2


class PendingBillType(IntEnum):
    PENDING_BILL_TYPE_UNSPECIFIED = 0
    PENDING_BILL_TYPE_STAGE = 1
    PENDING_BILL_TYPE_METADATA = 2

class ListSessionsRequest(BaseModel):
    pass

class ListSessionsResponse(BaseModel):
    sessions: typing.List[str] = Field(default_factory=list)

class BillFilters(BaseModel):
    model_config = ConfigDict(validate_default=True)
    session: str = Field(default="")
    chamber: Chamber = Field(default=0)
    sponsor: str = Field(default="")
    sponsor_affiliation: str = Field(default="")
    status: str = Field(default="")
    latest_activity: str = Field(default="")
    number: str = Field(default="")
    date_after: str = Field(default="")
    date_before: str = Field(default="")
    search_query: str = Field(default="")
    has_text: bool = Field(default=False)
    committee_only: bool = Field(default=False)

class ListBillsRequest(BaseModel):
    model_config = ConfigDict(validate_default=True)
    filters: BillFilters = Field(default_factory=BillFilters)
    sort_field: SortField = Field(default=0)
    sort_direction: SortDirection = Field(default=0)
    limit: int = Field(default=0)
    offset: int = Field(default=0)

class BillSummary(BaseModel):
    number: str = Field(default="")
    session: str = Field(default="")
    title_en: str = Field(default="")
    title_fr: str = Field(default="")
    sponsor_name: str = Field(default="")
    status: str = Field(default="")
    latest_event_date: str = Field(default="")

class ListBillsResponse(BaseModel):
    bills: typing.List[BillSummary] = Field(default_factory=list)
    total_count: int = Field(default=0)

class GetBillRequest(BaseModel):
    session: str = Field(default="")
    bill_number: str = Field(default="")

class BillStage(BaseModel):
    slug: str = Field(default="")
    name: str = Field(default="")
    date: str = Field(default="")
    source_type: str = Field(default="")

class BillDetail(BaseModel):
    number: str = Field(default="")
    session: str = Field(default="")
    title_en: str = Field(default="")
    title_fr: str = Field(default="")
    sponsor_name: str = Field(default="")
    sponsor_email: str = Field(default="")
    status: str = Field(default="")
    latest_event_date: str = Field(default="")
    stages: typing.List[BillStage] = Field(default_factory=list)

class GetBillResponse(BaseModel):
    bill: BillDetail = Field(default_factory=BillDetail)

class GetBillTextRequest(BaseModel):
    class Format(IntEnum):
        FORMAT_UNSPECIFIED = 0
        FORMAT_MARKDOWN = 1
        FORMAT_XML = 2

    model_config = ConfigDict(validate_default=True)
    session: str = Field(default="")
    bill_number: str = Field(default="")
    stage_slug: str = Field(default="")
    format: "GetBillTextRequest.Format" = Field(default=0)

class GetBillTextResponse(BaseModel):
    bill_number: str = Field(default="")
    session: str = Field(default="")
    stage_slug: str = Field(default="")
    content: str = Field(default="")
    format: str = Field(default="")

class StagePendingBill(BaseModel):
    session: str = Field(default="")
    bill_number: str = Field(default="")
    author_name: str = Field(default="")
    author_email: str = Field(default="")
    metadata_xml_path: str = Field(default="")
    summary_md_path: str = Field(default="")
    slug: str = Field(default="")
    stage_name: str = Field(default="")
    stage_date: typing.Optional[str] = Field(default="")
    stage_xml_path: str = Field(default="")
    stage_md_path: str = Field(default="")
    type: str = Field(default="")

class MetadataPendingBill(BaseModel):
    session: str = Field(default="")
    bill_number: str = Field(default="")
    author_name: str = Field(default="")
    author_email: str = Field(default="")
    metadata_xml_path: str = Field(default="")
    summary_md_path: str = Field(default="")
    event_date: typing.Optional[str] = Field(default="")
    restore_xml_path: typing.Optional[str] = Field(default="")
    restore_md_path: typing.Optional[str] = Field(default="")
    type: str = Field(default="")

class ScrapeResult(BaseModel):
    success: bool = Field(default=False)
    updated_stages: typing.List[str] = Field(default_factory=list)
    author_name: str = Field(default="")
    author_email: str = Field(default="")
    stage_pending_commits: typing.List[StagePendingBill] = Field(default_factory=list)
    metadata_pending_commits: typing.List[MetadataPendingBill] = Field(default_factory=list)

class BillIndexData(BaseModel):
    title: str = Field(default="")
    status: str = Field(default="")
    activity: str = Field(default="")
    stages: typing.List[str] = Field(default_factory=list)
    last_checked: str = Field(default="")

class SessionInfo(BaseModel):
    name: str = Field(default="")
    status: str = Field(default="")
    updated: str = Field(default="")

class DocViewerLinks(BaseModel):
    xml_links: "typing.Dict[str, str]" = Field(default_factory=dict)
    html_links: "typing.Dict[str, str]" = Field(default_factory=dict)
