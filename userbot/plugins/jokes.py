"""COMMAND : .join , .pay , .work , .push , .aag , .climb, .fuckoff, .ohh, .suckit, .lovestory"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="join"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`━━━━━┓ \n┓┓┓┓┓┃\n┓┓┓┓┓┃　ヽ○ノ ⇦ Me When You Joined \n┓┓┓┓┓┃.     /　 \n┓┓┓┓┓┃ ノ) \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

@borg.on(admin_cmd(pattern="pay"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`█▀▀▀▀▀█░▀▀░░░█░░░░█▀▀▀▀▀█\n█░███░█░█▄░█▀▀░▄▄░█░███░█\n█░▀▀▀░█░▀█▀▀▄▀█▀▀░█░▀▀▀░█\n▀▀▀▀▀▀▀░▀▄▀▄▀▄█▄▀░▀▀▀▀▀▀▀\n█▀█▀▄▄▀░█▄░░░▀▀░▄█░▄▀█▀░▀\n░█▄▀░▄▀▀░░░▄▄▄█░▀▄▄▄▀▄▄▀▄\n░░▀█░▀▀▀▀▀▄█░▄░████ ██▀█▄\n▄▀█░░▄▀█▀█▀░█▄▀░▀█▄██▀░█▄\n░░▀▀▀░▀░█▄▀▀▄▄░▄█▀▀▀█░█▀▀\n█▀▀▀▀▀█░░██▀█░░▄█░▀░█▄░██\n█░███░█░▄▀█▀██▄▄▀▀█▀█▄░▄▄\n█░▀▀▀░█░█░░▀▀▀░█░▀▀▀▀▄█▀░\n▀▀▀▀▀▀▀░▀▀░░▀░▀░░░▀▀░▀▀▀▀`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()



@borg.on(admin_cmd(pattern="climb"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`😏/\n/▌ \n/ \\n████\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\😦\n╬╬/▌\n╬╬/\`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

@borg.on(admin_cmd(pattern="aag"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`😲💨  🔥\n/|\     🔥🔥\n/ \   🔥🔥🔥`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

@borg.on(admin_cmd(pattern="push"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`.      😎\n          |\👐\n         / \\\n━━━━━┓ ＼＼ \n┓┓┓┓┓┃\n┓┓┓┓┓┃ ヽ😩ノ\n┓┓┓┓┓┃ 　 /　\n┓┓┓┓┓┃  ノ)　 \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@borg.on(admin_cmd(pattern="work"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`📔📚           📚\n📓📚📖  😫  📚📚📓\n📕📚📚  📝  📗💻📘\n📖⁣📖📖📖📖📖📖📖📖`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

@borg.on(admin_cmd("fuckoff"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`......................................../´¯/) \n......................................,/¯../ \n...................................../..../ \n..................................../´.¯/\n..................................../´¯/\n..................................,/¯../ \n................................../..../ \n................................./´¯./\n................................/´¯./\n..............................,/¯../ \n............................./..../ \n............................/´¯/\n........................../´¯./\n........................,/¯../ \n......................./..../ \n....................../´¯/\n....................,/¯../ \n.................../..../ \n............./´¯/'...'/´¯¯`·¸ \n........../'/.../..../......./¨¯\ \n........('(...´...´.... ¯~/'...') \n.........\.................'...../ \n..........''...\.......... _.·´ \n............\..............( \n..............\.............\...`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
    
@borg.on(admin_cmd("suckit"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`......................................... \n \n𝕔𝕠𝕞𝕖 𝕥𝕠 𝕞𝕖, 𝕞𝕪 𝕔𝕙𝕚𝕝𝕕𝕣𝕖𝕟 \n`` \n. . /. ))) . . . . . . . . . (((ヽ \n/. .ノ￣. . . ___. . .￣ Y .\ \n| . (.\, . . . ( ͡° ͜ʖ ͡°). . . ./.) . ) \nヽ.ヽ..ᯢ._.|﹀|._._ノ₄₂₀ // \n. . .\|. 𓀐𓂸Ｙ. . ࿕. . . / \n. . . .|. \. . ᯪ. . .|. . ᯪ. . ﾉ \n. . . . . \ .トー仝ーイ \n. . . . . . . |. ミ土彡 / \n. . . . . . . )\. . .° . ./( \n. . . . . . /. . .\͎̦ ̷̫ ̴́ ̴̢/̴͖. . \ \n. . . . . /. ⁶⁹ . /̴͝Ѽ̔̕☰̴̈́☰☰☰☰D,̰̱ \n. . . . /. / . . / . . .\. \. . \ \n. . . .((. . . .(. . . . .). . . .)) \n. . . .| . . . .). . . . .(|. . . / \n. . . . |. . . /. . . . /. . . ./ \n. . . . |. . ..| . . . ./. . ./. . ... . . 𓁉𓀏𓀃𓁏`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete() 
    
    
@borg.on(admin_cmd("ohh"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`´´´´´████████´´\n´´`´███▒▒▒▒███´´´´´\n´´´███▒●▒▒●▒██´´´\n´´´███▒▒👄▒▒██´´\n´´█████▒▒████´´´´´\n´█████▒▒▒▒███´´\n█████▒▒▒▒▒▒███´´´´\n´´▓▓▓▓▓▓▓▓▓▓▓▓▓▒´´\n´´▒▒▒▒▓▓▓▓▓▓▓▓▓▒´´´´´\n´.▒▒▒´´▓▓▓▓▓▓▓▓▒´´´´´\n´.▒▒´´´´▓▓▓▓▓▓▓▒\n..▒▒.´´´´▓▓▓▓▓▓▓▒\n´▒▒▒▒▒▒▒▒▒▒▒▒\n´´´´´´´´´███████´´´´\n´´´´´´´´████████´´´´´´\n´´´´´´´█████████´´´´´\n´´´´´´██████████´´´\n´´´´´´██████████´´\n´´´´´´´█████████´\n´´´´´´´█████████´\n´´´´´´´´████████´´´\n´´´´´´´´´´´▒▒▒▒▒´´´\n´´´´´´´´´´▒▒▒▒▒´´´\n´´´´´´´´´´▒▒▒▒▒´´´\n´´´´´´´´´´▒▒´▒▒´´´\n´´´´´´´´´▒▒´´▒▒´´´\n´´´´´´´´´´▒▒´´´▒▒´´´\n´´´´´´´´´▒▒´´´▒▒´´´\n´´´´´´´´▒▒´´´´´▒▒´´´\n´´´´´´´´▒▒´´´´´´▒▒´´´\n´´´´´´´´███´´´´███´´´\n´´´´´´´´████´´███´´´\n´´´´´´´´█´´███´´████´´´`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
    
@borg.on(admin_cmd(pattern="lovestory"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    #input_str = event.pattern_match.group(1)

    #if input_str == "lovestory":

    await event.edit("Starting asf")

    animation_chars = [

            "1 ❤️ love story",
            "  😐             😕 \n/👕\         <👗\ \n 👖               /|",    
            "  😉          😳 \n/👕\       /👗\ \n  👖            /|",
            "  😚            😒 \n/👕\         <👗> \n  👖             /|",
            "  😍         ☺️ \n/👕\      /👗\ \n  👖          /|",
            "  😍          😍 \n/👕\       /👗\ \n  👖           /|",
            "  😘   😊 \n /👕\/👗\ \n   👖   /|",
            " 😳  😁 \n /|\ /👙\ \n /     / |",    
            "😈    /😰\ \n<|\      👙 \n /🍆    / |",
            "😅 \n/(),✊😮 \n /\         _/\\/|",
            "😎 \n/\\_,__😫 \n  //    //       \\",
            "😖 \n/\\_,💦_😋  \n  //         //        \\",
            "  😭      ☺️ \n  /|\   /(👶)\ \n  /!\   / \ ",
            "The End 😂..."
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 103])    
