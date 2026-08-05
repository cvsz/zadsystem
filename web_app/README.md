# ZAD System - Content Dashboard (Web App)

Full-featured web dashboard matching [tina-claude.netlify.app/content_dashboard_demo](https://tina-claude.netlify.app/content_dashboard_demo)

## 🚀 Features

### Complete Dashboard
- **Real-time Brand Analysis** - Search any brand and get instant ad intelligence
- **5 Key Metrics** - Total Ads, Active Campaigns, Winning Ads, Angle Gaps, Creative Ideas
- **Winning Ad Patterns** - Identify top-performing ad patterns with confidence scores
- **Angle Gap Opportunities** - Discover untapped market opportunities with ROAS predictions
- **20 Creative Ideas** - Generate complete creative concepts for all platforms
- **Recent Ads Table** - View latest ads with performance scores

### Backend API (FastAPI)
- `/dashboard/{brand}` - Complete dashboard data
- `/search` - Search ads by brand
- `/analyze` - Comprehensive brand analysis
- `/winners/{brand}` - Get winning patterns
- `/angles/{brand}` - Find angle gaps
- `/creative/generate` - Generate creatives from brief
- `/creative/templates` - List all 20 creative templates
- `/report/{brand}` - Executive report generation

### Frontend (Vue 3 + Tailwind CSS)
- Modern, responsive UI
- Real-time updates
- Interactive charts and cards
- Country selection (US, TH, GB, AU, SG)
- Quick search suggestions
- Loading and error states

## 📁 Project Structure

```
web_app/
├── backend/
│   ├── main.py           # FastAPI server with all endpoints
│   └── requirements.txt  # Python dependencies
├── frontend/
│   ├── index.html        # Single-page Vue 3 app
│   └── public/           # Static assets
└── README.md             # This file
```

## 🛠️ Installation & Setup

### 1. Install Backend Dependencies

```bash
cd web_app/backend
pip install -r requirements.txt
```

### 2. Run Backend Server

```bash
# From web_app/backend directory
python main.py
```

Server will start at `http://localhost:8001` (or your chosen port)

### 3. Run Frontend

Option A: Simple HTTP Server
```bash
cd web_app/frontend
python -m http.server 3000
```

Option B: Open directly in browser
```bash
# Just open frontend/index.html in your browser
```

Frontend will be available at `http://localhost:3000`

## 🔌 API Endpoints

### GET /dashboard/{brand_name}
Get complete dashboard data for a brand.

**Parameters:**
- `brand_name` (path): Brand to analyze
- `country` (query, optional): Country code (default: US)

**Response:**
```json
{
  "metrics": {
    "total_ads": 50,
    "active_campaigns": 12,
    "winning_ads": 5,
    "angle_gaps": 8,
    "creative_ideas": 20,
    "last_updated": "2024-01-15T10:30:00"
  },
  "recent_ads": [...],
  "winner_patterns": [...],
  "angle_gaps": [...],
  "top_creatives": [...],
  "trends": {...}
}
```

### POST /search
Search ads for a brand.

**Body:**
```json
{
  "brand_name": "Sephora",
  "country": "US",
  "limit": 50
}
```

### GET /creative/templates
Get all 20 creative templates.

**Response:**
```json
{
  "templates": [
    {"no": 1, "angle": "Free Gift First Order", "category": "Promotion"},
    {"no": 2, "angle": "Gift Card", "category": "Promotion"},
    ...
  ],
  "total": 20
}
```

## 🎨 Creative Templates (20 Total)

| No | Angle | Category |
|----|-------|----------|
| 1 | Free Gift First Order | Promotion |
| 2 | Gift Card | Promotion |
| 3 | New Launch | Product |
| 4 | Catalog Bestsellers | Product |
| 5 | Carousel Routine | Format |
| 6 | UGC Review | Social Proof |
| 7 | Quiz Personalization | Engagement |
| 8 | Shade Match | Product |
| 9 | Mini Trial | Promotion |
| 10 | Bundle Stack | Promotion |
| 11 | Loyalty | Retention |
| 12 | Flash Gift 24h | Urgency |
| 13 | Sensitive Skin | Benefit |
| 14 | Clean Beauty | Benefit |
| 15 | Unboxing | Experience |
| 16 | Makeup Before/After | Transformation |
| 17 | Seasonal | Timing |
| 18 | Cart Retargeting | Retargeting |
| 19 | Social Proof | Social Proof |
| 20 | Routine Comparison | Education |

## 🧪 Testing

### Test Backend API

```bash
# Health check
curl http://localhost:8001/health

# Get dashboard
curl http://localhost:8001/dashboard/Sephora

# Get creative templates
curl http://localhost:8001/creative/templates
```

### Test Frontend

1. Start backend: `python backend/main.py`
2. Open `frontend/index.html` in browser
3. Enter brand name (e.g., "Sephora")
4. Click "Analyze" to see full dashboard

## 🔧 Configuration

### Backend Environment Variables

Create `.env` file in `backend/`:

```env
META_API_KEY=your_meta_api_key
DEBUG=true
LOG_LEVEL=INFO
```

### Frontend API URL

Edit `frontend/index.html` and change:

```javascript
apiBaseUrl: 'http://localhost:8001'  // Change to your backend URL
```

## 🚀 Deployment

### Deploy Backend (Production)

```bash
# Using uvicorn with workers
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

# Or with gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### Deploy Frontend

1. **Netlify**: Drag & drop `frontend/` folder
2. **Vercel**: Connect GitHub repo
3. **Static Hosting**: Upload to S3 + CloudFront

## 📊 Tech Stack

- **Backend**: FastAPI, Pydantic, Uvicorn
- **Frontend**: Vue 3, Tailwind CSS, Font Awesome
- **Data**: In-memory cache (Redis-ready)
- **Integration**: ZAD System CLI modules

## 🎯 Workflow (10 Minutes)

1. **Minute 1-2**: Search brand → View dashboard metrics
2. **Minute 3-4**: Review winning patterns → Identify success factors
3. **Minute 5-6**: Analyze angle gaps → Find opportunities
4. **Minute 7-8**: Generate 20 creatives → Select best concepts
5. **Minute 9-10**: Export report → Share with team

## 📝 License

MIT License - Part of ZAD System (Claude COWORK · Ad System)

---

**Powered by Claude COWORK · Ad System**  
Full-featured Ad Intelligence Platform
