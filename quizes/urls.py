from django.urls import path
from .views import (
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
    result_quiz_view
)

app_name = 'quizes'

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz-list'),
    path('<uuid:pk>/', quiz_view, name='quiz-view'),
    path('<uuid:pk>/save/', save_quiz_view, name='save-view'),
    path('<uuid:pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('<uuid:pk>/result/', result_quiz_view, name='result-quiz-view'),

]
