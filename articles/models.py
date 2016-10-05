from django.db import models

# Create your models here.

CATEGORIES = (('sport', 'спорт'),
				('news', 'новини'),
				('advert', 'оголошення'),
				('school', 'школа'),
				('holiday', 'свято'),
				('etc', 'різне'),)

class Article(models.Model):
	title = models.CharField(max_length=250)
	text = models.TextField()
	author = models.CharField(max_length=100)
	category = models.CharField(max_length=20, choices=CATEGORIES)
	create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)
	views = models.IntegerField(default=0)
	univiews = models.IntegerField(default=0)
	image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)

	class Meta():
		db_table = 'article'