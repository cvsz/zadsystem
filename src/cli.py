"""
Command Line Interface for Claude COWORK · Ad System
"""

import click
import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from .spy import AdSpy
from .winners import WinningAdAnalyzer
from .angles import AngleGapFinder
from .creative import CreativeFactory
from .report import ReportBuilder
from .meta_library import get_mock_ads

console = Console()


@click.group()
def main():
    """🚀 Claude COWORK · Ad System
    
    ระบบวิเคราะห์โฆษณาและสร้างสรรค์แคมเปญด้วย AI
    """
    pass


@main.command()
@click.argument('brand')
@click.option('--country', default='TH', help='Country code')
@click.option('--output', '-o', default=None, help='Output file')
def spy(brand, country, output):
    """🔍 Spy โฆษณาของแบรนด์คู่แข่ง"""
    console.print(f"\n🔍 กำลัง spy {brand} ในประเทศ {country}...\n")
    
    ad_spy = AdSpy()
    results = ad_spy.spy_brand(brand, country)
    
    # Display results
    table = Table(title=f"📊 ผลการ Spy: {brand}")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("จำนวนโฆษณา", str(results["total_ads"]))
    table.add_row("ประเทศ", results["country"])
    
    console.print(table)
    
    # Show ads preview
    if results["ads"]:
        console.print("\n💬 โฆษณาล่าสุด:")
        for i, ad in enumerate(results["ads"][:3], 1):
            body = ad.get("ad_creative_body", "")[:150]
            console.print(f"{i}. {body}...")
    
    if output:
        with open(output, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        console.print(f"\n✅ บันทึกผลลัพธ์ที่ {output}")


@main.command()
@click.argument('brand')
@click.option('--period', default='30d', help='Analysis period')
def winners(brand, period):
    """🏆 วิเคราะห์ Winning Ads"""
    console.print(f"\n🏆 กำลังวิเคราะห์ Winning Ads ของ {brand}...\n")
    
    # Get mock ads for demo
    ads = get_mock_ads(brand)
    
    analyzer = WinningAdAnalyzer()
    results = analyzer.analyze_winners(ads)
    
    # Display results
    table = Table(title="🎯 Winning Patterns")
    table.add_column("Category", style="cyan")
    table.add_column("Top Pattern", style="green")
    
    if results.get("top_hook"):
        table.add_row("Hook", results["top_hook"][0].replace("_", " ").title())
    if results.get("top_angle"):
        table.add_row("Angle", results["top_angle"][0].replace("_", " ").title())
    if results.get("top_cta"):
        table.add_row("CTA", results["top_cta"][0].replace("_", " ").title())
    
    console.print(table)
    
    # Show recommendations
    if results.get("recommendations"):
        console.print("\n💡 คำแนะนำ:")
        for rec in results["recommendations"]:
            console.print(f"  • {rec}")


@main.command()
@click.argument('brand')
@click.option('--competitors', '-c', multiple=True, help='Competitor brands')
def angles(brand, competitors):
    """🌟 หา Angle Gaps"""
    console.print(f"\n🌟 กำลังวิเคราะห์ Angle Gaps สำหรับ {brand}...\n")
    
    # Get mock data
    brand_ads = get_mock_ads(brand)
    competitor_ads = []
    for comp in competitors:
        competitor_ads.extend(get_mock_ads(comp))
    
    if not competitors:
        competitor_ads = get_mock_ads("competitor")
    
    finder = AngleGapFinder()
    results = finder.find_gaps(brand_ads, competitor_ads, brand)
    
    # Display gaps
    gaps = results.get("gaps_opportunities", {})
    
    console.print(Panel.fit(
        f"🔵 Blue Ocean: {', '.join(gaps.get('blue_ocean_unused', ['None'])[:5])}",
        title="Opportunities"
    ))
    
    console.print(Panel.fit(
        f"🔴 Should Consider: {', '.join(gaps.get('angles_competitors_use_but_we_dont', ['None']))}",
        title="Gaps"
    ))
    
    # Show recommendations
    if results.get("recommendations"):
        console.print("\n💡 Recommendations:")
        for rec in results["recommendations"]:
            console.print(f"  {rec}")


@main.command()
@click.argument('product')
@click.option('--angle', '-a', default='brightness_glow', help='Marketing angle')
@click.option('--platform', '-p', default='facebook', help='Platform')
@click.option('--count', '-n', default=3, help='Number of variations')
def creative(product, angle, platform, count):
    """🎨 สร้าง Creative Ideas"""
    console.print(f"\n🎨 กำลังสร้าง creative ideas สำหรับ {product}...\n")
    
    factory = CreativeFactory()
    variations = factory.generate_multiple_variations(product, angle, count)
    
    for var in variations:
        console.print(Panel(
            f"**Hook:** {var['hook']}\n\n{var['body']}\n\n**CTA:** {var['cta']}",
            title=f"Variation {var['variation_id']}",
            border_style="green"
        ))


@main.command()
@click.argument('brand')
@click.option('--output', '-o', default='report.md', help='Output file')
@click.option('--country', default='TH', help='Country code')
def report(brand, output, country):
    """📊 สร้างรายงานผู้บริหาร"""
    console.print(f"\n📊 กำลังสร้างรายงานสำหรับ {brand}...\n")
    
    # Gather all data
    ad_spy = AdSpy()
    spy_results = ad_spy.spy_brand(brand, country=country)
    
    ads = spy_results["ads"]
    
    winner_analyzer = WinningAdAnalyzer()
    winner_results = winner_analyzer.analyze_winners(ads)
    
    gap_finder = AngleGapFinder()
    gap_results = gap_finder.find_gaps(ads, ads, brand)
    
    creative_factory = CreativeFactory()
    creative_ideas = creative_factory.generate_creative_20(
        brand=brand,
        product=f"{brand} Product",
        target_audience="หญิง 25-40 ปี",
        offer="ลด 10% ออเดอร์แรก + ฟรี mini size"
    )
    
    # Build report
    builder = ReportBuilder()
    report_content = builder.build_competitive_report(
        brand_name=brand,
        spy_results=spy_results,
        winner_analysis=winner_results,
        gap_analysis=gap_results,
        creative_ideas=creative_ideas
    )
    
    # Save report
    builder.save_report(report_content, output)
    
    console.print(Panel.fit(f"✅ รายงานถูกบันทึกที่: {output}"))
    console.print(f"\n📄 สร้าง Creative Ideas แล้ว {len(creative_ideas)} แบบ")
    console.print("\n💡 ตัวอย่าง Creative 3 แบบแรก:")
    for idea in creative_ideas[:3]:
        console.print(f"  {idea['no']}. {idea['angle']}: {idea['hook']}")


if __name__ == "__main__":
    main()
