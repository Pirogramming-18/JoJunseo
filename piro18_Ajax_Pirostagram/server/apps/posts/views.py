from django.shortcuts import render, redirect
from .models import Comment

# Create your views here.

def post(request):
    comments = Comment.objects.all()
    context = {
        'comments' : comments,
    }
    return render(request, 'post.html', context=context)



import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    likestatus = req['likestatus']

    if likestatus == 'false':
        likestatus = 'true'
        return JsonResponse({'like': likestatus})
    else:
        likestatus = 'false'
        return JsonResponse({'like': likestatus})
    
@csrf_exempt
def post_comment(request):
    req = json.loads(request.body)

    content = req['comment']
    comment = Comment.objects.create(
        content = content
    )

    id = comment.id

    return JsonResponse({'comment': content, 'id': id})


@csrf_exempt
def comment_delete(request):
    req = json.loads(request.body)
    comment_id = req['id']

    comment = Comment.objects.get(id=comment_id)
    comment.delete()

    return JsonResponse({'id': comment_id})
