import telebot, os, schedule, time
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from bible_quotes import bible_message, bible_text_extraction

print("Bot started")

# Отравка поста
def send_message():
    
    load_dotenv()
    bot_token = os.environ.get("SENDER_BOT_TOKEN")
    bot = telebot.TeleBot(bot_token)
    open_ai_key = os.environ.get("OPENAI_API_KEY")
    llm = ChatOpenAI(model = "gpt-4-turbo-preview", openai_api_key = open_ai_key, temperature = 0.3)
    text = bible_text_extraction("t_web_cor.csv", 10)


    system = """You are an intelligent assistant capable of extracting a semantic fragment |fragment| from a text, which is the text of the Bible.
After extracting the fragment |fragment|, you should provide a commentary |comment| on this fragment in the style of a priest-philosopher. Your commentary should be deep and insightful, reflecting spiritual and philosophical aspects. You should also provide a reference |link| to the fragment |fragment|. The reference should be formatted as "Book Chapter:Verse(s)". For example, the Gospel of Matthew, chapter 4, verse 19 would be formatted as "Matthew 4:19". If the reference covers multiple verses, this is indicated by a dash, e.g., "Matthew 4:19-20". Add emojis in comment.
The answer should be formatted in HTML and include the following structure:
<b>|fragment|</b>\n\n
<i>-|link|</i>\n\n
<b>Комментарий</b>
|comment|
Отвечай на русском"""

    user_input = f"""Extract a fragment |fragment| from text of the Bible:
{text}
The answer should be formatted in HTML and include the following structure:
<b>|fragment|</b>\n\n
<i>-|link|</i>\n\n
<b>Комментарий</b>
|comment|

Ответь полностью на русском"""
    
    message_output = bible_message(system, user_input, llm) 

    bot.send_message(-1002132823556, text=message_output, parse_mode="HTML")


# Schedule the message to be sent every day at 04:30 AM UTC
schedule.every().day.at("04:30").do(send_message)

# Main loop
while True:
    schedule.run_pending()
    time.sleep(60)  # Увеличение времени ожидания до 3600 секунд