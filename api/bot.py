#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pyrogram import Client


class BotBase(object):
    def __init__(self, api_id, api_hash, proxy=None):
        self.api_id = api_id
        self.api_hash = api_hash
        self.proxy = proxy

    def login(self, sessions_path):
        session = os.path.join(sessions_path, str(self.api_id))
        self.client = Client(
            session,
            self.api_id,
            self.api_hash,
            proxy = self.proxy
        )
        self.client.start()

