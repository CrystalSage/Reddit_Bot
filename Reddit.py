import asyncio, discord
from discord.ext import commands
from setup import *


bot = commands.Bot(command_prefix=config['Prefix'], case_insensitive=True)
bot.remove_command('help')

@bot.event
async def on_ready():
	print("Sigh...Unzips...")

@bot.event
async def on_disconnect():
    print("Zips...Sigh...")


@bot.command(aliases=['h'])
async def reddit_Help(ctx):
    subreddit_display="\n".join(subreddits)
    display_subreddits=f"Available subreddits are : {subreddit_display}"
    await ctx.message.author.create_dm()
    await ctx.message.author.send(display_subreddits)
    await ctx.message.channel.send("Invoke me with `reddit.r <subreddit>`.Check your DMs :wink:")



@bot.command(aliases=['r'])
async def get_Reddit(ctx,*args):
	subreddit="".join(args)
	subreddit=subreddit.lower()
    

	if ctx.message.channel.is_nsfw():
		Get_Reddit_Images=Reddit_API(subreddit)
		Url_Buffer=Get_Reddit_Images.get_submissions(subreddit)

		if Url_Buffer=="That's not in the list":
			return await ctx.message.channel.send(Url_Buffer)

		await ctx.message.channel.send("Fetching...")
		form,Image,name=Get_Reddit_Images.GET_image(Url_Buffer)

		return await ctx.message.channel.send(file=discord.File(fp=Image,filename=name+form))

	else:
	    return await ctx.message.channel.send("Wait, This is not a NSFW channel...")

    






bot.run(config['Token'])