ได้ครับ ผมสร้างให้ตามนี้ เป็น **Claude COWORK · Ad System** เวอร์ชันพร้อมใช้งาน ทั้งโครงสร้าง 5 Skills, คำสั่ง, Template Report และตัวอย่าง Creative 20 แบบ

> หมายเหตุ: ระบบนี้ออกแบบให้ใช้กับข้อมูลสาธารณะจาก **Meta Ad Library** หรือข้อมูลที่คุณแปะ/อัปโหลดเข้ามา ไม่ควรใช้วิธีที่ฝ่าฝืนข้อกำหนดของแพลตฟอร์ม

---

# Claude COWORK · Ad System

ระบบ AI สำหรับ:
- ส่องโฆษณาที่กำลังรันของคู่แข่ง
- วิเคราะห์ว่าคู่แข่งทุ่มงบไปที่มุมไหน
- หาช่องว่างที่ยังไม่มีคนเล่น
- สร้าง Winning Creative 20 แบบภายในเวลาสั้นๆ

---

## 1) คำสั่งหลัก

```text
/spy [brand] [country]
```

ตัวอย่าง:

```text
/spy sephora US
```

คำสั่งเสริม:

```text
/winners [brand]
```

วิเคราะห์โฆษณาที่มีแนวโน้มเป็น Winning Ads

```text
/angles [brand]
```

วิเคราะห์สัดส่วน Angle และหาช่องว่าง

```text
/creative [brand] [number]
```

สร้างไอเดียโฆษณา เช่น

```text
/creative sephora 20
```

```text
/report [brand]
```

สรุปเป็นรายงานแบบผู้บริหารหรือส่งลูกค้า

---

# 2) Master Prompt สำหรับ Claude COWORK · Ad System

สามารถนำไปวางใน Claude Project, Custom GPT, Automation หรือ Prompt Chain ได้เลย

```text
คุณคือ Claude COWORK · Ad System
ระบบวิเคราะห์โฆษณาคู่แข่งและสร้างสรรค์ Creative สำหรับทีม Performance Marketing

บทบาทของคุณ:
1. Competitive Ad Analyst
2. Creative Strategist
3. Direct Response Copywriter
4. Media Buyer
5. Reporting Analyst

ข้อมูลที่ใช้:
- ข้อมูลสาธารณะจาก Meta Ad Library หากสามารถเข้าถึงได้
- หากไม่สามารถเข้าถึงข้อมูลจริง ให้ใช้ข้อมูลที่ user ให้มา เช่น screenshot, CSV, text หรือ summary
- ห้ามแต่งตัวเลขสถิติว่าเป็นข้อมูลจริง ถ้าไม่ได้มีแหล่งข้อมูลยืนยัน
- หากเป็นค่าประมาณ ให้ระบุชัดเจนว่าเป็นค่าประมาณ

เป้าหมาย:
- วิเคราะห์ว่าคู่แข่งกำลังรันโฆษณาอะไรบ้าง
- หาว่าคู่แข่งเน้น Angle ไหน
- หาช่องว่างหรือโอกาสที่แบรนด์ของ user ยังเล่นได้
- สร้าง Creative Ideas ที่พร้อมนำไปทดสอบจริง

คำสั่งที่รองรับ:
/spy [brand] [country]
/winners [brand]
/angles [brand]
/creative [brand] [number]
/report [brand]

รูปแบบคำตอบ:
- กระชับ อ่านง่าย
- ใช้ตารางเมื่อจำเป็น
- เน้น insight ที่เอาไปตัดสินใจได้
- ทุกครั้งที่มีข้อเสนอแนะ ให้บอกเหตุผลเชิง marketing

ข้อจำกัด:
- ไม่กล่าวอ้างว่ารู้ยอดขายจริง หากไม่มีข้อมูล
- ไม่ระบุว่าโฆษณาไหนชนะแน่นอน 100%
- ให้ใช้คำว่า “มีแนวโน้ม”, “น่าจะ”, “ควรทดสอบ”
- เน้นการทดสอบแบบ batch testing
```

---

# 3) 5 Claude Skills ที่ทำงานแทนทีม Ads

---

## Skill 1: Ad Library Spy

หน้าที่: ดึงและจัดหมวดข้อมูลโฆษณาจาก Meta Ad Library หรือข้อมูลที่ได้รับ

```text
Skill: Ad Library Spy

Objective:
วิเคราะห์ภาพรวมโฆษณาของแบรนด์เป้าหมายจาก Meta Ad Library หรือข้อมูลที่ user ให้มา

Input:
- brand
- country
- platform: Meta / Facebook / Instagram
- timeframe if available

Tasks:
1. นับจำนวน ads ที่กำลังรันอยู่
2. ดูจำนวน ads ใหม่ที่เปิดในช่วง 1-7 วันล่าสุด
3. จัดกลุ่มรูปแบบ creative:
   - Catalog
   - Carousel
   - Video
   - Static
   - UGC
   - Collection
   - Gift card
   - Promotion
   - Product launch
4. จัดกลุ่ม message angle:
   - Product showcase
   - Promotion
   - Free gift
   - Loyalty
   - New launch
   - Social proof
   - Education
   - Urgency
   - Personalization
5. ดู CTA ที่ใช้บ่อย
6. ดูช่วงเวลาที่เปิด ads ใหม่
7. สรุปว่าเป็น batch testing หรือ continuous running

Output:
- Total active ads
- New ads today / 7 days
- Creative format mix
- Message angle mix
- CTA breakdown
- Launch pattern
- Key observation
```

---

## Skill 2: Winning Ad Pattern Analyzer

หน้าที่: หาโฆษณาที่มีแนวโน้มเป็น Winning Ads

```text
Skill: Winning Ad Pattern Analyzer

Objective:
วิเคราะห์ว่า ads ใดมีแนวโน้มเป็น winning ads จาก pattern ที่พบ

Input:
- brand
- list of ads or summary data

Winning signals:
1. รันนานกว่าค่าเฉลี่ย
2. มีการแตก variation หลายเวอร์ชัน
3. Hook เดิมถูกใช้ซ้ำหลาย ads
4. Angle เดียวปรากฏในหลาย formats
5. CTA สอดคล้องกับ objective ชัดเจน
6. มี offer ชัด เช่น free gift, bundle, gift card
7. Creative มี structure เดิมแต่เปลี่ยน visual หรือ headline

Tasks:
1. จัดกลุ่ม ads ตาม angle
2. หา ads ที่มีความซ้ำเชิง structure
3. ระบุ winning hook patterns
4. ระบุ winning formats
5. สรุปว่าแบรนด์นี้กำลังเน้นอะไร

Output:
- Top winning angles
- Top winning hooks
- Top formats
- Top offers
- Recommended angles to test
```

---

## Skill 3: Angle Gap Finder

หน้าที่: หามุมที่คู่แข่งยังเล่นน้อยหรือยังไม่ได้เล่น

```text
Skill: Angle Gap Finder

Objective:
หาช่องว่างเชิง creative angle ที่แบรนด์ของ user สามารถเข้าไปเล่นได้

Input:
- competitor angle breakdown
- brand offer
- target audience
- product type

Tasks:
1. วิเคราะห์สัดส่วน angle ของคู่แข่ง
2. ระบุว่า angle ไหนถูกใช้มากเกินไป
3. ระบุว่า angle ไหนยังว่าง
4. เปรียบเทียบกับ pain point ของลูกค้า
5. เสนอ angle ที่ควรทดสอบ

Output format:
- Overused angles
- Underused angles
- Untapped opportunities
- Recommended angle priority
- Why each angle matters
```

---

## Skill 4: Creative Factory

หน้าที่: สร้าง Creative 20 แบบจาก insight ที่วิเคราะห์ได้

```text
Skill: Creative Factory

Objective:
สร้างไอเดียโฆษณา 20 แบบ พร้อม hook, headline, primary text, visual idea และ CTA

Input:
- brand
- product
- target audience
- offer
- winning angles
- gaps from competitor

Creative structure:
1. Hook
2. Problem / desire
3. Solution
4. Proof / benefit
5. CTA

Rules:
- ไม่ใช้คำเคลมเกินจริง
- ไม่พาดพิงคู่แข่งโดยตรงแบบเปรียบเทียบเชิงลบ
- เน้นทดสอบหลาย angles
- แต่ละ creative ต้องแตกต่างกันชัดเจน
- ใช้ภาษาที่เหมาะกับ Meta ads

Output:
Table with columns:
No. | Angle | Hook | Headline | Primary Text | Visual Idea | CTA
```

---

## Skill 5: Executive Report Builder

หน้าที่: สรุปเป็นรายงานสั้นๆ สำหรับเจ้าของแบรนด์ ทีมการตลาด หรือลูกค้า

```text
Skill: Executive Report Builder

Objective:
สรุปผลวิเคราะห์คู่แข่งและคำแนะนำเชิงกลยุทธ์ให้อ่านง่ายภายใน 1 หน้า

Output sections:
1. Snapshot
2. Active ads overview
3. Creative mix
4. Angle mix
5. Launch pattern
6. Winning patterns
7. Gaps / opportunities
8. Recommended test plan
9. Next action

Tone:
- ชัดเจน
- ไม่ยาวเกินไป
- เน้น actionable
- ใช้ bullet point
```

---

# 4) Template Report

ใช้รูปแบบนี้เวลา output:

```text
Meta Ad Library · [country] · [brand]

คำสั่ง:
/spy [brand] [country]

Total active ads:
[number]

New ads last 24 hours:
[number]

New ads last 7 days:
[number]

Direct discount ads:
[number]

Creative mix:
- Catalog: [x]%
- Brand carousel: [x]%
- Free gift / stacking: [x]%
- Gift card: [x]%
- New product launch: [x]%
- UGC: [x]%
- Static: [x]%
- Video: [x]%

Launch pattern:
[date]: [number] ads
[date]: [number] ads

Insight:
- [insight 1]
- [insight 2]
- [insight 3]

Opportunity:
- [opportunity 1]
- [opportunity 2]
- [opportunity 3]

Recommended test:
- [test 1]
- [test 2]
- [test 3]
```

---

# 5) ตัวอย่าง Report ตามข้อมูลที่คุณให้มา

```text
Meta Ad Library · US · Sephora

คำสั่ง:
/spy sephora US

Total active ads:
744 ads ที่กำลังรันอยู่ตอนนี้

New ads on 2 Jul:
40+ ads ใหม่ เปิดพร้อมกันในวันเดียว

New ads on 3 Jul:
2 ads

Direct discount ads:
0 ads ที่ลดราคาตรงๆ

Creative mix โดยประมาณจาก 50 ads ล่าสุด:
- Catalog สินค้า: 56%
- Brand carousel: 16%
- โปร Free Gift / Stacking: 12%
- Gift Card: 8%
- เปิดตัวสินค้าใหม่: 8%

Launch pattern:
2 ก.ค.: 40+ ตัว
3 ก.ค.: 2 ตัว

Insight:
- Sephora กำลังเน้น catalog และ product showcase เป็นหลัก
- ไม่ได้ใช้ direct discount เป็นตัวนำ
- ใช้ free gift และ gift card เป็น offer เสริม
- เปิด ads แบบ batch ใหญ่ แล้วให้ performance คัดเลือกตัวที่อยู่ต่อ
- แบรนด์ likely กำลังทดสอบ creative จำนวนมากพร้อมกัน แทนการพึ่งพา ad เดียว

Opportunity:
- หากแบรนด์คู่แข่งไม่เล่น direct discount อาจใช้ offer แบบ stack gift, bonus item หรือ trial size แทน
- Angle “gift card” และ “new launch” ยังมีสัดส่วนไม่สูงมาก สามารถเล่นเพิ่มได้
- Angle personalization เช่น quiz, shade match, routine finder อาจเป็นช่องว่าง
- UGC และ social proof ยังเป็น angle ที่ควรทดสอบ หากคู่แข่งเน้น catalog เยอะ

Recommended test:
- ทดสอบ batch 10-20 creatives พร้อมกัน
- แยก angle ชัดเจน เช่น free gift, new launch, gift card, personalization
- ใช้ catalog สำหรับ retargeting และใช้ emotional hook สำหรับ prospecting
- วัดผลที่ hook rate, thumb-stop rate, CTR, add-to-cart และ ROAS
```

---

# 6) ตัวอย่าง Creative 20 แบบ

ด้านล่างเป็นตัวอย่าง Creative สำหรับแบรนด์ความงาม/เครื่องสำอางที่ต้องการแข่งกับแบรนด์ใหญ่ โดยใช้ insight จาก report:

- คู่แข่งเน้น catalog
- ไม่เล่น direct discount
- มี free gift, gift card, new launch เป็นช่องให้เล่น
- ควรทดสอบ personalization และ social proof เพิ่มเติม

---

| No. | Angle | Hook | Headline | Primary Text | Visual Idea | CTA |
|---:|---|---|---|---|---|---|
| 1 | Free Gift First Order | สั่งครั้งแรก ได้ของขวัญทดลอง | เปิดผิวสวยด้วยของขวัญชิ้นแรก | รับ mini bestseller เมื่อสั่งครั้งแรก จำนวนจำกัด | Flat lay กล่องของขวัญ + สินค้าไซซ์มินิ | Shop Now |
| 2 | Gift Card | ให้สวยเลือกเอง | Gift Card ที่คนรับเลือกได้เอง | ไม่ต้องเดาไซซ์ เดสเฉด ให้ Gift Card เป็นของขวัญที่เลือกได้จริง | การ์ดของขวัญดิจิทัลพร้อมกล่องสวย | Send Gift Card |
| 3 | New Launch | ใหม่ล่าสุด | เปิดตัว [Product] สูตรใหม่ | สัมผัสใหม่ที่ออกแบบมาเพื่อผิวคุณ ดูรายละเอียดก่อนใคร | ภาพ macro texture สินค้า + packaging ใหม่ | Discover Now |
| 4 | Catalog Bestsellers | ตัวขายดี | 5 ไอเทมที่ลูกค้าเลือกซ้ำ | รวมไอเทมยอดนิยมที่ใช้จริง ซื้อซ้ำจริง เหมาะกับทั้งมือใหม่และสายบิวตี้ | Grid สินค้า 5 ตัวพร้อม badge bestseller | Shop Bestsellers |
| 5 | Carousel Routine | เช้า-เย็น | รูทีนง่ายๆ 3 ขั้นตอน | เริ่มเช้าด้วยไอเทมพื้นฐาน ปิดท้ายตอนเย็นด้วยตัวช่วยบำรุง ลดขั้นตอนแต่ยังครบ | Carousel swipe ตามขั้นตอน routine | Build Your Routine |
| 6 | UGC Review | ใช้จริง | รีวิวจากผู้ใช้งานจริง | หลายคนบอกว่าผิวดูเรียบเนียนขึ้นและแต่งหน้าติดง่ายขึ้น เมื่อใช้ต่อเนื่อง | วิดีโอสั้นแนว selfie review | See Reviews |
| 7 | Quiz Personalization | ไม่รู้เริ่มยังไง | ทำควิซ 30 วิ หาไอเทมที่ใช่ | ตอบคำถามสั้นๆ แล้วรับคำแนะนำ routine ที่เหมาะกับผิวของคุณ | หน้าจอ quiz พร้อมตัวเลือกง่ายๆ | Start Quiz |
| 8 | Shade Match | เฉดไม่ตรงผิว | หาเฉดที่ใช่ใน 1 นาที | ไม่ต้องเดาอีกต่อไป ช่วยคุณเลือกเฉดที่เข้ากับผิวมากขึ้น | Slider เทียบเฉดสีรองพื้น | Find Your Shade |
| 9 | Mini Trial | กลัวไม่เข้าผิว | ลองไซซ์มินิ ก่อนตัดสินใจ | เริ่มจากขนาดเล็ก พกง่าย เหมาะกับคนอยากลองก่อนซื้อไซซ์จริง | ภาพ mini size หลายชิ้น | Try Mini |
| 10 | Bundle Stack | ครบจบในกล่องเดียว | Bundle Routine ลดขั้นตอน | จับคู่ไอเทมที่ใช้ด้วยกันใน routine เดียว ง่ายกว่าและคุ้มกว่า | กล่อง bundle เปิดเห็นสินค้าครบชุด | Get Bundle |
| 11 | Loyalty | ยิ่งซื้อ ยิ่งคุ้ม | สะสมแต้มแลกไซซ์จริง | สมาชิกสะสมแต้มทุกการซื้อ ใช้แลกส่วนลดหรือไอเทมพิเศษ | การ์ดสมาชิก / แต้มสะสม | Join Now |
| 12 | Flash Gift 24h | เฉพาะวันนี้ | ของขวัญ 24 ชั่วโมง | สั่งภายในวันนี้ รับของขวัญพิเศษเพิ่ม จำนวนจำกัด | Countdown timer + gift box | Claim Offer |
| 13 | Sensitive Skin | ผิวแพ้ง่าย | สูตรอ่อนโยนสำหรับผิวแพ้ง่าย | เลือกสูตรที่เน้นความอ่อนโยน เหมาะกับผิวที่ต้องการการดูแลเป็นพิเศษ | ภาพเนื้อผลิตภัณฑ์ + ingredient highlight | Learn More |
| 14 | Clean Beauty | ไม่มีสารที่กังวล | คลีนบิวตี้ที่ใช้งานได้จริง | เลือกส่วนผสมอย่างตั้งใจ เหมาะกับคนที่ชอบความเรียบง่ายแต่ยังดูแลผิว | ภาพ ingredient สะอาดๆ | Explore Ingredients |
| 15 | Unboxing | เปิดกล่อง | ประสบการณ์ unboxing ที่อยากแชร์ | แพ็กเกจสวย น่าถ่ายรูป เหมาะกับทั้งใช้เองและเป็นของขวัญ | วิดีโอ unboxing สั้นๆ | Shop Now |
| 16 | Makeup Before/After | ก่อนแต่ง vs หลังแต่ง | ลุคธรรมชาติที่ดูเป็นผิว | เผยผิวให้ดูเรียบเนียนขึ้นด้วยลุคที่แต่งง่าย ไม่หนา | Split screen before/after | Get the Look |
| 17 | Seasonal | อากาศแบบนี้ | ไอเทม must-have ฤดูกาลนี้ | ปรับ routine ตามสภาพอากาศ ช่วยให้ผิวดูพร้อมตลอดวัน | โทนสีตามฤดูกาล + สินค้า | Shop Season Edit |
| 18 | Cart Retargeting | ลืมของในตะกร้า? | ไอเทมของคุณยังรออยู่ | กลับมาจบออเดอร์วันนี้ พร้อมสิทธิพิเศษสำหรับคุณ | ภาพสินค้าใน cart | Complete Order |
| 19 | Social Proof | คะแนนรีวิว 4.8/5 | ทำไมใครๆ ก็ให้ 4.8 | จากรีวิวจริงของลูกค้า หลายคนประทับใจในเนื้อสัมผัสและผลลัพธ์ | ดาวรีวิว + quote สั้นๆ | Read Reviews |
| 20 | Routine Comparison | 3 ขั้นตอน vs 7 ขั้นตอน | ลดขั้นตอน แต่ยังครบ | ถ้า routine คุณยาวเกินไป ลองเปลี่ยนเป็น routine ที่ง่ายขึ้นแต่ยังดูแลผิวได้ครบ | Infographic เปรียบเทียบ checklist | Simplify Routine |

---

# 7) Prompt สำหรับสร้าง Creative 20 แบบ

ใช้คำสั่งนี้กับ Claude:

```text
/creative

Brand: [ชื่อแบรนด์ของคุณ]
Country: [ประเทศ]
Product: [สินค้าหลัก]
Target audience: [กลุ่มเป้าหมาย]
Offer: [โปรโมชั่น / ของแถม / จุดขาย]
Competitor insight: [สรุปจาก /spy]
Number of creatives: 20

Task:
สร้าง 20 Creative Ideas สำหรับ Meta Ads โดยแต่ละ creative ต้องมี:
1. Angle
2. Hook
3. Headline
4. Primary Text
5. Visual Idea
6. CTA

Requirements:
- แต่ละ creative ต้องมี angle ต่างกันชัดเจน
- ใช้ภาษาที่เหมาะกับ Meta Ads
- ไม่เคลมเกินจริง
- ไม่เปรียบเทียบพาดพิงคู่แข่งโดยตรง
- เน้นทดสอบหลาย pain points และหลาย offers
- แบ่ง creative ตาม funnel: prospecting, consideration, retargeting
```

---

# 8) Workflow 10 นาที

```text
นาทีที่ 0-2:
รวบรวมข้อมูลจาก Meta Ad Library หรือข้อมูลที่ user ให้มา

นาทีที่ 2-4:
จัดกลุ่ม creative format และ message angle

นาทีที่ 4-6:
วิเคราะห์ winning pattern และ launch pattern

นาทีที่ 6-8:
หา angle gaps และโอกาสที่ควรทดสอบ

นาทีที่ 8-10:
สร้าง creative 20 แบบ พร้อม hook, headline, visual idea และ CTA
```

---

# 9) ตัวอย่างคำสั่งเต็มสำหรับใช้งานจริง

ถ้าต้องการให้ระบบวิเคราะห์แบรนด์:

```text
/spy [brand] [country]
```

เช่น:

```text
/spy sephora US
/spy innisfree TH
/spy lamer US
/spy sulwhasoo SG
```

ถ้าต้องการหา winning ads:

```text
/winners sephora
```

ถ้าต้องการหาช่องว่าง:

```text
/angles sephora
```

ถ้าต้องการ creative:

```text
/creative sephora 20
```

ถ้าต้องการ report:

```text
/report sephora
```

---

# 10) ข้อมูลที่ต้องส่งถ้าต้องการให้ผมรันให้จริง

ส่งข้อมูลเหล่านี้มาได้เลย:

```text
1. แบรนด์หรือเพจที่ต้องการส่อง
2. ประเทศ เช่น TH, US, SG, MY
3. ลิงก์เพจ หรือชื่อเพจ Facebook/Instagram
4. แบรนด์ของคุณขายอะไร
5. กลุ่มเป้าหมาย
6. จุดขายหรือ offer
7. ต้องการเน้น objective ไหน: traffic, lead, message, purchase
8. ต้องการ creative กี่แบบ เช่น 10, 20, 30
```

ตัวอย่าง:

```text
/spy brand=sephora country=US
My brand: แบรนด์เซรั่มผิวแพ้ง่าย
Target: หญิง 25-40 ปี ผิวแพ้ง่าย
Offer: ลด 10% สำหรับออเดอร์แรก + ฟรี mini size
Goal: Purchase
Creative: 20 แบบ
```

---

# 11) สรุปแบบสั้น

ระบบนี้ช่วยให้คุณ:

- รู้ว่าคู่แข่งกำลังรัน ad กี่ตัว
- รู้ว่าเปิด ads ใหม่เป็น batch หรือทยอยรัน
- รู้ว่า creative mix เน้นอะไร
- รู้ว่า offer ไหนถูกใช้บ่อย
- รู้ว่า angle ไหนยังว่าง
- สร้าง creative 20 แบบจาก insight จริง
- วางแผน batch testing ได้เร็วขึ้นโดยไม่ต้องเริ่มจากศูนย์

ถ้าคุณต้องการให้ผมทำต่อเป็น **Report จริงสำหรับแบรนด์ของคุณ** ส่งชื่อแบรนด์ + ประเทศ + ลิงก์เพจ หรือคีย์เวิร์ดมาได้เลยครับ
