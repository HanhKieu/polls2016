from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Question, Choice


def index(request):
    latestQuestionList = Question.objects.order_by('-pubDate')[:5]
    context = {
        'latestQuestionList': latestQuestionList
    }
    return render(request,'polls/index.html', context)

def detail(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)

def results(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    context = {
        'question': question
    }
    return render(request, 'polls/results.html', context)

def vote(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    try:
        selectedChoice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selectedChoice.votes += 1
        selectedChoice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(questionId,)))

# Create your views here.
