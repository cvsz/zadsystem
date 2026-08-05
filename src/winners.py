"""
Winning Ad Analyzer
วิเคราะห์โฆษณาที่ชนะ หา pattern ที่ประสบความสำเร็จ
"""

from typing import List, Dict
from collections import Counter


class WinningAdAnalyzer:
    """วิเคราะห์ Winning Ads และหา pattern"""
    
    def __init__(self):
        pass
    
    def analyze_winners(self, ads: List[Dict], criteria: str = "engagement") -> Dict:
        """
        วิเคราะห์โฆษณาที่ชนะตามเกณฑ์ที่กำหนด
        
        Args:
            ads: List ของโฆษณา
            criteria: เกณฑ์การวัด (engagement, longevity, frequency)
            
        Returns:
            Analysis results
        """
        if not ads:
            return {"message": "No ads to analyze"}
        
        # ในระบบจริง จะใช้ข้อมูล engagement จาก API
        # ที่นี่ใช้ heuristic ง่ายๆ
        
        winning_patterns = {
            "hooks": [],
            "angles": [],
            "formats": [],
            "ctas": []
        }
        
        for ad in ads:
            body = ad.get("ad_creative_body", "")
            caption = ad.get("ad_creative_link_caption", "")
            
            # ตรวจจับ hook patterns
            if any(word in body for word in ["ใหม่", "New", "เปิดตัว"]):
                winning_patterns["hooks"].append("new_product_launch")
            if any(word in body for word in ["ลด", "%", "Sale", "Promotion"]):
                winning_patterns["hooks"].append("discount_offer")
            if any(word in body for word in ["✨", "🔥", "💥"]):
                winning_patterns["hooks"].append("emoji_attention")
            if any(word in body for word in ["จำกัด", "Limited", "Only"]):
                winning_patterns["hooks"].append("urgency_scarcity")
            
            # ตรวจจับ angles
            if any(word in body for word in ["ใส", "bright", "glow"]):
                winning_patterns["angles"].append("brightness_glow")
            if any(word in body for word in ["ชุ่มชื้น", "hydrat", "น้ำ"]):
                winning_patterns["angles"].append("hydration")
            if any(word in body for word in ["ริ้วรอย", "anti-age", "วัย"]):
                winning_patterns["angles"].append("anti_aging")
            if any(word in body for word in ["ธรรมชาติ", "natural", "ออร์แกนิค"]):
                winning_patterns["angles"].append("natural_organic")
            
            # ตรวจจับ CTA
            if any(word in body.lower() for word in ["ซื้อเลย", "shop now", "order"]):
                winning_patterns["ctas"].append("direct_purchase")
            if any(word in body.lower() for word in ["คลิก", "click", "learn more"]):
                winning_patterns["ctas"].append("click_through")
            if any(word in body.lower() for word in ["ทักแชท", "inbox", "message"]):
                winning_patterns["ctas"].append("message_conversation")
        
        # นับความถี่
        pattern_summary = {
            key: dict(Counter(value).most_common(5))
            for key, value in winning_patterns.items()
        }
        
        return {
            "total_ads_analyzed": len(ads),
            "winning_patterns": pattern_summary,
            "top_hook": Counter(winning_patterns["hooks"]).most_common(1)[0] if winning_patterns["hooks"] else None,
            "top_angle": Counter(winning_patterns["angles"]).most_common(1)[0] if winning_patterns["angles"] else None,
            "top_cta": Counter(winning_patterns["ctas"]).most_common(1)[0] if winning_patterns["ctas"] else None,
            "recommendations": self._generate_recommendations(pattern_summary)
        }
    
    def _generate_recommendations(self, patterns: Dict) -> List[str]:
        """สร้างคำแนะนำจาก pattern ที่พบ"""
        recommendations = []
        
        if patterns.get("hooks"):
            top_hook = max(patterns["hooks"].items(), key=lambda x: x[1], default=(None, 0))
            if top_hook[0]:
                recommendations.append(f"ใช้ hook แบบ '{top_hook[0]}' เพราะพบมากที่สุดในโฆษณาที่ชนะ")
        
        if patterns.get("angles"):
            top_angle = max(patterns["angles"].items(), key=lambda x: x[1], default=(None, 0))
            if top_angle[0]:
                recommendations.append(f"เน้น angle '{top_angle[0]}' เป็นหลักในการสื่อสาร")
        
        if patterns.get("ctas"):
            top_cta = max(patterns["ctas"].items(), key=lambda x: x[1], default=(None, 0))
            if top_cta[0]:
                recommendations.append(f"ใช้ CTA แบบ '{top_cta[0]}' เพื่อเพิ่ม conversion")
        
        return recommendations if recommendations else ["ยังไม่มีข้อมูลเพียงพอสำหรับคำแนะนำ"]
