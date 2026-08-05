"""
Executive Report Builder
สร้างรายงานผู้บริหารแบบมืออาชีพ
"""

from typing import Dict, List
from datetime import datetime


class ReportBuilder:
    """สร้างรายงานผู้บริหาร"""
    
    def __init__(self):
        pass
    
    def build_competitive_report(
        self,
        brand_name: str,
        spy_results: Dict,
        winner_analysis: Dict,
        gap_analysis: Dict,
        creative_ideas: List[Dict] = None
    ) -> str:
        """
        สร้างรายงานการแข่งขันแบบครบวงจร
        
        Args:
            brand_name: ชื่อแบรนด์
            spy_results: ผลจากการ spy คู่แข่ง
            winner_analysis: ผลวิเคราะห์ winning ads
            gap_analysis: ผลวิเคราะห์ angle gaps
            creative_ideas: ไอเดียโฆษณาที่แนะนำ
            
        Returns:
            Markdown report
        """
        report_date = datetime.now().strftime("%d %B %Y")
        
        report = f"""# 📊 รายงานวิเคราะห์การแข่งขัน: {brand_name}

**วันที่:** {report_date}  
**ผู้สร้าง:** Claude COWORK · Ad System

---

## 🎯 สรุปผู้บริหาร (Executive Summary)

{self._generate_executive_summary(spy_results, winner_analysis, gap_analysis)}

---

## 🔍 ภาพรวมตลาด (Market Overview)

{self._generate_market_overview(spy_results)}

---

## 🏆 Winning Ads Analysis

{self._generate_winning_analysis(winner_analysis)}

---

## 🌟 Angle Gap Analysis

{self._generate_gap_section(gap_analysis)}

---

## 💡 คำแนะนำเชิงกลยุทธ์ (Strategic Recommendations)

{self._generate_strategic_recommendations(gap_analysis, winner_analysis)}

---

## 🎨 Creative Ideas แนะนำ

{self._generate_creative_section(creative_ideas) if creative_ideas else "ไม่มีข้อมูล"}

---

## 📋 แผนการดำเนินการถัดไป (Next Steps)

1. **สัปดาห์ที่ 1-2:** ทดสอบ creative ideas ใหม่ 3-5 แบบ
2. **สัปดาห์ที่ 3-4:** วัดผลและ optimize ตาม performance
3. **เดือนที่ 2:** ขยาย scale บน angle ที่ได้ผลดี
4. **เดือนที่ 3:** ทำ competitive analysis ซ้ำเพื่อติดตามการเปลี่ยนแปลง

---

*รายงานนี้ถูกสร้างโดยอัตโนมัติด้วย Claude COWORK · Ad System*
"""
        
        return report
    
    def _generate_executive_summary(self, spy: Dict, winner: Dict, gap: Dict) -> str:
        """Generate executive summary"""
        total_ads = spy.get("total_ads", 0) if isinstance(spy, dict) else 0
        
        summary_points = [
            f"- วิเคราะห์โฆษณาทั้งหมด **{total_ads} โฆษณา** จากคู่แข่งหลัก",
            f"- พบ angle ที่ได้รับความนิยมสูงสุด: **{self._get_top_angle(winner)}**",
            f"- identified **{len(gap.get('gaps_opportunities', {}).get('blue_ocean_unused', []))}** blue ocean opportunities"
        ]
        
        return "\n".join(summary_points)
    
    def _get_top_angle(self, winner: Dict) -> str:
        """Extract top angle from winner analysis"""
        if isinstance(winner, dict):
            top = winner.get("top_angle")
            if top and isinstance(top, tuple):
                return top[0].replace("_", " ").title()
        return "ยังไม่มีข้อมูล"
    
    def _generate_market_overview(self, spy_results: Dict) -> str:
        """Generate market overview section"""
        if not spy_results or not isinstance(spy_results, dict):
            return "*ไม่มีข้อมูล*"
        
        total = spy_results.get("total_ads", 0)
        brand = spy_results.get("brand", "แบรนด์")
        
        return f"""### โฆษณาของ {brand}

- **จำนวนโฆษณาที่วิเคราะห์:** {total} โฆษณา
- **ประเทศ:** {spy_results.get("country", "TH")}

#### โฆษณาล่าสุด

{self._format_ads_preview(spy_results.get("ads", [])[:3])}
"""
    
    def _format_ads_preview(self, ads: List[Dict]) -> str:
        """Format ads preview for report"""
        if not ads:
            return "*ไม่มีข้อมูลโฆษณา*"
        
        formatted = []
        for i, ad in enumerate(ads, 1):
            body = ad.get("ad_creative_body", "")[:100] + "..." if len(ad.get("ad_creative_body", "")) > 100 else ad.get("ad_creative_body", "")
            formatted.append(f"{i}. \"{body}\"")
        
        return "\n".join(formatted)
    
    def _generate_winning_analysis(self, winner: Dict) -> str:
        """Generate winning ads analysis section"""
        if not winner or not isinstance(winner, dict):
            return "*ไม่มีข้อมูล*"
        
        patterns = winner.get("winning_patterns", {})
        
        return f"""### Pattern ที่พบในโฆษณาที่ชนะ

**Hooks ยอดนิยม:**
{self._format_pattern_list(patterns.get("hooks", {}))}

**Angles ยอดนิยม:**
{self._format_pattern_list(patterns.get("angles", {}))}

**CTAs ยอดนิยม:**
{self._format_pattern_list(patterns.get("ctas", {}))}

### คำแนะนำจาก Winning Ads

{chr(10).join("- " + rec for rec in winner.get("recommendations", ["ไม่มีคำแนะนำ"]))}
"""
    
    def _format_pattern_list(self, pattern_dict: Dict) -> str:
        """Format pattern dictionary as list"""
        if not pattern_dict:
            return "*ไม่มีข้อมูล*"
        
        items = sorted(pattern_dict.items(), key=lambda x: x[1], reverse=True)[:5]
        return "\n".join(f"- {k.replace('_', ' ').title()}: {v} ครั้ง" for k, v in items)
    
    def _generate_gap_section(self, gap: Dict) -> str:
        """Generate angle gap section"""
        if not gap or not isinstance(gap, dict):
            return "*ไม่มีข้อมูล*"
        
        gaps = gap.get("gaps_opportunities", {})
        
        return f"""### การวิเคราะห์ช่องว่าง

| ประเภท | Angles |
|--------|--------|
| 🔴 Competitors Use (เราควรพิจารณา) | {", ".join(gaps.get("angles_competitors_use_but_we_dont", ["-"]))} |
| 🟢 Our Unique Angles (จุดแข็ง) | {", ".join(gaps.get("angles_we_use_but_competitors_dont", ["-"]))} |
| 🔵 Blue Ocean (ยังไม่มีใครใช้) | {", ".join(gaps.get("blue_ocean_unused", ["-"])[:5])} |
| ⚠️ Red Ocean (คนใช้เยอะ) | {", ".join(gaps.get("red_ocean_overcrowded", ["-"]))} |

### คำแนะนำจาก Gap Analysis

{chr(10).join("- " + rec for rec in gap.get("recommendations", ["ไม่มีคำแนะนำ"]))}
"""
    
    def _generate_strategic_recommendations(self, gap: Dict, winner: Dict) -> str:
        """Generate strategic recommendations"""
        recommendations = [
            "### ด้าน Content & Messaging",
            "1. เน้น angle ที่อยู่ใน Blue Ocean เพื่อสร้าง differentiation",
            "2. ทดสอบ hook types ที่พบมากใน winning ads",
            "",
            "### ด้าน Channel & Platform",
            "1. ใช้ platform ที่กลุ่มเป้าหมายใช้งานมากที่สุด",
            "2. ปรับ creative format ให้เหมาะกับแต่ละ platform",
            "",
            "### ด้าน Measurement",
            "1. ตั้งค่า tracking ให้ชัดเจนสำหรับแต่ละ angle",
            "2. A/B test อย่างน้อย 3 variations ต่อ angle"
        ]
        
        return "\n".join(recommendations)
    
    def _generate_creative_section(self, creative_ideas: List[Dict]) -> str:
        """Generate creative ideas section"""
        if not creative_ideas:
            return "*ไม่มีไอเดียโฆษณา*"
        
        formatted = []
        for idea in creative_ideas[:3]:  # Show top 3
            formatted.append(f"""#### Variation {idea.get("variation_id", "?")}

**Hook:** {idea.get("hook", "")}

**Body:**
{idea.get("body", "")}

**CTA:** {idea.get("cta", "")}

**Visual Recommendations:**
{chr(10).join("- " + v for v in idea.get("visual_recommendations", []))}

---
""")
        
        return "\n".join(formatted)
    
    def save_report(self, report: str, filename: str = "report.md") -> str:
        """Save report to file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        return filename
