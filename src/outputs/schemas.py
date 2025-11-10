from __future__ import annotations

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime

class Office(BaseModel):
    address: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    country_code: Optional[str] = None
    zip_code: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    is_headquarter: Optional[bool] = False

class SocialLinks(BaseModel):
    facebook: Optional[HttpUrl] = None
    instagram: Optional[HttpUrl] = None
    linkedin: Optional[HttpUrl] = None
    twitter: Optional[HttpUrl] = None
    youtube: Optional[HttpUrl] = None

class DescriptionSection(BaseModel):
    title: str
    body: str  # can be Markdown or HTML

class Organization(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
    nb_employees: Optional[int] = None
    social_networks: Optional[SocialLinks] = None
    logo: Optional[HttpUrl] = None

class Company(BaseModel):
    type: str = Field(default="company")
    organization_url: Optional[HttpUrl] = None
    slug: str
    name: str
    descriptions: List[DescriptionSection] = Field(default_factory=list)
    sectors: List[Dict[str, Optional[str]]] = Field(default_factory=list)
    size: Optional[str] = None
    jobs_count: Optional[int] = None
    technos_list: List[str] = Field(default_factory=list)
    social_networks: Optional[SocialLinks] = None
    offices: List[Office] = Field(default_factory=list)
    nb_employees: Optional[int] = None
    parity_men: Optional[float] = None
    parity_women: Optional[float] = None
    equality_indexes: Optional[Dict[str, Any]] = None
    images: List[HttpUrl] = Field(default_factory=list)
    videos: List[HttpUrl] = Field(default_factory=list)
    updated_at: Optional[datetime] = None
    published_at: Optional[datetime] = None
    jobs: List["Job"] = Field(default_factory=list)

class Job(BaseModel):
    type: str = Field(default="job")
    organization_url: Optional[HttpUrl] = None
    job_url: Optional[HttpUrl] = None
    slug: str
    name: str
    contract_type: Optional[str] = None
    remote: Optional[str] = None
    language: Optional[str] = None
    published_at_date: Optional[str] = None
    published_at_timestamp: Optional[int] = None
    experience_level: Optional[str] = None
    experience_level_minimum: Optional[int] = None
    salary_minimum: Optional[float] = None
    salary_maximum: Optional[float] = None
    salary_period: Optional[str] = None
    salary_currency: Optional[str] = None
    benefits: List[str] = Field(default_factory=list)
    skills: List[str] = Field(default_factory=list)
    offices: List[Office] = Field(default_factory=list)
    start_date: Optional[datetime] = None
    apply_url: Optional[HttpUrl] = None
    organization: Optional[Organization] = None

Company.model_rebuild()