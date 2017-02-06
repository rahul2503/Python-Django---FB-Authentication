from django.conf.urls import url, include
from django.contrib import admin

from TaskApp.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', UserDetail.as_view())
]
