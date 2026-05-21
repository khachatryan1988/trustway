from .i18n import TRANSLATIONS, LANGUAGES, DEFAULT_LANG

def language(request):
    lang = request.session.get("lang", DEFAULT_LANG)
    if lang not in TRANSLATIONS:
        lang = DEFAULT_LANG
    return {
        "lang": lang,
        "t": TRANSLATIONS[lang],
        "languages": LANGUAGES,
    }
