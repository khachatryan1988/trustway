import json
from datetime import datetime

from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment


def url(name, args=None, kwargs=None):
    return reverse(name, args=args or [], kwargs=kwargs or {})


def environment(**options):
    env = Environment(**options)

    env.globals.update({
        "static": static,
        "url": url,
        "current_year": datetime.now().year,
    })

    env.filters["tojson"] = lambda v: json.dumps(v, ensure_ascii=False)

    return env
