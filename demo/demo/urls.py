"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import users.urls,passport.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/',include(users.urls)),
    #把路由放在总路由和子路由方式
    # url(r'^passport/',include('passport.urls')),
    #把路由全都放在总路由方式
    # url(r'^passport/index/$',passport.views.index),
    #把路由全放子路由方式
    url(r'^',include('passport.urls')),
    url(r'^',include('booktest.urls'))
]
