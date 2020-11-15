from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Load static files

    path('admin/', admin.site.urls),
    path('', include(('cvmaker.urls', 'cvmaker'), namespace='cvmaker')),
]
