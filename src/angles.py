"""
Angle Gap Finder
หาช่องว่างทางการสื่อสารที่คู่แข่งยังไม่ได้ใช้
"""

from typing import List, Dict, Set
from collections import Counter


class AngleGapFinder:
    """หา Angle Gaps ที่คู่แข่งยังไม่ได้เล่น"""
    
    # Angles มาตรฐานในอุตสาหกรรมความงาม
    ALL_POSSIBLE_ANGLES = {
        "brightness_glow": "ผิวใส ออร่า",
        "hydration": "ชุ่มชื้น เติมน้ำ",
        "anti_aging": "ต้านริ้วรอย วัย",
        "acne_care": "รักษาสิว ควบคุมมัน",
        "sensitive_skin": "ผิวแพ้ง่าย อ่อนโยน",
        "natural_organic": "ธรรมชาติ ออร์แกนิค",
        "luxury_premium": "หรูหรา พรีเมียม",
        "affordable_value": "คุ้มค่า ราคาประหยัด",
        "scientific_clinical": "วิทยาศาสตร์ ทดลองทางคลินิก",
        "korean_beauty": "เกาหลี K-Beauty",
        "vegan_cruelty_free": "วีแกน ไม่ทดลองสัตว์",
        "eco_sustainable": "เป็นมิตรต่อสิ่งแวดล้อม",
        "quick_results": "เห็นผลเร็ว ทันใจ",
        "long_lasting": "ติดทน ตลอดวัน",
        "multi_function": "หลายฟังก์ชัน ครบในชิ้นเดียว",
        "gift_worthy": "เหมาะเป็นของขวัญ",
        "limited_edition": "Limited Edition พิเศษ",
        "celebrity_endorsed": "ดารา เซเลบใช้",
        "dermatologist_recommended": "แพทย์ผิวหนังแนะนำ",
        "award_winning": "ได้รับรางวัล"
    }
    
    def __init__(self):
        pass
    
    def find_gaps(
        self, 
        brand_ads: List[Dict], 
        competitor_ads: List[Dict],
        brand_name: str = "แบรนด์ของคุณ"
    ) -> Dict:
        """
        หา angle gaps ระหว่างแบรนด์กับคู่แข่ง
        
        Args:
            brand_ads: โฆษณาของแบรนด์เรา
            competitor_ads: โฆษณาของคู่แข่ง (รวมทั้งหมด)
            brand_name: ชื่อแบรนด์
            
        Returns:
            Gap analysis results
        """
        # วิเคราะห์ angles ที่ใช้แล้ว
        brand_angles = self._extract_angles(brand_ads)
        competitor_angles = self._extract_angles(competitor_ads)
        
        # หา gaps
        all_angles = set(self.ALL_POSSIBLE_ANGLES.keys())
        
        # Angles ที่คู่แข่งใช้แล้ว แต่เรายังไม่ได้ใช้ (โอกาสที่เราควรเล่น)
        competitor_only = competitor_angles - brand_angles
        
        # Angles ที่เราใช้แล้ว แต่คู่แข่งยังไม่ใช้ (จุดแข็งของเรา)
        brand_only = brand_angles - competitor_angles
        
        # Angles ที่ยังไม่มีใครใช้ (Blue Ocean)
        unused_angles = all_angles - brand_angles - competitor_angles
        
        # Angles ที่ทุกคนใช้ (Red Ocean - อาจต้องหลีกเลี่ยงหรือหาวิธีใหม่)
        common_angles = brand_angles & competitor_angles
        
        return {
            "brand_name": brand_name,
            "angles_used_by_brand": list(brand_angles),
            "angles_used_by_competitors": list(competitor_angles),
            "gaps_opportunities": {
                "angles_competitors_use_but_we_dont": list(competitor_only),
                "angles_we_use_but_competitors_dont": list(brand_only),
                "blue_ocean_unused": list(unused_angles),
                "red_ocean_overcrowded": list(common_angles)
            },
            "recommendations": self._generate_gap_recommendations(
                competitor_only, brand_only, unused_angles, common_angles
            ),
            "angle_descriptions": {
                angle: self.ALL_POSSIBLE_ANGLES.get(angle, angle)
                for angle in competitor_only | brand_only | unused_angles
            }
        }
    
    def _extract_angles(self, ads: List[Dict]) -> Set[str]:
        """Extract angles จากโฆษณา"""
        angles = set()
        
        angle_keywords = {
            "brightness_glow": ["ใส", "ออร่า", "bright", "glow", "radiant", "✨"],
            "hydration": ["ชุ่มชื้น", "น้ำ", "hydrat", "moisture", "เติมน้ำ"],
            "anti_aging": ["ริ้วรอย", "วัย", "anti-age", "wrinkle", "young"],
            "acne_care": ["สิว", "acne", "มัน", "oil-control", "รูขุมขน"],
            "sensitive_skin": ["แพ้", "sensitive", "อ่อนโยน", "gentle", "ระคายเคือง"],
            "natural_organic": ["ธรรมชาติ", "natural", "ออร์แกนิค", "organic", "plant"],
            "luxury_premium": ["หรู", "luxury", "premium", "exclusive", "high-end"],
            "affordable_value": ["คุ้ม", "value", "ประหยัด", "affordable", "budget"],
            "scientific_clinical": ["วิทย์", "science", "clinic", "research", "ทดลอง"],
            "korean_beauty": ["เกาหลี", "korean", "k-beauty", "seoul"],
            "vegan_cruelty_free": ["วีแกน", "vegan", "cruelty-free", "ไม่ทดลองสัตว์"],
            "eco_sustainable": ["eco", "sustain", "สิ่งแวดล้อม", "green", "recycle"],
            "quick_results": ["เร็ว", "quick", "ทันที", "instant", "7 วัน"],
            "long_lasting": ["ทน", "lasting", "24 ชม.", "all-day", "ตลอดวัน"],
            "multi_function": ["ครบ", "multi", "all-in-one", "3in1", "หลายอย่าง"],
            "gift_worthy": ["ของขวัญ", "gift", "set", "present", "ให้"],
            "limited_edition": ["limited", "พิเศษ", "exclusive", "จำนวนจำกัด"],
            "celebrity_endorsed": ["ดารา", "celebrity", "influencer", "เซเลบ"],
            "dermatologist_recommended": ["แพทย์", "derma", "หมอ", "recommended"],
            "award_winning": ["รางวัล", "award", "best", "winner", "#1"]
        }
        
        for ad in ads:
            text = ad.get("ad_creative_body", "") + " " + ad.get("ad_creative_link_caption", "")
            text_lower = text.lower()
            
            for angle, keywords in angle_keywords.items():
                if any(kw.lower() in text_lower or kw in text for kw in keywords):
                    angles.add(angle)
        
        return angles
    
    def _generate_gap_recommendations(
        self,
        competitor_only: Set[str],
        brand_only: Set[str],
        unused_angles: Set[str],
        common_angles: Set[str]
    ) -> List[str]:
        """สร้างคำแนะนำจาก gap analysis"""
        recommendations = []
        
        if competitor_only:
            top_gap = list(competitor_only)[:3]
            descriptions = [self.ALL_POSSIBLE_ANGLES.get(a, a) for a in top_gap]
            recommendations.append(
                f"🎯 พิจารณาเล่น angle ที่คู่แข่งใช้สำเร็จ แต่ยังไม่มีในแบรนด์เรา: {', '.join(descriptions)}"
            )
        
        if brand_only:
            strengths = [self.ALL_POSSIBLE_ANGLES.get(a, a) for a in list(brand_only)[:3]]
            recommendations.append(
                f"💪 จุดแข็งที่คู่แข่งยังไม่ได้ใช้: {', '.join(strengths)} - ควรเน้นให้มากขึ้น"
            )
        
        if unused_angles:
            blue_oceans = [self.ALL_POSSIBLE_ANGLES.get(a, a) for a in list(unused_angles)[:3]]
            recommendations.append(
                f"🌊 Blue Ocean ที่ยังไม่มีใครเล่น: {', '.join(blue_oceans)} - โอกาสสร้าง differentiation"
            )
        
        if common_angles:
            crowded = [self.ALL_POSSIBLE_ANGLES.get(a, a) for a in list(common_angles)[:2]]
            recommendations.append(
                f"⚠️ Angle ที่มีคนใช้เยอะ (Red Ocean): {', '.join(crowded)} - หาวิธีนำเสนอให้แตกต่าง"
            )
        
        return recommendations if recommendations else ["วิเคราะห์ข้อมูลเพิ่มเติมเพื่อคำแนะนำที่เฉพาะเจาะจง"]
