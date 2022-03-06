import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=".",case_insensitive=True,intents=intents) #Você pode trocar o "." do prefixo por outro símbolo como !, >, <, $, etc..
import random

#Mostra no console quando está online
@client.event
async def on_ready():
  print("Estou online!")

#Comando de mensagem simples
@client.command()
async def oi(ctx):
  await ctx.send(f"Olá, {ctx.author.mention}")

#Comando de embed
@client.command()
async def embed(ctx):
  embed=discord.Embed(
    title="Título da embed",
    description="Descrição da embed",
    color=1752220
  )
  embed.add_field(
    name="Field 1",
    value="Valor do field 1",
  )
  embed.add_field(
    name="Field 2",
    value="Valor do field 2",
    inline=True
  )
  embed.add_field(
    name="Field 3",
    value="Valor do field 3",
    inline=False
  )
  
  await ctx.send(embed=embed)

#Comando do dado
@client.command()
async def dado(ctx,num):
  variavel=random.randint(1,int(num))
  await ctx.send(f"O número do dado foi {variavel}")

#Comando da moeda
@client.command()
async def moeda(ctx,lado):
  variavel=random.randint(1,2)
  if variavel == 1:
    await ctx.send(f"O lado da moeda que saiu foi Cara.")
  if variavel == 2:
    await ctx.send(f"O lado da moeda que saiu foi Coroa.")

#Manda mensagem de boas vindas
@client.event
async def on_member_join(member):
  canalboasvindas=client.get_channel(ID do canal) #Coloque o ID canal de boas vindas ali
  await canalboasvindas.send(f"Seja bem vind@ {member.mention}")

client.run('TOKEN')
