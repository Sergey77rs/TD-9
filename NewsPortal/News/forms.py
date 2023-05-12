from django.forms import ModelForm
from .models import Post
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class ProductForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author_post', 'heading_post', 'text_post', 'category']
        labels = {
            'heading_post': ('Заголовок'),
            'text_post': ('Текст публикации'),
            'category': ('Категория'),
            'author_post': ('Автор публикации')
        }


class CommonSignupForm(SignupForm):

    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user