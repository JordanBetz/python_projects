import nextcord
from nextcord.ext import commands
from nextcord.shard import EventItem
import wavelink

bot_version = "0.0.1"

intents = nextcord.Intents.all()
client = nextcord.Client()
bot = commands.Bot("commands_prefix='.'", intents=intents)

@bot.event
async def on_ready():
    print("Bot Ready!")
    bot.loop.create_task(on_node())
    
async def on_node():
    node:  wavelink.Node = wavelink.Node(uri = 'https://lavalink.devamop.in:443', password='DevamOP')
    await wavelink.Pool.connect(client=bot, nodes=[node])
    wavelink.Player.autoplay = True
    
@bot.slash_command(guild_ids=[708632631901683723])
async def play(interaction : nextcord.Interaction, search : str):
    query = await wavelink.YouTubeTrack.search(search, return_first=True)
    destination = interaction.user.voice.channel
    
    if not interaction.guid.voice_client:
        vc: wavelink.Player = await destination.connect(cls=wavelink.Player)
    else:
        vc: wavelink.Player = interaction.guild.voice_client
        
    if vc.queue.is_empty and not vc.is_playing():
        await vc.play(query)
        await interaction.response.send_message(f"Now Playing {vc.current.title}")
    else:
        await vc.queue.put_wait(query)
        await interaction.response.send_message(f"Song was added to the queue")
        
@bot.slash_command(guild_ids=[708632631901683723])
async def skip(interaction : nextcord.Interaction):
    vc: wavelink.Player = interaction.guild.voice_client
    await vc.stop()
    await interaction.response.send_message(f"Song was skipped!")
    
@bot.slash_command(guild_ids=[708632631901683723])
async def pause(interaction : nextcord.Interaction):
    vc: wavelink.Player = interaction.guild.voice_client
    
    if vc.is_playing():
        await vc.pause()
        await interaction.response.send_message(f"Song was paused!")
    else:
        await interaction.response.send_message(f"Song is already paused!")
        
@bot.slash_command(guild_ids=[708632631901683723])
async def resume(interaction : nextcord.Interaction):
    vc: wavelink.Player = interaction.guild.voice_client
    
    if not vc.is_paused():
        await interaction.response.send_message(f"Song is already resumed!")
    else:
        await interaction.response.send_message(f"Song is resumed!")
        await vc.resume()
        
@bot.slash_command(guild_ids=[708632631901683723])
async def disconnect(interaction : nextcord.Interaction):
    vc: wavelink.Player = interaction.guild.voice_client
    await vc.disconnect()
    await interaction.response.send_message(f"The bot was disconnected!")
    
@bot.slash_command(guild_ids=[708632631901683723])
async def disconnect(interaction : nextcord.Interaction):
    vc: wavelink.Player = interaction.guild.voice_client
    
    if not vc.queue.is_empty:
        song_counter = 0
        songs = []
        queue = vc.queue.copy()
        embed = nextcord.Embed(title="Queue")
        
        for song in queue:
            song_counter += 1
            songs.append(song)
            embed.add_field(name=f"[{song_counter}] Duration {song.duration}", value=f"{song.title}", inline=False)
        
        await interaction.response.send_message(f"The bot was disconnected!")
        
    else:
        await interaction.response.send_message("The queue is empty!")

bot.run('MTIwMTUzMDg5ODk0MDY5NDUzOA.G-7M_5.E87hv5FLJiOEO980mrLdMWm6GliMngxOF7IIbw')