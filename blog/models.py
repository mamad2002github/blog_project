from django.db import models

# Create your models here.


class Articles(models.Model):
  title = models.CharField(max_length=70)
  body = models.TextField()
  image = models.ImageField(upload_to='image/articles')
  created = models.DateTimeField(auto_now_add=True)
  updeted = models.DateTimeField(auto_now=True)

  def __str__(self):
      return f'{self.title} - {self.body[:30]}'

