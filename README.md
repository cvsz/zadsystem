# Claude COWORK · Ad System

ระบบวิเคราะห์โฆษณาและสร้างสรรค์แคมเปญด้วย AI สำหรับนักการตลาด

## 🎯 วัตถุประสงค์

ช่วยให้นักการตลาดสามารถ:
- **Spy** คู่แข่งผ่าน Meta Ad Library
- **Analyze** Winning Ads และหา pattern ที่ชนะ
- **Find Angle Gaps** ช่องว่างที่ยังไม่มีใครเล่น
- **Generate Creative 20 แบบ** ไอเดียโฆษณาครบทุกมุม
- **Build Reports** รายงานผู้บริหารแบบมืออาชีพ

## 📁 โครงสร้างโปรเจค

```
zadsystem/
├── README.md           # ไฟล์นี้
├── AGENTS.md          # เอกสารรายละเอียดระบบ
├── requirements.txt    # Dependencies
├── config.yaml         # การตั้งค่า
├── src/                # Source code
│   ├── __init__.py
│   ├── cli.py          # คำสั่ง CLI (/spy /winners /angles /creative /report)
│   ├── spy.py          # Ad Library Spy skill
│   ├── winners.py      # Winning Ad Analyzer
│   ├── angles.py       # Angle Gap Finder
│   ├── creative.py     # Creative Factory (20 แบบ)
│   ├── report.py       # Executive Report Builder
│   └── meta_library.py # Meta Ad Library API
├── prompts/            # AI Prompts
│   ├── master.md       # Master Prompt
│   ├── spy.md          # Spy Prompt
│   ├── creative.md     # Creative Prompt  
│   └── report.md       # Report Prompt
├── templates/          # Report Templates
│   └── report_template.md
└── examples/           # ตัวอย่าง
    └── sephora_report.md
```

## 🚀 การติดตั้ง

```bash
# Clone repository
git clone <your-repo-url>
cd zadsystem

# ติดตั้ง dependencies
pip install -r requirements.txt

# ตั้งค่า config
cp config.yaml.example config.yaml  # หรือแก้ไข config.yaml โดยตรง
# แก้ไข config.yaml ใส่ API keys
```

## 💡 การใช้งาน

### 1. Spy คู่แข่ง (Ad Library)

```bash
python -m src.cli spy sephora --country US
```

หรือใช้คำสั่งลัด:
```bash
/spy sephora US
```

### 2. วิเคราะห์ Winning Ads

```bash
python -m src.cli winners sephora --period "30d"
```

### 3. หา Angle Gaps

```bash
python -m src.cli angles sephora --competitors laneige estee clinique
```

### 4. สร้าง Creative Ideas (20 แบบ)

```bash
# ใช้ในรายงานอัตโนมัติ
python -m src.cli report sephora --country US

# หรือเรียกใช้โดยตรงในโค้ด Python
from src.creative import CreativeFactory
factory = CreativeFactory()
creatives = factory.generate_creative_20(brand="sephora")
```

### 5. สร้างรายงานผู้บริหาร (พร้อม Creative 20 แบบ)

```bash
python -m src.cli report sephora --country US --output sephora_report.md
```

## 🔧 Configuration

แก้ไข `config.yaml` เพื่อตั้งค่า:

```yaml
meta:
  access_token: "YOUR_META_API_TOKEN"  # ได้จาก https://developers.facebook.com
  
openai:
  api_key: "YOUR_OPENAI_API_KEY"
  model: "gpt-4o"

languages:
  primary: "th"
  secondary: "en"
```

## 📋 คำสั่งทั้งหมด

| คำสั่ง | คำอธิบาย |
|--------|----------|
| `/spy [brand] [country]` | สืบโฆษณาของแบรนด์จาก Meta Ad Library |
| `/winners [brand]` | วิเคราะห์ Winning Ads patterns |
| `/angles [brand]` | หา Angle Gaps และ Blue Ocean opportunities |
| `/creative [brand] 20` | สร้าง Creative Ideas 20 แบบ |
| `/report [brand]` | สร้างรายงานผู้บริหารครบวงจร |

## 🎨 Creative 20 แบบที่รองรับ

ระบบสร้าง Creative 20 แบบตาม AGENTS.md specification:

1. Free Gift First Order
2. Gift Card
3. New Launch
4. Catalog Bestsellers
5. Carousel Routine
6. UGC Review
7. Quiz Personalization
8. Shade Match
9. Mini Trial
10. Bundle Stack
11. Loyalty
12. Flash Gift 24h
13. Sensitive Skin
14. Clean Beauty
15. Unboxing
16. Makeup Before/After
17. Seasonal
18. Cart Retargeting
19. Social Proof
20. Routine Comparison

แต่ละ Creative มีครบ: Hook, Headline, Primary Text, Visual Idea, CTA

## 📊 ตัวอย่าง Output

ดูตัวอย่างรายงานที่ [`examples/sephora_report.md`](examples/sephora_report.md)

## ⏱️ Workflow 10 นาที

```
นาทีที่ 0-2:  รวบรวมข้อมูลจาก Meta Ad Library
นาทีที่ 2-4:  จัดกลุ่ม creative format และ message angle
นาทีที่ 4-6:  วิเคราะห์ winning pattern และ launch pattern
นาทีที่ 6-8:  หา angle gaps และโอกาสที่ควรทดสอบ
นาทีที่ 8-10: สร้าง creative 20 แบบ พร้อม hook, headline, visual idea และ CTA
```

## 🤝 Contributing

ยินดีรับ contributions ทุกประเภท!

## 📄 License

MIT License
