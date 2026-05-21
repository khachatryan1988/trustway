from django.contrib import admin
from .models import SiteSettings, PageContent, Stat, Service, RoutePoint, Partner, ValueItem, WorkStep, ContactRequest, FooterLink

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Brand", {"fields": ("logo_text", "logo_image", "favicon")}),
        ("Contacts", {"fields": ("phone_main", "phone_second", "phone_third", "email", "whatsapp_number", "telegram_link")}),
        ("Address", {"fields": ("address_hy", "address_ru", "address_en")}),
        ("Footer", {"fields": ("footer_text_hy", "footer_text_ru", "footer_text_en")}),
    )

@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ("key", "title_ru", "title_hy", "title_en")
    search_fields = ("key", "title_ru", "title_hy", "title_en")

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ("number", "label_ru", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("name_ru", "name_hy", "name_en")

@admin.register(RoutePoint)
class RoutePointAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "x", "y", "size", "sort_order", "is_active")
    list_editable = ("x", "y", "size", "sort_order", "is_active")

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "icon", "color", "sort_order", "is_active")
    list_editable = ("icon", "color", "sort_order", "is_active")

@admin.register(ValueItem)
class ValueItemAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")

@admin.register(WorkStep)
class WorkStepAdmin(admin.ModelAdmin):
    list_display = ("num", "name_ru", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "route", "created_at", "is_processed")
    list_filter = ("is_processed", "created_at")
    search_fields = ("name", "phone", "email", "company", "route")
    readonly_fields = ("created_at",)

@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "url", "sort_order", "is_active")
    list_editable = ("url", "sort_order", "is_active")
    search_fields = ("title_hy", "title_ru", "title_en", "url")
