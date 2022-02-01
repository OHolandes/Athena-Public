from discord.ext import commands

__TOKEN__ = "Njc3OTEzNDYzNDY4ODUxMjA3.XkbKHA.d5OVBxGNsMGUUXRMBRoipkgi7u8"

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("."),
    description="Filha primogênita do capitão.",
    case_insensitive=True
)
bot.remove_command("help")

intents = bot.intents.all()
