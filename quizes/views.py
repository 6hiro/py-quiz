import json
from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from questions.models import Question, Answer
from results.models import Result


class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/quizlist.html'


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizes/quiz.html', {'obj': quiz, 'pk': pk})


def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    # 問題のリスト
    questions = []
    for q in quiz.get_questions():
        # 問題の選択肢のリスト
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })


def result_quiz_view(request, pk):
    print(request.POST)
    for p in request.POST:
        print(p)
    return render(request, 'quizes/result.html')


def save_quiz_view(request, pk):
    data = json.loads(request.body)
    q_texts = data.keys()

    # 正しい答えのリスト
    answers = list(Answer.objects.filter(
        question__text__in=data.keys(), correct=True).values_list('question__text', 'text'))
    # 辞書型に変更
    answers_ = {}
    for answer in answers:
        answers_[str(answer[0])] = answer[1]
    # 結果のリスト
    result = []
    for q_text in q_texts:
        if data[q_text] == answers_[q_text]:
            result.append({
                "question": q_text,
                "correct_answer": answers_[q_text],
                "answer": data[q_text],
                "correct": "正解"

            })
        else:
            if data[q_text] is None:
                result.append({
                    "question": q_text,
                    "correct_answer": answers_[q_text],
                    "answer": data[q_text],
                    "correct": "回答なし"
                })
            else:
                result.append({
                    "question": q_text,
                    "correct_answer": answers_[q_text],
                    "answer": data[q_text],
                    "correct": "不正解"
                })
    print(result)

    # if request.user.is_authenicated:
    #     print(request.user)
    #     quiz = Quiz.objects.get(pk=pk)
    #     score_ = score * multiplier
    #     Result.objects.create(quiz=quiz, user=request.user, score=score_)

    return JsonResponse({'data': result})
    # return render(request, 'quizes/result.html', {"obj": result})
