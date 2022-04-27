from discord.ext import commands

__TOKEN__ = "Njc3OTEzNDYzNDY4ODUxMjA3.XkbKHA.kXISzPmEYJ69FHDFPi_BdqK9vcs"

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("::"),
    description="Filha primogênita do capitão.",
    case_insensitive=True
)
bot.remove_command("help")
