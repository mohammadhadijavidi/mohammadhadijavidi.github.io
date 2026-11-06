#!/usr/bin/env python3
"""Generates index.html (en), fa/index.html and ar/index.html from one data source."""
import html, json, pathlib

ROOT = pathlib.Path(__file__).parent
SITE = "https://mohammadhadijavidi.github.io"
GH = "https://github.com/mohammadhadijavidi"
NAMES = ["Mohammad Hadi Javidi", "محمد هادی جاویدی", "محمد جاویدی", "هادی جاویدی",
         "Mohammad Javidi", "Hadi Javidi", "Mohammadhadi Javidi", "محمد هادي جاويدي"]

# (repo, group, en, fa, ar)
P = [
 ("modelfit","mac","Can your Mac run this AI model? Reads GGUF, safetensors and MLX headers and estimates memory per context length. Native SwiftUI + Quick Look.",
  "آیا مک تو می‌تونه این مدل هوش مصنوعی رو اجرا کنه؟ تحلیل GGUF، safetensors و MLX و تخمین رم برای هر طول کانتکست. اپ نیتیو مک.",
  "هل يستطيع جهاز Mac تشغيل هذا النموذج؟ يحلّل GGUF وsafetensors وMLX ويقدّر الذاكرة لكل طول سياق. تطبيق Mac أصلي."),
 ("underhood","mac","Everything running behind the scenes on your Mac, explained in plain English: launch agents, daemons, login items, signatures, reversible disable.",
  "هر چیزی که پشت پرده روی مک اجرا می‌شه، با زبان ساده: Launch Agentها، Daemonها، Login Itemها، امضای کد و غیرفعال‌سازی برگشت‌پذیر.",
  "كل ما يعمل في خلفية جهاز Mac بلغة بسيطة: وكلاء الإقلاع والخدمات وعناصر تسجيل الدخول والتواقيع، مع تعطيل قابل للاسترجاع."),
 ("harf","mac","Arabic text toolkit for macOS: Arabizi to Arabic, wrong keyboard layout fix, PDF Arabic repair, tashkeel and digit cleanup, in any app.",
  "ابزار متن عربی برای مک: تبدیل عربیزی به عربی، اصلاح کیبورد اشتباه، تعمیر عربی به‌هم‌ریخته‌ی PDF و پاک‌سازی اعراب، در هر اپی.",
  "أداة النص العربي على macOS: تحويل العربيزي إلى العربية، تصحيح لوحة المفاتيح، إصلاح العربية المنسوخة من PDF، وإزالة التشكيل."),
 ("agent-telegram-remote","dev","Run and supervise AI coding agents (Claude Code, Codex CLI, Aider) on your VPS from Telegram, with approval buttons and diffs.",
  "اجرا و کنترل ایجنت‌های کدنویسی هوش مصنوعی (Claude Code، Codex، Aider) روی سرور از طریق تلگرام، با دکمه‌ی تأیید و نمایش تغییرات.",
  "تشغيل وكلاء البرمجة بالذكاء الاصطناعي على خادمك والتحكم بهم من تيليجرام مع أزرار الموافقة وعرض التغييرات."),
 ("mcp-vps-toolkit","dev","Policy-gated MCP server that lets AI assistants inspect and operate a Linux server safely.",
  "سرور MCP با سیاست‌های امنیتی که به دستیارهای هوش مصنوعی اجازه می‌ده سرور لینوکس رو امن مدیریت کنن.",
  "خادم MCP محكوم بسياسات يتيح للمساعدات الذكية إدارة خادم لينكس بأمان."),
 ("prompt-regression","dev","Snapshot and regression tests for LLM prompts in CI, with an HTML diff report.",
  "تست رگرسیون و اسنپ‌شات برای پرامپت‌های مدل زبانی در CI با گزارش HTML.",
  "اختبارات الانحدار واللقطات لموجّهات النماذج اللغوية في CI مع تقرير HTML."),
 ("llm-cost-meter","dev","Drop-in proxy that meters LLM spend per project and key, with budgets, alerts and a dashboard.",
  "پراکسی که هزینه‌ی مدل‌های زبانی رو به تفکیک پروژه و کلید می‌سنجه، با بودجه، هشدار و داشبورد.",
  "وسيط يقيس تكلفة النماذج اللغوية لكل مشروع ومفتاح مع ميزانيات وتنبيهات ولوحة تحكم."),
 ("crash-to-fix","dev","iOS and Android crash logs to root cause, source line and a checked patch.",
  "تبدیل کرش‌لاگ iOS و اندروید به علت اصلی، خط کد مقصر و پچ پیشنهادی.",
  "من سجلات أعطال iOS وأندرويد إلى السبب الجذري وسطر الكود وتصحيح مقترح."),
 ("jarvis-hud","dev","Cinematic browser HUD for voice AI assistants that works with any realtime backend.",
  "رابط HUD سینمایی برای دستیارهای صوتی هوش مصنوعی در مرورگر، سازگار با هر بک‌اند ریل‌تایم.",
  "واجهة HUD سينمائية للمساعدات الصوتية في المتصفح تعمل مع أي خادم فوري."),
 ("voice-agent-starter","agents","Production-ready AI phone agent template: Twilio, STT, LLM, TTS, barge-in and tools.",
  "قالب آماده‌ی ایجنت تلفنی هوش مصنوعی: Twilio، تبدیل گفتار، مدل زبانی و ابزارها.",
  "قالب جاهز لوكيل هاتفي بالذكاء الاصطناعي: Twilio وتحويل الكلام والنموذج اللغوي والأدوات."),
 ("ai-support-inbox","agents","AI support agent and team inbox for Telegram, WhatsApp and Instagram DMs.",
  "ایجنت پشتیبانی هوش مصنوعی و اینباکس تیمی برای تلگرام، واتس‌اپ و دایرکت اینستاگرام.",
  "وكيل دعم ذكي وصندوق وارد للفريق لتيليجرام وواتساب ورسائل إنستغرام."),
 ("shorts-forge","agents","Turn long videos into ranked vertical shorts with AI highlights and captions.",
  "تبدیل ویدیوی بلند به شورت‌های عمودی با انتخاب هوشمند لحظه‌های برتر و زیرنویس.",
  "تحويل الفيديوهات الطويلة إلى مقاطع قصيرة عمودية مع أبرز اللحظات والترجمة."),
 ("mt5-ai-analyst","agents","AI trade analyst for MetaTrader 5 history and backtest reports.",
  "تحلیلگر هوش مصنوعی برای تاریخچه و بک‌تست متاتریدر ۵.",
  "محلل تداول بالذكاء الاصطناعي لسجلات MetaTrader 5 وتقارير الاختبار."),
 ("rag-farsi","fa","Chat with Persian documents (PDF, Word): Persian RAG with hybrid search and citations.",
  "چت با اسناد فارسی (PDF و Word): RAG فارسی با جست‌وجوی ترکیبی و ارجاع به منبع.",
  "الدردشة مع المستندات الفارسية: RAG فارسي مع بحث هجين واستشهادات."),
 ("zirnevis-ai","fa","Automatic Persian subtitles with Whisper and RTL-correct burn-in.",
  "زیرنویس خودکار فارسی با Whisper و سوزاندن درست راست‌به‌چپ.",
  "ترجمة فارسية تلقائية بـ Whisper مع حرق صحيح من اليمين لليسار."),
 ("tarjome-srt","fa","AI subtitle translation to Persian with exact timing and a glossary.",
  "ترجمه‌ی هوشمند زیرنویس به فارسی با حفظ دقیق تایمینگ و واژه‌نامه.",
  "ترجمة الترجمات إلى الفارسية بالذكاء الاصطناعي مع الحفاظ على التوقيت."),
 ("prompts-fa","fa","Persian prompt library for business with a searchable site.",
  "کتابخانه‌ی پرامپت فارسی برای کسب‌وکار، با سایت جست‌وجوپذیر.",
  "مكتبة موجّهات فارسية للأعمال مع موقع قابل للبحث."),
 ("support-userbot-fa","fa","Persian AI support assistant for Telegram that answers from a knowledge file.",
  "دستیار پشتیبانی فارسی برای تلگرام که از فایل دانش جواب می‌ده.",
  "مساعد دعم فارسي لتيليجرام يجيب من ملف المعرفة."),
 ("voice-note-bot-fa","fa","Telegram bot that turns Persian voice notes into text, summaries and to-dos.",
  "ربات تلگرام برای تبدیل ویس فارسی به متن، خلاصه و لیست کارها.",
  "بوت تيليجرام يحوّل الرسائل الصوتية الفارسية إلى نص وملخص ومهام."),
 ("call-agent-fa","fa","Persian-speaking AI phone agent for bookings and orders with Telegram summaries.",
  "ایجنت تلفنی فارسی‌زبان برای نوبت‌دهی و سفارش با خلاصه در تلگرام.",
  "وكيل هاتفي ناطق بالفارسية للحجوزات والطلبات مع ملخص في تيليجرام."),
 ("trade-journal-fa","fa","Persian trading journal with Jalali dates and grounded AI review.",
  "ژورنال ترید فارسی با تاریخ شمسی و بازبینی هوش مصنوعی.",
  "دفتر تداول فارسي بالتقويم الهجري الشمسي ومراجعة ذكية."),
 ("ocr-fa","fa","Persian invoice and receipt OCR to validated JSON.",
  "استخراج فاکتور و رسید فارسی به JSON معتبر.",
  "استخراج الفواتير والإيصالات الفارسية إلى JSON موثّق."),
 ("fa-llm-eval","fa","Open benchmark for language models on Persian tasks.",
  "بنچمارک باز مدل‌های زبانی روی تسک‌های فارسی.",
  "معيار مفتوح لتقييم النماذج اللغوية في المهام الفارسية."),
 ("arabic-rag","ar","Arabic RAG that understands hamza variants and Gulf dialect, with cited answers.",
  "RAG عربی که همزه‌ها و لهجه‌ی خلیجی رو می‌فهمه، با ارجاع به منبع.",
  "منصة RAG عربية تفهم الهمزات واللهجة الخليجية مع استشهاد بالمصادر."),
 ("whatsapp-agent-ar","ar","Arabic AI agent on the official WhatsApp Cloud API for UAE businesses.",
  "ایجنت هوش مصنوعی عربی روی API رسمی واتس‌اپ برای کسب‌وکارهای امارات.",
  "وكيل ذكاء اصطناعي عربي على واجهة WhatsApp Cloud الرسمية لأعمال الإمارات."),
 ("gulf-dialect-translator","ar","Emirati/Gulf Arabic, Modern Standard Arabic and English translator.",
  "مترجم لهجه‌ی اماراتی و خلیجی، عربی فصیح و انگلیسی.",
  "مترجم اللهجة الإماراتية والخليجية والفصحى والإنجليزية."),
 ("uae-vat-invoice-ai","ar","Invoice extraction with UAE 5% VAT and TRN checks.",
  "استخراج فاکتور با بررسی مالیات ۵٪ و شماره‌ی مالیاتی امارات.",
  "استخراج الفواتير مع التحقق من ضريبة القيمة المضافة 5% والرقم الضريبي."),
 ("arabic-subtitle-ai","ar","Arabic and Gulf dialect subtitles with RTL-correct burn-in.",
  "زیرنویس عربی و لهجه‌ی خلیجی با سوزاندن درست راست‌به‌چپ.",
  "ترجمة عربية ولهجة خليجية مع حرق صحيح من اليمين لليسار."),
 ("ar-llm-eval","ar","Open benchmark for language models in Arabic and Gulf dialect.",
  "بنچمارک باز مدل‌های زبانی به عربی و لهجه‌ی خلیجی.",
  "معيار مفتوح لتقييم النماذج اللغوية بالعربية واللهجة الخليجية."),
 ("arabic-content-studio","ar","Arabic social media content studio with a UAE occasions calendar.",
  "استودیوی محتوای عربی برای شبکه‌های اجتماعی با تقویم مناسبت‌های امارات.",
  "استوديو محتوى عربي للتواصل الاجتماعي مع تقويم المناسبات الإماراتية."),
 ("listing-writer-ae","ar","Bilingual Dubai property listing writer with DLD/RERA checks.",
  "نویسنده‌ی آگهی املاک دوزبانه برای دبی با بررسی قوانین DLD و RERA.",
  "كاتب إعلانات عقارية ثنائي اللغة لدبي مع فحص متطلبات DLD وRERA."),
 ("voice-agent-ar","ar","Arabic Gulf-dialect AI phone agent for restaurants and clinics.",
  "ایجنت تلفنی عربی با لهجه‌ی خلیجی برای رستوران‌ها و کلینیک‌ها.",
  "وكيل صوتي عربي باللهجة الخليجية للمطاعم والعيادات."),
 ("cv-tailor-gcc","ar","Tailor Arabic/English CVs to GCC job ads without inventing experience.",
  "تطبیق رزومه‌ی عربی/انگلیسی با آگهی‌های شغلی خلیج بدون جعل سابقه.",
  "تكييف السيرة الذاتية مع وظائف الخليج دون اختلاق خبرات."),
 ("rtl-burn","dev","Burn Persian, Arabic, Urdu and Hebrew subtitles with ffmpeg without broken punctuation.",
  "سوزاندن زیرنویس فارسی، عربی، اردو و عبری با ffmpeg بدون به‌هم‌ریختگی.",
  "حرق الترجمات الفارسية والعربية والأردية والعبرية بـ ffmpeg دون أخطاء."),
]

T = {
 "en": dict(dir="ltr", path="", lang="en",
   title="Mohammad Hadi Javidi (محمد هادی جاویدی) — AI products & macOS apps, Dubai",
   desc="Mohammad Hadi Javidi (محمد هادی جاویدی, Mohammad Javidi, Hadi Javidi) is an AI product builder and iOS/macOS developer in Dubai. 34 open-source projects: Mac apps, AI agents, RAG and Persian and Arabic AI tools.",
   eyebrow="AI products · macOS & iOS · Dubai",
   aka="Also written as محمد هادی جاویدی · Mohammad Javidi · Hadi Javidi",
   lead="I build AI products, native Apple apps and automation from Dubai: voice agents, RAG systems, support bots, developer tools and trading analytics, in English, Persian and Arabic. Everything below is free and open source.",
   s1="open-source projects", s2="languages: EN, FA, AR", s3="native Mac apps",
   b1="GitHub profile", b2="Mac apps",
   groups={"mac":("Native Mac apps","Built with SwiftUI. Free downloads on GitHub Releases."),
           "dev":("AI developer tools","For engineers building with LLMs and agents."),
           "agents":("AI agents for business","Phone, chat and video automation."),
           "fa":("Persian AI","Open-source AI tools for Persian (Farsi)."),
           "ar":("Arabic AI","Open-source AI tools for Arabic and the Gulf.")},
   about_h="About", about="Mohammad Hadi Javidi is an indie developer and founder based in Dubai. He shipped Technicalist, an AI trading analysis app for iOS and Android, and builds AI agents, automation systems, web platforms and native Apple apps. His open-source work focuses on practical AI tools and on languages that mainstream AI handles poorly, especially Persian and Arabic.",
   foot="Built by Mohammad Hadi Javidi. Projects are MIT-licensed.", idx=2),
 "fa": dict(dir="rtl", path="fa/", lang="fa",
   title="محمد هادی جاویدی (Mohammad Hadi Javidi) | سازنده‌ی محصولات هوش مصنوعی و اپ مک، دبی",
   desc="محمد هادی جاویدی (محمد جاویدی، هادی جاویدی) سازنده‌ی محصولات هوش مصنوعی و برنامه‌نویس iOS و مک در دبی. ۳۴ پروژه‌ی متن‌باز: اپ مک، ایجنت هوش مصنوعی، RAG و ابزارهای هوش مصنوعی فارسی و عربی.",
   eyebrow="هوش مصنوعی · مک و iOS · دبی",
   aka="Mohammad Hadi Javidi · محمد جاویدی · هادی جاویدی",
   lead="محمد هادی جاویدی هستم. از دبی محصولات هوش مصنوعی، اپ‌های نیتیو اپل و سیستم‌های اتوماسیون می‌سازم: ایجنت تلفنی، RAG، ربات پشتیبانی، ابزار برنامه‌نویسی و تحلیل ترید، به سه زبان انگلیسی، فارسی و عربی. همه‌ی پروژه‌های زیر رایگان و متن‌بازن.",
   s1="پروژه‌ی متن‌باز", s2="زبان: انگلیسی، فارسی، عربی", s3="اپ نیتیو مک",
   b1="پروفایل گیتهاب", b2="اپ‌های مک",
   groups={"mac":("اپ‌های نیتیو مک","ساخته‌شده با SwiftUI، دانلود رایگان از GitHub."),
           "fa":("هوش مصنوعی فارسی","ابزارهای متن‌باز هوش مصنوعی برای زبان فارسی."),
           "dev":("ابزارهای برنامه‌نویسی هوش مصنوعی","برای مهندس‌هایی که با مدل‌های زبانی و ایجنت کار می‌کنن."),
           "agents":("ایجنت‌های هوش مصنوعی برای کسب‌وکار","اتوماسیون تلفن، چت و ویدیو."),
           "ar":("هوش مصنوعی عربی","ابزارهای متن‌باز هوش مصنوعی برای عربی و کشورهای خلیج.")},
   about_h="درباره‌ی من", about="محمد هادی جاویدی برنامه‌نویس مستقل و بنیان‌گذار ساکن دبیه. اپ Technicalist، یه اپ تحلیل ترید با هوش مصنوعی برای iOS و اندروید، رو ساخته و منتشر کرده و ایجنت‌های هوش مصنوعی، سیستم‌های اتوماسیون، پلتفرم‌های وب و اپ‌های نیتیو اپل می‌سازه. تمرکز کارهای متن‌بازش روی ابزارهای کاربردی هوش مصنوعی و زبان‌هاییه که هوش مصنوعی رایج ضعیف پشتیبانی‌شون می‌کنه، مخصوصاً فارسی و عربی.",
   foot="ساخته‌ی محمد هادی جاویدی. پروژه‌ها با لایسنس MIT منتشر شدن.", idx=3),
 "ar": dict(dir="rtl", path="ar/", lang="ar",
   title="محمد هادي جاويدي (Mohammad Hadi Javidi) | منتجات الذكاء الاصطناعي وتطبيقات Mac، دبي",
   desc="محمد هادي جاويدي مطوّر منتجات ذكاء اصطناعي وتطبيقات iOS وmacOS في دبي. 34 مشروعاً مفتوح المصدر: تطبيقات Mac ووكلاء ذكاء اصطناعي وأدوات للعربية والفارسية.",
   eyebrow="الذكاء الاصطناعي · macOS وiOS · دبي",
   aka="Mohammad Hadi Javidi · محمد هادی جاویدی",
   lead="أبني من دبي منتجات الذكاء الاصطناعي وتطبيقات Apple الأصلية وأنظمة الأتمتة: وكلاء صوتيون، أنظمة RAG، روبوتات دعم، أدوات للمطورين وتحليلات التداول، بالإنجليزية والفارسية والعربية. جميع المشاريع أدناه مجانية ومفتوحة المصدر.",
   s1="مشروعاً مفتوح المصدر", s2="لغات: الإنجليزية والفارسية والعربية", s3="تطبيقات Mac أصلية",
   b1="الملف على GitHub", b2="تطبيقات Mac",
   groups={"mac":("تطبيقات Mac الأصلية","مبنية بـ SwiftUI، تنزيل مجاني من GitHub."),
           "ar":("الذكاء الاصطناعي بالعربية","أدوات مفتوحة المصدر للعربية ودول الخليج."),
           "agents":("وكلاء الذكاء الاصطناعي للأعمال","أتمتة الهاتف والدردشة والفيديو."),
           "dev":("أدوات المطورين","للمهندسين الذين يعملون مع النماذج اللغوية والوكلاء."),
           "fa":("الذكاء الاصطناعي بالفارسية","أدوات مفتوحة المصدر للغة الفارسية.")},
   about_h="نبذة", about="محمد هادي جاويدي مطوّر مستقل ومؤسس مقيم في دبي. أطلق تطبيق Technicalist لتحليل التداول بالذكاء الاصطناعي على iOS وأندرويد، ويبني وكلاء الذكاء الاصطناعي وأنظمة الأتمتة ومنصات الويب وتطبيقات Apple الأصلية. يركّز عمله المفتوح المصدر على أدوات عملية وعلى اللغات التي لا تخدمها أدوات الذكاء الاصطناعي الشائعة جيداً، خصوصاً العربية والفارسية.",
   foot="من إعداد محمد هادي جاويدي. المشاريع مرخّصة بموجب MIT.", idx=4),
}

def e(s): return html.escape(s, quote=True)

def page(code):
    t = T[code]; prefix = "../" if t["path"] else ""
    url = SITE + "/" + t["path"]
    ld = {"@context":"https://schema.org","@type":"Person","name":"Mohammad Hadi Javidi",
          "alternateName":NAMES,"url":SITE+"/","image":SITE+"/assets/og.png",
          "jobTitle":"AI Product Builder and iOS/macOS Developer",
          "homeLocation":{"@type":"Place","name":"Dubai, United Arab Emirates"},
          "knowsLanguage":["en","fa","ar"],"sameAs":[GH],
          "knowsAbout":["Artificial intelligence","AI agents","Retrieval-augmented generation","SwiftUI","macOS","iOS","Persian NLP","Arabic NLP","Automation"]}
    langs = "".join(f'<a href="{prefix}{T[c]["path"]}" hreflang="{c}"{" aria-current=\"page\"" if c==code else ""}>{lbl}</a>'
                    for c,lbl in (("en","EN"),("fa","فارسی"),("ar","العربية")))
    order = ["mac","dev","agents","fa","ar"] if code=="en" else list(t["groups"].keys())
    secs = []
    for g in order:
        h, sub = t["groups"][g]
        items = [p for p in P if p[1]==g]
        cards = []
        for repo,_,en,fa,ar in items:
            d = {"en":en,"fa":fa,"ar":ar}[code]
            link = f"{GH}/{repo}"
            if g=="mac":
                cards.append(f'<a class="card" href="{link}"><img loading="lazy" src="https://raw.githubusercontent.com/mohammadhadijavidi/{repo}/main/assets/hero.png" alt="{e(repo)} screenshot"><div class="in"><h3>{e(repo)}</h3><p>{e(d)}</p></div></a>')
            else:
                cards.append(f'<a class="card" href="{link}"><h3>{e(repo)}</h3><p>{e(d)}</p></a>')
        cls = "grid feature" if g=="mac" else "grid"
        secs.append(f'<section id="{g}"><div class="wrap"><h2>{e(h)}</h2><p class="sub">{e(sub)}</p><div class="{cls}">{"".join(cards)}</div></div></section>')
    alt = "".join(f'<link rel="alternate" hreflang="{c}" href="{SITE}/{T[c]["path"]}">' for c in T) + f'<link rel="alternate" hreflang="x-default" href="{SITE}/">'
    return f'''<!doctype html>
<html lang="{t["lang"]}" dir="{t["dir"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["desc"])}">
<meta name="author" content="Mohammad Hadi Javidi">
<link rel="canonical" href="{url}">
{alt}
<meta property="og:type" content="profile">
<meta property="og:title" content="{e(t["title"])}">
<meta property="og:description" content="{e(t["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{prefix}assets/style.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<header class="top"><div class="wrap"><a class="brand" href="{prefix}{t["path"]}">{"Mohammad Hadi Javidi" if code=="en" else ("محمد هادی جاویدی" if code=="fa" else "محمد هادي جاويدي")}</a><nav class="langs">{langs}</nav></div></header>
<main>
<section class="hero"><div class="wrap">
<div class="eyebrow">{e(t["eyebrow"])}</div>
<h1>{"Mohammad Hadi Javidi" if code=="en" else ("محمد هادی جاویدی" if code=="fa" else "محمد هادي جاويدي")}</h1>
<p class="aka">{e(t["aka"])}</p>
<p class="lead">{e(t["lead"])}</p>
<div class="stats"><div class="stat"><b>{len(P)}</b><span>{e(t["s1"])}</span></div><div class="stat"><b>3</b><span>{e(t["s2"])}</span></div><div class="stat"><b>3</b><span>{e(t["s3"])}</span></div></div>
<div class="cta"><a class="btn primary" href="{GH}">{e(t["b1"])}</a><a class="btn" href="#mac">{e(t["b2"])}</a></div>
</div></section>
{"".join(secs)}
<section class="about"><div class="wrap"><h2>{e(t["about_h"])}</h2><p>{e(t["about"])}</p></div></section>
</main>
<footer><div class="wrap"><span>{e(t["foot"])}</span><a href="{GH}">github.com/mohammadhadijavidi</a></div></footer>
</body>
</html>
'''

for code, t in T.items():
    out = ROOT / t["path"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(code), encoding="utf-8")

urls = "".join(f"<url><loc>{SITE}/{T[c]['path']}</loc>" + "".join(f'<xhtml:link rel="alternate" hreflang="{d}" href="{SITE}/{T[d]["path"]}"/>' for d in T) + "</url>" for c in T)
(ROOT/"sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">{urls}</urlset>\n', encoding="utf-8")
(ROOT/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
print("built", len(P), "projects")
