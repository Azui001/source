#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def folder_mkdirs(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def walk_files(path_temp):
    # path_temp = path_temp.replace("/", "\\")
    for root, dirs, files in os.walk(path_temp):
        for file in files:
            file_path = os.path.join(root, file)
            yield file_path
        for dir in dirs:
            path_temp = os.path.join(root, dir)
            walk_files(path_temp)


def write_readme():
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# 一些资源\n")
        for i in walk_files("doc"):
            if "assets" in i:
                continue
            file_name = os.path.splitext(os.path.basename(i))[0]
            f.write("* [{}](./{})\n".format(file_name, i.replace("\\","/")))
