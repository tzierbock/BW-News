from django.shortcuts import render, get_object_or_404
from .models import NewsArticle

# Create your views here.
def render_article(request, article_id):
	article = get_object_or_404(NewsArticle, title=article_id)

	return render(request, 'newscaster/article.html', {'title': article.title, 'slug': article.slug, 'content': article.content})