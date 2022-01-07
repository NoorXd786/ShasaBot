import html
import json
import os
from typing import Optional

from telegram import ParseMode, TelegramError, Update
from telegram.ext import CallbackContext, CommandHandler
from telegram.utils.helpers import mention_html

from ShasaBot import (
    DEV_USERS,
    FAFNIRS,
    LUINORS,
    OWNER_ID,
    REDLIONS,
    SPRYZONS,
    dispatcher,
)
from ShasaBot.modules.helper_funcs.chat_status import (
    dev_plus,
    sudo_plus,
    whitelist_plus,
)
from ShasaBot.modules.helper_funcs.extraction import extract_user
from ShasaBot.modules.log_channel import gloggable

ELEVATED_USERS_FILE = os.path.join(os.getcwd(), "ShasaBot/elevated_users.json")


def check_user_id(user_id: int, context: CallbackContext) -> Optional[str]:
    bot = context.bot
    if not user_id:
        reply = "That...is a chat! baka ka omae?"

    elif user_id == bot.id:
        reply = "This does not work that way."

    else:
        reply = None
    return reply


# This can serve as a deeplink example.
# disasters =
# """ Text here """

# do not async, not a handler
# def send_disasters(update):
#    update.effective_message.reply_text(
#        disasters, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

### Deep link example ends


@dev_plus
@gloggable
def addsudo(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in REDLIONS:
        message.reply_text("This member is already a RedLion Disaster")
        return ""

    if user_id in SPRYZONS:
        rt += "Requested HA to promote a Spryzon Disaster to RedLion."
        data["supports"].remove(user_id)
        SPRYZONS.remove(user_id)

    if user_id in LUINORS:
        rt += "Requested HA to promote a Luinor Disaster to RedLion."
        data["whitelists"].remove(user_id)
        LUINORS.remove(user_id)

    data["sudos"].append(user_id)
    REDLIONS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt
        + "\nSuccessfully set Disaster level of {} to RedLion!".format(
            user_member.first_name
        )
    )

    log_message = (
        f"#SUDO\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

    return log_message


@sudo_plus
@gloggable
def addsupport(
    update: Update,
    context: CallbackContext,
) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in REDLIONS:
        rt += "Requested HA to demote this RedLion to Spryzon"
        data["sudos"].remove(user_id)
        REDLIONS.remove(user_id)

    if user_id in SPRYZONS:
        message.reply_text("This user is already a Spryzon Disaster.")
        return ""

    if user_id in LUINORS:
        rt += "Requested HA to promote this Luinor Disaster to Spryzon"
        data["whitelists"].remove(user_id)
        LUINORS.remove(user_id)

    data["supports"].append(user_id)
    SPRYZONS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt + f"\n{user_member.first_name} was added as a Spryzon Disaster!"
    )

    log_message = (
        f"#SUPPORT\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

    return log_message


@sudo_plus
@gloggable
def addwhitelist(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in REDLIONS:
        rt += "This member is a RedLion Disaster, Demoting to Luinor."
        data["sudos"].remove(user_id)
        REDLIONS.remove(user_id)

    if user_id in SPRYZONS:
        rt += "This user is already a Spryzon Disaster, Demoting to Luinor."
        data["supports"].remove(user_id)
        SPRYZONS.remove(user_id)

    if user_id in LUINORS:
        message.reply_text("This user is already a Luinor Disaster.")
        return ""

    data["whitelists"].append(user_id)
    LUINORS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt + f"\nSuccessfully promoted {user_member.first_name} to a Luinor Disaster!"
    )

    log_message = (
        f"#WHITELIST\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))} \n"
        f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

    return log_message


@sudo_plus
@gloggable
def addfafnir(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in REDLIONS:
        rt += "This member is a RedLion Disaster, Demoting to Fafnir."
        data["sudos"].remove(user_id)
        REDLIONS.remove(user_id)

    if user_id in SPRYZONS:
        rt += "This user is already a Spryzon Disaster, Demoting to Fafnir."
        data["supports"].remove(user_id)
        SPRYZONS.remove(user_id)

    if user_id in LUINORS:
        rt += "This user is already a Luinor Disaster, Demoting to Fafnir."
        data["whitelists"].remove(user_id)
        LUINORS.remove(user_id)

    if user_id in FAFNIRS:
        message.reply_text("This user is already a Fafnir.")
        return ""

    data["fafnirs"].append(user_id)
    FAFNIRS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt + f"\nSuccessfully promoted {user_member.first_name} to a Fafnir Disaster!"
    )

    log_message = (
        f"#FAFNIR\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))} \n"
        f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

    return log_message


@dev_plus
@gloggable
def removesudo(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in REDLIONS:
        message.reply_text("Requested HA to demote this user to Civilian")
        REDLIONS.remove(user_id)
        data["sudos"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#UNSUDO\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = "<b>{}:</b>\n".format(html.escape(chat.title)) + log_message

        return log_message

    else:
        message.reply_text("This user is not a RedLion Disaster!")
        return ""


@sudo_plus
@gloggable
def removesupport(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in SPRYZONS:
        message.reply_text("Requested HA to demote this user to Civilian")
        SPRYZONS.remove(user_id)
        data["supports"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#UNSUPPORT\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

        return log_message

    else:
        message.reply_text("This user is not a Spryzon level Disaster!")
        return ""


@sudo_plus
@gloggable
def removewhitelist(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in LUINORS:
        message.reply_text("Demoting to normal user")
        LUINORS.remove(user_id)
        data["whitelists"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#UNWHITELIST\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

        return log_message
    else:
        message.reply_text("This user is not a Luinor Disaster!")
        return ""


@sudo_plus
@gloggable
def removefafnir(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in FAFNIRS:
        message.reply_text("Demoting to normal user")
        FAFNIRS.remove(user_id)
        data["fafnirs"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#UNFAFNIR\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

        return log_message
    else:
        message.reply_text("This user is not a Fafnir Disaster!")
        return ""


@whitelist_plus
def whitelistlist(update: Update, context: CallbackContext):
    reply = "<b>Known Luinor Disasters 🐺:</b>\n"
    m = update.effective_message.reply_text(
        "<code>Gathering Luinors..</code>", parse_mode=ParseMode.HTML
    )
    bot = context.bot
    for each_user in LUINORS:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)

            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)


@whitelist_plus
def fafnirlist(update: Update, context: CallbackContext):
    reply = "<b>Known Fafnir Disasters 🐯:</b>\n"
    m = update.effective_message.reply_text(
        "<code>Gathering Fafnirs..</code>", parse_mode=ParseMode.HTML
    )
    bot = context.bot
    for each_user in FAFNIRS:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)


@whitelist_plus
def supportlist(update: Update, context: CallbackContext):
    bot = context.bot
    m = update.effective_message.reply_text(
        "<code>Gathering Spryzons..</code>", parse_mode=ParseMode.HTML
    )
    reply = "<b>Known Spryzon Disasters 👹:</b>\n"
    for each_user in SPRYZONS:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)


@whitelist_plus
def sudolist(update: Update, context: CallbackContext):
    bot = context.bot
    m = update.effective_message.reply_text(
        "<code>Gathering Redlions..</code>", parse_mode=ParseMode.HTML
    )
    true_sudo = list(set(REDLIONS) - set(DEV_USERS))
    reply = "<b>Known RedLion Disasters 🐉:</b>\n"
    for each_user in true_sudo:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)


@whitelist_plus
def devlist(update: Update, context: CallbackContext):
    bot = context.bot
    m = update.effective_message.reply_text(
        "<code>Gathering Devs..</code>", parse_mode=ParseMode.HTML
    )
    true_dev = list(set(DEV_USERS) - {OWNER_ID})
    reply = "<b>Hero Association Members ⚡️:</b>\n"
    for each_user in true_dev:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)


# __help__ = f"""
# *⚠️ Notice:*
# Commands listed here only work for users with special access are mainly used for troubleshooting, debugging purposes.
# Group admins/group owners do not need these commands.
#
# *List all special users:*
# ❍ /REDLIONS*:* Lists all RedLion disasters
# ❍ /spryzon*:* Lists all Spryzon disasters
# ❍ /fafnirs*:* Lists all Fafnirs disasters
# ❍ /luinors*:* Lists all Luinor disasters
# ❍ /heroes*:* Lists all Hero Association members
# ❍ /addredlion*:* Adds a user to RedLion
# ❍ /addspryzon*:* Adds a user to Spryzon
# ❍ /addfafnir*:* Adds a user to Fafnir
# ❍ /addluinor*:* Adds a user to Luinor
# ❍ `Add dev doesnt exist, devs should know how to add themselves`
#
# *Ping:*
# ❍ /ping*:* gets ping time of bot to telegram server
# ❍ /pingall*:* gets all listed ping times
#
# *Broadcast: (Bot owner only)*
# *Note:* This supports basic markdown
# ❍ /broadcastall*:* Broadcasts everywhere
# ❍ /broadcastusers*:* Broadcasts too all users
# ❍ /broadcastgroups*:* Broadcasts too all groups
#
# *Groups Info:*
# ❍ /groups*:* List the groups with Name, ID, members count as a txt
# ❍ /leave <ID>*:* Leave the group, ID must have hyphen
# ❍ /stats*:* Shows overall bot stats
# ❍ /getchats*:* Gets a list of group names the user has been seen in. Bot owner only
# ❍ /ginfo username/link/ID*:* Pulls info panel for entire group
#
# *Access control:*
# ❍ /ignore*:* Blacklists a user from using the bot entirely
# ❍ /lockdown <off/on>*:* Toggles bot adding to groups
# ❍ /notice*:* Removes user from blacklist
# ❍ /ignoredlist*:* Lists ignored users

# *Speedtest:*
# ❍ /speedtest*:* Runs a speedtest and gives you 2 options to choose from, text or image output
#
# *Module loading:*
# ❍ /listmodules*:* Lists names of all modules
# ❍ /load modulename*:* Loads the said module to memory without restarting.
# ❍ /unload modulename*:* Loads the said module frommemory without restarting memory without restarting the bot
#
# *Windows self hosted only:*
# ❍ /reboot*:* Restarts the bots service
# ❍ /gitpull*:* Pulls the repo and then restarts the bots service
#
# *Debugging and Shell:*
# ❍ /debug <on/off>*:* Logs commands to updates.txt
# ❍ /logs*:* Run this in support group to get logs in pm
# ❍ /eval*:* Self explanatory
# ❍ /sh*:* Runs shell command
# ❍ /shell*:* Runs shell command
# ❍ /clearlocals*:* As the name goes
# ❍ /dbcleanup*:* Removes deleted accs and groups from db
# ❍ /py*:* Runs python code
#
# *Heroku Settings*
# *Owner only*
# ❍ /usage*:* Check your heroku dyno hours remaining.
# ❍ /see var <var>*:* Get your existing varibles, use it only on your private group!
# ❍ /set var <newvar> <vavariable>*:* Add new variable or update existing value variable.
# ❍ /del var <var>*:* Delete existing variable.
# ❍ /logs Get heroku dyno logs.
#
# `⚠️ Read from top`
# Visit @{SUPPORT_CHAT} for more information.
# """

SUDO_HANDLER = CommandHandler(("addsudo", "addredlion"), addsudo, run_async=True)
SUPPORT_HANDLER = CommandHandler(
    ("addsupport", "addspryzon"), addsupport, run_async=True
)
FAFNIR_HANDLER = CommandHandler(("addfafnir"), addfafnir, run_async=True)
WHITELIST_HANDLER = CommandHandler(
    ("addwhitelist", "addluinor"), addwhitelist, run_async=True
)
UNSUDO_HANDLER = CommandHandler(
    ("removesudo", "removeredlion"), removesudo, run_async=True
)
UNSUPPORT_HANDLER = CommandHandler(
    ("removesupport", "removespryzon"), removesupport, run_async=True
)
UNFAFNIR_HANDLER = CommandHandler(("removefafnir"), removefafnir, run_async=True)
UNWHITELIST_HANDLER = CommandHandler(
    ("removewhitelist", "removeluinor"), removewhitelist, run_async=True
)

WHITELISTLIST_HANDLER = CommandHandler(
    ["whitelistlist", "luinors"], whitelistlist, run_async=True
)
FAFNIRLIST_HANDLER = CommandHandler(["fafnirs"], fafnirlist, run_async=True)
SUPPORTLIST_HANDLER = CommandHandler(
    ["supportlist", "spryzon"], supportlist, run_async=True
)
SUDOLIST_HANDLER = CommandHandler(["sudolist", "REDLIONS"], sudolist, run_async=True)
DEVLIST_HANDLER = CommandHandler(["devlist", "heroes"], devlist, run_async=True)

dispatcher.add_handler(SUDO_HANDLER)
dispatcher.add_handler(SUPPORT_HANDLER)
dispatcher.add_handler(FAFNIR_HANDLER)
dispatcher.add_handler(WHITELIST_HANDLER)
dispatcher.add_handler(UNSUDO_HANDLER)
dispatcher.add_handler(UNSUPPORT_HANDLER)
dispatcher.add_handler(UNFAFNIR_HANDLER)
dispatcher.add_handler(UNWHITELIST_HANDLER)

dispatcher.add_handler(WHITELISTLIST_HANDLER)
dispatcher.add_handler(FAFNIRLIST_HANDLER)
dispatcher.add_handler(SUPPORTLIST_HANDLER)
dispatcher.add_handler(SUDOLIST_HANDLER)
dispatcher.add_handler(DEVLIST_HANDLER)

__mod_name__ = "Dev"
__handlers__ = [
    SUDO_HANDLER,
    SUPPORT_HANDLER,
    FAFNIR_HANDLER,
    WHITELIST_HANDLER,
    UNSUDO_HANDLER,
    UNSUPPORT_HANDLER,
    UNFAFNIR_HANDLER,
    UNWHITELIST_HANDLER,
    WHITELISTLIST_HANDLER,
    FAFNIRLIST_HANDLER,
    SUPPORTLIST_HANDLER,
    SUDOLIST_HANDLER,
    DEVLIST_HANDLER,
]
