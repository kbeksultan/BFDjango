from datetime import datetime

from django.db import models

from todo.auth_.models import MyUser


class ToDoListManager(models.Manager):

    def for_user(self, user):
        return self.filter(owner=user)


class ToDoList(models.Model):
    name = models.CharField(max_length=40)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    objects = ToDoListManager()

    class Meta:
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDo lists'

    def __str__(self):
        return f'{self.name} todo list'


class ToDo(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.now)
    due_on = models.DateTimeField(null=True, default=None)
    is_done = models.BooleanField(default=False)
    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='tasks')
    notes = models.CharField(max_length=255, default='', blank=True)

    objects = ToDoListManager()

    class Meta:
        verbose_name = 'ToDo task'
        verbose_name_plural = 'ToDo tasks'

    def __str__(self):
        return f'{self.name}, in {self.list}'