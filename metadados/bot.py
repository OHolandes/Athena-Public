from discord.ext import commands

__TOKEN__ = "TOKEN"

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("::"),
    description="Filha primogênita do capitão.",
    case_insensitive=True
)
bot.remove_command("help")
