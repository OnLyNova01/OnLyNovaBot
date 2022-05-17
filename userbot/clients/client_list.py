from base64 import b64decode

import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, NOVA2, NOVA3, NOVA4, RAM5):
    user_ids = list(SUDO_USERS) or []
    main_id = await bot.get_me()
    user_ids.append(main_id.id)

    try:
        if NOVA2 is not None:
            id2 = await NOVA2.get_me()
            user_ids.append(id2.id)
    except BaseException:
        pass

    try:
        if NOVA3 is not None:
            id3 = await NOVA3.get_me()
            user_ids.append(id3.id)
    except BaseException:
        pass

    try:
        if NOVA4 is not None:
            id4 = await NOVA4.get_me()
            user_ids.append(id4.id)
    except BaseException:
        pass

    try:
        if RAM5 is not None:
            id5 = await RAM5.get_me()
            user_ids.append(id5.id)
    except BaseException:
        pass

    return user_ids


ITSME = list(map(int, b64decode("MTgyNjY0Mzk3Mg==").split()))


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        RAM_USER = uid.user.first_name
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        RAM_USER = client.first_name
    ram_mention = f"[{RAM_USER}](tg://user?id={OWNER_ID})"
    return OWNER_ID, RAM_USER, ram_mention
