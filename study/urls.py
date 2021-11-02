from django.urls import path
from .views import (
    study_list,
    study_detail,
    like_study,
    study_tag,
    study_category
)

app_name = 'study'

urlpatterns = [
    path('', study_list, name='study-list'),
    path('detail/<uuid:pk>', study_detail, name='study-detail'),
    path('detail/like/<uuid:pk>', like_study, name='like'),
    path('category/<str:category>/', study_category, name='study-category'),
    path('tag/<str:tag>/', study_tag, name='study-tag'),
]
