from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('info-list/', views.userinfo, name="info-list"),
    path('', views.info, name="info"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)