import discord
from discord.ext import commands
import time
import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()  # Load biến môi trường từ file .env

TOKEN = os.getenv('DISCORD_BOT_TOKEN')  # Token từ biến môi trường
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))  # ID kênh gửi tin nhắn từ biến môi trường
GUILD_ID = int(os.getenv('GUILD_ID'))  # ID server Discord từ biến môi trường
ADMIN_ID = int(os.getenv('ADMIN_ID'))  # ID Admin để sử dụng bot từ biến môi trường
PREFIX = '!'

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

menu_gia = '''

🔴 Information
- Windows 10 - All Versions
- Windows 11 - All Versions until 22H2
- 8GB USB needed
- Windows Reinstallation NEEDED
- Flash BIOS Required

✅ Supported Motherboards
- ASUS
- HP
- Dell
- Abra
- TULPAR
- Lenovo
- NZXT
- ACER
- Any locked motherboard

🎯 Supported Games
- Riot Games
- EAC
- BE
- RICCOCHEATS

💰 Prices
- 1 Day = 50,000 VNĐ ➤ 
- Lifetime = 300,000 VNĐ ➤ '''

@bot.event
async def on_ready():
    print(f'✅ Bot đã online với {bot.user}')
    await bot.change_presence(activity=discord.Streaming(name='Valorant', url='https://www.twitch.tv/riotgames'))
    for guild in bot.guilds:
        if guild.id == GUILD_ID:
            print(f'🔗 Đã kết nối với server: {guild.name}')

@bot.command()
async def banggia(ctx):
    if ctx.guild.id == GUILD_ID and ctx.author.id == ADMIN_ID:
        logo = discord.File('logo.png', filename='logo.png')
        small_logo = discord.File('small_logo.png', filename='small_logo.png')
        embed = discord.Embed(description=menu_gia, color=discord.Color.blue())  # Chuyển vạch xanh nước biển
        embed.set_thumbnail(url='attachment://logo.png')  # Logo bé bên tay trái GHOSTY SWOOFER
        embed.set_image(url='attachment://amigos.gif')  # Chèn ảnh GIF vào trong menu
        embed.set_author(name='GHOSTY SWOOFER', icon_url='attachment://small_logo.png')  # Thêm logo bé cạnh GHOSTY SWOOFER
        embed.set_footer(text='BOT được phát triển bởi VÔ DANH', icon_url='attachment://small_logo.png')  # Gắn logo bé cạnh GHOSTY SWOOFER
        reply = await ctx.reply(files=[logo, small_logo, discord.File('amigos.gif', filename='amigos.gif')], embed=embed)  # Gửi và reply tin nhắn
        print("📌 Bảng Giá Đã Gửi Qua Lệnh")
    else:
        await ctx.send("❌ Bạn không có quyền sử dụng lệnh này hoặc bot không hoạt động trong server này.")

@bot.command()
async def ping(ctx):
    start_time = time.time()
    msg = await ctx.send("🏓 Pinging...")
    end_time = time.time()
    latency = round(bot.latency * 1000)
    duration = round((end_time - start_time) * 1000)
    await msg.edit(content=f"🏓 Pong! Bot latency: {latency}ms | API response time: {duration}ms")

@bot.command()
async def settup(ctx):
    await ctx.send("✅ Bot đã sẵn sàng hoạt động!")
    await banggia(ctx)  # Chạy lệnh banggia khi bot được setup

bot.run(TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot đang hoạt động!"

if __name__ == '__main__':
    os.system("pip install python-dotenv discord.py Flask")
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
