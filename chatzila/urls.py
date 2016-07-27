from django.conf.urls import include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

import dashboard.views as dashboard_views
from dashboard import auth_helper
from dashboard import api

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

    # apis
    url(r'^get_logged_users/$', api.get_logged_users, name='get_logged_users'),
    url(r'^send_message/$', api.send_message, name='send_message'),
    url(r'^get_user_messages/$', api.get_user_messages, name='get_user_messages'),
    url(r'^get_all_messages_of_user/$', api.get_all_messages_of_user, name='get_all_messages_of_user'),
    url(r'^get_received_messages_of_user/$', api.get_received_messages_of_user, name='get_received_messages_of_user'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
