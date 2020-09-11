#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, time, os
from pyrogram import Client

from utils.file import folder_mkdirs


class TeleUser(object):
    def __init__(self, client:Client):
        self.client = client


    def get_chats(self):
        chat_type = set()
        chat_infos = {}
        for dialog in self.client.iter_dialogs():
            chat_dict = json.loads(str(dialog.chat))

            if chat_dict["type"] not in chat_type:
                chat_type.add(chat_dict["type"])
                chat_infos[chat_dict["type"]] = []
            chat_info = {
                "title": chat_dict.get("title"),
                "id": chat_dict.get("id"),
                "username": chat_dict.get("username"),
                "members_count":chat_dict.get("members_count"),
                "type": chat_dict["type"]
            }
            chat = self.client.get_chat(chat_info["id"])
            time.sleep(1)
            chat_info["description"]  = str(chat.description).replace("\n", ", ").replace("|", "/")
            if chat_info["description"] == "None":
                chat_info["description"] = " "
            if chat_info["title"] == None:
                chat_info["title"] = chat.first_name
            else:
                chat_info["title"] = chat_info["title"].replace("|", "/")
            if chat_info["members_count"] == None:
                chat_info["members_count"] = " "
            if chat_info["username"] != None:
                chat_info["username"] = "https://t.me/"+chat_info["username"]
            else:
                chat_info["username"] = " "
            print(chat_info)
            chat_infos[chat_dict["type"]].append(chat_info)

        with open("chats.json", "w", encoding="utf-8") as f:
            json.dump(chat_infos, f, ensure_ascii=False, indent=4)


    def get_message(self, chat_id, folder="doc", filter_not=None, reverse=False):
        chat_obj = self.client.get_chat(chat_id=chat_id)
        folder_mkdirs(folder)
        file_path = os.path.join(folder, chat_obj.title+".md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("> 来源: https://t.me/{}\n\n".format(chat_obj.username))
            for message in self.client.iter_history(chat_id=chat_id, reverse=reverse):
                if filter_not:
                    if message.text:
                        if filter_not in message.text:
                            f.write("## {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(message.date))))
                            f.write(message.text+"\n")
                else:
                    if message.text:
                        f.write("## {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(message.date))))
                        f.write(message.text+"\n")

