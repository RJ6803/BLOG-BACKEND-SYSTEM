from django.shortcuts import render,redirect
from .models import postModel
from .forms import postModelForm, PostUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    posts=postModel.objects.all()
    if request.method=='POST':
        form=postModelForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('blog-index')
    else:
        form=postModelForm()
    context={
        'posts':posts,
        'form':form,
    }

    return render(request,'blog/Index.html',context)

@login_required
def post_detail(request,pk):
    post=postModel.objects.get(id=pk)
    if request.method=='POST':
        c_form=CommentForm(request.POST)
        if c_form.is_valid():
            instance=c_form.save(commit=False)
            instance.user=request.user
            instance.post=post
            instance.save()
            return redirect('blog-post-detail',pk=post.id)
    else:
        c_form=CommentForm()    
    context={
        'post':post,
        'c_form':c_form,

    }
    return render(request,'blog/post_detail.html',context)

@login_required
def post_edit(request, pk):
    post=postModel.objects.get(id=pk)
    if request.method=='POST':
        form=PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-post-detail',pk=post.id)
    else:
        form=PostUpdateForm(instance=post)
    context={
        'post':post,
        'form':form,
    }
    return render(request,'blog/post_edit.html',context)

@login_required
def post_delete(request,pk):
    post=postModel.objects.get(id=pk)
    if request.method=='POST':
        post.delete()
        return redirect('blog-index')
    context={
        'post':post,
    }
    return render(request,'blog/post_delete.html',context)