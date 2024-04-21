from fastapi import FastAPI
from strawberry.asgi import GraphQL

from router.schema import schema

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Welcome to the FastAPI Strawberry GraphQL example. Go to /graphql to use GraphQL."}

app.add_route("/graphql", GraphQL(schema))