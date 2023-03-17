from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404
from django.template import loader

from polls.models import Question


# Create your views here.

def index(request):
    # output=', '.join([q.question_text for q in latest_question_list])
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))

    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
    except Question.DoesNotExist as e:
        raise Http404("Question does not exist") from e
    # return HttpResponse(f"You're looking at question {question_id}.")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse(f"results from question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"you are voting un question {question_id}")
