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
    path('comment/create/<int:game_id>/', views.comment_create, name='comment_create'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('vote/game/<int:game_id>/', views.vote_game, name='vote_game')
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)