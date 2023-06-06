from django.urls import path, include
from django.contrib import admin
from home.views import home_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('', home_view, name='home'),

    path('post/', include('post.urls')),

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)