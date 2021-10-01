from django.urls import path

from .views import index, by_rubric, BbCreateViews

urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('add/', BbCreateViews.as_view(), name='add'),
    path('', index, name='index'),
]