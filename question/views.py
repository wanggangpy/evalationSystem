from django.shortcuts import render
from django.views.generic.base import TemplateView
from question import models
# Create your views here.


class Index(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        evaluation_table = models.EvaluationTable.objects.get(id=1)
        context = super().get_context_data(**kwargs)
        context['evaluation_table'] = evaluation_table
        return context

