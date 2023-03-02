import collections
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from news.forms import articleForm
from news.models import Article
from django.core import serializers
from django.http import JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from home.forms import FeedbackForm
from home.models import Feedback
from news.models import Article
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
import json 

# Create your views here.
def index(request):

    articleList = list(Article.objects.all())

    if len(articleList) >= 4:
        firstArticle = articleList[len(articleList) - 1]
        nextThreeArticles = articleList[len(articleList) - 4:len(articleList) - 1]
        nextThreeArticles = nextThreeArticles[::-1]

        context = {
        'firstArticle' : firstArticle,
        'nextThreeArticles' : nextThreeArticles,
        'articleList' : articleList
        }
        return render(request, 'news-home.html', context)

    else:
        context = {}
        return render(request, 'no-articles.html', context)

def read(request, id):
    article = Article.objects.get(title=id)
    context = {
        'article' : article
    }
    return render(request, 'news-read.html', context)

@login_required(login_url='/admin/login/')
def postArticle(request):
    context = {}
    if request.method == "POST":
        form = articleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/news/')
    else:
        form = articleForm()
    context['form'] = form
    return render(request, "article-post.html", context)

def load_more(request):

    articleQuer = Article.objects.all()
    articleQuer = articleQuer[::-1]
    articleQuer = articleQuer[1::]

    offset=int(request.POST['offset'])
    limit=3
    posts=articleQuer[offset:limit+offset]
    totalData=Article.objects.count() - 1
    data={}
    posts_json=serializers.serialize('json', posts)
    return JsonResponse(data={
        'posts':posts_json,
        'totalResult':totalData
    })

@csrf_exempt
def get_article(request):
    all_articles = Article.objects.all()

    articles_list = []
    for i in all_articles:
        dict = {
                "title" : i.title,
                "summary" : i.summary,
                "imageURL" : i.articleImage,
                "body" : i.body,
                "postDate" : str(i.postDate),
        }
        articles_list.append(dict)

    # Serialize query set to json
    data = json.dumps(articles_list)

    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def post_flutter(request):
    data = json.loads(request.body)
    form = articleForm(data)
    form.save()

    response = HttpResponse('success')
    response.status_code = 200
    return response