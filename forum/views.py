from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.template.defaultfilters import slugify
import json

# Create your views here.
@csrf_exempt
def get_forum_list(request):
    list_post = ForumPost.objects.all().order_by('-date_created')

    ret = []
    for posts in list_post:
        temp = {
            "author": posts.author,
            "topic": posts.topic,
            "description":posts.description,
            "date_created":posts.date_created.date(),
            "slug": posts.slug,
        }
        ret.append(temp)

    data = json.dumps(ret, default=str)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def add_new_forum_flutter(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        user = User.objects.get(username = body['username'])
            
        try:
            body['slug'] = slugify(body['topic'])
            body.pop('username')

            form = ForumForm(body)
            # print(form)

            instance = form.save(commit=False)
            instance.author = user
            instance.save()
            return HttpResponse(status=200)
        except:
            print("An error occurred")
            return HttpResponse(body, content_type='application/json')
            # return HttpResponse("An error occurred", status=400, content_type="text/plain")
    
    return HttpResponse("Wrong Method Used", status=405, content_type="text/plain")




def index(request):
    forumPost = ForumPost.objects.all().order_by('-date_created')
    response = {'forumPost': forumPost}

    
    return render(request, 'forumHome.html', response)

# TODO: implement function that will post to forum
def post_to_forum(request):
    form = ForumForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('/forum/')
    
    context = dict()
    context["form"] = form
    return render(request, "postToForum.html", context)

# TODO: Implement function that will view individual post
def forum_post_detail(request, slug):
    # return HttpResponse(slug)

    forumPost = ForumPost.objects.get(slug=slug)
    comments = Comment.objects.all().filter(parentForum=forumPost)
    if (len(comments) == 0):
        dummy = Comment()
        dummy.description = "Belum ada komentar"
        # dummy.author = ""
        comments = [dummy]

    form_data = {}
    if request.method == 'POST' and request.is_ajax():
        description = request.POST.get('description')

        response_data = {'description':description, 'author': request.user.get_username()}

        tmp = Comment(author=request.user,description=description, parentForum=forumPost)
        tmp.save()

        return JsonResponse(response_data)
    return render(request, 'forumDetail.html', {'forumPost':forumPost, 'comments':comments})

@login_required(login_url ='/auth/login/')
def post_comment(request, slug):
    form = CommentForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.parentForum = ForumPost.objects.get(slug=slug)
            instance.save()
            return redirect('/forum/' + slug)
    
    context = dict()
    context["form"] = form
    return render(request, "postComment.html", context)

