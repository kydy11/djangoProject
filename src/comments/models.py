from django.db import models

class Post(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=400)
    subtitle = models.CharField(max_length=1000, blank=True)
    author = models.CharField(max_length=100)
    text = models.TextField(max_length=50000000000000000000)


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length = 10000000000000000000)
    name =models.CharField(max_length =40)

    _post = models.ForeignKey(to=Post, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.created.strftime("%m/%d%Y")+ " " + self.name
    

