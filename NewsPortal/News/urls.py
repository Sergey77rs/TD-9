from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import NewsList, OnenewsDetail, SearchList, AddCreate, NewsEdit,\
   NewsDelete, upgrade_me, CategoryListView, subscribe

urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', OnenewsDetail.as_view(), name='onenews'),
   path('search/', SearchList.as_view(), name='search'),
   path('add/', AddCreate.as_view(), name='add'),
   path('<int:pk>/edit', NewsEdit.as_view(), name='edit'),
   path('<int:pk>/delete', NewsDelete.as_view(), name='delete'),
   path('login/', LoginView.as_view(template_name='login.html'), name='login'),
   path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
   path('upgrade/', upgrade_me, name='upgrade'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]