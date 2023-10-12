from rest_framework.views import APIView
import requests
from django.shortcuts import render
from rest_framework.response import Response

from .models import Questions
from .serializers import QuestionsSerializer

BASE_URL = 'http://127.0.0.1:8000/api/v1/questions'


def api_questions(request):
    context = {'title': 'API',
               'description': 'Введите POST запрос вида - {"questions_num": integer} для получения вопросов.'}
    return render(request, 'api/main_API.html', context)


def _question_to_db(answer):
    obj, created = Questions.objects.get_or_create(q_id=answer['id'])
    if obj:
        obj.question = answer['question']
        obj.answer = answer['answer']
        obj.created_at = answer['created_at']
        obj.save()
    else:
        print('Повторный запрос...')
        resp = requests.get(f'https://jservice.io/api/random?count=1').json()[0]
        obj = _question_to_db(resp)
    return obj


class QuestionViewSet(APIView):
    answers = []

    def post(self, request):
        questions_num = request.data["questions_num"]
        self.answers = requests.get(f'https://jservice.io/api/random?count={questions_num}').json()
        posts = self._handling_questions()
        resp = posts.data["posts"]["question"]
        if posts:
            return Response(resp)
        else:
            return Response({})

    def _handling_questions(self):
        obj = {}
        for answer in self.answers:
            obj = _question_to_db(answer)
        return Response({'posts': QuestionsSerializer(obj, many=False).data})

