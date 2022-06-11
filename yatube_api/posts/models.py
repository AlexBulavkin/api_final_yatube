from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель тематики постов."""
    title = models.CharField('название темы', max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField('описание темы')

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель постов."""
    text = models.TextField('текст поста')
    pub_date = models.DateTimeField('дата публикации', auto_now_add=True)
    author = models.ForeignKey(User,
                               verbose_name="автор поста",
                               on_delete=models.CASCADE,
                               related_name='posts')
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(Group,
                              verbose_name="тема поста",
                              on_delete=models.SET_NULL,
                              related_name="posts",
                              null=True,
                              blank=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Модель комментариев к постам."""
    author = models.ForeignKey(User,
                               verbose_name="автор комментария",
                               on_delete=models.CASCADE,
                               related_name='comments')
    post = models.ForeignKey(Post,
                             verbose_name="прокомментированный пост",
                             on_delete=models.CASCADE,
                             related_name='comments')
    text = models.TextField("текст комментария")
    created = models.DateTimeField('дата добавления',
                                   auto_now_add=True,
                                   db_index=True)

    def __str__(self):
        return self.text


class Follow(models.Model):
    """Модель подписок на авторов."""
    user = models.ForeignKey(User,
                             verbose_name="подписчик",
                             on_delete=models.CASCADE,
                             related_name='follower')
    following = models.ForeignKey(User,
                                  verbose_name="автор",
                                  on_delete=models.CASCADE,
                                  related_name='following')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='not_self_follow')
        ]

    def __str__(self):
        return f'{self.user} {self.following}'
