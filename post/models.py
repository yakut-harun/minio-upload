from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils import timezone
from blog.storages import MediaStorage

#
# # class UploadFile(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     file = models.FileField()
# #     uploaded_date = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    user = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    publishing_date = models.DateTimeField(verbose_name="Yayımlanma Tarihi", auto_now_add=True)
    # image = models.FileField(null=True, blank=True ,upload_to='media/')
    image = models.FileField(storage=MediaStorage(), null=True, blank=True )

    publish = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, editable=False, max_length=130)


    def __str__(self):
        return self.title




    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug})
        # return "/post/{}".format(self.id)

    def get_create_url(self):
        return reverse('post:create', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post:update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post:delete', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publishing_date', 'id']

