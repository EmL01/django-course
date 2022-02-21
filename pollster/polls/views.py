from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

def index(request):
    questions = Question.objects.order_by('-created')
    context = {
        'questions': questions
    }
    return render(request, 'polls/index.html', context)

def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    context = {
        'question': question
    }
    return render(request, 'polls/details.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/results.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': 'You did not select a choice'
        }
        return render(request, 'polls/details.html', context)
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))