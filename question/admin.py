from django.contrib import admin
from question import models
# Register your models here.


admin.site.register(models.EvaluationTable)
admin.site.register(models.EvaluationContent)
admin.site.register(models.Section)
admin.site.register(models.Item)
admin.site.register(models.Choose)
