# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.3.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 7.35.1 
# Pydantic Version: 2.13.4 
from google.protobuf.message import Message  # type: ignore
from pydantic import BaseModel
from pydantic import Field
import typing


class LobbyRegistration(BaseModel):
    registration_id: str = Field(default="")
    registrant_name: str = Field(default="")
    client_org_name: str = Field(default="")
    type: str = Field(default="")
    status: str = Field(default="")
    effective_date: str = Field(default="")
    posted_date: str = Field(default="")
    subject_matters: typing.List[str] = Field(default_factory=list)
    legislative_proposals: typing.List[str] = Field(default_factory=list)
    government_institutions: typing.List[str] = Field(default_factory=list)

class LobbyCommunication(BaseModel):
    communication_id: str = Field(default="")
    registration_id: str = Field(default="")
    client_org_name: str = Field(default="")
    communication_date: str = Field(default="")
    posted_date: str = Field(default="")
    lobbyist_name: str = Field(default="")
    dpoh_name: str = Field(default="")
    dpoh_title: str = Field(default="")
    government_institution: str = Field(default="")
    subject_matters: typing.List[str] = Field(default_factory=list)
    legislative_proposals: typing.List[str] = Field(default_factory=list)

class LobbyScrapeResult(BaseModel):
    success: bool = Field(default=False)
    total_scraped: int = Field(default=0)
    registrations_scraped: int = Field(default=0)
    communications_scraped: int = Field(default=0)

class ListRegistrationsRequest(BaseModel):
    search_query: str = Field(default="")
    registrant_name: str = Field(default="")
    client_org_name: str = Field(default="")
    status: str = Field(default="")
    limit: int = Field(default=0)
    offset: int = Field(default=0)

class ListRegistrationsResponse(BaseModel):
    registrations: typing.List[LobbyRegistration] = Field(default_factory=list)
    total_count: int = Field(default=0)

class GetRegistrationRequest(BaseModel):
    registration_id: str = Field(default="")

class GetRegistrationResponse(BaseModel):
    registration: LobbyRegistration = Field(default_factory=LobbyRegistration)

class ListCommunicationsRequest(BaseModel):
    search_query: str = Field(default="")
    client_org_name: str = Field(default="")
    lobbyist_name: str = Field(default="")
    dpoh_name: str = Field(default="")
    government_institution: str = Field(default="")
    date_after: str = Field(default="")
    date_before: str = Field(default="")
    limit: int = Field(default=0)
    offset: int = Field(default=0)

class ListCommunicationsResponse(BaseModel):
    communications: typing.List[LobbyCommunication] = Field(default_factory=list)
    total_count: int = Field(default=0)

class GetCommunicationRequest(BaseModel):
    communication_id: str = Field(default="")

class GetCommunicationResponse(BaseModel):
    communication: LobbyCommunication = Field(default_factory=LobbyCommunication)
