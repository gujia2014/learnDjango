from django.contrib import admin

# Register your models here.
from books.models import Publisher, Author, Book

class PublisherAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'city', 'state_province')
	#search_fields = ('name',)
	list_filter = ('name',)

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author)
admin.site.register(Book)
