from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from question import models
from question.forms import EvaluationTableForms

from question.utils import MessageMixin
# Create your views here.


class Index(TemplateView):

    template_name = 'question_list.html'


class NewQuestion(TemplateView):
    template_name = 'new_question.html'
    evaluation_table = ''

    def get(self, request, *args, **kwargs):
        evaluation_table_id = kwargs.get('slug')
        self.evaluation_table = models.EvaluationTable.objects.filter(id=evaluation_table_id).first()
        if not self.evaluation_table:
            return HttpResponse('访问出错')

        return super().get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['evaluation_table'] = self.evaluation_table
        return context


class AddEvaluationTable(MessageMixin, CreateView):

    model = models.EvaluationTable
    form_class = EvaluationTableForms
    error_url = '/'
    success_url = '/'
    success_msg = '成功添加新问卷!'

    def form_valid(self, form):
        self.object = form.save()
        self.success_url = '/new_question/{0}/'.format(self.object.id)
        return super(MessageMixin, self).form_valid(form)









