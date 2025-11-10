import json
from pathlib import Path

from src.extractors.jobs_parser import parse_job_html

def test_job_minimal_fields(tmp_path: Path):
    samples = json.loads(Path("data/samples.json").read_text(encoding="utf-8"))
    job = parse_job_html(samples["job_html"])
    assert job.type == "job"
    assert job.slug == samples["expected_job"]["slug"]
    assert job.name == samples["expected_job"]["name"]
    assert job.contract_type == samples["expected_job"]["contract_type"]
    assert job.remote == samples["expected_job"]["remote"]
    assert job.language == samples["expected_job"]["language"]

    # sanity: organization and offices parsed
    assert job.organization is not None
    assert len(job.offices) == 1
    assert job.published_at_date == "2024-10-25"