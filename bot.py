import telebot
from telebot import types
import time

# --- البيانات الأساسية ---
TOKEN = '8687760739:AAHC5S-LgdY0S2xZauN7NNacWmHttibiGfw'
ADMIN_ID = 692060862  # معرفك الشخصي اللي زودتني بيه
bot = telebot.TeleBot(TOKEN)

# متغير حالة الجائزة
first_user_won = False 

@bot.message_handler(commands=['start'])
def welcome(message):
    global first_user_won
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    # طباعة المراقبة في Pydroid
    print(f"إشعار: دخول جديد من {user_name} | ID: {user_id}")

    # تكتيك الجائزة: إذا كان المستخدم مو أنت، والجائزة لم تُربح بعد
    if not first_user_won and user_id != ADMIN_ID:
        congrats_text = (
            f"🎊 مبروووووك يا {user_name}! 🎊\n\n"
            "أنت الفائز الأول بمناسبة افتتاح بوت (نقطة)!\n"
            "لقد فزت بـ (عمل مجاني) من اختيارك. 🎁\n"
            "راسلني فوراً لتأكيد جائزتك: @namirshaker"
        )
        bot.send_message(message.chat.id, congrats_text)
        first_user_won = True
        print(f"🔥 الجائزة ذهبت لـ: {user_name}")
    
    # رسالة خاصة لك كمدير
    elif user_id == ADMIN_ID:
        bot.send_message(message.chat.id, "أهلاً سيادة الملازم نمير! تم التعرف عليك.. أنت في وضع الإدارة الآن. 🫡✨")

    # إظهار المنيو الشامل للكل
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    buttons = [
        types.InlineKeyboardButton("📄 طلب CV ملكي", callback_data='cv'),
        types.InlineKeyboardButton("🎓 بحوث وتقارير", callback_data='research'),
        types.InlineKeyboardButton("🖼️ تصميم إعلانات", callback_data='ads'),
        types.InlineKeyboardButton("📚 طباعة ملازم", callback_data='print'),
        types.InlineKeyboardButton("📄 تحرير PDF", callback_data='pdf_edit'),
        types.InlineKeyboardButton("📊 باوربوينت (PPT)", callback_data='ppt'),
        types.InlineKeyboardButton("🌐 ترجمة ملفات", callback_data='translate'),
        types.InlineKeyboardButton("💻 تفعيل برامج", callback_data='win_act'),
        types.InlineKeyboardButton("🔧 صيانة تقنية", callback_data='tech'),
        types.InlineKeyboardButton("📞 تواصل مباشر", url='https://t.me/namirshaker')
    ]
    
    markup.add(*buttons)
    
    welcome_text = (
        "✨ أهلاً بك في منصة (نقطة | Nukta)\n\n"
        "كل شيء عظيم بدايته نقطة.. 🎯\n"
        "اختر الخدمة التي تحتاجها من القائمة أدناه:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    bot.answer_callback_query(call.id)
    
    # قاعدة بيانات الردود لكل خدمة
    responses = {
        'cv': "👑 خدمة الـ CV الملكي:\nأرسل معلوماتك لنصمم لك سيرة ذاتية احترافية.\n👉 @namirshaker",
        'research': "🎓 البحوث والتقارير:\nكتابة وتنسيق البحوث الأكاديمية بدقة.\n👉 @namirshaker",
        'ads': "🖼️ تصميم الإعلانات:\nبوسترات ولوغوهات احترافية لمشروعك.\n👉 @namirshaker",
        'print': "📚 طباعة الملازم:\nطباعة واضحة وتجليد فني. أرسل ملفك هنا:\n👉 @namirshaker",
        'pdf_edit': "📄 تحرير PDF:\nتعديل النصوص وتحويل الملفات.\n👉 @namirshaker",
        'ppt': "📊 عروض باوربوينت:\nتصميم عروض PPT مميزة لمناقشاتك.\n👉 @namirshaker",
        'translate': "🌐 ترجمة ملفات:\nترجمة أكاديمية دقيقة للمصادر.\n👉 @namirshaker",
        'win_act': "💻 تفعيل برامج:\nتفعيل ويندوز وأوفيس وبرامج التصميم.\n👉 @namirshaker",
        'tech': "🔧 الصيانة والدعم:\nحلول مشاكل الحاسبات في كركوك والكوت.\n👉 @namirshaker"
    }
    
    if call.data in responses:
        bot.send_message(call.message.chat.id, responses[call.data])

# تشغيل البوت مع ميزة المقاومة للفصل
print("نقطة: النظام شغال 100%.. أهلاً سيادة الملازم! 🚀")
while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=20)
    except:
        time.sleep(5)
