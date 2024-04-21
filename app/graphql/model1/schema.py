import strawberry

from db.operations import MongoDBOperations
from models.model1 import dummy_score


@strawberry.type
class Model1Query:

    @strawberry.field
    def score(score: int) -> int:
        scr = dummy_score(score)

        operations = MongoDBOperations()
        new_score = {"score": scr}
        operations.insert_score(new_score)
        operations.client.close_connection()

        return scr
