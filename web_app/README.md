# ZAD System — Content Dashboard

Customer-facing demo dashboard for ZAD ad-intelligence workflows.

## Architecture

- **Backend:** FastAPI in `web_app/backend/`
- **Frontend:** static Vue 3 app in `web_app/frontend/`
- **Local frontend origin:** `http://localhost:3000`
- **Local backend origin:** `http://localhost:8001`

The frontend and backend are cross-origin in the supported local-development setup, so the backend must explicitly allow the frontend origin. Wildcard CORS is intentionally rejected.

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

Open `http://localhost:3000` in a browser.

Opening `index.html` directly with a `file://` URL is not a supported configuration because browsers use a `null` origin for local files and the backend intentionally does not allow wildcard/null-origin CORS.

## Production deployment

Prefer a same-origin reverse proxy so the browser frontend and API share one HTTPS origin. When the frontend is intentionally hosted on another origin, set `ZAD_CORS_ORIGINS` to the exact HTTPS frontend origin(s) before starting the API.

Example:

```bash
export ZAD_CORS_ORIGINS=https://dashboard.example.com
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

Do not use `*`. Do not add origins that are not owned and controlled by the deployment operator.

For Netlify, Vercel, S3/CloudFront, or another static-host deployment, configure the backend with that deployment's exact HTTPS origin before directing users to the frontend.

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
- Cross-origin access must be explicitly configured through `ZAD_CORS_ORIGINS`.
- Allowed CORS methods are limited to `GET`, `POST`, and `OPTIONS`.
- Allowed request headers are limited to `Authorization` and `Content-Type`.
- The repository CI validates dependency vulnerabilities, immutable GitHub Actions refs, trusted wheel hashes, offline installation, CycloneDX SBOMs, backend imports, and tests.

## Smoke checks

With the backend running:

```bash
curl http://localhost:8001/health
curl http://localhost:8001/dashboard/Sephora
curl http://localhost:8001/creative/templates
```

## License

MIT License — part of ZAD System / ZeaZDev.
