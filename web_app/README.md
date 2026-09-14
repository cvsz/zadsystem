# ZAD System — Content Dashboard

Customer-facing demo dashboard for ZAD ad-intelligence workflows.

## Architecture

- **Backend:** FastAPI in `web_app/backend/`
- **Frontend:** static Vue 3 app in `web_app/frontend/`
- **Local frontend origin:** `http://localhost:3000`
- **Local backend origin:** `http://localhost:8001`

The frontend and backend are cross-origin only in the supported local-development setup. Production uses a same-origin reverse proxy so the browser never needs a wildcard or broad CORS policy.

## Local development

### 1. Install backend dependencies

```bash
cd web_app/backend
pip install -r requirements.txt
```

### 2. Configure the backend

Copy the supported example configuration:

```bash
cp .env.example .env
```

The default example contains:

```env
ZAD_CORS_ORIGINS=http://localhost:3000
```

`ZAD_CORS_ORIGINS` is a comma-separated list of explicit `http://` or `https://` origins. Wildcards, URL credentials, paths, query strings, fragments, and non-HTTP(S) schemes are rejected. If the variable is absent, the API is same-origin only.

### 3. Start the backend

```bash
python main.py
```

The development server listens on `http://localhost:8001`.

### 4. Start the frontend

In another shell:

```bash
cd web_app/frontend
python -m http.server 3000
```

Open `http://localhost:3000` in a browser. The shipped frontend detects this local-development origin and calls `http://localhost:8001`.

Opening `index.html` directly with a `file://` URL is not supported because browsers use a `null` origin and the backend intentionally rejects wildcard/null-origin CORS.

## Production deployment

Serve the frontend and API through one HTTPS origin. Outside the supported local-development origin, the shipped frontend uses `window.location.origin` as its API base URL. A production reverse proxy therefore must route the API paths (`/health`, `/dashboard`, `/search`, `/winners`, `/angles`, `/creative`, and `/report`) to the FastAPI service while serving the static frontend from the same public origin.

Start the internal API service without a cross-origin allow-list when using that topology:

```bash
unset ZAD_CORS_ORIGINS
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

Do not expose the internal API port directly to browsers when the public dashboard is served elsewhere. Cross-origin production hosting of the shipped frontend is not a supported deployment mode until an explicit, operator-controlled frontend API-base configuration is added and tested.

## API endpoints

- `GET /` — API metadata
- `GET /health` — health status
- `GET /dashboard/{brand_name}` — dashboard data
- `POST /search` — brand search
- `GET /winners/{brand_name}` — winning patterns
- `GET /angles/{brand_name}` — angle-gap analysis
- `POST /creative/generate` — creative generation
- `GET /creative/templates` — creative templates
- `GET /report/{brand_name}` — report output

## Security notes

- CORS defaults to same-origin only.
- Local cross-origin access must be explicitly configured through `ZAD_CORS_ORIGINS`.
- Wildcard origins are rejected.
- Allowed CORS methods are limited to `GET`, `POST`, and `OPTIONS`.
- Allowed request headers are limited to `Authorization` and `Content-Type`.
- The repository CI validates dependency vulnerabilities, immutable GitHub Actions refs, trusted wheel hashes, offline installation, CycloneDX SBOMs, backend imports, and tests.

## Smoke checks

With the local backend running:

```bash
curl http://localhost:8001/health
curl http://localhost:8001/dashboard/Sephora
curl http://localhost:8001/creative/templates
```

## License

MIT License — part of ZAD System / ZeaZDev.
