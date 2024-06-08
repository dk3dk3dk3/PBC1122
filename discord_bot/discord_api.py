import sys
sys.path.append(r"C:\Users\emily\OneDrive\桌面")
from dotenv import load_dotenv
import discord
import os
from PBC1122.chatgpt_ai.openai import chatgpt_response
from PBC1122 import market

os.chdir(r"C:\Users\emily\OneDrive\桌面\PBC1122")
# print(os.getcwd())


load_dotenv(r"C:\Users\emily\OneDrive\桌面\PBC1122\token.env")

discord_token = os.getenv("DISCORD_TOKEN")
# print(discord_token)

df = market.df

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
                bot_response = chatgpt_response(prompt=user_message)
                await message.channel.send(f"Answer: {bot_response}")
            
            # 市集        
            # 查詢 單一日期
            # 查詢 單一日期 地點
            # 查詢 一段期間
            # 查詢 一段期間 地點
            
            
            for text in ["查詢 "]:
                if message.content.startswith(text):
                    command = message.content.split(" ")[0]
                    user_message = message.content.replace(text, "")
                    # print(command, user_message)
            
            if command in ["查詢"]:
                mkt_response = market.market_response(df, prompt=user_message)
                for i in mkt_response:
                    await message.channel.send(f"{i}")
            
        except:
            pass
            
        await message.channel.send(f"""{message.author.name}您好！
歡迎使用市集機器人
1. 呼叫機器人請說Hi+空格
2. 查詢市集請說查詢+空格
例如：
查詢 單一日期 2024-05-31
查詢 單一日期 地點 2024-05-31 台北市
查詢 一段期間 2024-05-01 2024-05-31
查詢 一段期間 地點 2024-05-01 2024-05-31 台北市""")
            
    
intents = discord.Intents.default()
intents.message_content = True

client = My_Client(intents=intents)



