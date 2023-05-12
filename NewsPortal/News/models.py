from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

artecle = 'AR'
news = 'NW'

POSITIONS = [
    (artecle, 'Статья'),
    (news, 'Новость')
]


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user}'

    def update_rating(self):
        rating_post_author = self.post_set.all().aggregate(Sum('rating_post'))['rating_post__sum']
        rating_comment = self.user.comment_set.all().aggregate(Sum('rating_comment'))['rating_comment__sum']
        rating_post_comment = self.post_set.all().aggregate(Sum('comment__rating_comment')
                                                            )['comment__rating_comment__sum']
        self.user_rating = rating_post_author * 3 + rating_comment + rating_post_comment
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    author_post = models.ForeignKey(Author, on_delete=models.CASCADE)
    сhoice_post = models.CharField(max_length=2, choices=POSITIONS, default=news)
    date_post = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    heading_post = models.CharField(max_length=255)
    text_post = models.TextField()
    rating_post = models.IntegerField(default=0)

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post += 1
        self.save()

    def preview(self):
        return self.text_post[: 124] + '...'

    def __str__(self):
        return f'"{self.heading_post}" автор: {self.author_post}'

    def get_absolute_url(self):
        return f'/news/{self.id}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    date_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment += 1
        self.save()