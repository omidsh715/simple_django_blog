from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    context = models.TextField()
    create_date = models.DateTimeField()
    published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)


class AboutMe(models.Model):
    context = models.TextField()
    email = models.EmailField()
    tel = models.CharField(max_length=12)
    telegram = models.URLField()

