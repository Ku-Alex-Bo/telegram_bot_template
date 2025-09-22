import enum
from datetime import datetime

from sqlalchemy import BigInteger, Boolean, Column, DateTime, Enum, ForeignKey, Integer
from sqlalchemy.orm import relationship


class UserRole(str, enum.Enum):
    owner = "owner"
    admin = "admin"
    user = "user"


class Lang(str, enum.Enum):
    russian = "ru"
    english = "en"


class UserModel(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    tg_id = Column(
        BigInteger,
        unique=True,
    )

    joined_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    role = Column(
        Enum(UserRole),
        default=UserRole.user
    )

    banned = Column(
        Boolean,
        default=False,
    )

    settings = relationship(
        "UserSettings",
        uselist=False,
        back_populates="user"
    )


class UserSettings(Base):
    __tablename__ = "settings"
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        primary_key=True,
    )
    lang = Column(
        Enum(Lang),
        default=Lang.russian
    )

    user = relationship(
        "UserModel",
        uselist=False,
        back_populates="settings"
    )
