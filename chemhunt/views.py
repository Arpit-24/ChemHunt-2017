from django.shortcuts import render

# Create your views here.
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views import generic
from django.views.generic import View, FormView
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Player, Question
from .forms import AnswerForm








def test(request):
    return render(request, 'chemhunt/test.html')


def main(request):
    user = request.user
    try:
        up = Player()
        up.name = user
        up.save()
    except:
        up = Player.objects.get(name=user)

    return HttpResponseRedirect('/accounts/profile/index')


class IndexView(generic.ListView):
    template_name = 'chemhunt/index.html'

    def get_queryset(self):
        return Question.objects.all()


class DetailView(generic.DetailView):
    model = Question
    template_name = 'chemhunt/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_pk = self.kwargs['pk']
        product = Question.objects.get(pk=product_pk)
        context.update({
            'product': product,


        })
        return context


def detail(request, pk):
    error = False
    product = Question.objects.get(pk=pk)
    user = request.user
    up = Player.objects.get(name=user)

    if up.question_no == product.question_no:
        list1 = list(up.answers_given)
        if list1[product.question_no] == '3':
            error = True

        leaderboard = Player.objects.order_by('score').reverse()
        i = 0

        for player in leaderboard:
            if up.score == player.score:
                up.rank = i + 1
                up.save()
            else:
                i += 1
        up.save()
        s = up.answers_given.count('2')
        skips = 1 - s
        return render(request, 'chemhunt/detail.html',
                      {'product': product, 'player': up, 'skips': skips,  'error': error})
    else:
        return HttpResponseRedirect('/accounts/logout/')




def index(request):
    user = request.user
    up = Player.objects.get(name=user)

    leaderboard = Player.objects.order_by('score').reverse()
    i = 0

    for player in leaderboard:
        if up.score == player.score:
            up.rank = i + 1
            up.save()
        else:
            i += 1
    up.save()
    s = up.answers_given.count('2')
    skips = 1 - s

    return render(request, 'chemhunt/index.html', {'player': up, "skips": skips, 'leaderboard': leaderboard})






def answer(request, pk):
    question = Question.objects.get(pk=pk)
    answerof = request.POST['answerof']

    user = request.user
    up = Player.objects.get(name=user)

    leaderboard = Player.objects.order_by('score').reverse()
    i = 0

    for player in leaderboard:
        if up.score == player.score:
            up.rank = i + 1
            up.save()
        else:
            i += 1
    up.save()

    if answerof == question.solution:
        list1 = list(up.answers_given)
        list1[question.question_no] = '1'
        up.answers_given = ''.join(list1)
        up.question_no += 1
        up.save()
        error = False
    else:
        list1 = list(up.answers_given)
        list1[question.question_no] = '3'
        up.answers_given = ''.join(list1)
        up.save()
        return HttpResponseRedirect('/accounts/profile/%s/' % pk)

    c = up.answers_given.count('1')
    s = up.answers_given.count('2')
    up.score = (c * 100) - (s * 25)
    up.save()
    return HttpResponseRedirect('/accounts/profile/%s/' % up.question_no, {'error': error})


def skip(request, pk):
    question = Question.objects.get(pk=pk)
    user = request.user
    up = Player.objects.get(name=user)
    s = up.answers_given.count('2')

    if s < 1:
        list1 = list(up.answers_given)
        list1[question.question_no] = '2'
        up.answers_given = ''.join(list1)
        up.question_no += 1
        up.save()
        c = up.answers_given.count('1')
        s = up.answers_given.count('2')
        up.score = (c * 100) - (s * 25)
        up.save()
        return HttpResponseRedirect('/accounts/profile/%s/' % up.question_no)

    else:
        return HttpResponseRedirect('/accounts/profile/%s/' % pk)







