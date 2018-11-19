from django.db import models


# Create your models here.
# Пользователь
class User(models.Model):
    chat_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    balance = models.BigIntegerField()

    def __str__(self):
        return self.name


# Категория
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# деньги
class Money(models.Model):
    count: models.BigIntegerField()
    user: models.ManyToManyField(User)
    category: models.ManyToManyField(Category)