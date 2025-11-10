import json
from pathlib import Path

from src.extractors.companies_parser import parse_company_html

def test_company_minimal_fields(tmp_path: Path):
    samples = json.loads(Path("data/samples.json").read_text(encoding="utf-8"))
    comp = parse_company_html(samples["company_html"])
    assert comp.type == "company"
    assert comp.slug == samples["expected_company"]["slug"]
    assert comp.name == samples["expected_company"]["name"]
    assert comp.jobs_count == samples["expected_company"]["jobs_count"]
    assert comp.organization_url == samples["expected_company"]["organization_url"]

    # sanity: techs, socials, offices parsed
    assert len(comp.technos_list) >= 5
    assert comp.social_networks is not None
    assert len(comp.offices) == 1