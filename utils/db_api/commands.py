from asyncpg import UniqueViolationError

from .schemas import User


async def add_user(user_id: int, full_name: str, mention: str, referrer: int = None):
    try:
        user = User(user_id=user_id, full_name=full_name, mention=mention, referrer=referrer)
        await user.create()
    except UniqueViolationError:
        pass


async def select_user(user_id: int):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def select_all_users():
    users = await User.query.gino.all()
    return users
