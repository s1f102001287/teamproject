from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils import timezone
from .models import Article, Comment
from .forms import UploadFileForm

# Create your views here.
def index(request):
	if request.method == 'POST':
		article = Article(title=request.POST['title'],
        image = request.FILES['myfile'],
		body = request.POST['text'],
		posted_at = timezone.now()
		)
		article.save()

		if ('sort' in request.GET) and (request.GET['sort'] == 'like'):
			articles = Article.objects.order_by('-like')
		else:
			articles = Article.objects.order_by('-posted_at')

		context = {'articles': articles
		}
		return render(request, 'miniblog/content.html', context)

	else:
		context = {
        	'articles': Article.objects.all()
            }
		return render(request, 'miniblog/content.html', context)

def detail(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")

	if request.method == 'POST':
		comment = Comment(article=article, text=request.POST['text'])
		comment.save()

	context = {
		'article': article,
		'comments': article.comments.order_by('-posted_at')
	}
	return render(request, "miniblog/detail.html", context)

def update(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	if request.method == 'POST':
		article.title = request.POST['title']
		article.body = request.POST['text']
		article.save()
		return redirect(detail, article_id)

	context = {
		'article' : article
	}
	return render(request, "miniblog/edit.html", context)



def delete(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	article.delete()
	return redirect(index)

def create(request):
	return render(request, "miniblog/newPost.html")

def like(request, article_id):
	try:
		article=Article.objects.get(pk=article_id)
		article.like += 1
		article.save()
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	return redirect(detail, article_id)

def api_like(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
		article.like += 1
		article.save()
	except Article.DoesNotExist:
		raise Http404("Article does not exist")

	result = {
		'id' : article_id,
		'like' : article.like
	}

	return JsonResponse(result)


