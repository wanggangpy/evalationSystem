from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from question import models
from question.forms import EvaluationTableForms
# Create your views here.


class Index(TemplateView):

    template_name = 'question_list.html'


class AddQuestion(CreateView):

    model = models.EvaluationTable
    form_class = EvaluationTableForms






