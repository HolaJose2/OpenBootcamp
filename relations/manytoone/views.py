from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Reporter
from datetime import date

def create(request):
    rep = Reporter(firstname="Miguel",lastname="Mora",email="miguel.m@hotmail.com")
    rep.save()

    article1 = Article(headline="Lorem ipsum",pub_date=date(2022,11,25),reporter = rep)
    article1.save()

    article2 = Article(headline="set lorem", pub_date=date(2022,5,5),reporter = rep)
    article2.save()

    article3 = Article(headline="Programacion con Django",pub_date=date(2021,4,28),reporter = rep)
    article3.save()

    result = rep.article_set.count()
    


    return HttpResponse(result)