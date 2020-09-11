#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml

def get_config(config_yaml):
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", config_yaml)
    with open(config_path, "r", encoding="utf-8") as config_file:
        configdata = yaml.safe_load(config_file.read())
    return configdata

