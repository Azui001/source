#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

from utils.file import folder_mkdirs


def chat_counts(info, channel_count=None, channel_people=None, supergroup_count=None, supergroup_people=None,
                bot_count=None, group_count=None, group_people=None):
    if info["type"] == "channel":
        channel_count += 1
        channel_people += info["members_count"]
    if info["type"] == "supergroup":
        supergroup_count += 1
        supergroup_people += info["members_count"]
    if info["type"] == "bot":
        bot_count += 1
    if info["type"] == "group":
        group_count += 1
        group_people += info["members_count"]
    return channel_count, channel_people, supergroup_count, supergroup_people, bot_count, group_count, group_people


def write_tglist(chat_infos, folder="doc"):
    channel_count = 0
    channel_people = 0
    supergroup_count = 0
    supergroup_people = 0
    bot_count = 0
    group_count = 0
    group_people = 0

    readme_head = "# 🥇Telegram🍦Group🍟Channel🍔Bot🍖List\n\n" \
                  "自用 `Telegram` 导航，群组人数累计规模🥇已逾 1000w ...\n" \
                  "## 目录\n" \
                  "1. [channel](#1channel)\n" \
                  "2. [bot](#2bot)\n" \
                  "3. [supergroup](#3supergroup)\n"\
                  "4. [group](#4group)\n" \
                  "5. [统计](#5统计)\n\n"
    folder_mkdirs(folder)
    file_path = os.path.join(folder, "Telegram群组导航.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(readme_head)
        chat_infos.pop("private")
        keys = chat_infos.keys()
        key_index = 0
        for key in keys:
            key_index += 1
            f.write("\n## {}.{}\n".format(key_index, key))
            f.write("| 序号 :id: | ID :key: | 标题 :arrow_heading_up: | 链接 🔗 | 人数 :family: | 类型 :abcd: | 描述 :book: |\n")
            f.write("| :---------------: | :-----------------: | ---------------------- | :-----------: | :---------: | :-----------: | --------- |\n")

            index_s = 0
            for info in chat_infos[key]:
                if info["title"] == None:
                    pass
                channel_count, channel_people, supergroup_count, supergroup_people, bot_count, group_count, group_people = \
                    chat_counts(info, channel_count, channel_people, supergroup_count, supergroup_people, bot_count, group_count, group_people)
                index_s += 1
                f.write("|%s|`%s`|%s|[🔗](%s)|%s|%s|%s|\n" %
                        (index_s, info["id"], info["title"], info["username"], info["members_count"], info["type"], info["description"]))

        f.write("## 5.统计\n\n")
        f.write("* 共 `{}` 个 `channel`, 累计人数 `{}` .\n".format(channel_count, channel_people))
        f.write("* 共 `{}` 个 `supergroup`, 累计人数 `{}` .\n".format(supergroup_count, supergroup_people))
        f.write("* 共 `{}` 个 `bot`.\n".format(bot_count))
        f.write("* 共 `{}` 个 `group`, 累计人数 `{}` .\n".format(group_count, group_people))
        f.write("* 最后统计日期：{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))


