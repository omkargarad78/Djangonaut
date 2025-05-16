import graphene
from todo.models import Task, Users
from todo.schema.types import TaskType

class CreateTask(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        user_id = graphene.Int(required=True)

    task = graphene.Field(TaskType)

    def mutate(self, info, title, user_id):
        user = Users.objects.get(id=user_id)
        task = Task(title=title, user=user)
        task.save()
        return CreateTask(task=task)

class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()
