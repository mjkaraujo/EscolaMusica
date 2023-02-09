from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('', include('posts.urls')),
    path('', include('django.contrib.auth.urls')),
    path('fotos/', include('fotos.urls')),
    path('alunos/', include('alunos.urls')),
    path('professores/', include('professores.urls')),
    path('mensalidades/', include('mensalidades.urls')),
    path("admin/", admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    