from django_filters import FilterSet, DateFilter, CharFilter
from .models import Post


class PostFilter(FilterSet):
    date_post = DateFilter(field_name='date_post', label='Публикации после', lookup_expr='gt')
    heading_post = CharFilter(field_name='heading_post', label='Заголовок')

    class Meta:
        model = Post
        fields = ('date_post', 'heading_post', 'author_post')
        #labels = {'author_post': ('Автор')}