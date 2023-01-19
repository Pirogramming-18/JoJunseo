from django.shortcuts import render, redirect
from server.apps.posts.models import Idea,Tool
from django.http.request import HttpRequest

def ideas_list(request:HttpRequest, *args, **kwargs):
    ideas = Idea.objects.all()

    # # text = request.GET.get("text")
    # # if text:
    # #     posts = posts.filter(content__contains=text)
    # min_price = request.GET.get("min_price")
    # max_price = request.GET.get("max_price")
    # if min_price and max_price:
    #     posts = posts.filter(price__range=(min_price,max_price))
        
    return render(request, "ideas_list.html", {"ideas":ideas})


def tools_list(request:HttpRequest, *args, **kwargs):
    tools = Tool.objects.all()

    # # text = request.GET.get("text")
    # # if text:
    # #     posts = posts.filter(content__contains=text)
    # min_price = request.GET.get("min_price")
    # max_price = request.GET.get("max_price")
    # if min_price and max_price:
    #     posts = posts.filter(price__range=(min_price,max_price))
        
    return render(request, "tools_list.html", {"tools":tools})

def ideas_retrieve(request:HttpRequest, pk, *args, **kwargs):
    idea = Idea.objects.get(id=pk)

    context = {
        "idea" : idea,
    }
    if request.method == "POST":
        idea.star=request.POST["star"]
        idea.save()
        return redirect(f"/")
    
    return render(request, "ideas_retrieve.html", context=context)

def tools_retrieve(request:HttpRequest, pk, *args, **kwargs):
    tool = Tool.objects.get(id=pk)

    all_idea = tool.idea_tool.all()

    context = {
        "tool" : tool,
        "all_idea" : all_idea,
    }
    return render(request, "tools_retrieve.html", context=context)

def tools_create(request:HttpRequest, *args, **kwargs):
    if request.method == "POST":
        tool=Tool.objects.create(
            name=request.POST["name"],
            kind=request.POST["kind"],
            content=request.POST["content"],
        )
        return redirect(f"/tools/{tool.id}")
    return render(request, "tools_create.html")

def ideas_create(request:HttpRequest, *args, **kwargs):
    all_tool = Tool.objects.all()
    context = {
            "all_tool" : all_tool,
        }
    if request.method == "POST":
        idea = Idea.objects.create(
            title=request.POST["title"],
            image=request.FILES["image"],
            content=request.POST["content"],
            interest=request.POST["interest"],
            devtool=Tool.objects.get(name=request.POST["devtool"]),
        )
        return redirect(f"/ideas/{idea.id}")
    return render(request, "ideas_create.html", context=context)

def ideas_delete(request:HttpRequest, pk, *args, **kwargs):
    if request.method == "POST":
        idea = Idea.objects.get(id=pk)
        idea.delete()
    return redirect("/")

def tools_delete(request:HttpRequest, pk, *args, **kwargs):
    if request.method == "POST":
        tool = Tool.objects.get(id=pk)
        tool.delete()
    return redirect("/toolslist")

def ideas_update(request:HttpRequest, pk, *args, **kwargs):
    all_tool = Tool.objects.all()
    idea = Idea.objects.get(id=pk)
    context = {
            "all_tool" : all_tool,
            "idea" : idea,
        }
    if request.method == "POST":
        idea.title=request.POST["title"]
        idea.image=request.FILES.get("image")
        idea.content=request.POST["content"]
        idea.interest=request.POST["interest"]
        idea.devtool=Tool.objects.get(name=request.POST["devtool"])
        idea.save()
        return redirect(f"/ideas/{idea.id}")
    return render(request, "ideas_update.html", context=context)

def tools_update(request:HttpRequest, pk, *args, **kwargs):
    tool = Tool.objects.get(id=pk)
    context = {
            "tool" : tool
        }
    if request.method == "POST":
        tool.name=request.POST["name"]
        tool.kind=request.POST["kind"]
        tool.content=request.POST["content"]
        tool.save()
        return redirect(f"/tools/{tool.id}")
    return render(request, "tools_update.html", context=context)