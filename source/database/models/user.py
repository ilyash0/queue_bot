from typing import Optional

from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from ..tools import TableNameMixin
from .base import Base


class UserOrm(Base, TableNameMixin):

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    name: Mapped[str] = mapped_column(String(64))
    username: Mapped[str | None] = mapped_column(String(32))
    language_code: Mapped[str | None] = mapped_column(String(2))
