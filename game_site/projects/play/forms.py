from django import forms
from play.models import Game, Game_images, Category, Comment

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['subject', 'content', 'files']
        labels = {
            'subject' : '제목',
            'content' : '내용',
            'files' : '파일'
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Game_images
        fields = ['image']
        labels = {
            'image' : '게임이미지',
        }

ImageFormSet = forms.inlineformset_factory(Game, Game_images, form=ImageForm, extra=2)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['subject']
        labels = {
            'subject' : '카테고리',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content' : '내용',
        }