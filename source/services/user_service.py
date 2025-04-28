from collections.abc import Sequence
from typing import Any

from source.database import AbstractUnitOfWork, UserOrm


class UserService:
    def __init__(self, uow: AbstractUnitOfWork):
        self._uow = uow

    async def register_user(
        self,
        user_id: int,
        name: str,
        username: str | None = None,
        language_code: str | None = "ru",
    ) -> UserOrm:
        async with self._uow:
            user_data = {
                "tg_id": user_id,
                "name": name,
                "username": username,
                "language_code": language_code,
            }

            user = await self._uow.users.get(user_id)

            if user:
                updated_user = await self._uow.users.update(user_id, user_data)

                if updated_user is None:
                    raise Exception(f"Couldn't update the user with tg_id {user_id}")
                user = updated_user
            else:
                user = await self._uow.users.add(user_data)

            return user

    async def add_user(self, data: dict[str, Any]) -> UserOrm:
        async with self._uow:
            user = await self._uow.users.add(data)
            return user

    async def get_user(self, tg_id: int) -> UserOrm | None:
        async with self._uow:
            user = await self._uow.users.get(tg_id)
            return user

    async def update_user(self, tg_id: int, data: dict[str, Any]) -> UserOrm | None:
        async with self._uow:
            updated_user = await self._uow.users.update(tg_id, data)
            return updated_user

    async def delete_user(self, tg_id: int) -> None:
        async with self._uow:
            await self._uow.users.delete(tg_id=tg_id)

    async def add_user_by_filters(self, data: dict[str, Any]) -> UserOrm:
        async with self._uow:
            user = await self._uow.users.add_by_filters(data)
            return user

    async def get_user_by_filters(self, **filters: Any) -> UserOrm | None:
        async with self._uow:
            user = await self._uow.users.get_by_filters(**filters)
            return user

    async def update_users_by_filters(
        self,
        filters: dict[str, Any],
        data: dict[str, Any],
    ) -> Sequence[UserOrm]:
        async with self._uow:
            updated_users = await self._uow.users.update_by_filters(filters, data)
            return updated_users

    async def delete_users_by_filters(self, **filters: Any) -> None:
        async with self._uow:
            await self._uow.users.delete_by_filters(**filters)

    async def list_users_by_filters(self, **filters: Any) -> Sequence[UserOrm]:
        async with self._uow:
            users = await self._uow.users.list_by_filters(**filters)
            return users
