from app.internal.models.simple_user import SimpleUser


def update_user_number(user_id, phone_number):
    SimpleUser.objects.filter(user_id=user_id).update(phone_number=phone_number)


def update_create_user(user_id, default_updates):
    SimpleUser.objects. \
        update_or_create(user_id=user_id, defaults=default_updates)
