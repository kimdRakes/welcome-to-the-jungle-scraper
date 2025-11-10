from __future__ import annotations

import json
import os
from typing import Iterable, Any, List, Union

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)

def to_jsonable(obj: Any) -> Any:
    # Pydantic BaseModel has model_dump; datetime is handled by default=str later.
    if hasattr(obj, "model_dump"):
        return obj.model_dump()
    return obj

def write_ndjson(filepath: str, rows: Iterable[Any]) -> None:
    ensure_dir(os.path.dirname(filepath) or ".")
    with open(filepath, "w", encoding="utf-8") as f:
        for row in rows:
            json.dump(to_jsonable(row), f, ensure_ascii=False, default=str)
            f.write("\n")

def write_json(filepath: str, rows: Union[List[Any], Iterable[Any]]) -> None:
    ensure_dir(os.path.dirname(filepath) or ".")
    data = list(rows)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump([to_jsonable(r) for r in data], f, ensure_ascii=False, indent=2, default=str)