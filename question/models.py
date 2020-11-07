from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class EvaluationTable(models.Model):
    title = models.CharField(max_length=255)
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class EvaluationContent(models.Model):
    title = models.CharField(max_length=255)
    scoring = models.IntegerField(default=0)
    weights = models.FloatField()
    total_score = models.IntegerField(default=0)

    evaluation_table = models.ForeignKey('EvaluationTable', related_name='evaluation_contents', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Section(models.Model):
    title = models.CharField(max_length=255)
    section_score = models.IntegerField()
    scoring = models.IntegerField(default=0)

    evaluation_content = models.ForeignKey('EvaluationContent', related_name='sections', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    item_score = models.IntegerField()
    scoring = models.IntegerField(default=0)

    section = models.ForeignKey('Section', related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Choose(models.Model):
    title = models.CharField(max_length=255)
    score = models.IntegerField()

    item = models.ForeignKey('Item', related_name='chooses', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
