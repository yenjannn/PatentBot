#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for IPC_Number

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_IPC_Number = True
userDefinedDICT = {"D": ["設計", "d"], "I": ["發明", "i"], "M": ["新型", "m"], "G06Q_020_24": ["信用方案", "信用", "後付", "pay after", "24"], "G06Q_020_26": ["轉帳方案", "轉帳", "現付", "pay now", "26"], "G06Q_020_28": ["預付方案", "預付", "pay before", "28"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_IPC_Number:
        print("[IPC_Number] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "G06Q-020[24]":
        # write your code here
        pass

    if utterance == "[24]":
        # write your code here
        pass

    if utterance == "[可以]找到[預付]的嗎":
        # write your code here
        pass

    if utterance == "[後付]的有哪些專利":
        # write your code here
        pass

    if utterance == "[我]想要比對跟[轉帳][相關]的專利":
        # write your code here
        pass

    if utterance == "[我]要找[預付]的":
        # write your code here
        pass

    if utterance == "[轉帳]的有嗎":
        # write your code here
        pass

    if utterance == "查[現付]的[相關]專利":
        # write your code here
        pass

    if utterance == "跟[預付]系統有關的是誰":
        # write your code here
        pass

    return resultDICT