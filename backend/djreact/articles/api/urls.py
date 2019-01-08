from django.conf.urls import url, include
from .views import ArticleListView, ArticleDetailtView


urlpatterns = [
    url('', ArticleListView.as_view()),
    url('<pk>', ArticleDetailtView.as_view())

]
