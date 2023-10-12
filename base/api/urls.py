from django.urls import path

from .views import QuestionViewSet


urlpatterns = [
    path('v1/questions', QuestionViewSet.as_view(), name='api_questions_viewSet'),
]
