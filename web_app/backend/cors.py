"""CORS origin policy helpers for the ZAD dashboard backend."""

import os
from urllib.parse import urlparse


def configured_cors_origins() -> list[str]:
    """Return validated explicit browser origins; empty means same-origin only."""
    raw = os.getenv("ZAD_CORS_ORIGINS", "").strip()
    if not raw:
        return []

    origins: list[str] = []
    for value in raw.split(","):
        origin = value.strip().rstrip("/")
        if not origin:
            continue
        if origin == "*":
            raise RuntimeError("ZAD_CORS_ORIGINS must not contain wildcard origins")
        parsed = urlparse(origin)
        if (
            parsed.scheme not in {"http", "https"}
            or not parsed.netloc
            or parsed.username is not None
            or parsed.password is not None
            or parsed.path not in {"", "/"}
            or parsed.params
            or parsed.query
            or parsed.fragment
        ):
            raise RuntimeError(f"Invalid CORS origin: {origin}")
        if origin not in origins:
            origins.append(origin)
    return origins
