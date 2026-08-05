"""
Creative Factory
สร้างไอเดียโฆษณาใหม่ๆ จาก AI
"""

from typing import List, Dict, Optional
import random


class CreativeFactory:
    """โรงงานผลิตไอเดียโฆษณา"""
    
    HOOK_TEMPLATES = {
        "question": [
            "รู้ไหมว่า... {benefit}?",
            "เคยสงสัยไหมว่า ทำไม... {problem}?",
            "อะไรคือความลับของ {result}?"
        ],
        "statement": [
            "{product} ใหม่! {benefit} ใน{timeframe}",
            "หยุด{problem} ด้วย{solution}",
            "นี่คือ{product} ที่คุณรอคอย"
        ],
        "urgency": [
            "⚡ ลดราคา{discount}% วันนี้เท่านั้น!",
            "จำนวนจำกัด! เหลือเพียง{quantity} ชิ้น",
            "โปรโมชั่นพิเศษ เฉพาะ{timeframe}นี้"
        ],
        "social_proof": [
            "⭐️⭐️⭐️⭐️⭐️ จากผู้ใช้มากกว่า{users}คน",
            " Bestseller #1 ในหมวด{category}",
            "ดาราและเซเลบแนะนำ!"
        ]
    }
    
    ANGLE_TO_BENEFIT = {
        "brightness_glow": ("ผิวใสออร่า", "เห็นผลใน 7 วัน", "วิตามินซี + ไนอาซินาไมด์"),
        "hydration": ("ผิวชุ่มชื้น 24 ชม.", "ทันทีที่ใช้", "Hyaluronic Acid 5 โมเลกุล"),
        "anti_aging": ("ริ้วรอยดูจางลง", "4 สัปดาห์", "Retinol + Peptides"),
        "acne_care": ("สิวแห้งไว ไม่ทิ้งรอย", "3 วัน", "Salicylic Acid + Tea Tree"),
        "sensitive_skin": ("อ่อนโยนแม้ผิวแพ้ง่าย", "ตั้งแต่ครั้งแรก", "Centella + Allantoin")
    }
    
    CTA_OPTIONS = [
        "🛒 ซื้อเลยที่ {link}",
        "💬 ทักแชทสอบถามเพิ่มเติม",
        "👉 คลิกเพื่อดูรายละเอียด",
        "📞 สั่งซื้อตอนนี้ {phone}",
        "🎁 รับส่วนลดพิเศษ เมื่อสั่งซื้อวันนี้"
    ]
    
    def __init__(self):
        pass
    
    def generate_creative(
        self,
        product: str,
        angle: str,
        platform: str = "facebook",
        tone: str = "friendly",
        language: str = "th"
    ) -> Dict:
        """
        สร้างไอเดียโฆษณา
        
        Args:
            product: ชื่อผลิตภัณฑ์
            angle: มุมการขาย (brightness_glow, hydration, etc.)
            platform: แพลตฟอร์ม (facebook, instagram, tiktok)
            tone: โทนเสียง (friendly, professional, urgent)
            language: ภาษา (th, en)
            
        Returns:
            Creative idea dictionary
        """
        # ดึงข้อมูลจาก angle
        benefit, timeframe, ingredient = self.ANGLE_TO_BENEFIT.get(
            angle, ("ผลลัพธ์ที่ดีขึ้น", "ไม่นาน", "ส่วนผสมคุณภาพ")
        )
        
        # สร้าง hook
        hook = self._generate_hook(product, benefit, angle)
        
        # สร้าง body
        body = self._generate_body(product, benefit, timeframe, ingredient, angle, tone)
        
        # สร้าง CTA
        cta = self._generate_cta(platform)
        
        # แนะนำรูปแบบภาพ/วิดีโอ
        visual_recommendations = self._get_visual_recommendations(angle, platform)
        
        # Hashtags
        hashtags = self._generate_hashtags(product, angle, platform)
        
        return {
            "product": product,
            "angle": angle,
            "platform": platform,
            "hook": hook,
            "body": body,
            "cta": cta,
            "visual_recommendations": visual_recommendations,
            "hashtags": hashtags,
            "full_ad_copy": f"{hook}\n\n{body}\n\n{cta}\n\n{hashtags}"
        }
    
    def _generate_hook(self, product: str, benefit: str, angle: str) -> str:
        """Generate hook line"""
        templates = self.HOOK_TEMPLATES["statement"]
        template = random.choice(templates)
        
        return template.format(
            product=product,
            benefit=benefit,
            result=benefit,
            problem="ผิวไม่ใส",
            solution=product,
            discount="30",
            quantity="50",
            timeframe="7 วัน",
            users="10,000",
            category="เซรั่ม"
        )
    
    def _generate_body(
        self, 
        product: str, 
        benefit: str, 
        timeframe: str, 
        ingredient: str,
        angle: str,
        tone: str
    ) -> str:
        """Generate body copy"""
        if tone == "friendly":
            body = f"""✨ {product} ตัวช่วยใหม่ที่จะทำให้คุณ{benefit}!

🔬 พิเศษด้วย{ingredient}
⏰ เห็นผลจริงภายใน{timeframe}

✅ ผ่านการทดสอบทางคลินิก
✅ ปลอดภัย แม้ผิวแพ้ง่าย
✅ ผลลัพธ์ที่พิสูจน์แล้ว"""
        elif tone == "professional":
            body = f"""{product} นวัตกรรมใหม่ล่าสุด

ส่วนประกอบสำคัญ: {ingredient}
ผลลัพธ์ที่คาดหวัง: {benefit}
ระยะเวลาในการเห็นผล: {timeframe}

ผ่านการรับรองความปลอดภัย"""
        else:  # urgent
            body = f"""🔥 ด่วน! {product} ลดราคาพิเศษ

⚡ {benefit} ใน{timeframe}
⚡ ส่วนผสม:{ingredient}
⚡ จำนวนจำกัด!

อย่าพลาดโอกาสดีๆ แบบนี้"""
        
        return body
    
    def _generate_cta(self, platform: str) -> str:
        """Generate Call-to-Action"""
        cta = random.choice(self.CTA_OPTIONS)
        return cta.format(
            link="sephora.co.th",
            phone="02-XXX-XXXX"
        )
    
    def _get_visual_recommendations(self, angle: str, platform: str) -> List[str]:
        """แนะนำรูปแบบภาพ/วิดีโอ"""
        recommendations = {
            "brightness_glow": [
                "Before/After ผิวใส",
                "Video: ทาเซรั่มแล้วผิว glow ทันที",
                "Flatlay: ผลิตภัณฑ์ + ส่วนผสมวิตามินซี"
            ],
            "hydration": [
                "Video: น้ำซึมเข้าสู่ผิว",
                "Close-up: ผิวชุ่มชื้น มีน้ำมีนวล",
                "Infographic: 5 โมเลกุล Hyaluronic Acid"
            ],
            "anti_aging": [
                "Before/After: ริ้วรอยจางลง",
                "Timeline: 4 สัปดาห์ของการใช้",
                "Scientific diagram: กลไกการทำงานของ Retinol"
            ]
        }
        
        base_recs = recommendations.get(angle, [
            "Product shot สวยๆ",
            "Lifestyle: คนใช้ผลิตภัณฑ์",
            "User testimonial"
        ])
        
        # ปรับตาม platform
        if platform == "tiktok":
            base_recs.append("Vertical video 9:16 สำหรับ TikTok")
        elif platform == "instagram":
            base_recs.append("Square 1:1 หรือ Story 9:16")
        
        return base_recs
    
    def _generate_hashtags(self, product: str, angle: str, platform: str) -> str:
        """Generate hashtags"""
        base_tags = ["#skincare", "#beauty", "#skincareroutine"]
        
        angle_tags = {
            "brightness_glow": ["#ผิวใส", "#glowingskin", "#vitaminc"],
            "hydration": ["#ผิวชุ่มชื้น", "#hydratedskin", "#hyaluronicacid"],
            "anti_aging": ["#ต้านวัย", "#antiaging", "#retinol"]
        }
        
        tags = base_tags + angle_tags.get(angle, [])
        
        if platform == "tiktok":
            tags.extend(["#tiktokbeauty", "#beautytok"])
        elif platform == "instagram":
            tags.extend(["#instabeauty", "#skincarelover"])
        
        return " ".join(tags)
    
    def generate_multiple_variations(
        self,
        product: str,
        angle: str,
        count: int = 5
    ) -> List[Dict]:
        """Generate multiple creative variations"""
        variations = []
        tones = ["friendly", "professional", "urgent"]
        
        for i in range(count):
            tone = tones[i % len(tones)]
            creative = self.generate_creative(
                product=product,
                angle=angle,
                tone=tone
            )
            creative["variation_id"] = i + 1
            variations.append(creative)
        
        return variations
