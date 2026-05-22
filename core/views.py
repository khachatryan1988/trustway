from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from django.conf import settings
from django.core.mail import send_mail
from .i18n import TRANSLATIONS, DEFAULT_LANG
from .models import SiteSettings, PageContent, Stat, Service, RoutePoint, Partner, ValueItem, WorkStep, ContactRequest, FooterLink
from .utils import tr, split_tags
from datetime import datetime

def get_settings():
    obj, _ = SiteSettings.objects.get_or_create(id=1)
    return obj

def get_page(key):
    return PageContent.objects.filter(key=key).first()

def common_context(active_page):
    return {
        "active_page": active_page,
        "site": get_settings(),
        "footer_links": FooterLink.objects.filter(is_active=True),
    }

def home_view(request):
    ctx = common_context("home")
    ctx.update({
        "page": get_page("home"),
        "stats": Stat.objects.filter(is_active=True),
        "services": Service.objects.filter(is_active=True)[:6],
        "routes": RoutePoint.objects.filter(is_active=True),
        "partners": Partner.objects.filter(is_active=True),
    })
    return render(request, "core/home.html", ctx)

def about_view(request):
    ctx = common_context("about")
    ctx.update({
        "page": get_page("about"),
        "values": ValueItem.objects.filter(is_active=True),
    })
    return render(request, "core/about.html", ctx)

def services_view(request):
    ctx = common_context("services")
    ctx.update({
        "page": get_page("services"),
        "services_detail": Service.objects.filter(is_active=True),
        "steps": WorkStep.objects.filter(is_active=True),
    })
    return render(request, "core/services.html", ctx)

def contacts_view(request):
    ctx = common_context("contacts")
    ctx.update({"page": get_page("contacts"), "form_sent": False, "form_error": None})

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        company = request.POST.get("company", "").strip()
        phone = request.POST.get("phone", "").strip()
        email = request.POST.get("email", "").strip()
        route = request.POST.get("route", "").strip()
        message_text = request.POST.get("message", "").strip()

        if not name or not phone:
            ctx["form_error"] = "Name and phone are required"
        else:
            try:
                ContactRequest.objects.create(
                    name=name,
                    company=company,
                    phone=phone,
                    email=email,
                    route=route,
                    message=message_text,
                )

                subject = "New request from Trust Way website"

                body = f"""
New request from Trust Way website

Name: {name}
Company: {company}
Phone: {phone}
Email: {email}
Route: {route}

Message:
{message_text}
"""

                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    ["logistics@trustway.am"],
                    fail_silently=False,
                )

                ctx["form_sent"] = True

            except Exception as e:
                ctx["form_error"] = str(e)

    return render(request, "core/contacts.html", ctx)

@require_GET
def set_language(request, code):
    if code in TRANSLATIONS:
        request.session["lang"] = code
    return redirect(request.META.get("HTTP_REFERER", "/"))

def privacy_view(request):
    ctx = common_context("privacy")
    ctx.update({
        "page": get_page("privacy"),
    })
    return render(request, "core/privacy.html", ctx)
