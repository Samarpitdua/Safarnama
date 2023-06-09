"""safarnama URL Configuration

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
from django.urls import path
from home import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('destinations', views.index , name = "destinations"),
    path('hotels', views.hotels ,name = "hotels"),
    path('checkout', views.checkout ,name = "checkout"),
    path('signup', views.handleSignup ,name = "handleSignup"),
    path('login', views.handleLogin ,name = "handleLogin"),
    path('logout', views.handleLogout ,name = "handleLogout"),
    path('booking', views.DoBooking ,name = "DoBooking"),
    path('guides', views.guides ,name = "Guides"),
    path('checkout_guide', views.checkout_guides, name="checkout_guides"),
    # path('otp' , views.otp , name = "otp")
    
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
