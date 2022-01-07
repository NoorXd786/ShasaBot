from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext, CommandHandler, Filters

from ShasaBot import dispatcher
from ShasaBot.modules.disable import DisableAbleCommandHandler
from ShasaBot.modules.helper_funcs.chat_status import user_admin

MARKDOWN_HELP = f"""
Markdown is a very powerful formatting tool supported by telegram. {dispatcher.bot.first_name} has some enhancements, to make sure that \
saved messages are correctly parsed, and to allow you to create buttons.

• <code>_italic_</code>: wrapping text with '_' will produce italic text
• <code>*bold*</code>: wrapping text with '*' will produce bold text
• <code>`code`</code>: wrapping text with '`' will produce monospaced text, also known as 'code'
• <code>[sometext](someURL)</code>: this will create a link - the message will just show <code>sometext</code>, \
and tapping on it will open the page at <code>someURL</code>.
<b>Example:</b><code>[test](example.com)</code>

• <code>[buttontext](buttonurl:someURL)</code>: this is a special enhancement to allow users to have telegram \
buttons in their markdown. <code>buttontext</code> will be what is displayed on the button, and <code>someurl</code> \
will be the url which is opened.
<b>Example:</b> <code>[This is a button](buttonurl:example.com)</code>

If you want multiple buttons on the same line, use :same, as such:
<code>[one](buttonurl://example.com)
[two](buttonurl://google.com:same)</code>
This will create two buttons on a single line, instead of one button per line.

Keep in mind that your message <b>MUST</b> contain some text other than just a button!
"""


@user_admin
def echo(update: Update, context: CallbackContext):
    args = update.effective_message.text.split(None, 1)
    message = update.effective_message

    if message.reply_to_message:
        message.reply_to_message.reply_text(
            args[1], parse_mode="MARKDOWN", disable_web_page_preview=True
        )
    else:
        message.reply_text(
            args[1], quote=False, parse_mode="MARKDOWN", disable_web_page_preview=True
        )
    message.delete()


def markdown_help_sender(update: Update):
    update.effective_message.reply_text(MARKDOWN_HELP, parse_mode=ParseMode.HTML)
    update.effective_message.reply_text(
        "Try forwarding the following message to me, and you'll see, and Use #test!"
    )
    update.effective_message.reply_text(
        "/save test This is a markdown test. _italics_, *bold*, code, "
        "[URL](example.com) [button](buttonurl:github.com) "
        "[button2](buttonurl://google.com:same)"
    )


def markdown_help(update: Update, context: CallbackContext):
    if update.effective_chat.type != "private":
        update.effective_message.reply_text(
            "Contact me in pm",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Markdown help",
                            url=f"t.me/{context.bot.username}?start=markdownhelp",
                        )
                    ]
                ]
            ),
        )
        return
    markdown_help_sender(update)


__help__ = """
*Available commands:*
*Markdown:*
 ❍ /markdownhelp*:* quick summary of how markdown works in telegram - can only be called in private chats
*Paste:*
 ❍ /paste*:* Saves replied content to `nekobin.com` and replies with a url
*React:*
 ❍ /react*:* Reacts with a random reaction 
*Urban Dictonary:*
 ❍ /ud <word>*:* Type the word or expression you want to search use
*Wikipedia:*
 ❍ /wiki <query>*:* wikipedia your query
*Wallpapers:*
 ❍ /wall <query>*:* get a wallpaper from wall.alphacoders.com
*Currency converter:* 
 ❍ /cash*:* currency converter

*MATHS*
Solves complex math problems using https://newton.now.sh
❍ /math*:* Math `/math 2^2+2(2)`
❍ /factor*:* Factor `/factor x^2 + 2x`
❍ /derive*:* Derive `/derive x^2+2x`
❍ /integrate*:* Integrate `/integrate x^2+2x`
❍ /zeroes*:* Find 0's `/zeroes x^2+2x`
❍ /tangent*:* Find Tangent `/tangent 2lx^3`
❍ /area*:* Area Under Curve `/area 2:4lx^3`
❍ /cos*:* Cosine `/cos pi`
❍ /sin*:* Sine `/sin 0`
❍ /tan*:* Tangent `/tan 0`
❍ /arccos*:* Inverse Cosine `/arccos 1`
❍ /arcsin*:* Inverse Sine `/arcsin 0`
❍ /arctan*:* Inverse Tangent `/arctan 0`
❍ /abs*:* Absolute Value `/abs -1`
❍ /log*:* Logarithm `/log 2l8`

*ENGLISH*
❍ /define `<text>`*:* Type the word or expression you want to search\nFor example /define kill
❍ /spell*:* while replying to a message, will reply with a grammar corrected version
❍ /synonyms `<word>`*:* Find the synonyms of a word
❍ /antonyms `<word>`*:* Find the antonyms of a word

💡`Read From Top`
"""

ECHO_HANDLER = DisableAbleCommandHandler(
    "echo", echo, filters=Filters.chat_type.groups, run_async=True
)
MD_HELP_HANDLER = CommandHandler("markdownhelp", markdown_help, run_async=True)

dispatcher.add_handler(ECHO_HANDLER)
dispatcher.add_handler(MD_HELP_HANDLER)

__mod_name__ = "Extras"
__command_list__ = ["id", "echo"]
__handlers__ = [
    ECHO_HANDLER,
    MD_HELP_HANDLER,
]
