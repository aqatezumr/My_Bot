from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your Render-hosted bot!")

app = ApplicationBuilder().token("7032229248:AAGsgYzua_Wng2-oFh1pIn0qOhhXIhPgDHU").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
