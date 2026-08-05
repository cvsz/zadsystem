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
    
    def generate_creative_20(
        self,
        brand: str,
        product: str = None,
        target_audience: str = "หญิง 25-40 ปี",
        offer: str = "ลด 10% ออเดอร์แรก + ฟรี mini size",
        competitor_insights: Dict = None
    ) -> List[Dict]:
        """
        สร้าง Creative 20 แบบตาม AGENTS.md specification
        
        Args:
            brand: ชื่อแบรนด์
            product: สินค้าหลัก (ถ้าไม่ระบุจะใช้ชื่อแบรนด์)
            target_audience: กลุ่มเป้าหมาย
            offer: โปรโมชั่น/จุดขาย
            competitor_insights: ข้อมูลจาก competitor analysis
            
        Returns:
            List ของ 20 creative ideas
        """
        if product is None:
            product = f"{brand} Product"
        
        # Angles ครบ 20 แบบตามที่ระบุในเอกสาร
        angles_config = [
            ("free_gift", "Free Gift First Order", "สั่งครั้งแรก ได้ของขวัญทดลอง", "เปิดผิวสวยด้วยของขวัญชิ้นแรก", "Flat lay กล่องของขวัญ + สินค้าไซซ์มินิ", "Shop Now"),
            ("gift_card", "Gift Card", "ให้สวยเลือกเอง", "Gift Card ที่คนรับเลือกได้เอง", "การ์ดของขวัญดิจิทัลพร้อมกล่องสวย", "Send Gift Card"),
            ("new_launch", "New Launch", "ใหม่ล่าสุด", "เปิดตัวสูตรใหม่", "ภาพ macro texture สินค้า + packaging ใหม่", "Discover Now"),
            ("catalog_bestsellers", "Catalog Bestsellers", "ตัวขายดี", "5 ไอเทมที่ลูกค้าเลือกซ้ำ", "Grid สินค้า 5 ตัวพร้อม badge bestseller", "Shop Bestsellers"),
            ("carousel_routine", "Carousel Routine", "เช้า-เย็น", "รูทีนง่ายๆ 3 ขั้นตอน", "Carousel swipe ตามขั้นตอน routine", "Build Your Routine"),
            ("ugc_review", "UGC Review", "ใช้จริง", "รีวิวจากผู้ใช้งานจริง", "วิดีโอสั้นแนว selfie review", "See Reviews"),
            ("quiz_personalization", "Quiz Personalization", "ไม่รู้เริ่มยังไง", "ทำควิซ 30 วิ หาไอเทมที่ใช่", "หน้าจอ quiz พร้อมตัวเลือกง่ายๆ", "Start Quiz"),
            ("shade_match", "Shade Match", "เฉดไม่ตรงผิว", "หาเฉดที่ใช่ใน 1 นาที", "Slider เทียบเฉดสีรองพื้น", "Find Your Shade"),
            ("mini_trial", "Mini Trial", "กลัวไม่เข้าผิว", "ลองไซซ์มินิ ก่อนตัดสินใจ", "ภาพ mini size หลายชิ้น", "Try Mini"),
            ("bundle_stack", "Bundle Stack", "ครบจบในกล่องเดียว", "Bundle Routine ลดขั้นตอน", "กล่อง bundle เปิดเห็นสินค้าครบชุด", "Get Bundle"),
            ("loyalty", "Loyalty", "ยิ่งซื้อ ยิ่งคุ้ม", "สะสมแต้มแลกไซซ์จริง", "การ์ดสมาชิก / แต้มสะสม", "Join Now"),
            ("flash_gift_24h", "Flash Gift 24h", "เฉพาะวันนี้", "ของขวัญ 24 ชั่วโมง", "Countdown timer + gift box", "Claim Offer"),
            ("sensitive_skin", "Sensitive Skin", "ผิวแพ้ง่าย", "สูตรอ่อนโยนสำหรับผิวแพ้ง่าย", "ภาพเนื้อผลิตภัณฑ์ + ingredient highlight", "Learn More"),
            ("clean_beauty", "Clean Beauty", "ไม่มีสารที่กังวล", "คลีนบิวตี้ที่ใช้งานได้จริง", "ภาพ ingredient สะอาดๆ", "Explore Ingredients"),
            ("unboxing", "Unboxing", "เปิดกล่อง", "ประสบการณ์ unboxing ที่อยากแชร์", "วิดีโอ unboxing สั้นๆ", "Shop Now"),
            ("before_after", "Makeup Before/After", "ก่อนแต่ง vs หลังแต่ง", "ลุคธรรมชาติที่ดูเป็นผิว", "Split screen before/after", "Get the Look"),
            ("seasonal", "Seasonal", "อากาศแบบนี้", "ไอเทม must-have ฤดูกาลนี้", "โทนสีตามฤดูกาล + สินค้า", "Shop Season Edit"),
            ("cart_retargeting", "Cart Retargeting", "ลืมของในตะกร้า?", "ไอเทมของคุณยังรออยู่", "ภาพสินค้าใน cart", "Complete Order"),
            ("social_proof", "Social Proof", "คะแนนรีวิว 4.8/5", "ทำไมใครๆ ก็ให้ 4.8", "ดาวรีวิว + quote สั้นๆ", "Read Reviews"),
            ("routine_comparison", "Routine Comparison", "3 ขั้นตอน vs 7 ขั้นตอน", "ลดขั้นตอน แต่ยังครบ", "Infographic เปรียบเทียบ checklist", "Simplify Routine")
        ]
        
        creatives = []
        for i, (angle_code, angle_name, hook, headline, visual, cta) in enumerate(angles_config, 1):
            # สร้าง primary text จาก insight
            primary_text = self._generate_primary_text(
                brand=brand,
                product=product,
                angle=angle_code,
                offer=offer,
                audience=target_audience
            )
            
            creative = {
                "no": i,
                "angle": angle_name,
                "hook": hook,
                "headline": headline,
                "primary_text": primary_text,
                "visual_idea": visual,
                "cta": cta
            }
            creatives.append(creative)
        
        return creatives
    
    def _generate_primary_text(
        self,
        brand: str,
        product: str,
        angle: str,
        offer: str,
        audience: str
    ) -> str:
        """Generate primary text สำหรับแต่ละ angle"""
        templates = {
            "free_gift": f"🎁 พิเศษ! สั่ง {product} ครั้งแรกรับฟรี mini bestseller จำนวนจำกัด\nเหมาะสำหรับ {audience} ที่อยากลองก่อนตัดสินใจ\n\n{offer}",
            "gift_card": "💝 ไม่ต้องเดาไซซ์ เดสเฉด ให้ Gift Card เป็นของขวัญที่เลือกได้จริง\n perfect สำหรับให้คนพิเศษหรือรางวัลให้ตัวเอง",
            "new_launch": f"✨ เปิดตัว {product} สูตรใหม่ล่าสุด!\nสัมผัสนวัตกรรมที่ออกแบบมาเพื่อคุณโดยเฉพาะ\nดูรายละเอียดก่อนใครวันนี้",
            "catalog_bestsellers": "🏆 รวมไอเทมยอดนิยมที่ใช้จริง ซื้อซ้ำจริง\nเหมาะทั้งมือใหม่และสายบิวตี้ตัวจริง",
            "carousel_routine": "📱 Swipe ดูรูทีนง่ายๆ 3 ขั้นตอน\nเช้า-เย็น ครบทุกความต้องการของผิวคุณ",
            "ugc_review": "⭐️⭐️⭐️⭐️⭐️\nรีวิวจริงจากผู้ใช้จริง หลายคนบอกว่าผิวดูเรียบเนียนขึ้นและแต่งหน้าติดง่ายขึ้น",
            "quiz_personalization": "❓ ทำควิซ 30 วินาที หาไอเทมที่ใช่สำหรับผิวคุณ\nรับคำแนะนำ routine ที่เหมาะกับผิวของคุณโดยเฉพาะ",
            "shade_match": "🎨 หาเฉดที่ใช่ใน 1 นาที\nไม่ต้องเดาอีกต่อไป ช่วยคุณเลือกเฉดที่เข้ากับผิวมากขึ้น",
            "mini_trial": "🧴 ลองไซซ์มินิ ก่อนตัดสินใจซื้อไซซ์จริง\nพกง่าย เหมาะกับคนอยากลองหรือเดินทาง",
            "bundle_stack": "📦 Bundle Routine ครบจบในกล่องเดียว\nจับคู่ไอเทมที่ใช้ด้วยกัน ง่ายกว่าและคุ้มกว่า",
            "loyalty": "💎 สมาชิกสะสมแต้มทุกการซื้อ\nใช้แลกส่วนลดหรือไอเทมพิเศษ ได้สิทธิ์ eksklusív",
            "flash_gift_24h": "⚡ เฉพาะวันนี้! สั่งภายใน 24 ชม. รับของขวัญพิเศษเพิ่ม\nจำนวนจำกัด อย่าพลาด!",
            "sensitive_skin": "🌿 สูตรอ่อนโยนสำหรับผิวแพ้ง่าย\nเลือกส่วนผสมอย่างตั้งใจ เหมาะกับผิวที่ต้องการการดูแลเป็นพิเศษ",
            "clean_beauty": "🍃 คลีนบิวตี้ที่ใช้งานได้จริง\nเลือกส่วนผสมอย่างตั้งใจ เหมาะกับคนที่ชอบความเรียบง่าย",
            "unboxing": "📸 ประสบการณ์ unboxing ที่อยากแชร์\nแพ็กเกจสวย น่าถ่ายรูป เหมาะทั้งใช้เองและเป็นของขวัญ",
            "before_after": "✨ เผยผิวให้ดูเรียบเนียนขึ้นด้วยลุคที่แต่งง่าย ไม่หนา\nดูผลลัพธ์ที่ชัดเจน",
            "seasonal": "🌸 ปรับ routine ตามสภาพอากาศ\nช่วยให้ผิวดูพร้อมตลอดวัน ไม่ว่าฤดูไหน",
            "cart_retargeting": "🛒 ไอเทม在你ตะกร้ายังรออยู่!\nกลับมาจบออเดอร์วันนี้ พร้อมสิทธิพิเศษสำหรับคุณ",
            "social_proof": "⭐️⭐️⭐️⭐️⭐️ 4.8/5\nจากรีวิวจริงของลูกค้า หลายคนประทับใจในเนื้อสัมผัสและผลลัพธ์",
            "routine_comparison": "✅ ลดขั้นตอนแต่ยังครบ!\nถ้า routine คุณยาวเกินไป ลองเปลี่ยนเป็น routine ที่ง่ายขึ้น"
        }
        
        return templates.get(angle, f"สัมผัสความแตกต่างของ {product} จาก {brand}\n{offer}")
    
    def generate_multiple_variations(
        self,
        product: str,
        angle: str,
        count: int = 5
    ) -> List[Dict]:
        """Generate multiple creative variations (backward compatible)"""
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
