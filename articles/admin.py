from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'author', 'views', 'create_date']
	list_display_links = ['create_date']
	list_editable = ['title']
	list_filter = ['category', 'create_date']
	search_fields = ['title', 'text']
	class Meta:
		model = Article

admin.site.register(Article, ArticleAdmin)