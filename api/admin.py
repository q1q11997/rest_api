from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(BookType)
class BookTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name','book_id','book_type','book_price','book_url')
