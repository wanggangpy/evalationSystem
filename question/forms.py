from django import forms
from question.models import EvaluationTable


class EvaluationTableForms(forms.ModelForm):
    class Meta:
        model = EvaluationTable
        fields = ['title']

        error_messages = {
            'title': {'required': "问卷标题不能为空"}
        }