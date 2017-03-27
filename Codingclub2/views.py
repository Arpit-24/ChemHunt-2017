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


def main(request):
    return HttpResponseRedirect('/accounts/login')

