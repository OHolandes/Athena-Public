from datetime import datetime
import random
import asyncio
from random import randint, choice
from metadados.bot import __TOKEN__, bot
from metadados.variaveis import (
                                msg_ajuda, 
                                CANAIS_ADM,
                                SAUDACOES,
                                GUIA_ANONIMA_ID,
                                alta_ajuda
                                )
from Atividades.base import atividades

import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.messages = True


@bot.event
async def on_ready():
    print("=" * 30)
    print("Estou pronta para trabalhar.")
    print(f"{str(bot.user):_^30}")
    print("-" * 30)

    while True:
        await bot.change_presence(activity=choice(choice(list(atividades.values()))))
        await asyncio.sleep(60)


def is_pin(msg):
        """
        Para não deletar mensagens pinadas.
        """
        return not msg.pinned


class CommandsPrivate:
    embed_missing_perm = discord.Embed(title="Permissão Negada.", 
                                        description="Você não tem permissão para usar este comando.",
                                        color=0xffa500)

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
    async def prompt(ctx):
        last_message = ""
        await ctx.send('Agora estarei monitorando suas mensagens... Mande "exit" para encerrar.')
        while True:
            msg = await ctx.channel.fetch_message(ctx.channel.last_message_id)
            if last_message != msg.content:
                if msg.author == ctx.author:
                    if "exit" in msg.content:
                        await ctx.send("Fechando console...")
                        break
                    else:
                        try:
                            await ctx.send(eval(msg.content))
                        except Exception as error:
                            await ctx.send(str(error))
                    last_message = msg.content
            await asyncio.sleep(1)


    @staticmethod
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def ping(ctx):
        await ctx.send(f"Pong! {bot.latency}")


    @staticmethod
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def cep(ctx):
        await ctx.send(ctx.channel.id)


    @staticmethod
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def relatorio(ctx):
        async with ctx.typing():
            type_time = random.uniform(1, 3)
            await asyncio.sleep(type_time)

        destino: discord.TextChannel = bot.get_channel(CANAIS_ADM["diretoria"])

        if ctx.channel != destino:
            await ctx.send(f"Pronto! Relatório enviado em {destino.mention}")

        temp_string = """
        Estatisticas:
        _{} Membros_.
        _{} Boosts_.
        Nível de verificação: _{}_.
        Limite de emojis: {}\n
        """.format(ctx.guild.member_count, 
                    ctx.guild.premium_subscription_count, 
                    ctx.guild.verification_level,
                    ctx.guild.emoji_limit
                )

        temp_string += f"Canais de texto **x{len(ctx.guild.text_channels)}**:\n\n"
        for chn in ctx.guild.text_channels:
            temp_string += "**{}** | ID:_{}_ \t| nsfw:{}\n".format(chn.name, chn.id, 'sim' if chn.nsfw else 'não')
        temp_string += "\n"

        temp_string += f"Categorias **x{len(ctx.guild.categories)}**:\n\n"
        for ctg in ctx.guild.categories:
            temp_string += "**{}** | ID:_{}_ | nsfw: {}\n".format(ctg.name, ctg.id, 'sim' if ctg.nsfw else 'não')
        temp_string += "\n"

        temp_string += f"Cargos **x{len(ctx.guild.roles) - 1}**:\n\n"
        for rls in ctx.guild.roles[-1::-1]:
            temp_string += "**{}** | ID:_{}_\n".format(rls.name, rls.id)
        temp_string += "\n"

        await destino.send(ctx.author.mention)
        await destino.send(embed=discord.Embed(title=f"Relatório feito ao {ctx.author}\n"
                                                     f"ID: _{ctx.author.id}_ ({ctx.author.roles[-1]})",
                                               description=temp_string,
                                               color=0xff0000))


    @staticmethod
    @bot.command()
    @commands.has_permissions(manage_messages=True)
    async def log(ctx, *args):
        limit = 15
        async with ctx.typing():
            type_time = random.uniform(0.5, 2)
            await asyncio.sleep(type_time)
        nome = " ".join(args)
        if not nome:
            nome = ctx.author.display_name
        cont = 0

        temp_string = f"Últimas {limit} mensagens de {nome}:\n"
        async for msg in ctx.channel.history():
            if cont == limit:
                break
            else:
                if nome == msg.author.display_name or nome == msg.author.mention:
                    temp_string += f"{msg.author}: {msg.content}\n"
                    cont += 1
        await ctx.send(temp_string)


    @staticmethod
    @bot.command()
    @commands.has_permissions(manage_messages=True)
    async def faxina(ctx, limit:int = 100):
        await ctx.channel.purge(limit=limit + 1, check=is_pin)


    @staticmethod
    @bot.command()
    @commands.has_permissions(manage_messages=True)
    async def basta(ctx):
        react = discord.utils.get(ctx.guild.emojis, name="Crusanos")
        await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=True,
                                                send_messages=False)
        await ctx.message.add_reaction(react)


    @staticmethod
    @bot.command()
    @commands.has_permissions(manage_messages=True)
    async def liberado(ctx):
        react = discord.utils.get(ctx.guild.emojis, name="confusedwat")
        await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=True,
                                                send_messages=True)
        await ctx.message.add_reaction(react)
    

    @staticmethod
    @bot.command()
    @commands.has_permissions(manage_messages=True)
    async def aviso(ctx, membro: discord.Member):
        rol = discord.utils.get(ctx.guild.roles, name="Avisado")
        if not rol in membro.roles:
            await membro.add_roles(rol)
        else:
            await membro.remove_roles(rol)


    @staticmethod
    @bot.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, nome: discord.Member, *motivo: str):
        destino: discord.TextChannel = bot.get_channel(CANAIS_ADM["secretaria"])
        await nome.kick()
        if not motivo:
            motivo = "Sem motivo ||abuso de autoridade...||"
        else:
            motivo = " ".join(motivo)
        _string = f"""
        **Nick:** {nome.display_name}
        **Expulsão feita por** {ctx.author}
        **Motivo:** {motivo}
        """
        await destino.send(embed=discord.Embed(title="Usuário expulso:",
                                               description=_string,
                                               color=0xff0000).set_image(url="https://j.gifs.com/Kj1P90.gif"))


    @staticmethod
    @bot.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, nome: discord.Member, *motivo: str):
        destino: discord.TextChannel = bot.get_channel(CANAIS_ADM["secretaria"])
        await nome.ban()
        if not motivo:
            motivo = "Sem motivo ||abuso de autoridade...||"
        else:
            motivo = " ".join(motivo)
        _string = f"""
        **Nick:** {nome.display_name}
        **Banimento feito por** {ctx.author}
        **Motivo:** {motivo}
        """
        await destino.send(embed=discord.Embed(title="Usuário banido:",
                                               description=_string,
                                               color=0xff0000).set_image(url="https://c.tenor.com/MyqcGt-kAN8AAAAC/banido.gif"))


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
            await ctx.send('O formato tem que estar em NdN!')
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
    async def stalk(ctx, nome: discord.member.BaseUser = ""):
        vc = nome if nome != "" else ctx.author
        async with ctx.typing():
            type_time = random.uniform(0.5, 2)
            await asyncio.sleep(type_time)
        _string = f"""
        Seu cracha(ID): _{vc.id}_
        Entrou aqui em: **{vc.joined_at:%d-%m-%Y %H:%M}**
        Seu cargo mais alto: **{vc.top_role}**
        Está no Discord desde: **{vc.created_at:%d-%m-%Y %H:%M}**
        """
        await ctx.send(embed=discord.Embed(
            title=f"Tag:`{vc.name}#{vc.discriminator}`/**{vc.display_name}**",
            description=_string, colour=0xff0000).set_thumbnail(url=vc.avatar_url)
        )


    @staticmethod
    @bot.command()
    async def privilegios(ctx):
        pms = ctx.author.permissions_in(ctx.channel)
        privis = f"""
        **Administrador**: {"sim" if pms.administrator else "não(ufa!)"}

        **Neste canal:**
        Gerenciar emojis: {"sim" if pms.manage_emojis else "não"}
        Gerenciar canais: {"sim" if pms.manage_channels else "não"}
        Gerenciar mensagens: {"sim" if pms.manage_messages else "não"}
        Enviar arquivos: {"sim" if pms.attach_files else "não"}
        Usar emojis externos: {"sim" if pms.use_external_emojis else "não"}

        **Geral:**
        Mudar apelido: {"sim" if pms.change_nickname else "não"}
        Gerenciar apelidos: {"sim" if pms.manage_nicknames else "não"}
        Gerenciar cargos: {"sim" if pms.manage_permissions else "não"}
        Ver auditoria: {"sim" if pms.view_audit_log else "não"}
        Kickar Membros: {"sim" if pms.kick_members else "não"}
        Banir membros: {"sim" if pms.ban_members else "não"}
        """
        await ctx.send(embed=discord.Embed(
                                        title="Suas permissões:",
                                        description=privis
                                    )
                    )

    @staticmethod
    @bot.command()
    async def cool(ctx, string:str):
        """Isso é cool?"""
        async with ctx.typing():
            type_time = random.uniform(0.5, 2)
            await asyncio.sleep(type_time)

        if "thena" in string:
            await ctx.send('Sim, Essa é COOL.')
        else:
            await ctx.send(f'Não, isso não é cool.')


    @staticmethod
    @bot.command()
    async def convite(ctx):
        await ctx.send("https://discord.gg/DyNMgay")


    @staticmethod
    @bot.command()
    async def chegamais(ctx, *guests: discord.Member):
        if not guests:
            await ctx.send("Irá conversar sozinho(a), jovem?")

        elif ctx.channel.category_id != GUIA_ANONIMA_ID:
            hehe = discord.utils.get(bot.emojis, name="Cringe")
            category_private = discord.utils.get(ctx.guild.categories, id=GUIA_ANONIMA_ID)
            embedincog = f"""
            Foi mal, mas você não está num canal apropriado para isso.
            Só posso deixar vocês "a sós" {hehe} nestes canais:
            """

            for chn in category_private.channels:
                embedincog += chn.mention

            embed_incog = discord.Embed(title="Não se precipite.", description=embedincog,
                                        color=0xffa500)
            await ctx.send(embed=embed_incog)

        else:
            await ctx.send("Preparando o canal...")
            await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=False)
            conservative = [guest for guest in guests]
            conservative.append(ctx.author)

            for people in conservative:
                await ctx.channel.set_permissions(people, read_messages=True)

            await ctx.send("Pronto!")
            await ctx.send("Obs: lembrando que administradores e moderadores ainda tem acesso a esse canal")
            await ctx.send(f"Não viole as <#441263333807751178> nem as diretrizes do Discord")

            init_message = await ctx.channel.fetch_message(ctx.channel.last_message_id)
            last_message = init_message
            seconds = 0

            while (init_message == last_message) and (seconds < 600):
                last_message = await ctx.channel.fetch_message(ctx.channel.last_message_id)
                if init_message != last_message:
                    seconds = 0
                    init_message = last_message
                await asyncio.sleep(1)
                seconds += 1

            await ctx.send(f"{ctx.author.mention} tempo limite excedido!")
            await ctx.send("Puxando a descarga em **5** segundos")
            await asyncio.sleep(5)
            await ctx.channel.purge(limit=999)
            await ctx.channel.edit(sync_permissions=True)


    @staticmethod
    @bot.command(aliases=("comandos",))
    async def ajuda(ctx, _command: str = None):
        if _command in [cmd.name for cmd in bot.commands]:
            await ctx.send(embed=discord.Embed(title="::"+_command,
                                            description=alta_ajuda[_command],
                                            color=0xff0000))
        else:
            async with ctx.typing():
                type_time = random.uniform(0.5, 2)
                await asyncio.sleep(type_time)
            await ctx.send(embed=discord.Embed(title="Veja oquê eu posso fazer...",
                                            description=msg_ajuda,
                                            color=0xff0000))



@CommandsPrivate.teste.error
async def raise_permission(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send(ctx.author.mention, embed=CommandsPrivate.embed_missing_perm)
    else:
        raise error


@CommandsPrivate.prompt.error
async def raise_permission(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send(ctx.author.mention, embed=CommandsPrivate.embed_missing_perm)
    else:
        raise error

@CommandsPrivate.ping.error
async def raise_permission(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send(ctx.author.mention, embed=CommandsPrivate.embed_missing_perm)
    else:
        raise error


@CommandsPrivate.relatorio.error
async def raise_permission(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send(ctx.author.mention, embed=CommandsPrivate.embed_missing_perm)
    else:
        raise error


@CommandsPrivate.faxina.error
async def raise_permission(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send(ctx.author.mention, embed=CommandsPrivate.embed_missing_perm)
    else:
        raise error


@CommandsPrivate.ban.error
async def raise_permission(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send(ctx.author.mention, embed=CommandsPrivate.embed_missing_perm)
    else:
        raise error


@CommandsPrivate.kick.error
async def raise_permission(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send(ctx.author.mention, embed=CommandsPrivate.embed_missing_perm)
    else:
        raise error


@CommandsPrivate.cep.error
async def raise_permission(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send(ctx.author.mention, embed=CommandsPrivate.embed_missing_perm)
    else:
        raise error


@CommandsPrivate.liberado.error
async def raise_permission(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send(ctx.author.mention, embed=CommandsPrivate.embed_missing_perm)
    else:
        raise error


@CommandsPrivate.log.error
async def raise_permission(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send(ctx.author.mention, embed=CommandsPrivate.embed_missing_perm)
    else:
        raise error


@CommandsPrivate.basta.error
async def raise_permission(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send(ctx.author.mention, embed=CommandsPrivate.embed_missing_perm)
    else:
        raise error


bot.run(__TOKEN__)
