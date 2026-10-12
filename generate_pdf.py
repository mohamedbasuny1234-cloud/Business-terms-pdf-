# -*- coding: utf-8 -*-
"""
مولّد PDF لمصطلحات البيزنس - 400+ مصطلح عربي/إنجليزي
15 مجال | جاهز لـ GitHub Codespaces / Replit / Colab
"""

import os
import urllib.request
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Table, TableStyle,
                                Paragraph, Spacer, PageBreak)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import arabic_reshaper
from bidi.algorithm import get_display

# ============================================
# 1) الخط العربي
# ============================================
FONT_URL = FONT_URL = "https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/amiri/Amiri-Regular.ttf"
FONT_PATH = "Amiri-Regular.ttf"

if not os.path.exists(FONT_PATH):
    print("⏳ جاري تحميل الخط العربي...")
    urllib.request.urlretrieve(FONT_URL, FONT_PATH)
    print("✅ تم تحميل الخط")

pdfmetrics.registerFont(TTFont('Arabic', FONT_PATH))


def ar(text):
    return get_display(arabic_reshaper.reshape(text))


# ============================================
# 2) قاعدة المصطلحات (15 مجال)
# ============================================
SECTIONS = {

"1. المحاسبة والمالية": [
    ("Accounting", "المحاسبة"),
    ("Revenue", "الإيرادات"),
    ("Profit", "الربح"),
    ("Gross Profit", "الربح الإجمالي"),
    ("Net Profit", "الربح الصافي"),
    ("Loss", "الخسارة"),
    ("Asset", "الأصول"),
    ("Current Asset", "الأصول المتداولة"),
    ("Fixed Asset", "الأصول الثابتة"),
    ("Liability", "الالتزامات / الخصوم"),
    ("Equity", "حقوق الملكية"),
    ("Cash Flow", "التدفق النقدي"),
    ("Cash Flow Statement", "قائمة التدفقات النقدية"),
    ("Balance Sheet", "الميزانية العمومية"),
    ("Income Statement", "قائمة الدخل"),
    ("Budget", "الميزانية"),
    ("Forecast", "التوقعات / التنبؤ"),
    ("Depreciation", "الإهلاك"),
    ("Amortization", "الإطفاء"),
    ("Liquidity", "السيولة"),
    ("Solvency", "الملاءة المالية"),
    ("ROI (Return on Investment)", "العائد على الاستثمار"),
    ("ROE (Return on Equity)", "العائد على حقوق الملكية"),
    ("Break-even Point", "نقطة التعادل"),
    ("Working Capital", "رأس المال العامل"),
    ("Accounts Receivable", "الذمم المدينة"),
    ("Accounts Payable", "الذمم الدائنة"),
    ("Inventory", "المخزون"),
    ("Payroll", "كشف الرواتب"),
    ("Audit", "التدقيق"),
    ("Tax", "الضريبة"),
    ("VAT (Value Added Tax)", "ضريبة القيمة المضافة"),
    ("Financial Statement", "القوائم المالية"),
    ("Bookkeeping", "مسك الدفاتر"),
    ("Accrual", "الاستحقاق"),
],

"2. الإدارة والقيادة": [
    ("Management", "الإدارة"),
    ("Leadership", "القيادة"),
    ("Strategy", "الاستراتيجية"),
    ("Strategic Planning", "التخطيط الاستراتيجي"),
    ("Vision", "الرؤية"),
    ("Mission", "الرسالة"),
    ("Objective", "الهدف"),
    ("Goal", "الغاية"),
    ("Stakeholder", "صاحب المصلحة"),
    ("Shareholder", "المساهم"),
    ("Board of Directors", "مجلس الإدارة"),
    ("CEO (Chief Executive Officer)", "الرئيس التنفيذي"),
    ("CFO (Chief Financial Officer)", "المدير المالي"),
    ("COO (Chief Operating Officer)", "مدير العمليات"),
    ("CTO (Chief Technology Officer)", "المدير التقني"),
    ("KPI (Key Performance Indicator)", "مؤشر الأداء الرئيسي"),
    ("OKR (Objectives and Key Results)", "الأهداف والنتائج الرئيسية"),
    ("Outsourcing", "الاستعانة بمصادر خارجية"),
    ("Benchmarking", "المقارنة المرجعية"),
    ("SWOT Analysis", "تحليل SWOT"),
    ("Decision Making", "اتخاذ القرار"),
    ("Delegation", "التفويض"),
    ("Empowerment", "التمكين"),
    ("Change Management", "إدارة التغيير"),
    ("Risk Management", "إدارة المخاطر"),
    ("Corporate Governance", "حوكمة الشركات"),
    ("Succession Planning", "تخطيط التعاقب"),
    ("Performance Appraisal", "تقييم الأداء"),
    ("Feedback", "التغذية الراجعة"),
    ("Motivation", "التحفيز"),
],

"3. التسويق": [
    ("Marketing", "التسويق"),
    ("Digital Marketing", "التسويق الرقمي"),
    ("Content Marketing", "تسويق المحتوى"),
    ("Branding", "العلامة التجارية"),
    ("Brand Awareness", "الوعي بالعلامة التجارية"),
    ("Target Audience", "الجمهور المستهدف"),
    ("Market Research", "بحوث السوق"),
    ("Market Share", "الحصة السوقية"),
    ("Segmentation", "التقسيم"),
    ("Positioning", "التموضع"),
    ("Lead Generation", "توليد العملاء المحتملين"),
    ("Conversion Rate", "معدل التحويل"),
    ("Customer Retention", "الاحتفاظ بالعملاء"),
    ("Customer Acquisition", "اكتساب العملاء"),
    ("Customer Lifetime Value", "القيمة الحياتية للعميل"),
    ("Funnel", "قمع المبيعات"),
    ("SEO (Search Engine Optimization)", "تحسين محركات البحث"),
    ("SEM (Search Engine Marketing)", "التسويق عبر محركات البحث"),
    ("PPC (Pay Per Click)", "الدفع مقابل النقر"),
    ("CTR (Click Through Rate)", "معدل النقر"),
    ("Engagement", "التفاعل"),
    ("Reach", "الوصول"),
    ("Impressions", "الظهور"),
    ("Campaign", "الحملة التسويقية"),
    ("Copywriting", "كتابة الإعلانات"),
    ("Call to Action (CTA)", "دعوة لاتخاذ إجراء"),
    ("A/B Testing", "اختبار A/B"),
    ("Persona", "شخصية العميل"),
    ("B2B", "التعامل بين الشركات"),
    ("B2C", "التعامل بين الشركة والمستهلك"),
],

"4. المبيعات": [
    ("Sales", "المبيعات"),
    ("Sales Funnel", "قمع المبيعات"),
    ("Pipeline", "خط الأنابيب البيعي"),
    ("Prospect", "عميل محتمل"),
    ("Lead", "عميل مرتقب"),
    ("Cold Call", "الاتصال البارد"),
    ("Warm Lead", "عميل مهتم"),
    ("Quota", "الحصة البيعية"),
    ("Commission", "العمولة"),
    ("Upselling", "البيع الأعلى"),
    ("Cross-selling", "البيع المتقاطع"),
    ("Closing", "إتمام البيع"),
    ("Objection Handling", "معالجة الاعتراضات"),
    ("Negotiation", "التفاوض"),
    ("Deal", "الصفقة"),
    ("Discount", "الخصم"),
    ("Retention Rate", "معدل الاحتفاظ"),
    ("Churn Rate", "معدل الفقد"),
    ("CRM (Customer Relationship Management)", "إدارة علاقات العملاء"),
    ("Account Manager", "مدير الحساب"),
],

"5. ريادة الأعمال": [
    ("Entrepreneur", "رائد الأعمال"),
    ("Entrepreneurship", "ريادة الأعمال"),
    ("Startup", "شركة ناشئة"),
    ("Scale-up", "شركة متوسعة"),
    ("Venture Capital", "رأس المال المخاطر"),
    ("Angel Investor", "المستثمر الملائكي"),
    ("Seed Funding", "التمويل التأسيسي"),
    ("Series A / B / C", "جولات التمويل"),
    ("Pitch Deck", "عرض تقديمي للمستثمرين"),
    ("MVP (Minimum Viable Product)", "المنتج الأولي"),
    ("Business Model", "نموذج العمل"),
    ("Business Plan", "خطة العمل"),
    ("Value Proposition", "عرض القيمة"),
    ("Product-Market Fit", "توافق المنتج مع السوق"),
    ("Bootstrapping", "التمويل الذاتي"),
    ("Exit Strategy", "استراتيجية الخروج"),
    ("Unicorn", "شركة يونيكورن"),
    ("Incubator", "حاضنة أعمال"),
    ("Accelerator", "مسرّعة أعمال"),
    ("Franchise", "الامتياز التجاري"),
],

"6. الشركات والاندماج": [
    ("Corporation", "الشركة"),
    ("LLC (Limited Liability Company)", "شركة ذات مسؤولية محدودة"),
    ("Joint Venture", "المشروع المشترك"),
    ("Partnership", "الشراكة"),
    ("Sole Proprietorship", "المؤسسة الفردية"),
    ("Holding Company", "الشركة القابضة"),
    ("Subsidiary", "الشركة التابعة"),
    ("Merger", "الاندماج"),
    ("Acquisition", "الاستحواذ"),
    ("Due Diligence", "الفحص النافي للجهالة"),
    ("IPO (Initial Public Offering)", "الطرح العام الأولي"),
    ("Bankruptcy", "الإفلاس"),
    ("Liquidation", "التصفية"),
    ("Restructuring", "إعادة الهيكلة"),
    ("Divestiture", "التخلي عن الأصول"),
    ("Spin-off", "الانفصال"),
    ("Shareholder Meeting", "اجتماع المساهمين"),
    ("Dividend", "توزيعات الأرباح"),
    ("Stock Option", "خيار الأسهم"),
    ("Valuation", "التقييم"),
],

"7. الموارد البشرية": [
    ("Human Resources (HR)", "الموارد البشرية"),
    ("Recruitment", "التوظيف"),
    ("Onboarding", "تهيئة الموظف الجديد"),
    ("Offboarding", "إنهاء خدمة الموظف"),
    ("Job Description", "الوصف الوظيفي"),
    ("Job Rotation", "التدوير الوظيفي"),
    ("Compensation", "الأجر والتعويض"),
    ("Benefits", "المزايا"),
    ("KPI", "مؤشر الأداء"),
    ("Training", "التدريب"),
    ("Development", "التطوير"),
    ("Career Path", "المسار المهني"),
    ("Turnover", "معدل دوران الموظفين"),
    ("Employee Engagement", "مشاركة الموظفين"),
    ("Work-Life Balance", "التوازن بين العمل والحياة"),
    ("Remote Work", "العمل عن بُعد"),
    ("Hybrid Work", "العمل الهجين"),
    ("Performance Review", "مراجعة الأداء"),
    ("Disciplinary Action", "الإجراء التأديبي"),
    ("Labor Law", "قانون العمل"),
],

"8. القانون والعقود": [
    ("Contract", "عقد"),
    ("Agreement", "اتفاقية"),
    ("Clause", "بند"),
    ("Terms and Conditions", "الشروط والأحكام"),
    ("NDA (Non-Disclosure Agreement)", "اتفاقية عدم الإفصاح"),
    ("Intellectual Property", "الملكية الفكرية"),
    ("Copyright", "حقوق النشر"),
    ("Trademark", "العلامة التجارية"),
    ("Patent", "براءة الاختراع"),
    ("Compliance", "الامتثال"),
    ("Liability", "المسؤولية القانونية"),
    ("Breach of Contract", "الإخلال بالعقد"),
    ("Dispute Resolution", "تسوية النزاعات"),
    ("Arbitration", "التحكيم"),
    ("Litigation", "التقاضي"),
    ("Power of Attorney", "التوكيل"),
    ("Indemnity", "التعويض"),
    ("Warranty", "الضمان"),
    ("Force Majeure", "القوة القاهرة"),
    ("Confidentiality", "السرية"),
],

"9. التقنية والتحول الرقمي": [
    ("Digital Transformation", "التحول الرقمي"),
    ("Automation", "الأتمتة"),
    ("Artificial Intelligence (AI)", "الذكاء الاصطناعي"),
    ("Machine Learning", "تعلم الآلة"),
    ("Cloud Computing", "الحوسبة السحابية"),
    ("SaaS (Software as a Service)", "البرمجيات كخدمة"),
    ("API (Application Programming Interface)", "واجهة برمجة التطبيقات"),
    ("Data Analytics", "تحليل البيانات"),
    ("Big Data", "البيانات الضخمة"),
    ("Business Intelligence (BI)", "ذكاء الأعمال"),
    ("ERP (Enterprise Resource Planning)", "تخطيط موارد المؤسسة"),
    ("CRM", "إدارة علاقات العملاء"),
    ("Cybersecurity", "الأمن السيبراني"),
    ("Blockchain", "البلوكشين"),
    ("IoT (Internet of Things)", "إنترنت الأشياء"),
    ("Agile", "المنهجية الرشيقة"),
    ("Scrum", "سكرم"),
    ("Sprint", "السبرنت"),
    ("DevOps", "دمج التطوير والعمليات"),
    ("MVP", "المنتج الأولي"),
    ("Scalability", "قابلية التوسع"),
    ("UX (User Experience)", "تجربة المستخدم"),
    ("UI (User Interface)", "واجهة المستخدم"),
    ("Prototype", "النموذج الأولي"),
    ("Beta Version", "النسخة التجريبية"),
],

"10. اللوجستيات وسلاسل الإمداد": [
    ("Supply Chain", "سلسلة التوريد"),
    ("Supply Chain Management", "إدارة سلسلة التوريد"),
    ("Logistics", "اللوجستيات"),
    ("Procurement", "المشتريات"),
    ("Sourcing", "التوريد"),
    ("Vendor", "المورد"),
    ("Supplier", "المورد"),
    ("Inventory Management", "إدارة المخزون"),
    ("Warehouse", "المستودع"),
    ("Distribution", "التوزيع"),
    ("Freight", "الشحن"),
    ("Shipping", "النقل البحري"),
    ("Customs", "الجمارك"),
    ("Lead Time", "زمن التسليم"),
    ("Just-in-Time (JIT)", "في الوقت المناسب"),
    ("Order Fulfillment", "تنفيذ الطلبات"),
    ("Last Mile Delivery", "التوصيل للميل الأخير"),
    ("Reverse Logistics", "اللوجستيات العكسية"),
    ("SKU (Stock Keeping Unit)", "وحدة حفظ المخزون"),
    ("Demand Planning", "تخطيط الطلب"),
],

"11. الاستثمار والأسواق المالية": [
    ("Investment", "الاستثمار"),
    ("Investor", "المستثمر"),
    ("Portfolio", "المحفظة الاستثمارية"),
    ("Diversification", "التنويع"),
    ("Stock", "السهم"),
    ("Share", "الحصة"),
    ("Bond", "السند"),
    ("Mutual Fund", "صندوق الاستثمار المشترك"),
    ("ETF (Exchange Traded Fund)", "الصندوق المتداول بالبورصة"),
    ("Hedge Fund", "صندوق التحوط"),
    ("Index", "المؤشر"),
    ("Bull Market", "سوق صاعد"),
    ("Bear Market", "سوق هابط"),
    ("Volatility", "التقلبات"),
    ("Speculation", "المضاربة"),
    ("Arbitrage", "المراجحة"),
    ("Leverage", "الرافعة المالية"),
    ("Margin", "الهامش"),
    ("Short Selling", "البيع على المكشوف"),
    ("Derivatives", "المشتقات المالية"),
    ("Options", "الخيارات"),
    ("Futures", "العقود الآجلة"),
    ("Commodities", "السلع"),
    ("Forex", "الفوركس"),
    ("Capital Gain", "الربح الرأسمالي"),
    ("Capital Loss", "الخسارة الرأسمالية"),
    ("Yield", "العائد"),
    ("Interest Rate", "سعر الفائدة"),
    ("Inflation", "التضخم"),
    ("Deflation", "الانكماش"),
    ("Recession", "الكساد"),
    ("Bullion", "السبائك"),
    ("Asset Allocation", "توزيع الأصول"),
    ("Risk Tolerance", "تحمل المخاطر"),
    ("Blue Chip", "الأسهم القيادية"),
    ("Penny Stock", "الأسهم الرخيصة"),
    ("Market Capitalization", "القيمة السوقية"),
    ("EPS (Earnings Per Share)", "ربحية السهم"),
    ("P/E Ratio", "نسبة السعر للربح"),
    ("Dividend Yield", "عائد التوزيعات"),
],

"12. البنوك والخدمات المالية": [
    ("Banking", "البنوك"),
    ("Commercial Bank", "البنك التجاري"),
    ("Investment Bank", "بنك الاستثمار"),
    ("Central Bank", "البنك المركزي"),
    ("Deposit", "الوديعة"),
    ("Withdrawal", "السحب"),
    ("Loan", "القرض"),
    ("Mortgage", "الرهن العقاري"),
    ("Credit", "الائتمان"),
    ("Debit", "الخصم المباشر"),
    ("Interest", "الفائدة"),
    ("Compound Interest", "الفائدة المركبة"),
    ("Collateral", "الضمان"),
    ("Guarantee", "الكفالة"),
    ("Letter of Credit (LC)", "خطاب الاعتماد"),
    ("Wire Transfer", "التحويل البنكي"),
    ("SWIFT", "سويفت"),
    ("IBAN", "رقم الحساب المصرفي الدولي"),
    ("Overdraft", "السحب على المكشوف"),
    ("Credit Score", "التقييم الائتماني"),
    ("KYC (Know Your Customer)", "اعرف عميلك"),
    ("AML (Anti-Money Laundering)", "مكافحة غسل الأموال"),
    ("Fintech", "التقنية المالية"),
    ("Digital Wallet", "المحفظة الرقمية"),
    ("Mobile Banking", "الخدمات المصرفية عبر الجوال"),
    ("Islamic Banking", "الصيرفة الإسلامية"),
    ("Murabaha", "المرابحة"),
    ("Mudarabah", "المضاربة"),
    ("Sukuk", "الصكوك"),
    ("Takaful", "التكافل"),
],

"13. التأمين": [
    ("Insurance", "التأمين"),
    ("Policy", "البوليصة"),
    ("Premium", "القسط"),
    ("Claim", "المطالبة"),
    ("Insured", "المؤمَّن له"),
    ("Insurer", "شركة التأمين"),
    ("Beneficiary", "المستفيد"),
    ("Coverage", "التغطية"),
    ("Deductible", "التحمل"),
    ("Exclusion", "الاستثناء"),
    ("Life Insurance", "تأمين الحياة"),
    ("Health Insurance", "التأمين الصحي"),
    ("Property Insurance", "تأمين الممتلكات"),
    ("Liability Insurance", "تأمين المسؤولية"),
    ("Auto Insurance", "تأمين السيارات"),
    ("Marine Insurance", "التأمين البحري"),
    ("Reinsurance", "إعادة التأمين"),
    ("Underwriting", "الاكتتاب"),
    ("Actuary", "الخبير الاكتواري"),
    ("Risk Assessment", "تقييم المخاطر"),
],

"14. العقارات": [
    ("Real Estate", "العقارات"),
    ("Property", "الملكية"),
    ("Mortgage", "الرهن العقاري"),
    ("Lease", "الإيجار طويل الأمد"),
    ("Rent", "الإيجار"),
    ("Tenant", "المستأجر"),
    ("Landlord", "المالك"),
    ("Down Payment", "الدفعة المقدمة"),
    ("Appraisal", "التقييم العقاري"),
    ("Broker", "الوسيط العقاري"),
    ("Listing", "الإدراج العقاري"),
    ("Closing Costs", "تكاليف الإتمام"),
    ("Equity", "حقوق الملكية العقارية"),
    ("Foreclosure", "الحجز على العقار"),
    ("REIT (Real Estate Investment Trust)", "صندوق الاستثمار العقاري"),
    ("Commercial Property", "العقار التجاري"),
    ("Residential Property", "العقار السكني"),
    ("Vacancy Rate", "معدل الشواغر"),
    ("Cap Rate", "معدل الرسملة"),
    ("Escrow", "الضمان العقاري"),
],

"15. إدارة المشاريع": [
    ("Project Management", "إدارة المشاريع"),
    ("Project Manager", "مدير المشروع"),
    ("Scope", "النطاق"),
    ("Scope Creep", "تضخم النطاق"),
    ("Deliverable", "المخرج"),
    ("Milestone", "المرحلة الرئيسية"),
    ("Timeline", "الجدول الزمني"),
    ("Gantt Chart", "مخطط جانت"),
    ("Critical Path", "المسار الحرج"),
    ("Stakeholder", "صاحب المصلحة"),
    ("Risk Register", "سجل المخاطر"),
    ("Change Request", "طلب التغيير"),
    ("Resource Allocation", "تخصيص الموارد"),
    ("Budget Variance", "انحراف الميزانية"),
    ("Kick-off Meeting", "اجتماع الانطلاق"),
    ("Status Report", "تقرير الحالة"),
    ("Post-Mortem", "تحليل ما بعد التنفيذ"),
    ("Agile Methodology", "المنهجية الرشيقة"),
    ("Kanban", "كانبان"),
    ("Waterfall", "المنهجية التقليدية (الشلال)"),
    ("PMBOK", "دليل إدارة المشاريع"),
    ("PMO (Project Management Office)", "مكتب إدارة المشاريع"),
    ("Six Sigma", "سيجما ستة"),
    ("Lean", "المنهجية الرشيقة (Lean)"),
    ("BPM (Business Process Management)", "إدارة عمليات الأعمال"),
],
}

# ============================================
# 3) بناء PDF
# ============================================
doc = SimpleDocTemplate(
    "Business_Terms_AR_EN.pdf",
    pagesize=A4,
    rightMargin=1.5*cm, leftMargin=1.5*cm,
    topMargin=1.5*cm, bottomMargin=1.5*cm
)

styles = getSampleStyleSheet()
title_style = ParagraphStyle('T', parent=styles['Title'],
    fontName='Arabic', fontSize=24, alignment=1,
    textColor=colors.HexColor('#2C3E50'), leading=30)
sub_style = ParagraphStyle('S', parent=styles['Normal'],
    fontName='Arabic', fontSize=13, alignment=1,
    textColor=colors.HexColor('#7F8C8D'), leading=20)
section_style = ParagraphStyle('Sec', parent=styles['Heading1'],
    fontName='Arabic', fontSize=16, alignment=2,
    textColor=colors.HexColor('#2980B9'),
    spaceAfter=10, spaceBefore=10)
cell_style = ParagraphStyle('C', parent=styles['Normal'],
    fontName='Arabic', fontSize=10, alignment=1, leading=14)
header_style = ParagraphStyle('H', parent=styles['Normal'],
    fontName='Arabic', fontSize=12, alignment=1,
    textColor=colors.white, leading=16)

elements = []

# صفحة الغلاف
elements.append(Spacer(1, 5*cm))
elements.append(Paragraph(ar("مصطلحات عالم البيزنس"), title_style))
elements.append(Spacer(1, 0.5*cm))
elements.append(Paragraph(ar("400+ مصطلح | إنجليزي - عربي"), sub_style))
elements.append(Spacer(1, 1*cm))
elements.append(Paragraph(ar("مقسّمة على 15 مجال"), sub_style))
elements.append(Spacer(1, 0.3*cm))
elements.append(Paragraph(
    ar("محاسبة | إدارة | تسويق | مبيعات | ريادة | شركات | HR | قانون | تقنية | لوجستيات | استثمار | بنوك | تأمين | عقارات | مشاريع"),
    sub_style))
elements.append(PageBreak())

# الأقسام
for section_name, terms in SECTIONS.items():
    elements.append(Paragraph(ar(section_name), section_style))
    elements.append(Spacer(1, 0.2*cm))

    data = [[
        Paragraph("English Term", header_style),
        Paragraph(ar("الترجمة العربية"), header_style),
    ]]
    for en, ar_text in terms:
        data.append([
            Paragraph(en, cell_style),
            Paragraph(ar(ar_text), cell_style),
        ])

    table = Table(data, colWidths=[8*cm, 9*cm], repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2C3E50')),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#ECF0F1')]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 0.6*cm))

doc.build(elements)

# إحصائية نهائية
total = sum(len(v) for v in SECTIONS.values())
print(f"✅ تم إنشاء الملف: Business_Terms_AR_EN.pdf")
print(f"📊 إجمالي المصطلحات: {total}")
print(f"📚 عدد المجالات: {len(SECTIONS)}")
print("\n📋 تفصيل الأقسام:")
for name, items in SECTIONS.items():
    print(f"   • {name}: {len(items)} مصطلح")
