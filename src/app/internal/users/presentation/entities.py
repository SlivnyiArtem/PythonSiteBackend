from ninja import Schema
from pydantic import Field


class SimpleUserSchema(Schema):
    full_username: str = Field()
    simple_user_id: int = Field()
