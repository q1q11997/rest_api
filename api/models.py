from django.db import models

# Create your models here.

class BookType(models.Model):
    type_name = models.CharField(max_length=200,verbose_name='书籍类型名称')

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = '书籍类型'
        verbose_name_plural = '书籍类型'

class Book(models.Model):
    book_name = models.CharField(max_length=200,verbose_name='书籍名')
    book_id = models.IntegerField(default=0,verbose_name='书籍商品id')
    book_type = models.ForeignKey(BookType,on_delete=models.DO_NOTHING,verbose_name='书籍类型')
    book_url = models.URLField(verbose_name='书籍链接')
    book_price = models.IntegerField(verbose_name='书籍价格')

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = '书籍名称'
        verbose_name_plural = '书籍名称'