# 參考資料：https://youtu.be/wdgVv4UP08c?si=ROOjMrVIGip8Inae

# 機器人網址：https://discord.com/oauth2/authorize?client_id=1245199022117879808&permissions=8&scope=bot

import sys
sys.path.append(r"C:\Users\emily\OneDrive\桌面")

from PBC1122.discord_bot.discord_api_new import client, discord_token

if __name__ == "__main__":
    client.run(discord_token)