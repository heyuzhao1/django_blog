from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "posts/posts_list.html", {"posts": posts})


# 读取的地址默认为当前的templates
def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "posts/post_page.html", {"post": post})


# {'post': post}: 是一个上下文字典，将上下文数据传递给模板。这里传递了一个键值对，键是 'post'，值是从数据库中获取到的 Post 对象。在模板中，你可以通过 {{ post }} 来访问这个对象的属性，比如 {{ post.title }} 显示帖子标题


@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect("posts:list")
    else:
        form = forms.CreatePost()
    return render(request, "posts/post_new.html", {"form": form})


@login_required  # 确保用户已登录
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)  # 获取帖子，如果不存在则返回404

    # 检查当前用户是否为帖子发布者
    if post.author == request.user:
        post.delete()  # 删除帖子
        return redirect("posts:list")  # 删除后重定向到帖子列表页面
    else:
        return render(
            request, "403.html", status=403
        )  # 如果用户不是发布者，返回403错误页面


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user:
        #print('author right')
        # Check if the current user is the author of the post
        if request.method == "POST":
            #若为post请求，即提交表单时
            #print('this is a post request')
            form = forms.CreatePost(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect("posts:list")
                # return redirect("posts:page" ,pk=post.pk)
        else:
            # print('this is a get request')
            form = forms.CreatePost(instance=post)
    return render(
        request, "posts/post_edit.html", {"form": form, "post": post}
    )  # 返回渲染的表单
    #也可以通过 <input type="hidden" name="action" value="edit"> 在表单中添加隐藏字段来识别操作
    #  action = request.POST.get('action')
    #         if action == 'edit':