from ninja import Schema
from ninja.orm import create_schema
from pydantic import Field

from app.internal.users.db_data.models import AuthUser, SimpleUser

UserSchema = create_schema(SimpleUser)

AuthUserSchema = create_schema(AuthUser)


class TestInfSchema(Schema):
    id: int = Field()


class UserInfSchema(Schema):
    inf: str = Field()
