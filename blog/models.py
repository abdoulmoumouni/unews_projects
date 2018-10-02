from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):
    date_ajout = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    image = models.ImageField(upload_to ="images/",blank=True, null=True)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    resume = models.TextField(blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category',on_delete = models.CASCADE)
    utilisateur = models.ForeignKey(User,on_delete = models.CASCADE,blank=True, null=True)

    class Meta:
        ordering = ["posted", "title"]

    def __unicode__(self):
        return '%s' % self.title

    def __str__(self):
        return self.title

        # @permalink
        # def get_absolute_url(self):
        #     return ('view_post', None, { 'slug': self.slug })
    def get_absolute_url(self):
        return reverse('view_post', args=[str(self.id)])

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_category', args=[str(self.slug)])

        # @permalink
        # def get_absolute_url(self):
        #     return ('view_category', None, { 'slug': self.slug })
