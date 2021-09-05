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
userDefinedDICT = {"D": ["設計", "d", "D"], "I": ["發明", "i", "I"], "M": ["新型", "m", "M"], "G06Q_020_24": ["信用方案", "信用", "後付", "pay after", "24"], "G06Q_020_26": ["轉帳方案", "轉帳", "現付", "pay now", "26"], "G06Q_020_28": ["預付方案", "預付", "pay before", "28"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Type:
        print("[Type] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我]要看[發明]":
        if args[1] in userDefinedDICT["D"]:
            resultDICT["Type"] = "_D"
        elif args[1] in userDefinedDICT["I"]:
            resultDICT["Type"] = "_I"
        elif args[1] in userDefinedDICT["M"]:
            resultDICT["Type"] = "_M"
        else:
            pass

    if utterance == "[發明]":
        if args[0] in userDefinedDICT["D"]:
            resultDICT["Type"] = "_D"
        elif args[0] in userDefinedDICT["I"]:
            resultDICT["Type"] = "_I"
        elif args[0] in userDefinedDICT["M"]:
            resultDICT["Type"] = "_M"
        else:
            pass

    if utterance == "有[發明]的嗎":
        if args[0] in userDefinedDICT["D"]:
            resultDICT["Type"] = "_D"
        elif args[0] in userDefinedDICT["I"]:
            resultDICT["Type"] = "_I"
        elif args[0] in userDefinedDICT["M"]:
            resultDICT["Type"] = "_M"
        else:
            pass

    if utterance == "查找[發明]":
        if args[0] in userDefinedDICT["D"]:
            resultDICT["Type"] = "_D"
        elif args[0] in userDefinedDICT["I"]:
            resultDICT["Type"] = "_I"
        elif args[0] in userDefinedDICT["M"]:
            resultDICT["Type"] = "_M"
        else:
            pass

    if utterance == "[M]":
        if args[0] in userDefinedDICT["D"]:
            resultDICT["Type"] = "_D"
        elif args[0] in userDefinedDICT["I"]:
            resultDICT["Type"] = "_I"
        elif args[0] in userDefinedDICT["M"]:
            resultDICT["Type"] = "_M"
        else:
            pass

    if utterance == "[我]想比對[轉帳]類別[下]跟[發明][相關]的專利":
        confusion = []
        for a in args[1:4]:
            if a in userDefinedDICT["D"]:
                confusion.append("_D")
            elif a in userDefinedDICT["I"]:
                confusion.append("_I")
            elif a in userDefinedDICT["M"]:
                confusion.append("_M")   
        if len(confusion) > 1:
            resultDICT["Type"] = "不確定"
        elif len(confusion) == 1:
            resultDICT["Type"] = confusion[0]  
        else:
            pass             
            
    return resultDICT