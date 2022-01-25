from telegram import ParseMode, Update
from telegram.ext import CallbackContext, CommandHandler

from ShasaBot import dispatcher


def warns_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        """*Warns Help:*
  |• `/warns <userhandle>`*:* get a user's number, and reason, of warns.
  |• `/warnlist`*:* list of all current warning filters
*Admins only:*
  |• `/warn <userhandle>`*:* warn a user. After 3 warns, the user will be banned from the group. Can also be used as a reply.
  |• `/dwarn <userhandle>`*:* warn a user and delete the message. After 3 warns, the user will be banned from the group. Can also be used as a reply.
  |• `/resetwarn <userhandle>`*:* reset the warns for a user. Can also be used as a reply.
  |• `/addwarn <keyword> <reply message>`*:* set a warning filter on a certain keyword. If you want your keyword to \
be a sentence, encompass it with quotes, as such: `/addwarn "very angry" This is an angry user`. 
  |• `/nowarn <keyword>`*:* stop a warning filter
  |• `/warnlimit <num>`*:* set the warning limit
  |• `/strongwarn <on/yes/off/no>`*:* If set to on, exceeding the warn limit will result in a ban. Else, will just kick.\n""",
        parse_mode=ParseMode.MARKDOWN,
    )


def approvals_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        """*Approvals Help:*
Sometimes, you might trust a user not to send unwanted content.
Maybe not enough to make them admin, but you might be ok with locks, blacklists, and antiflood not applying to them.
That's what approvals are for - approve of trustworthy users to allow them to send.
*User commands*:
  |• `/approval`*:* Check a user's approval status in this chat.

*Admins commands*:
  |• `/approve`*:* Approve of a user. Locks, blacklists, and antiflood won't apply to them anymore.
  |• `/unapprove`*:* Unapprove of a user. They will now be subject to locks, blacklists, and antiflood again.
  |• `/approved`*:* List all approved users.

*Group Owner commands*:
  |• `/unapproveall: Unapprove ALL users in a chat. This cannot be undone.\n""",
        parse_mode=ParseMode.MARKDOWN,
    )


def blacklist_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        """*Blacklist Help:*
Blacklists are used to stop certain triggers from being said in a group. Any time the trigger is mentioned, the message will immediately be deleted. A good combo is sometimes to pair this up with warn filters!

*NOTE*: Blacklists do not affect group admins.

 ❍ /blacklist*:* View the current blacklisted words.

Admin only:
 ❍ /addblacklist <triggers>*:* Add a trigger to the blacklist. Each line is considered one trigger, so using different lines will allow you to add multiple triggers.
 ❍ /unblacklist <triggers>*:* Remove triggers from the blacklist. Same newline logic applies here, so you can remove multiple triggers at once.
 ❍ /blacklistmode <off/del/warn/ban/kick/mute/tban/tmute>*:* Action to perform when someone sends blacklisted words.

Blacklist sticker is used to stop certain stickers. Whenever a sticker is sent, the message will be deleted immediately.
*NOTE:* Blacklist stickers do not affect the group admin
 ❍ /blsticker*:* See current blacklisted sticker
*Only admin:*
 ❍ /addblsticker <sticker link>*:* Add the sticker trigger to the black list. Can be added via reply sticker
 ❍ /unblsticker <sticker link>*:* Remove triggers from blacklist. The same newline logic applies here, so you can delete multiple triggers at once
 ❍ /rmblsticker <sticker link>*:* Same as above
 ❍ /blstickermode <ban/tban/mute/tmute>*:* sets up a default action on what to do if users use blacklisted stickers
Note:
 ❍ <sticker link> can be `https://t.me/addstickers/<sticker>` or just `<sticker>` or reply to the sticker message\n""",
        parse_mode=ParseMode.MARKDOWN,
    )


def connect_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        """*Connect Help:*
Sometimes, you just want to add some notes and filters to a group chat, but you don't want everyone to see; This is where connections come in...
This allows you to connect to a chat's database, and add things to it without the commands appearing in chat! For obvious reasons, you need to be an admin to add things; but any member in the group can view your data.

 ❍ /connect: Connects to chat (Can be done in a group by /connect or /connect <chat id> in PM)
 ❍ /connection: List connected chats
 ❍ /disconnect: Disconnect from a chat
 ❍ /helpconnect: List available commands that can be used remotely

*Admin only:*
 ❍ /allowconnect <yes/no>: allow a user to connect to a chat\n""",
        parse_mode=ParseMode.MARKDOWN,
    )


def channel_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        """*Channel Help:*
*Admins only:*
 ❍ /logchannel*:* get log channel info
 ❍ /setlog*:* set the log channel.
 ❍ /unsetlog*:* unset the log channel.
Setting the log channel is done by:
❍ adding the bot to the desired channel (as an admin!)
❍ sending /setlog in the channel
❍ forwarding the /setlog to the group\n""",
        parse_mode=ParseMode.MARKDOWN,
    )


def control_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        """*Control Help:*
*Blue text cleaner* removed any made up commands that people send in your chat.
 ❍ /cleanblue <on/off/yes/no>*:* clean commands after sending
 ❍ /ignoreblue <word>*:* prevent auto cleaning of the command
 ❍ /unignoreblue <word>*:* remove prevent auto cleaning of the command
 ❍ /listblue*:* list currently whitelisted commands

*Antiflood* allows you to take action on users that send more than x messages in a row. Exceeding the set flood \
will result in restricting that user.
 This will mute users if they send more than 10 messages in a row, bots are ignored.
 ❍ /flood*:* Get the current flood control setting
• *Admins only:*
 ❍ /setflood <int/'no'/'off'>*:* enables or disables flood control
 *Example:* `/setflood 10`
 ❍ /setfloodmode <ban/kick/mute/tban/tmute> <value>*:* Action to perform when user have exceeded flood limit. ban/kick/mute/tmute/tban
• *Note:*
 • Value must be filled for tban and tmute!!
 It can be:
 `5m` = 5 minutes
 `6h` = 6 hours
 `3d` = 3 days
 `1w` = 1 week\n""",
        parse_mode=ParseMode.MARKDOWN,
    )


def disable_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        """*Disable Help:*
❍ /cmds*:* check the current status of disabled commands

    *Admins only:*
    ❍ /enable <cmd name>*:* enable that command
    ❍ /disable <cmd name>*:* disable that command
    ❍ /enablemodule <module name>*:* enable all commands in that module
    ❍ /disablemodule <module name>*:* disable all commands in that module
    ❍ /listcmds*:* list all possible toggleable commands\n""",
        parse_mode=ParseMode.MARKDOWN,
    )


def fsub_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        """*F-Sub Help:*
❍ Shasa can mute members who are not subscribed your channel until they subscribe
❍ When enabled I will mute unsubscribed members and show them a unmute button. When they pressed the button I will unmute them
*Setup*
*Only creator*
❍ Add me in your group as admin
❍ Add me in your channel as admin

*Commmands*
 ❍ /fsub {channel username} - To turn on and setup the channel.
  💡Do this first...
 ❍ /fsub - To get the current settings.
 ❍ /fsub disable - To turn of ForceSubscribe..
  💡If you disable fsub, you need to set again for working.. /fsub {channel username}
 ❍ /fsub clear - To unmute all members who muted by me.\n""",
        parse_mode=ParseMode.MARKDOWN,
    )


def filters_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        """*Cust Filters Help:*
 ❍ /filters*:* List all active filters saved in the chat.

*Admin only:*
 ❍ /filter <keyword> <reply message>*:* Add a filter to this chat. The bot will now reply that message whenever 'keyword'\
is mentioned. If you reply to a sticker with a keyword, the bot will reply with that sticker. NOTE: all filter \
keywords are in lowercase. If you want your keyword to be a sentence, use quotes. eg: /filter "hey there" How you \
doin?
 Separate diff replies by `%%%` to get random replies
 *Example:* 
 `/filter "filtername"
 Reply 1
 %%%
 Reply 2
 %%%
 Reply 3`
 ❍ `/stop <filter keyword>`*:* Stop that filter.

*Chat creator only:*
 ❍ /removeallfilters*:* Remove all chat filters at once.

*Note*: Filters also support markdown formatters like: {first}, {last} etc.. and buttons.
Check `/markdownhelp` to know more!\n""",
        parse_mode=ParseMode.MARKDOWN,
    )


def greeting_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        """*Greetings Help:*
  *Admins only:*
  |• `/welcome <on/off>`*:* enable/disable welcome messages.
  |• `/welcome`*:* shows current welcome settings.
  |• `/welcome noformat`*:* shows current welcome settings, without the formatting - useful to recycle your welcome messages!
  |• `/goodbye`*:* same usage and args as `/welcome`.
  |• `/setwelcome <sometext>`*:* set a custom welcome message. If used replying to media, uses that media.
  |• `/setgoodbye <sometext>`*:* set a custom goodbye message. If used replying to media, uses that media.
  |• `/resetwelcome`*:* reset to the default welcome message.
  |• `/resetgoodbye`*:* reset to the default goodbye message.
  |• `/cleanwelcome <on/off>`*:* On new member, try to delete the previous welcome message to avoid spamming the chat.
  |• `/welcomemutehelp`*:* gives information about welcome mutes.
  |• `/cleanservice <on/off`*:* deletes telegrams welcome/left service messages.
 *Example:*
user joined chat, user left chat.
*Welcome markdown:*
  |• `/welcomehelp`*:* view more formatting information for custom welcome/goodbye messages.\n""",
        parse_mode=ParseMode.MARKDOWN,
    )


def infos_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        """*Infos Help:*
*Away from group*
 ❍ /afk <reason>*:* mark yourself as AFK(away from keyboard).

*ID:*
 ❍ /id*:* get the current group id. If used by replying to a message, gets that user's id.
 ❍ /gifid*:* reply to a gif to me to tell you its file ID.

*Self addded information:*
 ❍ /setme <text>*:* will set your info
 ❍ /me*:* will get your or another user's info.
*Examples:* 💡
 ➩ /setme I am a luinor.
 ➩ /me @username(defaults to yours if no user specified)

*Information others add on you:*
 ❍ /bio*:* will get your or another user's bio. This cannot be set by yourself.
 ❍ /setbio <text>*:* while replying, will save another user's bio
*Examples:* 💡
 ➩ /bio @username(defaults to yours if not specified).`
 ➩ /setbio This user is a luinor` (reply to the user)

*Overall Information about you:*
 ❍ /info*:* get information about a user.

*What is that health thingy?*
 Come and see [HP System explained](https://t.me/Shasa_News/2)\n""",
        parse_mode=ParseMode.MARKDOWN,
    )


def locks_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        """*Locks Help:*
Do stickers annoy you? or want to avoid people sharing links? or pictures? \
You're in the right place!
The locks module allows you to lock away some common items in the \
telegram world; the bot will automatically delete them!

 ❍ /locktypes*:* Lists all possible locktypes

*Admins only:*
 ❍ /lock <type>*:* Lock items of a certain type (not available in private)
 ❍ /unlock <type>*:* Unlock items of a certain type (not available in private)
 ❍ /locks*:* The current list of locks in this chat.

Locks can be used to restrict a group's users.
eg:
Locking urls will auto-delete all messages with urls, locking stickers will restrict all \
non-admin users from sending stickers, etc.
Locking bots will stop non-admins from adding bots to the chat.

*Note:*
 • Unlocking permission *info* will allow members (non-admins) to change the group information, such as the description or the group name
 • Unlocking permission *pin* will allow members (non-admins) to pinned a message in a group\n""",
        parse_mode=ParseMode.MARKDOWN,
    )


def notes_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        """*Notes Help:*
  |• `/get <notename>`*:* get the note with this notename
 ❍ `#<notename>`*:* same as /get
  |• `/notes` or `/saved`*:* list all saved notes in this chat
  |• `/number` *:* Will pull the note of that number in the list
If you would like to retrieve the contents of a note without any formatting, use `/get <notename> noformat`. This can \
be useful when updating a current note

*Admins only:*
  |• `/save <notename> <notedata>`*:* saves notedata as a note with name notename
A button can be added to a note by using standard markdown link syntax - the link should just be prepended with a \
`buttonurl:` section, as such: `[somelink](buttonurl:example.com)`. Check `/markdownhelp` for more info
  |• `/save <notename>`*:* save the replied message as a note with name notename
 Separate diff replies by `%%%` to get random notes
 *Example:*
 `/save notename
 Reply 1
 %%%
 Reply 2
 %%%
 Reply 3`
  |• `/clear <notename>`*:* clear note with this name
  |• `/removeallnotes`*:* removes all notes from the group
 *Note:* Note names are case-insensitive, and they are automatically converted to lowercase before getting saved.\n""",
        parse_mode=ParseMode.MARKDOWN,
    )


def rules_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        """*Rules Help:*
 ❍ /rules*:* get the rules for this chat.

*Admins only:*
 ❍ /setrules <your rules here>*:* set the rules for this chat.
 ❍ /clearrules*:* clear the rules for this chat.\n""",
        parse_mode=ParseMode.MARKDOWN,
    )


def shasa_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        """*Shasa Help:*
Full Details of Commands in Shasa
        ✨`/shasahelp`✨
 ❍ /animehelp
 ❍ /approvalshelp
 ❍ /blacklisthelp
 ❍ /connecthelp
 ❍ /channelhelp
 ❍ /controlhelp
 ❍ /disablehelp
 ❍ /fsubhelp
 ❍ /filtershelp
 ❍ /greetinghelp
 ❍ /infoshelp
 ❍ /noteshelp
 ❍ /ruleshelp
   Full Help List for All Cmnds\n""",
        parse_mode=ParseMode.MARKDOWN,
    )


def nekos_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        """*Neko*
 Fun Gifs And Images

 - /neko: Sends Random SFW Neko source Images.
 - /feet: Sends Random Anime Feet Images.
 - /yuri: Sends Random Yuri source Images.
 - /trap: Sends Random Trap source Images.
 - /futanari: Sends Random Futanari source Images.
 - /hololewd: Sends Random Holo Lewds.
 - /lewdkemo: Sends Random Kemo Lewds.
 - /sologif: Sends Random Solo GIFs.
 - /cumgif: Sends Random Cum GIFs.
 - /erokemo: Sends Random Ero-Kemo Images.
 - /lesbian: Sends Random Les Source Images.
 - /wallpaper: Sends Random Wallpapers.
 - /lewdk: Sends Random Kitsune Lewds.
 - /ngif: Sends Random Neko GIFs.
 - /tickle: Sends Random Tickle GIFs.
 - /lewd: Sends Random Lewds.
 - /feed: Sends Random Feeding GIFs.
 - /eroyuri: Sends Random Ero-Yuri source Images.
 - /eron: Sends Random Ero-Neko source Images.
 - /cum: Sends Random Cum Images.
 - /bjgif: Sends Random Blow Job GIFs.
 - /bj: Sends Random Blow Job source Images.
 - /nekonsfw: Sends Random NSFW Neko source Images.
 - /solo: Sends Random NSFW Neko GIFs.
 - /kemonomimi: Sends Random KemonoMimi source Images.
 - /avatarlewd: Sends Random Avater Lewd Stickers.
 - /gasm: Sends Random Orgasm Stickers.
 - /poke: Sends Random Poke GIFs.
 - /anal: Sends Random Anal GIFs.
 - /hentai: Sends Random Hentai source Images.
 - /avatar: Sends Random Avatar Stickers.
 - /erofeet: Sends Random Ero-Feet source Images.
 - /holo: Sends Random Holo source Images.
 - /tits: Sends Random Tits source Images.
 - /pussygif: Sends Random Pussy GIFs.
 - /holoero: Sends Random Ero-Holo source Images.
 - /pussy: Sends Random Pussy source Images.
 - /hentaigif: Sends Random Hentai GIFs.
 - /classic: Sends Random Classic Hentai GIFs.
 - /kuni: Sends Random Pussy Lick GIFs.
 - /waifu: Sends Random Waifu Stickers.
 - /kiss: Sends Random Kissing GIFs.
 - /femdom: Sends Random Femdom source Images.
 - /cuddle: Sends Random Cuddle GIFs.
 - /erok: Sends Random Ero-Kitsune source Images.
 - /foxgirl: Sends Random FoxGirl source Images.
 - /titsgif: Sends Random Tits GIFs.
 - /ero: Sends Random Ero source Images.
 - /smug: Sends Random Smug GIFs.
 - /baka: Sends Random Baka Shout GIFs.
 - /dva: Sends Random D.VA source Images.\n""",
        parse_mode=ParseMode.MARKDOWN,
    )


WARNS_HELP_HANDLER = CommandHandler("warnshelp", warns_help, run_async=True)
APPROVALS_HELP_HANDLER = CommandHandler("approvalshelp", approvals_help, run_async=True)
BLACKLIST_HELP_HANDLER = CommandHandler("blacklisthelp", blacklist_help, run_async=True)
CONNECT_HELP_HANDLER = CommandHandler("connecthelp", connect_help, run_async=True)
CHANNEL_HELP_HANDLER = CommandHandler("channelhelp", channel_help, run_async=True)
CONTROL_HELP_HANDLER = CommandHandler("controlhelp", control_help, run_async=True)
DISABLE_HELP_HANDLER = CommandHandler("disablehelp", disable_help, run_async=True)
FSUB_HELP_HANDLER = CommandHandler("fsubhelp", fsub_help, run_async=True)
FILTERS_HELP_HANDLER = CommandHandler("filtershelp", filters_help, run_async=True)
GREETING_HELP_HANDLER = CommandHandler("greetinghelp", greeting_help, run_async=True)
INFOS_HELP_HANDLER = CommandHandler("infoshelp", infos_help, run_async=True)
LOCKS_HELP_HANDLER = CommandHandler("lockshelp", locks_help, run_async=True)
NOTES_HELP_HANDLER = CommandHandler("noteshelp", notes_help, run_async=True)
RULES_HELP_HANDLER = CommandHandler("ruleshelp", rules_help, run_async=True)
SHASA_HELP_HANDLER = CommandHandler("shasahelp", shasa_help, run_async=True)
NEKOS_HELP_HANDLER = CommandHandler("nekoshelp", nekos_help, run_async=True)

dispatcher.add_handler(WARNS_HELP_HANDLER)
dispatcher.add_handler(APPROVALS_HELP_HANDLER)
dispatcher.add_handler(BLACKLIST_HELP_HANDLER)
dispatcher.add_handler(CONNECT_HELP_HANDLER)
dispatcher.add_handler(CHANNEL_HELP_HANDLER)
dispatcher.add_handler(CONTROL_HELP_HANDLER)
dispatcher.add_handler(DISABLE_HELP_HANDLER)
dispatcher.add_handler(FSUB_HELP_HANDLER)
dispatcher.add_handler(FILTERS_HELP_HANDLER)
dispatcher.add_handler(GREETING_HELP_HANDLER)
dispatcher.add_handler(INFOS_HELP_HANDLER)
dispatcher.add_handler(LOCKS_HELP_HANDLER)
dispatcher.add_handler(NOTES_HELP_HANDLER)
dispatcher.add_handler(RULES_HELP_HANDLER)
dispatcher.add_handler(SHASA_HELP_HANDLER)
dispatcher.add_handler(NEKOS_HELP_HANDLER)

__mod_name__ = "◎Fᴜʟʟ Cᴍᴅs"

__help__ = """
Full Details of Commands in Shasa
        ✨`/shasahelp`✨
 |• /animehelp
 |• /approvalshelp
 |• /blacklisthelp
 |• /connecthelp
 |• /channelhelp
 |• /controlhelp
 |• /disablehelp
 |• /fsubhelp
 |• /filtershelp
 |• /greetinghelp
 |• /infoshelp
 |• /lockshelp
 |• /noteshelp
 |• /nekoshelp
 |• /ruleshelp

You can use this command in groups also to find full details.
This can make easy to find all commands in Shasa.
"""
