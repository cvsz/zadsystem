"""
Ad Library Spy Skill
สืบโฆษณาของคู่แข่ง วิเคราะห์กลยุทธ์
"""

from typing import List, Dict
from .meta_library import MetaLibraryClient, get_mock_ads


class AdSpy:
    """Skill สำหรับ spy โฆษณาของคู่แข่ง"""
    
    def __init__(self):
        self.client = MetaLibraryClient()
    
    def spy_brand(self, brand: str, country: str = "TH", use_mock: bool = True) -> Dict:
        """
        Spy โฆษณาของแบรนด์ที่ระบุ
        
        Args:
            brand: ชื่อแบรนด์ที่ต้องการ spy
            country: รหัสประเทศ
            use_mock: ใช้ mock data หากไม่มี API token
            
        Returns:
            Dictionary containing ads and analysis
        """
        # พยายามดึงข้อมูลจริงก่อน
        ads = self.client.search_ads(query=brand, country=country)
        
        # หากไม่มีข้อมูล (อาจเพราะไม่มี API token) ใช้ mock data
        if not ads and use_mock:
            print(f"📋 Using mock data for '{brand}'")
            ads = get_mock_ads(brand)
        
        # วิเคราะห์เบื้องต้น
        analysis = self._quick_analysis(ads, brand)
        
        return {
            "brand": brand,
            "country": country,
            "total_ads": len(ads),
            "ads": ads,
            "analysis": analysis
        }
    
    def _quick_analysis(self, ads: List[Dict], brand: str) -> Dict:
        """วิเคราะห์เบื้องต้นของโฆษณา"""
        if not ads:
            return {"message": "No ads to analyze"}
        
        # นับความถี่ของคีย์เวิร์ด
        keywords = {}
        angles = []
        
        for ad in ads:
            body = ad.get("ad_creative_body", "")
            
            # ตรวจจับ angle จาก emoji และคีย์เวิร์ด
            if "✨" in body or "ใส" in body or "bright" in body.lower():
                angles.append("brightness")
            if "💄" in body or "ลิป" in body:
                angles.append("lipstick")
            if "🎁" in body or "gift" in body.lower() or "set" in body.lower():
                angles.append("promotion")
            if "ลด" in body or "%" in body:
                angles.append("discount")
            if "ใหม่" in body or "new" in body.lower():
                angles.append("new_product")
        
        # นับ angle ที่พบบ่อย
        from collections import Counter
        angle_counts = Counter(angles)
        
        return {
            "top_angles": dict(angle_counts.most_common(5)),
            "avg_ad_length": sum(len(ad.get("ad_creative_body", "")) for ad in ads) / len(ads),
            "unique_messages": len(set(ad.get("ad_creative_body", "") for ad in ads))
        }
    
    def compare_brands(self, brands: List[str]) -> Dict:
        """
        เปรียบเทียบโฆษณาระหว่างหลายแบรนด์
        
        Args:
            brands: List ของชื่อแบรนด์
            
        Returns:
            Comparison results
        """
        results = {}
        for brand in brands:
            print(f"\n🔍 Spying {brand}...")
            results[brand] = self.spy_brand(brand)
        
        # สรุป comparison
        comparison = {
            "brands_compared": brands,
            "total_ads_per_brand": {b: results[b]["total_ads"] for b in brands},
            "top_angles_per_brand": {b: results[b]["analysis"].get("top_angles", {}) for b in brands}
        }
        
        return comparison
