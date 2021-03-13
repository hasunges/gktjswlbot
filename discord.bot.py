import discord
import os

client = discord.client()

token = "ODE5ODQ3Mzk5Mzc5OTU5ODU3.YEskZA.oTE3ssBg83QgN7hFMBsiLBovj7g"

@client.event
async def on-ready():

    print(client.user.name)
    print('봇 시작됨')
    game = discord.Game("띠껍아 도워줘!")
    await client.change_presence(status=discord.status.online, activity=game)

@client.event
async def on_measage(measage):
    if message.content == "띠껍아 안녕":
        await message.channel.send("안녕하세요ㅋ")

        @client.event
async def on_measage(measage):
    if message.content == "띠껍아 정보":
        await message.channel.send(개발자:하선지/n 개발팀:Team dawnair | 팀 새벽공기/n 버전 0.1/n 개발 환경:discord.py로 만들었고, Visual Studio Code를 이용해 편집했습니다.)
        access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
