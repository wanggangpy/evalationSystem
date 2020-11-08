from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView
from question import models
from question.forms import EvaluationTableForms, EvaluationContentForms, SectionForms, ItemForms

from question.utils import MessageMixin
# Create your views here.


class Index(TemplateView):

    template_name = 'question_list.html'


class NewQuestion(TemplateView):
    template_name = 'new_question.html'
    evaluation_table = ''

    def get(self, request, *args, **kwargs):
        self.request.session['from_url'] = self.request.path
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


class AddEvaluationContent(MessageMixin, CreateView):
    model = models.EvaluationContent
    form_class = EvaluationContentForms
    success_msg = '成功添加新的评估内容！'
    error_url = '/'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        evaluation_table_id = request.POST.get('evaluation_table')
        redirect_url = '/new_question/{0}/'.format(evaluation_table_id)
        self.error_url = redirect_url
        self.success_url = redirect_url
        return super().post(self, request, *args, **kwargs)


class DelEvaluationContent(MessageMixin, DeleteView):

    model = models.EvaluationContent
    success_msg = '删除成功！'

    def get_success_url(self):
        return self.request.session['from_url']


class AddSection(MessageMixin, CreateView):

    model = models.Section
    success_msg = '成功添加新的分部内容!'
    form_class = SectionForms

    def get_success_url(self):
        return self.request.session['from_url']


class DelSection(MessageMixin, DeleteView):

    model = models.Section
    success_msg = '删除成功！'

    def get_success_url(self):
        return self.request.session['from_url']


class AddItem(MessageMixin, CreateView):

    model = models.Item
    form_class = ItemForms
    success_msg = '添加成功'

    def form_valid(self, form):
        chooses_list = list(filter(lambda item: item.startswith('choose-title'), self.request.POST.keys()))
        self.object = form.save()
        for index, choose in enumerate(chooses_list):

            models.Choose.objects.create(**{
                'title': str(self.request.POST.get('choose-title{0}'.format(index+1))),
                'score': self.request.POST.get('choose-score{0}'.format(index+1)),
                'item': self.object
            }).save()
        return super(MessageMixin, self).form_valid(form)

    def get_success_url(self):
        return self.request.session['from_url']















