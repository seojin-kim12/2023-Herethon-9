from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from accounts.models import CustomUser
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

@login_required
def create(request,customUser_id):
    print(customUser_id)
    user =get_object_or_404(CustomUser, pk=customUser_id)
    customUser_id=customUser_id


    if request.method == 'POST':
        post = Post()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.category = request.POST['category']
        post.author = user
        post.save()
        return render(request, "html/post.html", {'customUser_id': customUser_id})
    return render(request, "html/post.html",  {'customUser_id': customUser_id})



def post_list(request):
    # 모든 게시글 가져오기
    posts = Post.objects.all()
    page = request.GET.get('page')

    # 한 페이지에 게시글 2개를 보여줌
    paginator = Paginator(posts, 2)

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger: # 첫번째 페이지 접속시 나는 오류 해결
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)

    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex+1)

    context = {
        'posts': posts,
        'custom_range': custom_range,
        'page_obj': page_obj,
        'paginator': paginator,
    }

    return render(request, 'html/post_list.html', context)


def post_detail(request, post_id, customUser_id):
    post = get_object_or_404(Post, pk=post_id)
    post_id = post_id
    page = request.GET.get('page')
    user =get_object_or_404(CustomUser, pk=customUser_id)
    customUser_id=customUser_id

    # 댓글 생성
    if request.method == 'POST':
        comment = Comment()
        comment.post = post
        comment.text = request.POST['text']
        comment.author = user
        comment.save()
        return redirect('post_detail', post_id=post_id, customUser_id= customUser_id)


    # 댓글 페이징 처리
    comments = post.comments.order_by('datetime')

    paginator = Paginator(comments, 2)


    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger: #페이지 첫화면일 때
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage: #댓글이 없을때
        page = paginator.num_pages
        page_obj = paginator.page(page)

#댓글 페이지 총 5장씩
    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex+1)

    context = {
        'post': post,
        'comments': comments,
        'custom_range': custom_range,
        'page_obj': page_obj,
        'paginator': paginator,
        'customUser_id': customUser_id,
    }

    return render(request, 'html/post_detail.html', context)

