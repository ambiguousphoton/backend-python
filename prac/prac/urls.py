from django.contrib import admin
from django.urls import path
from prac import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/',views.about_us),
    path('om', views.jai_ho),
    path('om/<slug:numbering>', views.diffpages),
    path("", views.homePage)
]
