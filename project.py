# 參考資料：https://youtu.be/wdgVv4UP08c?si=ROOjMrVIGip8Inae

import sys
sys.path.append(r"C:\Users\emily\OneDrive\桌面")
# from dotenv import load_dotenv
# import discord
# import os
# from PBC1122.chatgpt_ai.openai import chatgpt_response
from PBC1122.discord_bot.discord_api import client, discord_token

if __name__ == "__main__":
    client.run(discord_token)



