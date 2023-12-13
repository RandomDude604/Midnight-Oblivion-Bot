import discord
from discord.ext import commands, tasks

intents = discord.Intents.all()
intents.messages = True  # Enable message-related events

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    announce_loop.start()

@tasks.loop(minutes=1)  # Adjust the time interval as needed
async def announce_loop():
    # Check for new announcements, e.g., in a specific channel
    # Implement your logic to fetch announcements and send them
    pass

@bot.command(name='announce')
async def announce(ctx, *, message):
    # Command to allow moderators to send announcements
    if ctx.author.guild_permissions.manage_messages:
        # Implement logic to send announcements to a specific channel
        channel_id = 1184557214908825630  # Replace with your channel ID
        channel = bot.get_channel(channel_id)
        await channel.send(f'rahhhhh')
    else:
        await ctx.send("You don't have the required permissions to use this command.")

# Run the bot with the token

bot.run('YMTE4NDU1MDIzMDYyMDkxNzg4MA.GrHQGH.tSHqUTOOvYC8RZ1HzKHJ0r3YlZl2QbX0humhYQ')

@bot.event
async def on_disconnect():
    print("Bot disconnected. Reconnecting...")
