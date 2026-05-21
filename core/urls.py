from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("services/", views.services_view, name="services"),
    path("contacts/", views.contacts_view, name="contacts"),
    path("privacy/", views.privacy_view, name="privacy"),
    path("set-lang/<str:code>/", views.set_language, name="set_lang"),
]
