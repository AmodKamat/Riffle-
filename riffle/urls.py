
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('customusermodel.urls')),
    path('',include('support.urls')),
    path('',include('socialmedia.urls')),
    path('',include('authentication.urls')),
    path('',include('home.urls')),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)