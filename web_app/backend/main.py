"""ZAD System - Content Dashboard API - Standalone Demo"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
from datetime import datetime
import random

app = FastAPI(title="ZAD System - Content Dashboard", version="2.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

class BrandSearch(BaseModel):
    brand_name: str
    country: str = "US"
    limit: int = 50

class CreativeBrief(BaseModel):
    brand_name: str
    target_audience: str
    product_category: str
    key_message: str
    tone: str = "professional"
    platforms: List[str] = ["facebook", "instagram", "tiktok"]

def gen_ads(brand, limit=50):
    headlines = [f"New {brand} Collection", f"Shop {brand} Bestsellers", f"Limited Offer from {brand}", f"Discover {brand}", f"{brand} Sale 50% Off"]
    ctas = ["Shop Now", "Learn More", "Get Offer", "Book Now", "Sign Up"]
    platforms = ["facebook", "instagram", "tiktok"]
    return {"ads": [{"id": f"ad_{brand.lower()}_{i:04d}", "brand": brand, "headline": headlines[i%len(headlines)], "primary_text": f"Amazing {brand} products.", "cta": ctas[i%len(ctas)], "platform": platforms[i%len(platforms)], "start_date": "2024-01-01", "status": "active" if i%3!=0 else "paused", "performance_score": round(random.uniform(0.6, 0.95), 2)} for i in range(limit)], "total": limit}

def gen_winners(brand):
    patterns = [{"id": f"w{i}", "name": n, "description": d, "confidence": c, "examples": [], "metrics": m} for i, (n, d, c, m) in enumerate([("UGC Review Format", "User content performs 3x better", 0.89, {"avg_ctr": "2.8%", "conversion": "+45%"}), ("Before/After Transformation", "Visual transformation shows value", 0.85, {"avg_ctr": "3.1%", "conversion": "+62%"}), ("Limited Time Urgency", "Flash sales create action", 0.78, {"avg_ctr": "2.4%", "conversion": "+89%"}), ("Bundle Value", "Bundles increase AOV 35%", 0.82, {"avg_ctr": "2.6%", "conversion": "+35%"}), ("Social Proof", "Reviews build trust", 0.91, {"avg_ctr": "3.4%", "conversion": "+51%"})])]
    return {"brand": brand, "patterns": patterns, "summary": {"total_patterns": len(patterns), "avg_confidence": sum(p["confidence"] for p in patterns)/len(patterns)}}

def gen_angles(brand):
    gaps = [{"id": f"g{i}", "angle": a, "score": s, "competition": c, "gap_description": f"Opportunity in {a.lower()} for {brand}", "recommendation": f"Launch {a.lower()} campaign", "potential_roas": r} for i, (a, s, c, r) in enumerate([("Clean Beauty Movement", 8.7, "low", 4.5), ("Personalized Quiz", 7.9, "medium", 3.8), ("Sustainability Story", 8.2, "low", 4.1), ("Men's Market", 6.5, "very low", 5.2), ("TikTok Native Content", 9.1, "high", 3.5), ("Subscription Model", 7.3, "medium", 4.8), ("AR Try-On", 8.5, "low", 3.9), ("Community Building", 7.6, "medium", 4.3)])]
    return {"brand": brand, "gaps": gaps, "summary": {"total_opportunities": len(gaps), "avg_score": sum(g["score"] for g in gaps)/len(gaps)}}

def gen_creatives(brand):
    return [{"no": i+1, "angle": t[0], "hook": f"{t[0]} for {brand}", "headline": t[1], "primary_text": f"Great {t[0].lower()} content", "visual_idea": t[2], "cta": t[3], "platforms": t[4].split(","), "predicted_ctr": round(random.uniform(0.025, 0.055), 3), "complexity": t[5]} for i, t in enumerate([("Free Gift First Order", "Welcome Gift Inside", "Gift box opening", "Claim Free Gift", "facebook,instagram", "low"), ("Gift Card", "Bonus Gift Card", "Gift card reveal", "Shop & Earn", "facebook,instagram", "low"), ("New Launch", "Just Launched", "Product hero shot", "Shop New", "instagram,tiktok", "medium"), ("Catalog Bestsellers", "Top 5 Bestsellers", "Carousel products", "View Bestsellers", "facebook,instagram", "low"), ("Carousel Routine", "Build Your Routine", "Step carousel", "Build Routine", "facebook,instagram", "medium"), ("UGC Review", "5-Star Reviews", "Testimonial video", "Read Reviews", "tiktok,instagram", "low"), ("Quiz Personalization", "Find Formula in 60s", "Quiz preview", "Take Quiz", "facebook,instagram", "high"), ("Shade Match", "Perfect Match Guaranteed", "Shade tool demo", "Find My Shade", "instagram,tiktok", "high"), ("Mini Trial", "Discovery Set $15", "Mini flatlay", "Get Sample Set", "facebook,instagram", "low"), ("Bundle Stack", "Stack & Save", "Bundle graphic", "Build Bundle", "facebook,instagram", "low"), ("Loyalty", "Earn Rewards", "VIP benefits", "Join Free", "facebook,instagram", "low"), ("Flash Gift 24h", "Last Chance Alert", "Countdown timer", "Shop Before Midnight", "instagram,tiktok", "medium"), ("Sensitive Skin", "Dermatologist Tested", "Calm skin before/after", "Shop Sensitive", "facebook,instagram", "medium"), ("Clean Beauty", "Natural Ingredients", "Ingredient spotlight", "Shop Clean", "instagram,tiktok", "medium"), ("Unboxing", "Premium Packaging", "ASMR unboxing", "Experience It", "tiktok,instagram", "medium"), ("Makeup Before/After", "See Difference", "Split-screen", "Get Look", "tiktok,instagram", "low"), ("Seasonal", "Limited Edition", "Seasonal imagery", "Shop Collection", "facebook,instagram", "medium"), ("Cart Retargeting", "Complete Order", "Cart display", "Checkout Now", "facebook,instagram", "low"), ("Social Proof", "Join Movement", "Customer collage", "Join Now", "facebook,tiktok", "low"), ("Routine Comparison", "Upgrade Regimen", "Comparison chart", "Upgrade Now", "facebook,instagram", "medium")])]

@app.get("/")
async def root():
    return {"message": "ZAD System - Content Dashboard API", "version": "2.0.0", "endpoints": ["/dashboard", "/search", "/winners", "/angles", "/creative", "/health"]}

@app.get("/health")
async def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat(), "services": {"api": "running", "data": "mock_mode"}}

@app.get("/dashboard/{brand_name}")
async def dashboard(brand_name: str, country: str = "US"):
    ads = gen_ads(brand_name, 50)
    winners = gen_winners(brand_name)
    angles = gen_angles(brand_name)
    creatives = gen_creatives(brand_name)
    return {"metrics": {"total_ads": len(ads["ads"]), "active_campaigns": 12, "winning_ads": len(winners["patterns"]), "angle_gaps": len(angles["gaps"]), "creative_ideas": len(creatives), "last_updated": datetime.now().isoformat()}, "recent_ads": ads["ads"][:10], "winner_patterns": winners["patterns"], "angle_gaps": angles["gaps"], "top_creatives": creatives[:8], "all_creatives": creatives, "trends": {"top_performing_angles": ["UGC Review", "Before/After", "Social Proof"], "emerging_trends": ["Short-form Video", "Authentic Reviews"], "seasonal_opportunities": ["Holiday Campaigns"]}}

@app.post("/search")
async def search(request: BrandSearch):
    return gen_ads(request.brand_name, request.limit)

@app.get("/winners/{brand_name}")
async def winners(brand_name: str, limit: int = 10):
    w = gen_winners(brand_name)
    return {"brand": brand_name, "patterns": w["patterns"][:limit], "summary": w["summary"]}

@app.get("/angles/{brand_name}")
async def angles(brand_name: str):
    return gen_angles(brand_name)

@app.post("/creative/generate")
async def generate(brief: CreativeBrief):
    c = gen_creatives(brief.brand_name)
    return {"brief": brief.dict(), "creatives": [{**x, "tone": brief.tone} for x in c], "total_generated": len(c)}

@app.get("/creative/templates")
async def templates():
    creatives = gen_creatives("X")
    return {"templates": [{"no": i+1, "angle": c["angle"], "category": "Promotion" if i<5 else "Product" if i<10 else "Engagement"} for i, c in enumerate(creatives)], "total": 20}

@app.get("/report/{brand_name}")
async def report(brand_name: str):
    return {"brand": brand_name, "generated_at": datetime.now().isoformat(), "summary": f"{brand_name} shows strong potential.", "findings": gen_winners(brand_name), "opportunities": gen_angles(brand_name)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
