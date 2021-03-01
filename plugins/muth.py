"""
Available Commands
.muth"""

from telethon import events

import asyncio





@ultroid_cmd(
    pattern="muth$",
)
async def cko(ult):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

        await event.edit(input_str)

        animation_chars = [

            "8✊️===D",

            "8=✊️==D",

            "8==✊️=D",

            "8===✊️D",

            "8==✊️=D",

            "8=✊️==D",

            "8✊️===D",

            "8===✊️D💦",

            "8==✊️=D💦💦",

            "8=✊️==D💦💦💦"

        ]

        for i in animation_ttl:
        
            await asyncio.sleep(animation_interval)
        
            await event.edit(animation_chars[i % 8])

HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.HNDLR)}"})
