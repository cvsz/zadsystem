# Claude COWORK · Ad System

ระบบวิเคราะห์โฆษณาและสร้างสรรค์แคมเปญด้วย AI สำหรับนักการตลาด

## 🎯 วัตถุประสงค์

ช่วยให้นักการตลาดสามารถ:
- **Spy** คู่แข่งผ่าน Meta Ad Library
- **Analyze** Winning Ads และหา pattern ที่ชนะ
- **Find Angle Gaps** ช่องว่างที่ยังไม่มีใครเล่น
- **Generate Creative** ไอเดียโฆษณาใหม่ๆ
- **Build Reports** รายงานผู้บริหารแบบมืออาชีพ

## 📁 โครงสร้างโปรเจค

```
zadsystem/
├── README.md           # ไฟล์นี้
├── requirements.txt    # Dependencies
├── config.yaml         # การตั้งค่า
├── src/                # Source code
│   ├── __init__.py
│   ├── cli.py          # คำสั่ง CLI (/spy /winners /creative)
│   ├── spy.py          # Ad Library Spy skill
│   ├── winners.py      # Winning Ad Analyzer
│   ├── angles.py       # Angle Gap Finder
│   ├── creative.py     # Creative Factory
│   ├── report.py       # Executive Report Builder
│   └── meta_library.py # Meta Ad Library API
├── prompts/            # AI Prompts
│   ├── master.md
│   ├── spy.md
│   ├── creative.md
│   └── report.md
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
cp config.yaml.example config.yaml
# แก้ไข config.yaml ใส่ API keys
```

## 💡 การใช้งาน

### 1. Spy คู่แข่ง (Ad Library)

```bash
python -m src.cli spy --brand "sephora" --country "TH"
```

หรือใช้คำสั่งลัด:
```bash
/spy sephora
```

### 2. วิเคราะห์ Winning Ads

```bash
python -m src.cli winners --brand "sephora" --period "30d"
```

### 3. หา Angle Gaps

```bash
python -m src.cli angles --brand "sephora" --competitors "laneige,estee,clinique"
```

### 4. สร้าง Creative Ideas

```bash
python -m src.cli creative --product "serum" --angle "hydration" --platform "facebook"
```

### 5. สร้างรายงานผู้บริหาร

```bash
python -m src.cli report --brand "sephora" --output "report.md"
```

## 🔧 Configuration

แก้ไข `config.yaml` เพื่อตั้งค่า:

```yaml
meta:
  access_token: "YOUR_META_API_TOKEN"
  
openai:
  api_key: "YOUR_OPENAI_API_KEY"
  model: "gpt-4o"

languages:
  primary: "th"
  secondary: "en"
```

## 📋 ตัวอย่าง Output

ดูตัวอย่างรายงานที่ [`examples/sephora_report.md`](examples/sephora_report.md)

## 🤝 Contributing

ยินดีรับ contributions ทุกประเภท!

## 📄 License

MIT License
