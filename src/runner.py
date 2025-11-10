from __future__ import annotations

import argparse
import json
import logging
import os
from typing import List, Dict

from .extractors.companies_parser import parse_company_html
from .extractors.jobs_parser import parse_job_html
from .outputs.exporters import write_ndjson, write_json
from .outputs.schemas import Company, Job

def configure_logging(level: str = "INFO") -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(message)s",
    )

def load_samples(path: str) -> Dict[str, str]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def run(mode: str, input_source: str, out_dir: str, out_format: str, filename: str) -> str:
    os.makedirs(out_dir, exist_ok=True)
    samples = load_samples(input_source)

    records: List[Dict] = []

    if mode in {"companies", "both"}:
        company_html = samples["company_html"]
        company: Company = parse_company_html(company_html)
        records.append(company)

    if mode in {"jobs", "both"}:
        job_html = samples["job_html"]
        job: Job = parse_job_html(job_html)
        records.append(job)

    output_path = os.path.join(out_dir, filename)
    if out_format.lower() in {"ndjson", "jsonl"}:
        write_ndjson(output_path, records)
    else:
        write_json(output_path, records)

    logging.info("Wrote %d records to %s", len(records), output_path)
    return output_path

def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Welcome to the Jungle scraper runner (sample-driven).")
    p.add_argument("--mode", choices=["companies", "jobs", "both"], default="both")
    p.add_argument("--input", default="data/samples.json")
    p.add_argument("--out-dir", default="dist")
    p.add_argument("--format", choices=["ndjson", "json"], default="ndjson")
    p.add_argument("--filename", default="dataset.ndjson")
    p.add_argument("--log-level", default="INFO")
    return p

def main() -> None:
    args = build_arg_parser().parse_args()
    configure_logging(args.log_level)
    run(args.mode, args.input, args.out_dir, args.format, args.filename)

if __name__ == "__main__":
    main()