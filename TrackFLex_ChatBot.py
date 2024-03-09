import os
from groq import Groq
from typing import Final
from telegram import Update
from telegram.ext import Application , CommandHandler , MessageHandler ,filters , ContextTypes

# Contants
API_KEY :Final = "YOUR_GROQ_API_KEY"  #my key
TOKEN: Final = 'YOUR_TELEGRAM_BOT_TOKEN'
BOT_USERNAME: Final ='@TrackFlex_bot'

#commands
async def start_command(update :Update , context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello Im TrackFlex Bot! How may I help you ?')

async def help_command(update :Update , context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello There , To chat with TrackFlex Bot Please enter your question!')

async def custom_command(update :Update , context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command under development!  Please use the other commands...')

def use_ai(input_string):
    client = Groq(
        api_key=API_KEY,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content":input_string,
            }
        ],
        model="mixtral-8x7b-32768",
    )

    response_from_ai = chat_completion.choices[0].message.content
    return response_from_ai


# Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'hello' in processed:
        return 'hey there , Im TrackFlex Bot How may I help You'
    elif 'whats your name' in processed:
        return 'Im TrackFlex Bot , for more information please contact the developer! @"TrackFlex"'
    elif processed != '':
        return use_ai(processed)
    
    return 'Sorry! Im not able to understand what your are saying...'


async def handle_message(update :Update , context : ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}:"{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
         response: str = handle_response(text)
         
    print('TrackFlex Bot: ',response)
    await update.message.reply_text(response)


async def error(update :Update , context : ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error : { context.error}')

if __name__ == '__main__':
    print('Starting Bot....')
    app = Application.builder().token(TOKEN).build()

    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #messages 
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    app.add_error_handler(error)

    #polling the bot 
    print('Polling ....')
    app.run_polling(poll_interval=3)
