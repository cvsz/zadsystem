import pytest

from web_app.backend.main import configured_cors_origins


def test_cors_defaults_to_same_origin(monkeypatch):
    monkeypatch.delenv("ZAD_CORS_ORIGINS", raising=False)
    assert configured_cors_origins() == []


def test_cors_accepts_only_explicit_http_origins(monkeypatch):
    monkeypatch.setenv(
        "ZAD_CORS_ORIGINS",
        "https://app.zeaz.dev, http://localhost:5173/, https://app.zeaz.dev",
    )
    assert configured_cors_origins() == [
        "https://app.zeaz.dev",
        "http://localhost:5173",
    ]


@pytest.mark.parametrize(
    "value",
    [
        "*",
        "https://user:pass@app.zeaz.dev",
        "https://app.zeaz.dev/path",
        "https://app.zeaz.dev?debug=1",
        "ftp://app.zeaz.dev",
        "app.zeaz.dev",
    ],
)
def test_cors_rejects_unsafe_or_malformed_origins(monkeypatch, value):
    monkeypatch.setenv("ZAD_CORS_ORIGINS", value)
    with pytest.raises(RuntimeError):
        configured_cors_origins()
