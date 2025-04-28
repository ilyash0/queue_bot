from collections.abc import Sequence
from typing import Any

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import UserOrm
from .base import AbstractRepository


class UserRepository(AbstractRepository[UserOrm]):
    model = UserOrm

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def add(self, data: dict[str, Any]) -> UserOrm:
        user = self.model(**data)
        self.session.add(user)
        return user

    async def get(self, tg_id: int) -> UserOrm | None:
        stmt = select(self.model).filter_by(tg_id=tg_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def update(self, tg_id: int, data: dict[str, Any]) -> UserOrm | None:
        user = await self.get(tg_id=tg_id)

        if user:
            for key, value in data.items():
                if hasattr(user, key) and key not in ["id", "tg_id"]:
                    setattr(user, key, value)
            return user
        return None

    async def delete(self, **filters: Any) -> None:
        stmt = delete(self.model).filter_by(**filters)
        await self.session.execute(stmt)

    async def add_by_filters(self, data: dict[str, Any]) -> UserOrm:
        user = self.model(**data)
        self.session.add(user)
        return user

    async def get_by_filters(self, **filters: Any) -> UserOrm | None:
        stmt = select(self.model).filter_by(**filters)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def update_by_filters(
        self,
        filters: dict[str, Any],
        data: dict[str, Any],
    ) -> Sequence[UserOrm]:
        users_to_update = await self.list_by_filters(
            **filters,
        )

        updated_users = []
        if users_to_update:
            for user in users_to_update:
                for key, value in data.items():
                    if hasattr(user, key) and key not in ["id", "tg_id"]:
                        setattr(user, key, value)
                updated_users.append(user)

        return updated_users

    async def delete_by_filters(self, **filters: Any) -> None:
        stmt = delete(self.model).filter_by(**filters)
        await self.session.execute(stmt)

    async def list_by_filters(self, **filters: Any) -> Sequence[UserOrm]:
        stmt = select(self.model).filter_by(**filters)
        result = await self.session.execute(stmt)
        return result.scalars().all()
