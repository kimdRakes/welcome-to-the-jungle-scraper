from __future__ import annotations

from typing import List, Dict
from bs4 import BeautifulSoup

from ..outputs.schemas import Job, Organization, SocialLinks, Office
from .utils_normalize import (
    parse_date,
    extract_socials,
    normalize_office_attrs,
    normalize_remote,
)

def parse_job_html(html: str) -> Job:
    """
    Best-effort parser for a WelcomeToTheJungle job card/page.
    Works with simplified HTML used in tests/samples.
    """
    soup = BeautifulSoup(html, "lxml")

    article = soup.select_one("#job") or soup.select_one("article")
    slug = (article.get("data-slug") if article else "") or ""

    title_el = soup.select_one(".job-title") or soup.find("h1")
    title = (title_el.get_text(strip=True) if title_el else "").strip()

    job_url_el = soup.select_one(".job-url[href]")
    job_url = job_url_el["href"] if job_url_el else None

    contract = article.get("data-contract") if article else None
    remote_flag = normalize_remote(article.get("data-remote") if article else None)
    language = article.get("data-language") if article else None

    published_el = soup.select_one(".published-at")
    published_dt = parse_date(published_el.get("datetime") if published_el else None)
    published_date = published_dt.date().isoformat() if published_dt else None
    published_ts = int(published_dt.timestamp()) if published_dt else None

    benefits = [li.get_text(strip=True) for li in soup.select(".benefits li")]
    skills = [li.get_text(strip=True) for li in soup.select(".skills li")]

    # Offices
    offices: List[Office] = []
    for li in soup.select(".offices li"):
        attrs: Dict[str, str] = {**li.attrs, "text": li.get_text(strip=True)}
        offices.append(Office(**normalize_office_attrs(attrs)))

    start_el = soup.select_one(".start-date")
    start_date = parse_date(start_el.get("datetime") if start_el else None)

    apply_el = soup.select_one(".apply-url[href]")
    apply_url = apply_el["href"] if apply_el else None

    org_url_el = soup.select_one(".organization-url[href]")
    org_url = org_url_el["href"] if org_url_el else None

    # Organization block
    org_section = soup.select_one(".organization")
    organization = None
    if org_section:
        socials_map: Dict[str, str] = {}
        for a in org_section.select(".socials a[href]"):
            key = a.get("rel")[0] if a.get("rel") else (a.get_text(strip=True) or "link")
            socials_map[str(key)] = a["href"]
        organization = Organization(
            name=org_section.get("data-name"),
            slug=org_section.get("data-slug"),
            nb_employees=int(org_section.get("data-nb-employees"))
            if org_section.get("data-nb-employees")
            else None,
            social_networks=SocialLinks(**extract_socials(socials_map))
            if socials_map
            else None,
        )

    job = Job(
      organization_url=org_url,
      job_url=job_url,
      slug=slug,
      name=title or "",
      contract_type=contract,
      remote=remote_flag,
      language=language,
      published_at_date=published_date,
      published_at_timestamp=published_ts,
      benefits=benefits,
      skills=skills,
      offices=offices,
      start_date=start_date,
      apply_url=apply_url,
      organization=organization,
    )
    return job