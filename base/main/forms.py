from django import forms


class QuestionForm(forms.Form):
    questions_num = forms.IntegerField(label='Введите количество вопросов')