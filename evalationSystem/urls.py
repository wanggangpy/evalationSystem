"""evalationSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from question import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view()),
    re_path(r'new_question/(?P<slug>\w+)/$', views.NewQuestion.as_view()),
    path('add_evaluation_content/', views.AddEvaluationContent.as_view()),
    re_path(r'del_evaluation_content/(?P<pk>\w+)/$', views.DelEvaluationContent.as_view()),
    path('add_evaluation_table/', views.AddEvaluationTable.as_view()),

    path('add_section/', views.AddSection.as_view()),
    re_path(r'del_section/(?P<pk>\w+)/$', views.DelSection.as_view()),

    path('add_item/', views.AddItem.as_view())
]
