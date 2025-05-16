import graphene
from todo.models import Users, Task
from todo.schema.types import UsersType, TaskType

class Query(graphene.ObjectType):
    all_users=graphene.List(UsersType)
    all_tasks=graphene.List(TaskType)
    tasks_by_user=graphene.List(TaskType,user_id=graphene.Int(required=True))

    def resolve_all_users(self, info):
        return Users.objects.all()
    
    def resolve_all_tasks(self,info):
        return Task.objects.all()
    
    def resolve_task_by_user(self, info, user_id):
        return Task.objects.filter(user_id=user_id)
