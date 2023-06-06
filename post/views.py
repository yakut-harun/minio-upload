import boto3
import io
import math
import os
import shutil
from PIL import Image
from django.contrib import messages

from django.core.cache import cache
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import JsonResponse
#
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from blog import settings
from .forms import PostForm
from .models import Post


def post_index(request):
    post_list = Post.objects.all()
    # post_list = document.objects.all()

    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()

    paginator = Paginator(post_list, 20)  # Show 5 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, "post/index.html", {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)


    context = {
        'post': post,
        # 'form': form
    }
    # return render(request, "post/detail.html", context)
    return redirect("post:create")




def upload_to_aws(file, bucket_name, key):

        # AWS kimlik bilgilerini al
        aws_access_key_id = settings.AWS_ACCESS_KEY_ID
        aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY

        # S3 istemcisini oluştur
        s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

        # Dosyayı S3'e yükle
        s3.upload_fileobj(file, bucket_name, key)

        # Yükleme başarılı olduğunda dosyanın genel URL'sini oluştur
        file_url = f"https://{bucket_name}.s3.amazonaws.com/{key}"

        return file_url


def post_create(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        bucket_name = 'your-bucket-name'  # AWS S3 kova adı
        file_key = file.name  # S3'de kaydedilecek dosya adı

        # Dosyayı AWS'ye yükle
        file_url = upload_to_aws(file, bucket_name, file_key)

        # Yükleme sonucunu döndür
        return JsonResponse({'file_url': file_url}, status=200)

    return JsonResponse({'error': 'Dosya bulunamadı veya POST isteği yapılmadı.'}, status=400)

# def post_create(request):
#     posts = Post.objects.all()
#
#     if not request.user.is_authenticated:
#         # Eğer kullanıcı giriş yapmamış ise hata sayfası gönder
#         return Http404()
#
#     form = PostForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         post = form.save(commit=False)
#         post.user = request.user
#         post.save()
#         messages.success(request, "Başarılı bir şekilde oluşturdunuz.", extra_tags='mesaj-basarili')
#         return HttpResponseRedirect(post.get_absolute_url())
#
#     context = {
#         'posts': posts,
#         'form': form
#     }
#
#     return render(request, "post/form.html", context)
#

def post_update(request, slug):
    if not request.user.is_authenticated:
        # Eğer kullanıcı giriş yapmamış ise hata sayfası gönder
        return Http404()

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "Başarılı bir şekilde güncellediniz.")
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, "post/form.html", context)
    # return render(request, "post/detail.html", context)


def post_delete(request, slug):
    if not request.user.is_authenticated:
        # Eğer kullanıcı giriş yapmamış ise hata sayfası gönder
        return Http404()

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect("post:index")

