from asyncpg import UniqueViolationError

from data.config import owners, admins, moderators
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


async def list_of_owners():
    owners_objects = await User.query.where(User.permissions == "owner").gino.all()
    owners_list = [owner.user_id for owner in owners_objects]
    owners.extend(owners_list)
    return owners


async def list_of_admins():
    admins_objects = await User.query.where(User.permissions == "admin").gino.all()
    admins_list = [admin.user_id for admin in admins_objects]
    admins.extend(admins_list)
    return admins


async def list_of_moderators():
    moderators_objects = await User.query.where(User.permissions == "moderator").gino.all()
    moderators_list = [moderator.user_id for moderator in moderators_objects]
    moderators.extend(moderators_list)
    return moderators


async def permissions_groups():
    await list_of_owners()
    await list_of_admins()
    await list_of_moderators()
    admins.extend(owners)
    moderators.extend(admins)
