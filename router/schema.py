import strawberry

from app.graphql.model1.schema import Model1Query


@strawberry.type
class Query(Model1Query): ...


schema = strawberry.Schema(query=Query)
