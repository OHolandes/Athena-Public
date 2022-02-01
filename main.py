import random
import asyncio
from random import randint, choice
from metadados.bot import __TOKEN__, bot
from metadados.variaveis import atividaddes, msg_ajuda, CANAIS_ADM, SAUDACOES

import discord
from discord.ext import commands


@bot.event
async def on_ready():
    print("=" * 30)
    print('Buenas tardes!')
    print("Estou pronta para trabalhar.")
    print(f"{bot.user.id:_^30}")
    print("-" * 30)

    while True:
        await bot.change_presence(activity=choice(choice(list(atividaddes.values()))))
        await asyncio.sleep(60)


class CommandsPrivate:

    @staticmethod
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def teste(ctx, times=5, _string="Testando"):
        """Repete a mensagem um número de vezes."""
        async with ctx.typing():
            type_time = random.uniform(0.5, 2)
            await asyncio.sleep(type_time)
        for i in range(times):
            await ctx.send(_string)

    @staticmethod
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def ping(ctx):
        await ctx.send(f"Pong! {bot.latency}")

    @staticmethod
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def idchn(ctx):
        await ctx.send(ctx.channel.id)

    @staticmethod
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def relatorio(ctx):
        async with ctx.typing():
            type_time = random.uniform(1, 3)
            await asyncio.sleep(type_time)

        destino = bot.get_channel(CANAIS_ADM["diretoria"])

        if ctx.channel != destino:
            await ctx.send(f"Pronto! Relatório enviado em {destino.mention}")

        temp_string = f"""
        Estatisticas:
        {ctx.guild.member_count} Membros.
        {ctx.guild.premium_subscription_count} Boosts.
        Nível: {ctx.guild.verification_level}.\n
        """

        temp_string += f"{len(ctx.guild.text_channels)} canais de texto:\n"
        for chn in ctx.guild.text_channels:
            temp_string += f"{chn.name} \t| ID:{chn.id} \t| nsfw:{chn.nsfw}\n"
        temp_string += "\n"

        temp_string += f"{len(ctx.guild.categories)} categorias:\n"
        for ctg in ctx.guild.categories:
            temp_string += f"{ctg.name} \t| ID:{ctg.id} \t| nsfw: {ctg.nsfw}\n"
        temp_string += "\n"

        temp_string += f"{len(ctx.guild.roles) - 1} cargos:\n"
        for rls in ctx.guild.roles[1:]:
            temp_string += f"{rls.name} \t| ID:{rls.id}\n"
        temp_string += "\n"

        await destino.send(ctx.author.mention)
        await destino.send(embed=discord.Embed(title=f"Relatório feito ao {ctx.author}\n"
                                                     f"ID: {ctx.author.id} ({ctx.author.roles[-1]})",
                                               description=temp_string,
                                               color=0xff0000))

    @staticmethod
    @bot.command()
    @commands.has_permissions(administrator=True, manage_messages=True)
    async def log(ctx, nome: discord.Member = None, limit=10, *, audit=False):
        async with ctx.typing():
            type_time = random.uniform(0.5, 2)
            await asyncio.sleep(type_time)
        if nome is None:
            nome = ctx.author
        cont = 0

        temp_string = f"Últimas {limit} mensagens de {nome.mention}:\n"
        async for msg in ctx.channel.history():
            if cont == limit:
                break
            else:
                if nome == msg.author:
                    temp_string += f"{msg.author}: {msg.content}\n"
                    cont += 1
        await ctx.send(temp_string)

        if audit:
            temp_string = f"Últimas {limit * 2} ações no servidor:"
            async for entrada in ctx.guild.audit_logs(limit=limit * 2):
                temp_string += f"{entrada.user}: {entrada.action} -> {entrada.target}\n"
            ctx.send(temp_string)

    @staticmethod
    @bot.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, nome: discord.Member):
        destino = bot.get_channel(CANAIS_ADM["secretaria"])
        await nome.kick()
        _string = f"""
        Nick: {nome.nick}
        **EXPULSO** por {ctx.author}
        """
        await destino.send(embed=discord.Embed(title="Usuário expulso:",
                                               description=_string,
                                               color=0xff0000))

    @staticmethod
    @bot.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, nome: discord.Member):
        destino = bot.get_channel(CANAIS_ADM["secretaria"])
        await nome.ban()
        _string = f"""
        Nick: {nome.nick}
        **BANIDO** por {ctx.author}
        """
        await destino.send(embed=discord.Embed(title="Usuário banido:",
                                               description=_string,
                                               color=0xff0000))

    @staticmethod
    @bot.command()
    @commands.has_permissions(ban_members=True)
    async def desban(ctx, nome: discord.Member):
        destino = bot.get_channel(CANAIS_ADM["secretaria"])
        await nome.unban()
        _string = f"""
        Nick: {nome.nick}
        **desbanido** por {ctx.author}
        """
        await destino.send(embed=discord.Embed(title="Usuário desbanido:",
                                               description=_string,
                                               color=0xff0000))


class CommandsPublic:

    @staticmethod
    @bot.command(aliases=("oi", "iai", "athena"))
    async def ola(ctx):
        async with ctx.typing():
            type_time = random.uniform(0.5, 2)
            await asyncio.sleep(type_time)
        resp = choice(SAUDACOES)
        await ctx.send(resp)

    @staticmethod
    @bot.command()
    async def soma(ctx, *nums: int):
        """Somo uns números números."""
        async with ctx.typing():
            type_time = random.uniform(0.5, 2)
            await asyncio.sleep(type_time)
        await ctx.send(str(sum(nums)))

    @staticmethod
    @bot.command(aliases=("dado",))
    async def rola(ctx, dice: str):
        """Lança um dado em formato NdN."""
        async with ctx.typing():
            type_time = random.uniform(0.5, 2)
            await asyncio.sleep(type_time)
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('O formato tem de estar em NdN!')
            return

        result = ', '.join(str(randint(1, limit)) for _ in range(rolls))
        await ctx.send(result)

    @staticmethod
    @bot.command(description='Quando se quer ajustar as contas de outra forma', aliases=("prefere",))
    async def escolha(ctx, *choices: str):
        """Escolhas entre escolhas."""
        async with ctx.typing():
            type_time = random.uniform(0.5, 2)
            await asyncio.sleep(type_time)
        await ctx.send(choice(choices))

    @staticmethod
    @bot.command()
    async def ajuda(ctx):
        async with ctx.typing():
            type_time = random.uniform(0.5, 2)
            await asyncio.sleep(type_time)
        await ctx.send(embed=discord.Embed(title="Alguns comandozinhos",
                                           description=msg_ajuda,
                                           color=0xff0000))

    @staticmethod
    @bot.command()
    async def meuid(ctx):
        await ctx.send(ctx.author.id)

    @staticmethod
    @bot.command()
    async def cool(ctx):
        """Isso é cool?"""
        async with ctx.typing():
            type_time = random.uniform(0.5, 2)
            await asyncio.sleep(type_time)

        msg = ctx.message.content

        if msg.lower() == "athena":
            await ctx.send('Sim, Essa é COOL.')
        else:
            await ctx.send(f'Não, {msg} não é cool.')


bot.run(__TOKEN__)
