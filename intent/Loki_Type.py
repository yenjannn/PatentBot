#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Type

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Type = True
userDefinedDICT = {"D": ["設計", "d"], "I": ["發明", "i"], "M": ["新型", "m"], "G06Q_020_24": ["信用方案", "信用", "後付", "pay after", "24"], "G06Q_020_26": ["轉帳方案", "轉帳", "現付", "pay now", "26"], "G06Q_020_28": ["預付方案", "預付", "pay before", "28"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Type:
        print("[Type] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我]要看[發明]":
        # write your code here
        pass

    if utterance == "[發明]":
        # write your code here
        pass

    if utterance == "有[發明]的嗎":
        # write your code here
        pass

    if utterance == "查找[發明]":
        # write your code here
        pass

    return resultDICT