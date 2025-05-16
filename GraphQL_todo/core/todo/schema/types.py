from graphene_django import DjangoObjectType
from todo.models import Users, Task

class UsersType(DjangoObjectType):
    class Meta:
        model=Users
        fields="__all__"

class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = ("id", "title", "is_completed", "user")