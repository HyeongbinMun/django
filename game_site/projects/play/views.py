from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Category, Game_images, Comment
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import GameForm, ImageForm, CategoryForm, ImageFormSet, CommentForm
import urllib, os, mimetypes
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count

# Create your views here.
def index(request):
    game_list = Game.objects.order_by('-create_date')
    context = {'game_list': game_list}
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'recommend':
        game_list = Game.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        game_list = Game.objects.annotate(num_comment=Count('comment')).order_by('-num_comment', '-create_date')
    else:  # recent
        game_list = Game.objects.order_by('-create_date')
    if kw:
        game_list = game_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw)  # 질문 글쓴이검색
        ).distinct()
    # 페이징처리
    paginator = Paginator(game_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'game_list': page_obj, 'page': page, 'kw': kw, 'so':so}
    return render(request, 'play/play_list.html', context)

def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    context = {'game' : game}
    return render(request, 'play/play_detail.html', context)

@login_required(login_url='user:login')
def create(request):
    if request.method == 'POST':
        game = GameForm(request.POST, request.FILES)
        if game.is_valid():
            play = game.save(commit=False)
            play.create_date = timezone.now()
            play.author = request.user
            play.save()
            for img in request.FILES.getlist('imgs'):
                gimage = Game_images()
                gimage.game = play
                gimage.image = img
                gimage.save()
            for ctg in request.POST.getlist('category'):
                category = Category()
                category.game = play
                category.subject = ctg
                category.save()
        return redirect('play:index')
    else:
        game = GameForm()
    context = {'game' : game}
    return render(request, 'play/play_create.html', context)

def download(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    url = game.files.url[1:]
    file_url = urllib.parse.unquote(url)
    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            quote_file_url = urllib.parse.quote(game.subject.encode('utf-8'))
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'attachment;filename*UTF-8\'\'%s' % quote_file_url
            return response
        raise Http404

def comment_create(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_data = timezone.now()
            comment.game = game
            comment.save()
            return redirect('play:detail', game_id=game.id)
    else:
        form = CommentForm()
    context = {'game': game, 'form': form}
    return render(request, 'play/game_detail.html', context)

@login_required(login_url='user:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('play:detail', game_id=comment.game.id)

@login_required(login_url='user:login')
def vote_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    game.voter.add(request.user)
    return redirect('play:detail', game_id=game_id)
