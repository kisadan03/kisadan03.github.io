from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = MarkdownxField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/review/{self.pk}/'

    def get_content_markdown(self):
        return markdown(self.content)

    def get_avatar_url(self):
        if self.author is not None:
            if self.author.socialaccount_set.exists():
                return self.author.socialaccount_set.first().get_avatar_url()
            else:
                return f'https://avatars.dicebear.com/api/human/{self.author.email}.svg'
        else:
            return 'http://placehold.it/50X50'
