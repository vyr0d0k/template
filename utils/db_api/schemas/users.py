from sqlalchemy import Column, sql, Integer, BigInteger, String

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)

    user_id = Column(BigInteger)
    full_name = Column(String(255))
    mention = Column(String(320))

    referrer = Column(BigInteger)
    permissions = Column(String(25), default="user")

    query: sql.Select
