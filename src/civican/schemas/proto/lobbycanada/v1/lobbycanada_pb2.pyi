from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LobbyRegistration(_message.Message):
    __slots__ = ("registration_id", "registrant_name", "client_org_name", "type", "status", "effective_date", "posted_date", "subject_matters", "legislative_proposals", "government_institutions")
    REGISTRATION_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTRANT_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_DATE_FIELD_NUMBER: _ClassVar[int]
    POSTED_DATE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_MATTERS_FIELD_NUMBER: _ClassVar[int]
    LEGISLATIVE_PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    GOVERNMENT_INSTITUTIONS_FIELD_NUMBER: _ClassVar[int]
    registration_id: str
    registrant_name: str
    client_org_name: str
    type: str
    status: str
    effective_date: str
    posted_date: str
    subject_matters: _containers.RepeatedScalarFieldContainer[str]
    legislative_proposals: _containers.RepeatedScalarFieldContainer[str]
    government_institutions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, registration_id: _Optional[str] = ..., registrant_name: _Optional[str] = ..., client_org_name: _Optional[str] = ..., type: _Optional[str] = ..., status: _Optional[str] = ..., effective_date: _Optional[str] = ..., posted_date: _Optional[str] = ..., subject_matters: _Optional[_Iterable[str]] = ..., legislative_proposals: _Optional[_Iterable[str]] = ..., government_institutions: _Optional[_Iterable[str]] = ...) -> None: ...

class LobbyCommunication(_message.Message):
    __slots__ = ("communication_id", "registration_id", "client_org_name", "communication_date", "posted_date", "lobbyist_name", "dpoh_name", "dpoh_title", "government_institution", "subject_matters", "legislative_proposals")
    COMMUNICATION_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    POSTED_DATE_FIELD_NUMBER: _ClassVar[int]
    LOBBYIST_NAME_FIELD_NUMBER: _ClassVar[int]
    DPOH_NAME_FIELD_NUMBER: _ClassVar[int]
    DPOH_TITLE_FIELD_NUMBER: _ClassVar[int]
    GOVERNMENT_INSTITUTION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_MATTERS_FIELD_NUMBER: _ClassVar[int]
    LEGISLATIVE_PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    communication_id: str
    registration_id: str
    client_org_name: str
    communication_date: str
    posted_date: str
    lobbyist_name: str
    dpoh_name: str
    dpoh_title: str
    government_institution: str
    subject_matters: _containers.RepeatedScalarFieldContainer[str]
    legislative_proposals: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, communication_id: _Optional[str] = ..., registration_id: _Optional[str] = ..., client_org_name: _Optional[str] = ..., communication_date: _Optional[str] = ..., posted_date: _Optional[str] = ..., lobbyist_name: _Optional[str] = ..., dpoh_name: _Optional[str] = ..., dpoh_title: _Optional[str] = ..., government_institution: _Optional[str] = ..., subject_matters: _Optional[_Iterable[str]] = ..., legislative_proposals: _Optional[_Iterable[str]] = ...) -> None: ...

class LobbyScrapeResult(_message.Message):
    __slots__ = ("success", "total_scraped", "registrations_scraped", "communications_scraped")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SCRAPED_FIELD_NUMBER: _ClassVar[int]
    REGISTRATIONS_SCRAPED_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_SCRAPED_FIELD_NUMBER: _ClassVar[int]
    success: bool
    total_scraped: int
    registrations_scraped: int
    communications_scraped: int
    def __init__(self, success: bool = ..., total_scraped: _Optional[int] = ..., registrations_scraped: _Optional[int] = ..., communications_scraped: _Optional[int] = ...) -> None: ...

class ListRegistrationsRequest(_message.Message):
    __slots__ = ("search_query", "registrant_name", "client_org_name", "status", "limit", "offset")
    SEARCH_QUERY_FIELD_NUMBER: _ClassVar[int]
    REGISTRANT_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    search_query: str
    registrant_name: str
    client_org_name: str
    status: str
    limit: int
    offset: int
    def __init__(self, search_query: _Optional[str] = ..., registrant_name: _Optional[str] = ..., client_org_name: _Optional[str] = ..., status: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListRegistrationsResponse(_message.Message):
    __slots__ = ("registrations", "total_count")
    REGISTRATIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    registrations: _containers.RepeatedCompositeFieldContainer[LobbyRegistration]
    total_count: int
    def __init__(self, registrations: _Optional[_Iterable[_Union[LobbyRegistration, _Mapping]]] = ..., total_count: _Optional[int] = ...) -> None: ...

class GetRegistrationRequest(_message.Message):
    __slots__ = ("registration_id",)
    REGISTRATION_ID_FIELD_NUMBER: _ClassVar[int]
    registration_id: str
    def __init__(self, registration_id: _Optional[str] = ...) -> None: ...

class GetRegistrationResponse(_message.Message):
    __slots__ = ("registration",)
    REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    registration: LobbyRegistration
    def __init__(self, registration: _Optional[_Union[LobbyRegistration, _Mapping]] = ...) -> None: ...

class ListCommunicationsRequest(_message.Message):
    __slots__ = ("search_query", "client_org_name", "lobbyist_name", "dpoh_name", "government_institution", "date_after", "date_before", "limit", "offset")
    SEARCH_QUERY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    LOBBYIST_NAME_FIELD_NUMBER: _ClassVar[int]
    DPOH_NAME_FIELD_NUMBER: _ClassVar[int]
    GOVERNMENT_INSTITUTION_FIELD_NUMBER: _ClassVar[int]
    DATE_AFTER_FIELD_NUMBER: _ClassVar[int]
    DATE_BEFORE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    search_query: str
    client_org_name: str
    lobbyist_name: str
    dpoh_name: str
    government_institution: str
    date_after: str
    date_before: str
    limit: int
    offset: int
    def __init__(self, search_query: _Optional[str] = ..., client_org_name: _Optional[str] = ..., lobbyist_name: _Optional[str] = ..., dpoh_name: _Optional[str] = ..., government_institution: _Optional[str] = ..., date_after: _Optional[str] = ..., date_before: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListCommunicationsResponse(_message.Message):
    __slots__ = ("communications", "total_count")
    COMMUNICATIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    communications: _containers.RepeatedCompositeFieldContainer[LobbyCommunication]
    total_count: int
    def __init__(self, communications: _Optional[_Iterable[_Union[LobbyCommunication, _Mapping]]] = ..., total_count: _Optional[int] = ...) -> None: ...

class GetCommunicationRequest(_message.Message):
    __slots__ = ("communication_id",)
    COMMUNICATION_ID_FIELD_NUMBER: _ClassVar[int]
    communication_id: str
    def __init__(self, communication_id: _Optional[str] = ...) -> None: ...

class GetCommunicationResponse(_message.Message):
    __slots__ = ("communication",)
    COMMUNICATION_FIELD_NUMBER: _ClassVar[int]
    communication: LobbyCommunication
    def __init__(self, communication: _Optional[_Union[LobbyCommunication, _Mapping]] = ...) -> None: ...
