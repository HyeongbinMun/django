from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'play'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('download/<int:game_id>/', views.download, name='download'),
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)