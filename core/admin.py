from django.utils.html import format_html
from django.contrib import admin
from .models import SiteSettings, PageContent, Stat, Service, RoutePoint, Partner, ValueItem, WorkStep, ContactRequest, FooterLink

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    readonly_fields = ("jctrans_logo_preview",)

    fieldsets = (
        ("Brand", {
            "fields": (
                "logo_text",
                "logo_image",
                "favicon",
                "jctrans_logo",
                "jctrans_logo_preview",
            )
        }),
        ("Contacts", {
            "fields": (
                "phone_main",
                "phone_second",
                "phone_third",
                "email",
                "whatsapp_number",
                "telegram_link",
            )
        }),
        ("Address", {
            "fields": (
                "address_hy",
                "address_ru",
                "address_en",
            )
        }),
        ("Footer", {
            "fields": (
                "footer_text_hy",
                "footer_text_ru",
                "footer_text_en",
            )
        }),
    )

    def jctrans_logo_preview(self, obj):
        if obj.jctrans_logo:
            return format_html(
                '<img src="{}" style="height:70px; max-width:280px; object-fit:contain; background:#0b1224; padding:10px; border-radius:10px;" />',
                obj.jctrans_logo.url
            )
        return "-"

    jctrans_logo_preview.short_description = "JCTRANS logo preview"

@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ("key", "title_ru", "title_hy", "title_en", "hero_preview", "content_preview")
    search_fields = ("key", "title_ru", "title_hy", "title_en")
    readonly_fields = ("hero_preview", "content_preview")

    fieldsets = (
        ("Page", {
            "fields": (
                "key",
                "hero_image",
                "hero_preview",
                "content_image",
                "content_preview",
            )
        }),
        ("HY", {"fields": ("title_hy", "subtitle_hy", "body_hy")}),
        ("RU", {"fields": ("title_ru", "subtitle_ru", "body_ru")}),
        ("EN", {"fields": ("title_en", "subtitle_en", "body_en")}),
    )

    def hero_preview(self, obj):
        if obj and obj.hero_image:
            return format_html(
                '<img src="{}" style="max-width:260px; max-height:140px; border-radius:10px; border:1px solid #444;" />',
                obj.hero_image.url
            )
        return "No hero image"

    hero_preview.short_description = "Hero image preview"

    def content_preview(self, obj):
        if obj and obj.content_image:
            return format_html(
                '<img src="{}" style="max-width:260px; max-height:140px; border-radius:10px; border:1px solid #444;" />',
                obj.content_image.url
            )
        return "No content image"

    content_preview.short_description = "Content image preview"

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
    list_display = ("id", "name", "logo_preview", "sort_order", "is_active")
    list_editable = ("sort_order", "is_active")
    search_fields = ("name",)
    list_filter = ("is_active",)
    readonly_fields = ("logo_preview",)

    fieldsets = (
        ("Partner", {
            "fields": (
                "name",
                "logo",
                "logo_preview",
                "icon",
                "color",
                "sort_order",
                "is_active",
            )
        }),
    )

    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="height:45px; max-width:140px; object-fit:contain; background:#0b1224; padding:6px; border-radius:8px;" />',
                obj.logo.url
            )
        return "-"

    logo_preview.short_description = "Logo"

    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="height:45px; max-width:140px; object-fit:contain; background:#0b1224; padding:6px; border-radius:8px;" />',
                obj.logo.url
            )
        return "-"

    logo_preview.short_description = "Logo"

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
