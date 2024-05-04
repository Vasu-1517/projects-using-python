
 

import warnings
warnings.filterwarnings("ignore", category=UserWarning, message="python-telegram-bot is using upstream urllib3.")


import telegram.ext

token = "7071019757:AAE4pS_aW0bM-LObAZCyjB8IEtNhl0JUNWQ"
updater = telegram.ext.Updater("7071019757:AAE4pS_aW0bM-LObAZCyjB8IEtNhl0JUNWQ", use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Hello! Welcome to vasbot.")

def help(update, context):
    update.message.reply_text("""
    /start --> Welcome message
    /help --> Help message
    /python --> Python tutorial link
    /sql --> SQL tutorial link
    /java --> Java tutorial link
    /javascript --> javascript tutorial link
    /aptitude --> aptitude tutorial
    /htmlcss -->htmlcss tutorial
    /communication -->To improve communication skills follow this tedx videos daily at least 30min 
    /dsa -->dsa tutorails
    /etltalend -->etl talend tutorial link
    /nosql --> nosql tutorial link
    
    """)



def python(update, context):
    update.message.reply_text("tutorials link :https://www.youtube.com/watch?v=EyEqWFvLDT8&t=132s")

def sql(update, context):
    update.message.reply_text("Tutorial link: https://www.youtube.com/watch?v=q_JsgpiuY98&list=PL9ooVrP1hQOG6DQnOD6ujdCEchaqADfCU")

def java(update, context):
    update.message.reply_text("Tutorial link: https://www.youtube.com/watch?v=BGTx91t8q50&list=PLsyeobzWxl7q6oUFts2erdot6jxF_lisP")
    
def nosql(update, context):
    update.message.reply_text("Tutorial link:https://www.youtube.com/watch?v=qEhNHOEa5sE&list=PLsyeobzWxl7r0bn6dzVA8bQNxcx7DRl5F ")
def dsa(update, context):
    update.message.reply_text("Tutorial link: https://www.youtube.com/watch?v=xWLxhF3b5P8")
def javascript(update, context):
    update.message.reply_text("Tutorial link: https://www.youtube.com/watch?v=SBmSRK3feww&list=PLEPye7A7EcQaCkSNNSTLdlfPm4f2fkQgG")
def htmlcss(update, context):
    update.message.reply_text("Tutorial link: https://www.youtube.com/watch?v=G3e-cpL7ofc&list=PLEPye7A7EcQZrT3VSBb7jtxnxIfY3yyG6")
    
def aptitude(update, context):
    update.message.reply_text("Tutorial link: https://www.youtube.com/@ChandanLogics")
    
def communication(update, context):
    update.message.reply_text("Tutorial link: https://www.youtube.com/watch?v=Hu4Yvq-g7_Y")
    
def etltalend(update, context):
    update.message.reply_text("Tutorial link: https://www.youtube.com/watch?v=kCX_H9_Y2Ls&list=PLErD1cRL87W-J1RqryotlquXxJRaY6DQ_")
    
dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.CommandHandler('communication', communication))
dispatcher.add_handler(telegram.ext.CommandHandler('python', python))
dispatcher.add_handler(telegram.ext.CommandHandler('sql', sql))
dispatcher.add_handler(telegram.ext.CommandHandler('java', java))
dispatcher.add_handler(telegram.ext.CommandHandler('javascirpt', javascript))
dispatcher.add_handler(telegram.ext.CommandHandler('htmlcss', htmlcss))
dispatcher.add_handler(telegram.ext.CommandHandler('nosql', nosql))

dispatcher.add_handler(telegram.ext.CommandHandler('aptitude', aptitude))
dispatcher.add_handler(telegram.ext.CommandHandler('dsa', dsa))
dispatcher.add_handler(telegram.ext.CommandHandler('etltalend', etltalend))


updater.start_polling()
updater.idle()
