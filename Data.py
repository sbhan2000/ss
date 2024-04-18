from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("بدء استخراج الجلسة", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="العودة إلى الصفحة الرئيسية", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "قـناة الـبوت", url="https://t.me/ah07v"
            )
        ],
        [
            InlineKeyboardButton("كيفية استخدام البوت ?", callback_data="help"),
            InlineKeyboardButton("حـول", callback_data="about"),
        ],
        [InlineKeyboardButton("المطور", url="https://t.me/ah_2_v")],
    ]

    START = """**
أهلًا {} ♦
ومرحبًا بك عزيزي في {}
هذا البوت مخصص لاستخراج الجلسات
إذا كنـت تريـد أن يكون حسـابك في أمـان تام فاختر بايروجـرام أمـا إذا كـان رقمك حقيقـي فاختر تيرمـكس
المطور :- @ah_2_v
    **"""

    HELP = """
 **الأوامر المتاحة**

**🥤| /about - لحول البوت
🥤| /help - لمساعدتك
🥤| /start - لبدء البوت 
🥤| /repo - لإعطاء ريبو البوت
🥤| /generate - لاستخراج الجلسات 
🥤| /cancel - لإلغاء الاستخراج 
🥤| /restart - لترسيت البوت
**"""

    # About Message
    ABOUT = """
**حول البوت** 

**🥤| هذا هو بوت استخراج كود تيرمكس وبايروجرام 

🥤| [قـناة الـبوت](https://t.me/ah07v)
🥤| [سورس زاد](https://t.me/source_zad)
🥤| [المطور](https://t.me/ah_2_v)
    **"""

    # Repo Message
    REPO = """**
━━━━━━━━━━━━━━━━━━━━━━━━
🥤| انا بوت اعمل على استخراج جلسات تيرمكس وبايروجرام
┏━━━━━━━━━━━━━━━━━┓
┣★ [المطور](https://t.me/lMl10l)
┣★ [قناة البوت](https://t.me/ah07v)
┗━━━━━━━━━━━━━━━━━┛
   **"""
