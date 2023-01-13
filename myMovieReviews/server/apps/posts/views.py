from django.shortcuts import render, redirect
from server.apps.posts.models import Post


def posts_list(request, *args, **kwargs):
   
    posts = Post.objects.all()

    return render(request, "posts/posts_list.html", {"posts": posts})

def posts_retrieve(request, pk, *args, **kwargs):
    post = Post.objects.all().get(id=pk)
    return render(request, "posts/posts_retrieve.html",{"post":post})

def posts_create(request, *args, **kwargs):
    if request.method == "POST":
        Post.objects.create(
            title=request.POST["title"],
            year=request.POST["year"],
            genre=request.POST["genre"],
            rating=request.POST["rating"],
            time=request.POST["time"],
            hour = int(request.POST["time"])/60,
            minute = int(request.POST["time"])%60,
            review=request.POST["review"],
            producer=request.POST["producer"],
            actor=request.POST["actor"],
            poster=request.POST["poster"],
        )
        return redirect("/")
    return render(request, "posts/posts_create.html")

def posts_update(request, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)

    if request.method == "POST":
        post.title = request.POST["title"]
        post.year = request.POST["year"]
        post.genre = request.POST["genre"]
        post.rating = request.POST["rating"]
        post.time = request.POST["time"]
        post.hour = int(request.POST["time"])/60
        post.minute = int(request.POST["time"])%60
        post.review = request.POST["review"]
        post.producer = request.POST["producer"]
        post.actor = request.POST["actor"]
        post.poster = request.POST["poster"]
        post.save()
        return redirect(f"/posts/{post.id}")

    return render(request, "posts/posts_update.html", {"post":post})

def posts_delete(request, pk, *args, **kwargs):
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("/")