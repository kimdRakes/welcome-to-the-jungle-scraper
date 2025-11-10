from __future__ import annotations

from typing import Dict, List
from bs4 import BeautifulSoup

from ..outputs.schemas import Company, DescriptionSection, SocialLinks, Office
from .utils_normalize import (
    parse_int,
    parse_date,
    extract_socials,
    normalize_office_attrs,
)

def parse_company_html(html: str) -> Company:
    """
    Best-effort parser for a WelcomeToTheJungle company page.
    Works on simplified HTML used in tests/samples, and is resilient for real pages.
    """
    soup = BeautifulSoup(html, "lxml")

    article = soup.select_one("#company") or soup.select_one("article")
    slug = article.get("data-slug") if article else None

    name_el = soup.select_one(".company-name") or soup.find("h1")
    name = (name_el.get_text(strip=True) if name_el else "").strip()

    size_el = soup.select_one(".company-size")
    size = size_el.get_text(strip=True) if size_el else None

    jobs_count_el = soup.select_one(".jobs-count")
    jobs_count = parse_int(jobs_count_el.get_text()) if jobs_count_el else None

    org_url_el = soup.select_one(".org-url[href]")
    org_url = org_url_el["href"] if org_url_el else None

    # Descriptions
    descriptions: List[DescriptionSection] = []
    for sec in soup.select(".descriptions section"):
        title_el = sec.find(["h2", "h3"])
        title = title_el.get_text(strip=True) if title_el else "Description"
        body_el = sec.select_one(".body")
        body = body_el.decode_contents() if body_el else sec.get_text(" ", strip=True)
        descriptions.append(DescriptionSection(title=title, body=body))

    # Sectors
    sectors: List[Dict[str, str]] = []
    for li in soup.select(".company-sectors li"):
        sectors.append(
            {"name": li.get_text(strip=True), "parent_name": li.get("data-parent")}
        )

    # Tech stack
    technos = [li.get_text(strip=True) for li in soup.select(".technos li")]

    # Socials
    socials_map: Dict[str, str] = {}
    for a in soup.select(".socials a[href]"):
        key = a.get("rel")[0] if a.get("rel") else (a.get_text(strip=True) or "link")
        socials_map[str(key)] = a["href"]
    social_links = SocialLinks(**extract_socials(socials_map)) if socials_map else None

    # Offices
    offices: List[Office] = []
    for li in soup.select(".offices li"):
        attrs = {**li.attrs, "text": li.get_text(strip=True)}
        offices.append(Office(**normalize_office_attrs(attrs)))

    updated_at_el = soup.select_one(".updated-at")
    updated_at = parse_date(updated_at_el.get("datetime") if updated_at_el else None)

    comp = Company(
        organization_url=org_url,
        slug=slug or "",
        name=name or "",
        descriptions=descriptions,
        sectors=sectors,
        size=size,
        jobs_count=jobs_count,
        technos_list=technos,
        social_networks=social_links,
        offices=offices,
        updated_at=updated_at,
    )
    return comp