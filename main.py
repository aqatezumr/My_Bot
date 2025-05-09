from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I'm your bot!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start\n/help\n/echo\n/sum x y")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = ' '.join(context.args)
    await update.message.reply_text(msg if msg else "Use: /echo something")

async def sum_numbers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        x, y = map(int, context.args)
        await update.message.reply_text(f"The sum is {x + y}")
    except:
        await update.message.reply_text("Use: /sum 4 5")

app = ApplicationBuilder().token("7032229248:AAGsgYzua_Wng2-oFh1pIn0qOhhXIhPgDHU").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("echo", echo))
app.add_handler(CommandHandler("sum", sum_numbers))
app.run_polling()
