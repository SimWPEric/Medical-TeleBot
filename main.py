from typing import Final
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext, ConversationHandler
import csv

TOKEN: Final = ''
BOT_USERNAME: Final = ''

SYMPTOMS, PVD_CVA_FH, RECENT_TEST, RF_FHX_PREM, RF_CKD, RF_DM, RF_OTHERS, SCORING = range(8)

async def start_command(update: Update, context: CallbackContext):
    context.user_data.clear()

    keyboard = [
        [
            InlineKeyboardButton("FALSE", callback_data="symptoms:FALSE"),
            InlineKeyboardButton("SOB", callback_data="symptoms:SOB"),
            InlineKeyboardButton("Chest pain", callback_data="symptoms:Chest pain"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("To end the current questionnaire, type /end\nWhat are the patient's symptoms?", reply_markup=reply_markup)

    return SYMPTOMS

async def symptoms_callback_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    symptoms_option = query.data.split(":")[1]
    context.user_data['symptoms'] = symptoms_option

    keyboard = [
        [
            InlineKeyboardButton("TRUE", callback_data="pvd_cva_fh:TRUE"),
            InlineKeyboardButton("FALSE", callback_data="pvd_cva_fh:FALSE"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_text("Does the patient have PVD/CVA/FH (Peripheral Vascular Disease / Cerebrovascular Disease / Family History)?", reply_markup=reply_markup)

    return PVD_CVA_FH

async def pvd_cva_fh_callback_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    pvd_cva_fh_option = query.data.split(":")[1]
    context.user_data['pvd_cva_fh'] = pvd_cva_fh_option

    keyboard = [
        [
            InlineKeyboardButton("NEGATIVE", callback_data="recent_test:NEGATIVE"),
            InlineKeyboardButton("N/A", callback_data="recent_test:N/A"),
            InlineKeyboardButton("SUGGESTIVE", callback_data="recent_test:SUGGESTIVE"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_text("What's the result of the recent test?", reply_markup=reply_markup)

    return RECENT_TEST

async def recent_test_callback_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    recent_test_option = query.data.split(":")[1]
    context.user_data['recent_test'] = recent_test_option

    keyboard = [
        [
            InlineKeyboardButton("TRUE", callback_data="rf_fhx_prem:TRUE"),
            InlineKeyboardButton("FALSE", callback_data="rf_fhx_prem:FALSE"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_text("Does the patient have a family history of premature CAD (Coronary Artery Disease)?", reply_markup=reply_markup)

    return RF_FHX_PREM

async def rf_fhx_prem_callback_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    rf_fhx_prem_option = query.data.split(":")[1]
    context.user_data['rf_fhx_prem'] = rf_fhx_prem_option

    keyboard = [
        [
            InlineKeyboardButton("DM", callback_data="rf_ckd:DM"),
            InlineKeyboardButton("Moderate risk", callback_data="rf_ckd:Moderate risk"),
            InlineKeyboardButton("Very high risk or high risk", callback_data="rf_ckd:Very high risk or high risk"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_text("Does the patient have CKD (Chronic Kidney Disease)?", reply_markup=reply_markup)

    return RF_CKD

async def rf_ckd_callback_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    rf_ckd_option = query.data.split(":")[1]
    context.user_data['rf_ckd'] = rf_ckd_option

    keyboard = [
        [
            InlineKeyboardButton("DM", callback_data="rf_dm:DM"),
            InlineKeyboardButton("Moderate risk", callback_data="rf_dm:Moderate risk"),
            InlineKeyboardButton("Very high risk or high risk", callback_data="rf_dm:Very high risk or high risk"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_text("Does the patient have DM (Diabetes Mellitus)?", reply_markup=reply_markup)

    return RF_DM

async def rf_dm_callback_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    rf_dm_option = query.data.split(":")[1]
    context.user_data['rf_dm'] = rf_dm_option

    keyboard = [
        [
            InlineKeyboardButton("TRUE", callback_data="rf_others:TRUE"),
            InlineKeyboardButton("FALSE", callback_data="rf_others:FALSE"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_text("Are there other risk factors according to ACC 2019 guidelines?", reply_markup=reply_markup)

    return RF_OTHERS

async def rf_others_callback_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    rf_others_option = query.data.split(":")[1]
    context.user_data['rf_others'] = rf_others_option

    keyboard = [
        [
            InlineKeyboardButton("LOW", callback_data="scoring:LOW"),
            InlineKeyboardButton("INT", callback_data="scoring:INT"),
            InlineKeyboardButton("HIGH", callback_data="scoring:HIGH"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_text("What's the scoring for FHS TYR (Framingham Hard Coronary Heart Disease Ten-Year Risk)?", reply_markup=reply_markup)

    return SCORING

async def scoring_callback_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    scoring_option = query.data.split(":")[1]
    context.user_data['scoring'] = scoring_option

    symptoms_option = context.user_data.get('symptoms', 'Unknown')
    pvd_cva_fh_option = context.user_data.get('pvd_cva_fh', 'Unknown')
    recent_test_option = context.user_data.get('recent_test', 'Unknown')
    rf_fhx_prem_option = context.user_data.get('rf_fhx_prem', 'Unknown')
    rf_ckd_option = context.user_data.get('rf_ckd', 'Unknown')
    rf_dm_option = context.user_data.get('rf_dm', 'Unknown')
    rf_others_option = context.user_data.get('rf_others', 'Unknown')
    scoring_option = context.user_data.get('scoring', 'Unknown')
    
    decision = "Unknown"  

    csv_file_path = "Data.csv"

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        try: 
            next(csv_reader)
            for row in csv_reader:
                if (
                    row[0] == symptoms_option and
                    row[1] == pvd_cva_fh_option and
                    row[2] == recent_test_option and 
                    row[3] == rf_fhx_prem_option and
                    row[4] == rf_ckd_option and
                    row[5] == rf_dm_option and
                    row[6] == rf_others_option and
                    row[7] == scoring_option 
                ):
                    decision = row[8]
                    break
        except StopIteration: 
            decision = "Error in reading dataset"

    user_choices = context.user_data
    message = "Here are the choices you made:\n"
    for key, value in user_choices.items():
        message += f"{key}: {value}\n"
    message += f"Valve Decision: {decision}"

    await query.message.reply_text(message)

    await query.message.reply_text("Do you want to start again? Type /start to begin a new assessment.")

    return ConversationHandler.END

async def cancel_command(update: Update, context: CallbackContext):
    context.user_data.clear()
    await update.message.reply_text("Conversation cancelled. Type /start to begin a new assessment.")
    return ConversationHandler.END

if __name__ == '__main__':
    print('Starting bot ...')
    app = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start_command)],
        states={
            SYMPTOMS: [CallbackQueryHandler(symptoms_callback_handler)],
            PVD_CVA_FH: [CallbackQueryHandler(pvd_cva_fh_callback_handler)],
            RECENT_TEST: [CallbackQueryHandler(recent_test_callback_handler)],
            RF_FHX_PREM: [CallbackQueryHandler(rf_fhx_prem_callback_handler)],
            RF_CKD: [CallbackQueryHandler(rf_ckd_callback_handler)],
            RF_DM: [CallbackQueryHandler(rf_dm_callback_handler)],
            RF_OTHERS: [CallbackQueryHandler(rf_others_callback_handler)],
            SCORING: [CallbackQueryHandler(scoring_callback_handler)],
        },
        fallbacks=[CommandHandler('end', cancel_command)],
    )
    app.add_handler(conv_handler)

    print("Polling ...")
    app.run_polling(poll_interval=1)
