#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json

from api.bot import BotBase
from api.teleuser import TeleUser
from utils.config import get_config
from utils.file import walk_files, write_readme

from utils.tglist import write_tglist


config = get_config("config.yaml")
config_telegram = config["telegram_api"]
api_id = config_telegram["api_id"]
api_hash = config_telegram["api_hash"]
sessions_path = "sessions"


if __name__ == '__main__':
    botbase = BotBase(api_id, api_hash, proxy = dict(hostname="127.0.0.1",port=7890))
    botbase.login(sessions_path)
    client = botbase.client
    teleuser = TeleUser(client)

    # TG群组导航
    # teleuser.get_chats()
    # with open("chats.json", "r", encoding="utf-8") as f:
    #     chat_infos = json.loads(f.read())
    # write_tglist(chat_infos)

    # 心理学笔记
    # teleuser.get_message("xlxbj",reverse=True)

    # VIP账号共享-百度云svip共享
    teleuser.get_message("zh_vip")

    teleuser.client.stop()
    write_readme()

