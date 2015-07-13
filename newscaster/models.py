from django.db import models

# Create your models here.
class NewsArticle(models.Model):
	"""Standard news article which is to be displayed on the site. Each article is linked to a User object in the database."""
	class Meta:
		verbose_name = "Article"
		verbose_name_plural = "Articles"

	# Meta data
	title = models.CharField('Title', max_length=200)
	slug = models.CharField('Slug', max_length=600)

	# Content store
	raw_body = models.TextField('Raw Text', help_text='Unmodified input text. Accepts markdown')
	content = models.TextField('Content', help_text='XHTML of compiled markdown', blank=True, null=True)

	def __str__(self):
	    return self.title + ' - ' + self.slug[:20] + '...'

	def save(self):
		import markdown
		self.content = markdown.markdown(self.raw_body)
		super(NewsArticle, self).save()