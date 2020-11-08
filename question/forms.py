from django import forms
from question.models import EvaluationTable, EvaluationContent, Section, Item
from django.core.validators import ValidationError


class EvaluationTableForms(forms.ModelForm):
    class Meta:
        model = EvaluationTable
        fields = ['title']

        error_messages = {
            'title': {'required': "问卷标题不能为空"}
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        res = EvaluationTable.objects.filter(title=title).first()
        if res:
            raise ValidationError("添加失败，问卷名称已存在！")
        return title


class EvaluationContentForms(forms.ModelForm):
    class Meta:
        model = EvaluationContent
        fields = ['title', 'weights', 'evaluation_table']

        error_messages = {
            'title': {'required': '评估内容标题不能为空！'},
            'weights': {'required': '权重不能为空！'},
        }


class SectionForms(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['title', 'section_score', 'evaluation_content']

        error_messages = {
            'title': {'required': '评估内容标题不能为空！'},
            'section_score': {'required': '分部分数不能为空！'},
        }


class ItemForms(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'content', 'item_score', 'section']
