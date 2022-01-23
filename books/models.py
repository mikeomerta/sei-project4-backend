from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=50, unique=True)
    image = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return f'{self.title} - {self.author}'

class Comment(models.Model):
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(
        Book,
        related_name='comments',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='comments_posted',
        on_delete=models.CASCADE
    )


    def __str__(self):
        return f'Comment {self.id} on Book {self.book}'
