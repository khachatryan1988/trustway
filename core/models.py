from django.db import models

class SiteSettings(models.Model):
    logo_text = models.CharField(max_length=100, default="Trust Way")
    logo_image = models.FileField(upload_to="site/", blank=True, null=True)
    favicon = models.ImageField(upload_to="site/", blank=True, null=True)
    phone_main = models.CharField(max_length=50, default="+374 33 787790")
    phone_second = models.CharField(max_length=50, default="+374 043 00 33 59", blank=True)
    phone_third = models.CharField(max_length=50, default="+374 95 608020", blank=True)
    email = models.EmailField(default="logistics@trustway.am")
    address_hy = models.CharField(max_length=255, default="Երևան, Հայաստան")
    address_ru = models.CharField(max_length=255, default="Ереван, Армения")
    address_en = models.CharField(max_length=255, default="Yerevan, Armenia")
    whatsapp_number = models.CharField(max_length=50, default="37433787790")
    telegram_link = models.URLField(default="https://t.me/+37433787790")
    footer_text_hy = models.TextField(default="Միջազգային լոգիստիկ լուծումներ։")
    footer_text_ru = models.TextField(default="Международные логистические решения.")
    footer_text_en = models.TextField(default="International logistics solutions.")

    class Meta:
        verbose_name = "Site settings"
        verbose_name_plural = "Site settings"

    def __str__(self):
        return self.logo_text

class PageContent(models.Model):
    key = models.SlugField(unique=True)
    title_hy = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    subtitle_hy = models.TextField(blank=True)
    subtitle_ru = models.TextField(blank=True)
    subtitle_en = models.TextField(blank=True)
    body_hy = models.TextField(blank=True)
    body_ru = models.TextField(blank=True)
    body_en = models.TextField(blank=True)

    hero_image = models.ImageField(upload_to="pages/hero/", blank=True, null=True)
    content_image = models.ImageField(upload_to="pages/content/", blank=True, null=True)

    def __str__(self):
        return self.key

class Stat(models.Model):
    number = models.CharField(max_length=30)
    label_hy = models.CharField(max_length=100)
    label_ru = models.CharField(max_length=100)
    label_en = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, default="ti-chart-bar")
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.number

class Service(models.Model):
    icon = models.CharField(max_length=100, default="ti-truck-delivery")
    name_hy = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    desc_hy = models.TextField()
    desc_ru = models.TextField()
    desc_en = models.TextField()
    tags_hy = models.CharField(max_length=255, blank=True, help_text="Comma separated")
    tags_ru = models.CharField(max_length=255, blank=True, help_text="Comma separated")
    tags_en = models.CharField(max_length=255, blank=True, help_text="Comma separated")
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.name_ru

class RoutePoint(models.Model):
    name_hy = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)

    lat = models.FloatField(default=40.1772)
    lng = models.FloatField(default=44.5035)

    x = models.FloatField(default=500)
    y = models.FloatField(default=250)
    size = models.PositiveIntegerField(default=7)
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.name_ru

class Partner(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, default="ti-building")
    color = models.CharField(max_length=20, default="#f59e0b")
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.name

class ValueItem(models.Model):
    icon = models.CharField(max_length=100, default="ti-shield-check")
    title_hy = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    desc_hy = models.TextField()
    desc_ru = models.TextField()
    desc_en = models.TextField()
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.title_ru

class WorkStep(models.Model):
    num = models.CharField(max_length=10, default="01")
    name_hy = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    desc_hy = models.TextField()
    desc_ru = models.TextField()
    desc_en = models.TextField()
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return f"{self.num} {self.name_ru}"

class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    route = models.CharField(max_length=150, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.phone}"

class FooterLink(models.Model):
    title_hy = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)

    url = models.CharField(max_length=255, default="#")

    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Footer link"
        verbose_name_plural = "Footer links"

    def __str__(self):
        return self.title_ru
