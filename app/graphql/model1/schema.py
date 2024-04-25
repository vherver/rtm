import logging

import strawberry

from app.graphql.model1.exceptions import ScoreCalculationError
from app.graphql.model1.input import Model1Input
from db.operations import MongoDBOperations
from models.model1 import dummy_score


@strawberry.type
class ErrorResult:
    message: str


logger = logging.getLogger(__name__)


@strawberry.type
class Model1Query:

    @strawberry.field
    def score(self, info, input: Model1Input) -> int:
        try:
            scr = dummy_score(10)
            if scr:
                new_score = {"score": scr}
                MongoDBOperations().insert_score(new_score)

                return scr

            raise ScoreCalculationError("No score retrieved for input params")

        except ScoreCalculationError as e:
            logger.info(f"Model1 Error: {str(e)}")
            return ErrorResult(message=str(e))