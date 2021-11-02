from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from study.models import Study


def study_list(request):
    studies = Study.objects.all()
    context = {
        'studies': studies
    }
    return render(request, 'study/studylist.html', context)


def study_category(request, category):
    studies = Study.objects.filter(category__name=category)
    context = {
        'studies': studies
    }
    return render(request, 'study/studylist.html', context)


def study_tag(request, tag):
    studies = Study.objects.filter(tags__name=tag)
    context = {
        'studies': studies
    }
    return render(request, 'study/studylist.html', context)


def study_detail(request, pk):
    study = get_object_or_404(Study, id=pk)
    user_id = request.user.id
    is_liked = str(user_id) in [str(i.id) for i in study.liked.all()]

    print([str(i.id) for i in study.liked.all()])
    context = {
        'study': study,
        'is_liked': is_liked
    }
    # print(study.content)
    return render(request, 'study/studydetail.html', context)


@login_required
def like_study(request, pk):
    # いいねをするもしくは外すUser
    user = request.user
    try:
        # いいねされるまたは外される学習項目
        to_like = Study.objects.get(id=pk)

        if user in to_like.liked.all():
            to_like.liked.remove(user)
            to_like.save()

            return JsonResponse({'result': 'unlike'})
        else:
            to_like.liked.add(user)
            to_like.save()
            return JsonResponse({'result': 'like'})
    except Exception as e:
        print(e)
