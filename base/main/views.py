import requests
from django.shortcuts import render
from .forms import QuestionForm

BASE_URL = 'http://127.0.0.1:8000/api/v1/questions'


def index(request):
    form = QuestionForm()
    description = 'Запрос...'
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            questions_num = form.cleaned_data['questions_num']
            description = requests.post(f'{BASE_URL}', data={"questions_num": questions_num}).json()
        else:
            form = QuestionForm()
            description = 'Введите целое число'
    context = {'form': form,
               'description': description,
               }
    return render(request, 'main/index.html', context)

