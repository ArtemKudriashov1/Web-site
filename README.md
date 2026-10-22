# KAPM — сайт компании

Статический сайт kapm.uz. Страницы собираются скриптом из контента:

```
python3 tools/build.py
```

- `tools/content_ru.py` — тексты и данные (услуги, секторы, проекты) на русском; `content_en.py`, `content_uz.py` — переводы.
- `tools/build.py` — шаблон страницы, логотипы, sitemap, robots.
- `assets/` — стили, скрипт, фото, логотипы; `favicon/` — иконки и манифест.
- Готовые HTML-файлы лежат в корне (`/`, `/services/...`, `/en/...`) — их не редактируют вручную, только через сборку.

Хостинг: Cloudflare Pages (build command — `python3 tools/build.py`, output directory — `/`), либо любой статический хостинг.

Форма заявки: endpoint задаётся в `SITE["form_action"]` (Formspree или аналог).
