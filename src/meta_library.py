"""
Meta Ad Library API Client
ดึงข้อมูลโฆษณาจาก Meta Ad Library
"""

import requests
from typing import Dict, List, Optional
import yaml
import os


class MetaLibraryClient:
    """Client สำหรับดึงข้อมูลจาก Meta Ad Library API"""
    
    def __init__(self, config_path: str = "config.yaml"):
        """Initialize with configuration"""
        self.config = self._load_config(config_path)
        self.access_token = self.config.get("meta", {}).get("access_token", "")
        self.base_url = self.config.get("meta", {}).get("base_url", "https://graph.facebook.com/v18.0")
        
    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from YAML file"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            return {}
    
    def search_ads(
        self, 
        query: str, 
        country: str = "TH",
        limit: int = 50,
        fields: str = "ad_creative_body,ad_creative_link_caption,page_name,page_id"
    ) -> List[Dict]:
        """
        ค้นหาโฆษณาจาก Meta Ad Library
        
        Args:
            query: คำค้นหา (ชื่อแบรนด์, คีย์เวิร์ด)
            country: รหัสประเทศ (TH, US, etc.)
            limit: จำนวนผลลัพธ์สูงสุด
            fields: Fields ที่ต้องการดึง
            
        Returns:
            List ของโฆษณาที่พบ
        """
        if not self.access_token:
            print("⚠️  Warning: Meta access token not configured")
            return []
        
        url = f"{self.base_url}/ads_archive"
        params = {
            "access_token": self.access_token,
            "search_terms": query,
            "ad_reached_countries": country,
            "limit": min(limit, 100),  # API max limit
            "fields": fields
        }
        
        try:
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            ads = data.get("data", [])
            print(f"✅ พบ {len(ads)} โฆษณาสำหรับ '{query}'")
            return ads
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching ads: {e}")
            return []
    
    def get_page_ads(self, page_id: str, limit: int = 50) -> List[Dict]:
        """
        ดึงโฆษณาทั้งหมดจาก Page ที่ระบุ
        
        Args:
            page_id: Facebook Page ID
            limit: จำนวนผลลัพธ์สูงสุด
            
        Returns:
            List ของโฆษณาจาก Page นั้น
        """
        return self.search_ads(query=page_id, limit=limit)
    
    def analyze_competitors(
        self, 
        brands: List[str], 
        country: str = "TH"
    ) -> Dict[str, List[Dict]]:
        """
        วิเคราะห์โฆษณาของคู่แข่งหลายแบรนด์
        
        Args:
            brands: List ของชื่อแบรนด์
            country: รหัสประเทศ
            
        Returns:
            Dictionary {brand_name: [ads]}
        """
        results = {}
        for brand in brands:
            print(f"\n🔍 กำลังวิเคราะห์ {brand}...")
            ads = self.search_ads(query=brand, country=country)
            results[brand] = ads
        return results


# Mock data สำหรับทดสอบ (เมื่อไม่มี API token)
def get_mock_ads(brand: str = "sephora") -> List[Dict]:
    """Return mock ad data for testing"""
    return [
        {
            "ad_creative_body": "เซรั่มวิตามินซี ใหม่! ผิวใสออร่าใน 7 วัน ✨ ลดราคา 30% วันนี้เท่านั้น",
            "ad_creative_link_caption": "Vitamin C Brightening Serum - Sephora Thailand",
            "page_name": "Sephora Thailand",
            "page_id": "123456789",
            "ad_snapshot_url": "https://www.facebook.com/ads/library/?id=123456789"
        },
        {
            "ad_creative_body": "💄 ลิปสติกเนื้อแมท ติดทน 24 ชม. ไม่หลุดไม่ลอก มีทั้งหมด 20 เฉดสี",
            "ad_creative_link_caption": "Matte Lipstick Collection - Sephora",
            "page_name": "Sephora Thailand",
            "page_id": "123456789",
            "ad_snapshot_url": "https://www.facebook.com/ads/library/?id=987654321"
        },
        {
            "ad_creative_body": "🎁 Set เครื่องสำอางครบครัน เหมาะสำหรับเป็นของขวัญ ราคาพิเศษ 990.- เท่านั้น",
            "ad_creative_link_caption": "Gift Set Promotion - Sephora TH",
            "page_name": "Sephora Thailand",
            "page_id": "123456789",
            "ad_snapshot_url": "https://www.facebook.com/ads/library/?id=456789123"
        }
    ]
