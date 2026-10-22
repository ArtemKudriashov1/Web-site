# -*- coding: utf-8 -*-
"""Сборка статического сайта KAPM. Запуск: python3 tools/build.py (из корня репозитория).
Контент — в tools/content_ru.py (и content_en.py / content_uz.py, когда появятся)."""
import pathlib, importlib, json, html, sys, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

KA = "M0 100V0H25.71V40.14L60.57 0H88.57L51.43 41.14L91.43 100H61.43L34 57.86L25.71 67V100Z M99.86 100 136.43 0H162.14L198.57 100H171.43L164.57 80.86H131.14L124.29 100ZM138.43 61.14H157.29L147.86 31.43Z"
PM = "M262.14 100V0H302.86Q316.86 0 325.86 4.07Q334.86 8.14 339.21 15.79Q343.57 23.43 343.57 34.14Q343.57 44.71 339.21 52.43Q334.86 60.14 325.86 64.21Q316.86 68.29 302.86 68.29H287.86V100ZM287.86 47.14H300Q309.86 47.14 313.86 43.86Q317.86 40.57 317.86 34.14Q317.86 27.71 313.86 24.43Q309.86 21.14 300 21.14H287.86Z M360.71 100V0H387L414.71 50.71L442.14 0H467.86V100H442.14V42.71L421.43 80.71H407.14L386.43 42.71V100Z"
K_MARK = "M0 100V0H25.71V40.14L60.57 0H88.57L51.43 41.14L91.43 100H61.43L34 57.86L25.71 67V100Z"

def logo_svg(ka, acc, cls=""):
    return (f'<svg class="logo {cls}" viewBox="0 0 467.86 100" role="img" aria-label="KAPM">'
            f'<path fill="{ka}" d="{KA}"/><rect fill="{acc}" x="227.14" y="0" width="6.43" height="100"/><path fill="{acc}" d="{PM}"/></svg>')

def write_logos():
    d = ROOT / "assets/logo"; d.mkdir(parents=True, exist_ok=True)
    variants = {"kapm-logo-primary.svg": ("#0A1F44", "#0F57D8"), "kapm-logo-reversed.svg": ("#FFFFFF", "#6FB8F5"),
                "kapm-logo-white.svg": ("#FFFFFF", "#FFFFFF"), "kapm-logo-navy.svg": ("#0A1F44", "#0A1F44")}
    for name, (ka, acc) in variants.items():
        (d / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 467.86 100" role="img" aria-labelledby="t"><title id="t">KAPM</title><path fill="{ka}" d="{KA}"/><rect fill="{acc}" x="227.14" y="0" width="6.43" height="100"/><path fill="{acc}" d="{PM}"/></svg>', encoding="utf-8")
    fav = ROOT / "favicon"; fav.mkdir(exist_ok=True)
    (fav / "favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" fill="#0A1F44"/><g transform="translate(14 25) scale(0.5)">'
        f'<path fill="#fff" d="{K_MARK}"/><rect fill="#6FB8F5" x="113" y="0" width="9" height="100"/></g></svg>', encoding="utf-8")

# ---------- шаблон страницы ----------
def page(lang, L, c, p):
    """lang: 'ru'|'en'|'uz'; L: словарь общих строк; c: контент сайта; p: dict страницы"""
    prefix = "" if lang == "ru" else f"/{lang}"
    def u(path): return f"{prefix}{path}"
    nav = "".join(f'<a href="{u(h)}"{" class=on" if p.get("nav")==k else ""}>{t}</a>' for k, h, t in L["nav"])
    alts = "".join(f'<link rel="alternate" hreflang="{lg}" href="{c["site"]}{("" if lg=="ru" else "/"+lg)}{p["path"]}">' for lg in c["langs"])
    langsw = "".join(f'<a href="{("" if lg=="ru" else "/"+lg)}{p["path"]}"{" class=on" if lg==lang else ""}>{lg.upper()}</a>' for lg in c["langs"])
    canon = f'{c["site"]}{prefix}{p["path"]}'
    ld = p.get("ld") or []
    ldjson = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    og_img = c["site"] + "/assets/img/og.jpg"
    foot_services = "".join(f'<a href="{u(h)}">{t}</a>' for h, t in L["foot_services"])
    foot_company = "".join(f'<a href="{u(h)}">{t}</a>' for h, t in L["foot_company"])
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(p["title"])}</title>
<meta name="description" content="{html.escape(p["desc"])}">
<link rel="canonical" href="{canon}">
{alts}
<meta property="og:type" content="website"><meta property="og:site_name" content="KAPM"><meta property="og:title" content="{html.escape(p["title"])}"><meta property="og:description" content="{html.escape(p["desc"])}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{og_img}"><meta property="og:locale" content="{L["locale"]}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon/favicon.svg" type="image/svg+xml"><link rel="manifest" href="/favicon/site.webmanifest"><meta name="theme-color" content="#0A1F44">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="/assets/site.css?v={c["build"]}">
{ldjson}
</head>
<body>
<a class="skip" href="#main">{L["skip"]}</a>
<header class="hdr"><div class="wrap">
<a class="brand" href="{u("/")}" aria-label="KAPM">{logo_svg("#0A1F44","#0F57D8")}</a>
<nav class="nav" aria-label="{L["nav_label"]}">{nav}</nav>
<div class="hdr-r"><div class="langs">{langsw}</div><a class="btn btn-sm" href="{u("/contact/")}">{L["cta_short"]}</a>
<button class="burger" type="button" aria-label="{L["menu"]}" aria-expanded="false" aria-controls="mnav"><span></span><span></span><span></span></button></div>
</div>
<nav id="mnav" class="mnav" aria-label="{L["nav_label"]}">{nav}<div class="langs">{langsw}</div></nav>
</header>
<main id="main">
{p["body"]}
{"" if p.get("nocta") else f'''<section class="cta"><div class="wrap cta-in"><div><h2>{p.get("cta_h", L["cta_h"])}</h2><p>{L["cta_p"]}</p></div><div class="cta-act"><a class="btn" href="{u("/contact/")}">{L["cta_btn"]}</a><a class="tel" href="tel:+998910040152">+998 91 004 0152</a></div></div></section>'''}
</main>
<footer class="ftr"><div class="wrap">
<div class="ftr-grid">
<div class="ftr-col"><a href="{u("/")}" aria-label="KAPM">{logo_svg("#FFFFFF","#6FB8F5")}</a><p class="muted">{L["foot_tag"]}</p><p class="muted">{c["address_short"]}<br><a href="tel:+998910040152">+998 91 004 0152</a><br><a href="mailto:{c["email"]}">{c["email"]}</a></p></div>
<div class="ftr-col"><span class="ftr-h">{L["foot_services_h"]}</span>{foot_services}</div>
<div class="ftr-col"><span class="ftr-h">{L["foot_company_h"]}</span>{foot_company}</div>
<div class="ftr-col"><span class="ftr-h">{L["foot_contact_h"]}</span><a href="{c["linkedin"]}" rel="noopener">LinkedIn</a><a href="https://t.me/+998910040152" rel="noopener">Telegram</a><a href="https://wa.me/998910040152" rel="noopener">WhatsApp</a><div class="langs">{langsw}</div></div>
</div>
<div class="ftr-b"><span>© {datetime.date.today().year} {c["legal_name"]} · {L["inn"]} {c["inn"]}</span><a href="{u("/privacy/")}">{L["privacy"]}</a></div>
</div></footer>
<div class="cookie" id="cookie" hidden><p>{L["cookie"]} <a href="{u("/privacy/")}">{L["privacy"]}</a>.</p><div><button type="button" class="btn btn-sm" data-c="1">{L["cookie_ok"]}</button><button type="button" class="btn btn-sm btn-o" data-c="0">{L["cookie_no"]}</button></div></div>
<script src="/assets/site.js?v={c["build"]}" defer></script>
</body>
</html>'''

def build_lang(lang):
    mod = importlib.import_module(f"content_{lang}")
    L, c, pages = mod.L, mod.SITE, mod.pages()
    out_root = ROOT if lang == "ru" else ROOT / lang
    urls = []
    for p in pages:
        d = out_root / p["path"].strip("/")
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(page(lang, L, c, p), encoding="utf-8")
        urls.append(("" if lang == "ru" else f"/{lang}") + p["path"])
    return c, urls

def main():
    write_logos()
    all_urls, site = [], None
    for lang in ("ru", "en", "uz"):
        if (ROOT / "tools" / f"content_{lang}.py").exists():
            c, urls = build_lang(lang); site = c["site"]; all_urls += urls
    today = datetime.date.today().isoformat()
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
        "".join(f"  <url><loc>{site}{u}</loc><lastmod>{today}</lastmod></url>\n" for u in all_urls) + "</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {site}/sitemap.xml\n", encoding="utf-8")
    print(f"built {len(all_urls)} pages")

if __name__ == "__main__":
    main()
