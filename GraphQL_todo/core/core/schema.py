import graphene
from todo.schema.queries import Query as TodoQuery
from todo.schema.mutations import Mutation as TodoMutation

class Query(TodoQuery, graphene.ObjectType):
    pass

class Mutation(TodoMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
