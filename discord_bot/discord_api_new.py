import sys
sys.path.append(r"C:\Users\emily\OneDrive\桌面")
from dotenv import load_dotenv
import discord
import os
from PBC1122.chatgpt_ai.openai import chatgpt_response
from PBC1122 import market_new

os.chdir(r"C:\Users\emily\OneDrive\桌面\PBC1122")
# print(os.getcwd())


load_dotenv(r"C:\Users\emily\OneDrive\桌面\PBC1122\token.env")

discord_token = os.getenv("DISCORD_TOKEN")
# print(discord_token)

df = market_new.df

class My_Client(discord.Client):
    async def on_ready(self):
        print("成功登入，目前身分為：%s" % self.user)
        
    async def on_message(self, message):
        # print(message.content)
        
        if message.author == self.user:
            return
        
        command, user_message = None, None
        
        try:
            # openai api (目前沒有付費無法串接)
            for text in ["Hi ", "hi "]:
                if message.content.startswith(text):
                    command = message.content.split(" ")[0]
                    user_message = message.content.replace(text, "")
                    # print(command, user_message)
            
            if command in ["Hi", "hi"]:
                await message.channel.send("抱歉，目前無法使用openai\n若要使用查詢市集功能，請輸入查詢+空格")
                
                # openai api 聊天功能
                # bot_response = chatgpt_response(prompt=user_message)
                # await message.channel.send(f"Answer: {bot_response}")
            
            # 判斷是否有查詢字樣，以及將查詢和後面的字串內容切割開
            for text in ["查詢 "]:
                if message.content.startswith(text):
                    command = message.content.split(" ")[0]
                    user_message = message.content.replace(text, "")
            
            if command in ["查詢"]:
                mkt_response = market_new.market_response(df, prompt=user_message)
                for i in mkt_response:
                    await message.channel.send(f"{i}")
            
            # 非"Hi", "hi"(呼叫openai)及"查詢"(查詢市集)
            if command not in ["Hi", "hi", "查詢"]:
                await message.channel.send(f"""{message.author.name}您好！
歡迎使用市集機器人
1. 呼叫openai請說Hi+空格
2. 查詢市集
(1)縣市名稱，格式為 查詢 縣市名稱 （例如：查詢 台北市）
(2)查詢特定月份的所有市集，格式為 查詢 YYYY/MM ( 例如：查詢 2024/06）
(3)查詢特定日期，格式為 查詢 YYYY/MM/DD-DD ( 例如：查詢 2024/06/01-05）
(4)同時查詢縣市和日期，格式為 查詢 縣市名稱 YYYY/MM/DD-DD ( 例如：查詢 台北市 2024/06/01-05）
*請記得開頭要加上查詢""")
            
        except Exception as e:
            print(e)
            await message.channel.send(f"""請重新確認查詢的格式
查詢市集
(1)縣市名稱，格式為 查詢 縣市名稱 （例如：查詢 台北市）
(2)查詢特定月份的所有市集，格式為 查詢 YYYY/MM ( 例如：查詢 2024/06）
(3)查詢特定日期，格式為 查詢 YYYY/MM/DD-DD ( 例如：查詢 2024/06/01-05）
(4)同時查詢縣市和日期，格式為 查詢 縣市名稱 YYYY/MM/DD-DD ( 例如：查詢 台北市 2024/06/01-05）
*請記得開頭要加上查詢""")
            
    
intents = discord.Intents.default()
intents.message_content = True

client = My_Client(intents=intents)



