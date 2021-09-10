#!/user/bin/env python
# -*- coding: utf-8 -*-


import logging
import discord
import json
import re

from PatentBot import runLoki 
from Patent_Articut import articut4PatentBot
from pprint import pprint


logging.basicConfig(level=logging.CRITICAL)

# <取得多輪對話資訊>
client = discord.Client()

patentTemplate = {"IPC_Number":"",
                  "Type":"",
                  "Content":"",
                  "ArticutresultDICT":"",
                  "completed":""}

mscDICT = {}
# </取得多輪對話資訊>

with open("account.info", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())
# 另一個寫法是：accountDICT = json.load(open("account.info", encoding="utf-8"))

punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")

# 接上NLU模型: PatentBot
def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Loki Result => {}".format(resultDICT))
    return resultDICT

# 接上Articut分析模型: articut4PatentBot
def getArticutResult(IPC_Number, Type, inputSTR):
    category = IPC_Number + Type
    resultDICT = articut4PatentBot(category, inputSTR)
    print("Articut Result => {}".format(resultDICT))
    return resultDICT



@client.event
async def on_ready():
    logging.info("[READY INFO] {} 上工啦!".format(client.user))
    print("[READY INFO] {} 上工啦!".format(client.user))
    
    
@client.event
async def on_message(message):
    #if message.channel.name != "bot_test":
        #return

    if not re.search("<@[!&]{}> ?".format(client.user.id), message.content):    # 只有 @Bot 才會回應
        return

    if message.author == client.user:
        return

    try: # try except 先拿掉
        print("收到來自 {} 的訊息".format(client.user), "\n訊息內容是 {}: ".format(message.content))
        msgSTR = re.sub("<@[!&]{}> ?".format(client.user.id), "", message.content)    # 收到 User 的訊息，將 id 取代成 ""
        print("msgSTR =", msgSTR)
        replySTR = ""    # Bot 回應訊息
        
        # datetime

        if re.search("(hi|hello|哈囉|嗨|[你您]好)", msgSTR.lower()):
            replySTR = "Hi，您想比對哪個領域的專利呢？"
            await message.reply(replySTR)
        
        #if msgSTR == "是":
        #    replySTR = "比對中，請稍後..."
        #    await message.reply(replySTR)
        #    print("mscDICT = ")
        #    pprint(mscDICT)
        #    #if set(patentTemplate.keys()).difference(mscDICT[client.user.id].keys()) == set():
        #    url = "https://twpat4.tipo.gov.tw/tipotwoc/tipotwkm?!!FR_" + list(mscDICT[client.user.id]["ArticutresultDICT"]["All_Max"].keys())[0]
        #    replySTR = """為您找到最相似的專利為證書號 {} 的專利，
        #    其"{}"的餘弦相似度經過Articut的分析為 {} ，
        #    更完整的專利文件請參考: {}""".format(list(mscDICT[client.user.id]["ArticutresultDICT"]["All_Max"].keys())[0], 
        #                                           mscDICT[client.user.id]["ArticutresultDICT"]["All_Max"][list(mscDICT[client.user.id]["ArticutresultDICT"]["All_Max"].keys())[0]][1], 
        #                                           mscDICT[client.user.id]["ArticutresultDICT"]["All_Max"][list(mscDICT[client.user.id]["ArticutresultDICT"]["All_Max"].keys())[0]][0],
        #                                           url)
        #    await message.reply(replySTR)
        #    mscDICT[client.user.id]["completed"] = True
        #    return
        
        lokiResultDICT = getLokiResult(msgSTR) # 取得 Loki 回傳結果
        
        if lokiResultDICT:
            if client.user.id not in mscDICT:    # 判斷 User 是否為第一輪對話
                mscDICT[client.user.id] = {#"IPC_Number":"",
                                           #"Type":"",
                                           #"Content":"",
                                           #"ArticutresultDICT":
                                           "completed":False}
                
            for k in lokiResultDICT:    # 將 Loki Intent 的結果，存進 Global mscDICT 變數，可替換成 Database。
                if k == "IPC_Number":
                    mscDICT[client.user.id]["IPC_Number"] = lokiResultDICT["IPC_Number"]
                elif k == "Type":
                    mscDICT[client.user.id]["Type"] = lokiResultDICT["Type"]
                elif k == "msg":
                    replySTR = lokiResultDICT[k]
                    print("Loki msg:", replySTR, "\n")
                    await message.reply(replySTR)     # 有更動
                    return                    
                elif k == "confirm":
                    if lokiResultDICT["confirm"]:
                        replySTR = "正在為您比對的是IPC_Number為{}中類別為{}的專利，請您稍後片刻，謝謝...".format(mscDICT[client.user.id]["IPC_Number"], mscDICT[client.user.id]["Type"]).replace("    ", "")
                        await message.reply(replySTR)                        
                    else:
                        replySTR = "請重新輸入您想比對哪個領域的專利範圍，謝謝"
                        await message.reply(replySTR)
                        del mscDICT[client.user.id]["Content"]
                        return
            
                        
            if mscDICT[client.user.id]["IPC_Number"] != "" and mscDICT[client.user.id]["Type"] != "":
                replySTR = "請輸入您想比對的專利範圍..."
                print("Loki msg:", replySTR, "\n")
                await message.reply(replySTR)     # 有更動
                return  
            
            
        mscDICT[client.user.id]["Content"] = msgSTR
                
        ArticutresultDICT = getArticutResult(mscDICT[client.user.id]["IPC_Number"], mscDICT[client.user.id]["Type"], mscDICT[client.user.id]["Content"])
                
        if ArticutresultDICT:
            mscDICT[client.user.id]["ArticutresultDICT"] = ArticutresultDICT
            replySTR = "再次確認您想比對的是IPC_Number為{}中類別為{}的專利，沒錯嗎?".format(mscDICT[client.user.id]["IPC_Number"], mscDICT[client.user.id]["Type"])
            await message.reply(replySTR)         
            return
        
                
        if set(patentTemplate.keys()).difference(mscDICT[client.user.id].keys()) == set():
            url = "https://twpat4.tipo.gov.tw/tipotwoc/tipotwkm?!!FR_" + list(mscDICT[client.user.id]["ArticutresultDICT"]["All_Max"].keys())[0]
            replySTR = """為您找到最相似的專利為證書號 {} 的專利，
            其"{}"的餘弦相似度經過Articut的分析為 {} ，
            更完整的專利文件請參考: {}""".format(list(mscDICT[client.user.id]["ArticutresultDICT"]["All_Max"].keys())[0], 
                                               mscDICT[client.user.id]["ArticutresultDICT"]["All_Max"][list(mscDICT[client.user.id]["ArticutresultDICT"]["All_Max"].keys())[0]][1], 
                                               mscDICT[client.user.id]["ArticutresultDICT"]["All_Max"][list(mscDICT[client.user.id]["ArticutresultDICT"]["All_Max"].keys())[0]][0],
                                               url).replace("    ", "")
            await message.reply(replySTR)
            mscDICT[client.user.id]["completed"] = True
        
        print("mscDICT = ")
        pprint(mscDICT) 
            
        if mscDICT[client.user.id]["completed"]:    # 清空 User Dict
            del mscDICT[client.user.id]
    
        if replySTR:    # 回應 User 訊息
            await message.reply(replySTR)
        return
        
    except Exception as e:
        logging.error("[MSG ERROR] {}".format(str(e)))
        print("[MSG ERROR] {}".format(str(e)))          
            
            
            
        
        
if __name__ == "__main__":
    client.run(accountDICT["discord_token"])
    
    # getLokiResult("我想辦房屋貸款，我是一位會計師")