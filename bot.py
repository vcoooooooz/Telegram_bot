import telebot
import yt_dlp
import os

# 🔹 أدخل توكن البوت هنا
BOT_TOKEN = "7901978719:AAED7f2fJ1ut0JTXyBaWqNagVt3uowiTxOoا"

bot = telebot.TeleBot(BOT_TOKEN)

# 🔹 عند استقبال /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🎥 مرحبًا! أرسل لي رابط فيديو من أي منصة وسأقوم بتحميله لك.")

# 🔹 عند استقبال رابط فيديو
@bot.message_handler(func=lambda message: "http" in message.text)
def download_video(message):
    url = message.text
    bot.reply_to(message, "⏳ جاري تحميل الفيديو...")

    # إعدادات التحميل
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.mp4'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # إرسال الفيديو
        video = open("video.mp4", "rb")
        bot.send_video(message.chat.id, video)
        video.close()
        os.remove("video.mp4")

        # 🔹 رسالة بعد التحميل
        bot.send_message(message.chat.id, "✅ تم تحميل الفيديو بنجاح!\n\nبواسطة 🄳🄰🅁🄺 @F3_9F")

    except Exception as e:
        bot.send_message(message.chat.id, f"❌ حدث خطأ: {str(e)}")

# 🔹 تشغيل البوت
bot.polling()