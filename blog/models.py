from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="姓名")
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField(default=timezone.now)
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField(default=0)
    n_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.headline


class AuthorManager(models.Manager):
    def get_queryset(self):
        return super(AuthorManager, self).get_queryset().filter(role='A')


class EditorMananger(models.Manager):
    def get_queryset(self):
        return super(EditorMananger, self).get_queryset().filter(role='E')


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=(('A', _('Author')), ('E', _('Editor'))))
    objects = models.Manager()
    authors = AuthorManager()
    editors = EditorMananger()


class User(models.Model):
    name = models.CharField(max_length=10)
    groups = models.ManyToManyField('blog.Group', related_name="groups")

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class User1(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Group1(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class User1_Groups(models.Model):
    user1_id = models.ForeignKey(User1, on_delete=models.CASCADE)
    group1_id = models.ForeignKey(Group1, on_delete=models.CASCADE)
    expired = models.DateTimeField()

    def __str__(self):
        return self.name