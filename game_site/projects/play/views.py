from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Category
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    game_list = Game.objects.order_by('-create_date')
    context = {'game_list': game_list}
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    # 조회
    game_list = Game.objects.order_by('-create_date')
    # 페이징처리
    paginator = Paginator(game_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'game_list': page_obj}
    return render(request, 'play/play_list.html', context)

def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    context = {'game' : game}
    return render(request, 'play/play_detail.html', context)