import discord
from discord.ext import commands
import tm
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def resim_kaydet(ctx):
    if ctx.message.attachments:
        for dosya in ctx.message.attachments:
            await dosya.save(f"./resim/{dosya.filename}")
            await ctx.send("resmin başarıyla kaydedildi.")
            x,y = tm.siyah(f'./resim/{dosya.filename}')
            a = round(y * 100,3)
            await ctx.send(f'Bu %{a} ihtimalle bir {x}')
            if x == 'Guvercin':
                await ctx.send('Bulgur ve pirinci bolca tüketen güvercinler oldukça sıcakkanlı canlılardır. Güvercinler aynı zamanda çeşitli sebzeleri de beraberinde tüketmektedir. Lahana, bezelye, karnabahar ve marul gibi yiyecekleri dilimleyerek güvercine verebilirsiniz. Dilerseniz petshoplarda yer alan güvercin yemlerini de tercih edebilirsiniz.')
            elif x == 'Serce':
                await ctx.send('Genellikle meyve, tohum, böcek ve larva gibi besinler tüketirler. Göçmen değildirler. Çekirdek ve ekmek artıkları da yerler.')
            elif x == 'Baykuslar':
                await ctx.send('Omnivor bir beslenme şekline sahiptirler, hemen hemen her şeyi yerler. Meyve, sebze, tahıl, kuruyemiş, besin çöpleri, leş, her türlü et çeşidi, böcekler, omurgasızlar, tohum, yavru kuşlar, kuş yumurtaları, yavru hayvanlar (kendinden boyut olarak küçük olan, yavru veya sakat olan canlıları avlayıp yerler)')
            elif x == 'Diger':
                await ctx.send('Uzgunuz maalesef bu kus veri setimizde bulunmuyor eger fotografta kusun belirli bir sekilde gozuktugunden eminsen bizlerle iltesime gecebilirsin')
            else:
                await ctx.send('Uzgunuz sistemsel bir sorun yasiyoruz sorun devam ederse bize bildirin')




    else:
        await ctx.send('Sanirim bir hata olustu tekrar deneyebilirsin')













































































bot.run('BOT TOKEN')