import os
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN", "8988127187:AAEs4wpokxVlGdZCx13fMh2kVLbRpkNcs6k")
VIDEO_URL = os.getenv("VIDEO_URL", "t.me/xbd_viralbot/xbd_bot")

WELCOME_MESSAGE = (
    "🔥 Welcome to Viral XBD! 🎬\n\n"
    "🇧🇩 বাংলাদেশের ট্রেন্ডিং ও ভাইরাল ভিডিওর "
    "দুনিয়ায় আপনাকে স্বাগতম!\n\n"
    "💎 উপভোগ করুন আকর্ষণীয় ভিডিও ও এক্সক্লুসিভ কনটেন্ট।\n\n"
    "👇 শুরু করতে নিচের বাটনে ক্লিক করুন!\n\n"
    "🚀 Viral XBD — Your Ultimate Viral Video Experience! ❤️"
)

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    keyboard = [[
        InlineKeyboardButton(
            "▶️ Play Video",
            url=VIDEO_URL
        )
    ]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.effective_message.reply_text(
        WELCOME_MESSAGE,
        reply_markup=reply_markup
    )

def main():
    if BOT_TOKEN == "8988127187:AAEs4wpokxVlGdZCx13fMh2kVLbRpkNcs6k":
        raise ValueError("BOT_TOKEN সেট করুন!")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Viral XBD Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()