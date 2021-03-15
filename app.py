import datetime
import logging

import pytz
from telegram.ext import Updater

# bot = Bot("1613665060:AAEjoWaTYAbUxBU0goORZ2wOj3zt_Knhf5s")

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


def start(update, context):
    print(update.message.chat_id)
    context.job_queue.run_daily(msg,
                                datetime.time(hour=22, minute=00, tzinfo=pytz.timezone('Asia/Kolkata')),
                                days=(0, 1, 2, 3, 4, 5, 6), context=update.message.chat_id)


def msg(context):
    #     context.bot.send_message(chat_id=context.job.context, text='''।इच्छाकारेणं संदीसह भगवं।
    #
    # पंच परमेषष्ठी, तीर्थंकर परमात्मा प्रभु महावीर , आचार्य भगवंत श्री आनंदऋषिजी म. सा और ज्ञानदाता, अर्हम् विज्जा प्रणेता श्री. ऋषि प्रवीण के चरणों में समर्पित होते हुवे , हम प्रभु वचनों को समझने, ग्रहण करने और अपने जीवन में समा लेने की आज्ञा लेते है। 🙏''')
    #     context.bot.send_photo(chat_id=context.job.context, photo=open('Praveen-Rishi.jpg', 'rb'))
    #     context.bot.send_audio(chat_id=context.job.context, audio=open('AUD-20210220-WA0023.mp3', 'rb'))
    #     context.bot.send_audio(chat_id=context.job.context, audio=open('AUD-20210220-WA0022.mp3', 'rb'))
    text = "https://www.anandtirth.com/daliygathavivechan-shrimaduttaradhyayansutrashrutaradhanadailyverseinterpretation/"
    text = 'https://www.youtube.com/watch?v=yH8tEX0Th1Q'

    context.bot.send_message(chat_id=context.job.context,
                             text=f'link : {text}', disable_web_page_preview=False)

    # context.bot.send_document(chat_id=context.job.context, document=open('Gatha_48_Adhyaya_01_Hindi.pdf', 'rb'))
    # context.bot.send_document(chat_id=context.job.context, document=open('Gatha_48_Adhyaya 01_English.pdf', 'rb'))
    # context.bot.send_file()

    # with open('JordanPeterson.jpg', 'rb') as jordan_picture:
    #     caption = "<a href='https://twitter.com/jordanbpeterson'>Jordan B. Peterson</a>"
    #     context.bot.send_photo(
    #         chat_id,
    #         photo=jordan_picture,
    #         caption=caption,
    #         parse_mode=ParseMode.HTML
    #     )
    #


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # value = Bot('1613665060:AAEjoWaTYAbUxBU0goORZ2wOj3zt_Knhf5s').get_updates()
    # for i in value:
    #     print(i)
    updater = Updater('1613665060:AAEjoWaTYAbUxBU0goORZ2wOj3zt_Knhf5s', use_context=True)
    dp = updater.dispatcher
    dp.add_error_handler(error)
    job = updater.job_queue

    job.run_daily(msg,
                  datetime.time(hour=22, minute=11, tzinfo=pytz.timezone('Asia/Kolkata')),
                  days=(0, 1, 2, 3, 4, 5, 6), context=-1001414466079)

    # dp.add_handler(CommandHandler("start", start, pass_job_queue=True))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
