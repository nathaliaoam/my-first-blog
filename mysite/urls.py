from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'http://nathaliaoam.pythonanywhere.com/', include('blog.urls')),
    url(r'', include('blog.urls')),
]
