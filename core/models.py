from django.db import models

# Create your models here.
# this is a manager, with managers you don't need to specify filter for each query
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(published=1)


class Category(models.Model):
    title = models.CharField(max_length=255,verbose_name='نام دسته بندی')
    slug = models.SlugField(unique=True,verbose_name='اسلاگ دسته بندی')
    status = models.BooleanField(default=True, max_length=100,verbose_name='وضعیت انتشار')
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
    def __str__(self):
        return self.title



class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='تیتر')
    slug = models.SlugField(unique=True, max_length=100,verbose_name='اسلاگ')
    catgory = models.ManyToManyField(Category, verbose_name='دسته بندی')
    pre_context = models.CharField(max_length=255,verbose_name='پیش مقاله')
    context = models.TextField(verbose_name='محتوای اصلی')
    create_date = models.DateTimeField(verbose_name='زمان انتشار')
    published = models.BooleanField(default=True,verbose_name='وضعیت انتشار')
    image = models.ImageField(upload_to='images/', verbose_name='تصویر مقاله')

    objects = ArticleManager()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ('-create_date',)





class AboutMe(models.Model):
    context = models.TextField()
    email = models.EmailField()
    tel = models.CharField(max_length=12)
    telegram = models.URLField()

    def __str__(self):
        return self.email
    class Meta:
        verbose_name= 'درباره من'
        verbose_name_plural = 'درباره من'


