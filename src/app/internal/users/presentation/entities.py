from ninja import Schema
from ninja.orm import create_schema
from pydantic import Field

from app.internal.users.db_data.models import AuthUser, SimpleUser

UserSchema = create_schema(SimpleUser)

AuthUserSchema = create_schema(AuthUser)


class SimpleUserSchema(Schema):
    user_name: str = Field()
    surname: str = Field()
    full_username: str = Field()
    simple_user_id: str = Field()


class TestInfSchema(Schema):
    id: int = Field()


class UserInfSchema(Schema):
    inf: str = Field()
