from django.shortcuts import redirect, render
from .models import Post
from blog.common_func import checkUserPermission 
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def post_create(request):
    if not checkUserPermission(request, 'can_add', '/blog/create'):
        return render(request, 'blog/no_permission.html')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        

        post = Post(
            title=title,
            content=content,
            image=image,
            author=request.user,
            )
        post.save() 
        
        
    return render(request, 'blog/post_create.html')

# @login_required
def post_detail(request, slug):
    
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return render(request, 'blog/post_not_found.html')
    
    can_edit = checkUserPermission(
        request=request,
        access_type="can_edit",
        menu_url="/blog/edit",
        obj_owner=post.author
    )
    print(can_edit)

    can_delete = checkUserPermission(
            request=request,
            access_type="can_delete",
            menu_url="/blog/delete",
            obj_owner=post.author
        )
    print(can_delete)

    context = {
        "post": post,
        "can_edit": can_edit,
        "can_delete": can_delete,
    }
    
    return render(request, 'blog/post_detail.html', context)

@login_required
def post_edit(request, slug):

    try:
       
        post = Post.objects.get(slug=slug)
        if not checkUserPermission(request, 'can_edit', '/blog/edit', obj_owner=post.author):
            return render(request, 'blog/no_permission.html')
    except Post.DoesNotExist:
        return render(request, 'blog/post_not_found.html')

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        post.title = title
        post.content = content
       
        if image:
            post.image = image
        post.save()

        return render(request, 'blog/post_edit.html', {'post': post, 'success': True})

    return render(request, 'blog/post_edit.html', {'post': post})

def post_delete(request, slug):
    post = Post.objects.get(slug=slug)
    if not checkUserPermission(request, 'can_delete', '/blog/delete', obj_owner=post.author):
         return render(request, 'blog/no_permission.html')
    try:
        post.delete()
        return redirect('home')
    except Post.DoesNotExist:
        return render(request, 'blog/post_not_found.html')