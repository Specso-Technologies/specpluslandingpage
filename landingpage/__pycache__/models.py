from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField()

    class Meta:
        verbose_name="Query"
        verbose_name_plural="Queries"

    def __str__(self):
        return(self.name)

class Blog(models.Model):
    title = models.CharField(max_length=120)
    shortdes = models.CharField(max_length=200)
    description = models.TextField()
    higlight = models.CharField(max_length=120)
    image = models.ImageField(upload_to="blog" )
    imagealt = models.CharField(max_length=20)
    detailmeatdes = models.TextField()
    keyword = models.TextField()
    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

    def __str__(self):
        return(self.title)

