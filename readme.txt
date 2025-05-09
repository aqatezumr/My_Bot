Step-by-Step Guide: Host Telegram Bot on Render (Free)
🚀 What You’ll Need:
A GitHub account

Your Telegram Bot Token from @BotFather

A simple Python bot (I'll provide the code)

📦 Step 1: Create Your Bot Code & Upload to GitHub
a) Create a new folder on your computer with these files:
main.py

python
Копировать
Редактировать
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your Render-hosted bot!")

app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
👉 Replace "YOUR_BOT_TOKEN" with your actual bot token.

requirements.txt

ini
Копировать
Редактировать
python-telegram-bot==20.3
render.yaml (optional, but useful)

yaml
Копировать
Редактировать
services:
  - type: worker
    name: telegram-bot
    env: python
    plan: free
    buildCommand: "pip install -r requirements.txt"
    startCommand: "python main.py"
b) Push this project to GitHub
Create a new GitHub repo

Upload all 3 files

Commit and push

🛠️ Step 2: Deploy on Render
Go to: https://render.com

Sign in with your GitHub account

Click "New" → "Web Service" (we’ll change this to a Worker next)

Choose your repo with the bot code

Set these:

Environment: Python

Build Command: pip install -r requirements.txt

Start Command: python main.py

Service Type: Change to "Background Worker"

Plan: Select Free

Click Create Web Service

✅ That’s It!
Render will build and run your bot automatically. If everything is set correctly, your Telegram bot will respond to /start 24/7!