# -*-coding:utf-8-*-
# Author: alphadl
# bpe_result_process.py 2018/8/14 10:07

"""
I:读取bpe处理之后的结果
O:去掉@@之后的结果
e.g.：
I:A@@ 78@@ 19@@ : Yes. These people are serious.
O:A 78 19 : Yes. These people are serious.
"""

import os

read_file_path = "zh.24000.bpe_1000"
write_file_path = "{:s}.final".format(read_file_path)


def clean(text):
    return str(text).replace("@@", "")


if os.path.isfile(read_file_path):
    filePath = os.path.join(read_file_path)
    with open(filePath, 'rb+') as fr:
        raw_lines = fr.readlines()
        lines = [clean(line.strip()) + "\n" for line in raw_lines]

        with open(write_file_path, 'wb+') as fw:
            fw.writelines(lines)
