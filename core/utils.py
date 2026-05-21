def tr(obj, field, lang):
    return getattr(obj, f"{field}_{lang}", None) or getattr(obj, f"{field}_hy", "") or ""

def split_tags(value):
    return [x.strip() for x in (value or "").split(",") if x.strip()]
