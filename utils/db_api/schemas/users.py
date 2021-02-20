from sqlalchemy import Column, BigInteger, String, sql

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'

    user_id = Column(BigInteger, primary_key=True, index=True)
    full_name = Column(String(255))
    mention = Column(String(320))
    role = Column(String)

    query: sql.Select
