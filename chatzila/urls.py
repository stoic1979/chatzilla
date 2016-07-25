from django.conf.urls import include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

import dashboard.views as dashboard_views
import dashboard.auth_helper

import reg.views as reg_views
import settings

urlpatterns = [
    url(r'^$', dashboard_views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),

    # login/logout
    url(r'^login/$', auth_helper.login_page, name='login_page'),
    url(r'^logout/$', auth_helper.logout_page, name='logout_page'),
    url(r'^accounts/logout/$', auth_helper.logout_page, name='logout_page'),
    url(r'^accounts/login/$', auth_helper.login_page, name='login_page'),

    # registration
    url(r'^register/$', reg_views.regform, name='regform'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
