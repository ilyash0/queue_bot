import abc
from collections.abc import Sequence
from typing import Any, Generic, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType")


class AbstractRepository(abc.ABC, Generic[ModelType]):
    model: type[ModelType]

    def __init__(self, session: AsyncSession):
        self.session = session

    @abc.abstractmethod
    async def add(self, data: dict) -> ModelType:
        raise NotImplementedError

    @abc.abstractmethod
    async def get(self, tg_id: int) -> ModelType | None:
        raise NotImplementedError

    @abc.abstractmethod
    async def update(self, tg_id: int, data: dict) -> ModelType | None:
        raise NotImplementedError

    @abc.abstractmethod
    async def delete(self, **filters) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    async def add_by_filters(self, data: dict) -> ModelType:
        raise NotImplementedError

    @abc.abstractmethod
    async def get_by_filters(self, **filters) -> ModelType | None:
        raise NotImplementedError

    @abc.abstractmethod
    async def update_by_filters(
        self,
        filters: dict[str, Any],
        data: dict[str, Any],
    ) -> Sequence[ModelType]:
        raise NotImplementedError

    @abc.abstractmethod
    async def delete_by_filters(self, **filters) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    async def list_by_filters(self, **filters) -> Sequence[ModelType]:
        raise NotImplementedError
