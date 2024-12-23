"""djangopro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type = 'text/plain')),
    path('fashion/', include('fashion.urls')),
    path('supermarket/', include('supermarket.urls')),
    path('services/', include('services.urls')),
    path('crypto/', include('crypto.urls')),
    path('food/', include('food.urls')),
    path('electronics/', include('electronics.urls')),
    path('blogs/', include('blogs.urls')),
    path('users/', include('users.urls')),
    path('', include('bluemartin.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
