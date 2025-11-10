from __future__ import annotations

import re
from datetime import datetime
from typing import Dict, Optional

from dateutil import parser as dateparser
from langdetect import detect, LangDetectException

def parse_int(value: str) -> Optional[int]:
    if value is None:
        return None
    m = re.search(r"(\d+)", str(value).replace("\xa0", " ").replace(",", ""))
    return int(m.group(1)) if m else None

def parse_float(value: str) -> Optional[float]:
    if value is None:
        return None
    m = re.search(r"(\d+(?:\.\d+)?)", str(value).replace("\xa0", " ").replace(",", "."))
    return float(m.group(1)) if m else None

def parse_date(dt: str) -> Optional[datetime]:
    if not dt:
        return None
    try:
        return dateparser.parse(dt)
    except (ValueError, TypeError):
        return None

def normalize_remote(flag: Optional[str]) -> Optional[str]:
    if not flag:
        return None
    flag = flag.strip().lower()
    if flag in {"oui", "yes", "true", "1", "remote"}:
        return "yes"
    if flag in {"non", "no", "false", "0", "office", "onsite"}:
        return "no"
    if flag in {"hybrid"}:
        return "hybrid"
    return flag

def detect_language(text: str, fallback: str = "fr") -> str:
    if not text or len(text.strip()) < 10:
        return fallback
    try:
        return detect(text)
    except LangDetectException:
        return fallback

def extract_socials(links: Dict[str, str]) -> Dict[str, str]:
    """
    Input map of rel/name -> href, returns normalized keys limited to known networks.
    """
    out: Dict[str, str] = {}
    for key, url in links.items():
        k = key.strip().lower()
        if "facebook" in k or "fb" == k:
            out["facebook"] = url
        elif "instagram" in k or "ig" == k:
            out["instagram"] = url
        elif "linkedin" in k or "in" == k:
            out["linkedin"] = url
        elif "twitter" in k or "x" == k or "tw" == k:
            out["twitter"] = url
        elif "youtube" in k or "yt" == k:
            out["youtube"] = url
    return out

def normalize_office_attrs(attrs: Dict[str, str]) -> Dict[str, object]:
    return {
        "address": attrs.get("text"),
        "city": attrs.get("data-city") or attrs.get("city"),
        "district": attrs.get("data-district") or attrs.get("district"),
        "country_code": attrs.get("data-country") or attrs.get("country_code"),
        "zip_code": attrs.get("data-zip") or attrs.get("zip"),
        "latitude": parse_float(attrs.get("data-lat") or attrs.get("lat")),
        "longitude": parse_float(attrs.get("data-lng") or attrs.get("lng")),
        "is_headquarter": str(attrs.get("data-hq") or "").lower() in {"1", "true", "yes"}
    }