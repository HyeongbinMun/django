from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Category, Game_images
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import GameForm, ImageForm, CategoryForm, ImageFormSet
import urllib, os, mimetypes
from django.http import HttpResponse, Http404

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
    form = ImageFormSet()
    category = CategoryForm()
    context = {'game' : game, 'form' : form, 'category' : category}
    return render(request, 'play/play_detail.html', context)

def create(request):
    if request.method == 'POST':
        game = GameForm(request.POST, request.FILES)
        if game.is_valid():
            play = game.save(commit=False)
            play.create_date = timezone.now()
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

def download(reqeust, game_id):
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




