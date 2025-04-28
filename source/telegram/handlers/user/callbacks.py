from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from source.services import UserService

user_callbacks_router = Router(name=__name__)


@user_callbacks_router.callback_query(F.data == "language_ru")
async def language_ru(
    callback: CallbackQuery,
    i18n: I18nContext,
    user_service: UserService,
) -> None:
    await user_service.update_user(callback.from_user.id, {"language_code": "ru"})
    await i18n.set_locale("ru")

    await callback.answer("")

    changed_language = "русский"

    await callback.message.edit_text(
        text=i18n.get("changed_language", language=changed_language),
    )


@user_callbacks_router.callback_query(F.data == "language_en")
async def language_en(
    callback: CallbackQuery,
    i18n: I18nContext,
    user_service: UserService,
) -> None:
    await user_service.update_user(callback.from_user.id, {"language_code": "en"})
    await i18n.set_locale("en")

    await callback.answer("")

    changed_language = "english"

    await callback.message.edit_text(
        text=i18n.get("changed_language", language=changed_language),
    )


@user_callbacks_router.callback_query(F.data == "on_click_data")
async def on_click_data(
    callback: CallbackQuery,
    i18n: I18nContext,
) -> None:
    await callback.answer(text=i18n.get("clicked"))
