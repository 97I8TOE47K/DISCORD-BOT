import discord
from discord import message
from discord import *
from discord.ext import commands
import requests
import json
from pprint import pprint
from weather import *
from keep_alive import *


client = discord.Client()
api_key = "API_KEY"
cmd1 = commands.Bot(command_prefix='$')
cmds = '$hello\n$name\n$version\n$info\n$help\n$inspire\n$devinfo\n$joke\n$cat_fact\n$weather (Syntax: `$weather [City]`, e.g. `$weather Lucknow`)'



#functions to be performed
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=racist&type=single")
    json_data = json.loads(response.text)
    joke = json_data["joke"]
    return (joke)    



#on ready function
@client.event
async def on_ready():
  #The bot is watching commands and nerdy stuff
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$help"))
  print('ICBM launched by {0.user}, expect destruction soon (of your brain). Dimag Tikka Order being made...'.format(client))


#executables
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello there! I am a friendly, general-purpose, nerdy bot made by abhishek#4309')

  if message.content.startswith('$name'):
    await message.channel.send('Hello my name is AxC 777')

  if message.content.startswith('$version'):
    my_embed = discord.Embed(title = "Current version", description = "The bot is in version 0.1, currently in Pre-Alpha stage of development", color = 0x00ff00)
    my_embed.add_field(name ="version code:", value ="v0.1", inline=False)
    my_embed.add_field(name = "Time Released:", value="Sep 21", inline=False)
    my_embed.set_footer(text="")
    my_embed.set_author(name="abhishek#4309")
    await message.channel.send(embed = my_embed)

  if message.content.startswith('$info'):
    my_embed = discord.Embed(title = "Name:", description = "AxC 777", color = 0x00ff00)
    my_embed.add_field(name ="Description:", value ="A Genral Purpose Discord Bot, currently in it's infancy, made by Abhishek", inline=False)
    my_embed.add_field(name = "Version Info:", value="0.1 (Pre-Alpha)" )
    my_embed.set_footer(text="")
    my_embed.set_author(name="abhishek#4309")
    await message.channel.send(embed = my_embed)
    
  if message.content.startswith('$devinfo'):
    my_embed = discord.Embed(title = "The Creator himself:", description = "Abhishek Saxena")
    my_embed.add_field(name = "Creator description:", value="Just a *Homo sapien* with God powers in programming", inline=False)
    my_embed.add_field (name = "Co-Creator:", value = "Chinmay Krishna", inline=False)
    my_embed.add_field(name = "Creator description:", value="A person that has more knowledge in physics than our physics teacher",inline=False)
    await message.channel.send(embed = my_embed)

  if message.content.startswith('$help'):
    my_embed = discord.Embed(title = "All commands:", description = cmds, color = 0x00ff00)
    my_embed.set_author(name="abhishek#4309")
    await message.channel.send(embed = my_embed)

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('$joke'):
    joke = get_joke()
    await message.channel.send(joke)

  if message.content.startswith('$cat_fact'):
    data = requests.get('https://catfact.ninja/fact').json()
    embed = discord.Embed(title=f'Random Cat Fact Number: **{data["length"]}**', description=f'Cat Fact: {data["fact"]}', colour=0x400080)
    embed.set_footer(text="")
    await message.channel.send(embed=embed)    

  if message.content.startswith('$weather'):
            location = message.content.replace("$weather ", '')
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            try:
                data = parse_data(json.loads(requests.get(url).content)['main'])
                await message.channel.send(embed=weather_message(data, location))
            except KeyError:
                await message.channel.send(embed=error_message(location))


#keep_alive()
client.run('Bot Token')
