from subprocess import call
from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, bot
from keyboards.inline.menu_keyboards import *

from utils.db_api.db_commands import get_question_result, add_message, delete_message

import logging

@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    logging.info(f"id={message.from_user.id}, full_name={message.from_user.full_name}, locale={message.from_user.locale}, mention={message.from_user.mention}, username={message.from_user.username}")
    await list_degrees(message)

#Запись в базу о сообщении для удаления и отправка файла в чат
async def send_file(question_callbackdata, callback):
    check_file = await check_have_file(question_callbackdata)
    if check_file:
        file_names = await get_file_names(question_callbackdata)
        
        for file_name in eval(file_names):
            msg = await bot.send_document(chat_id = callback.message['chat']['id'], document = open(f'files/documents/{file_name}', 'rb'))
            await add_message(
                message_id = msg.message_id, 
                chat_id = msg.chat.id, 
                question_callbackdata = question_callbackdata
            )
                     
async def list_degrees(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await degrees_keyboard()

    if isinstance(message, types.Message):
        await message.answer(f"{message['from']['first_name']}, пожалуйста выберите уровень, на котором вы обучаетесь:", reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_text(
            text=f"{call['from']['first_name']}, пожалуйста выберите уровень, на котором вы обучаетесь:"
        )

        await call.message.edit_reply_markup(markup)

async def list_specialities(callback: types.CallbackQuery, degree, speciality, level, menu1, menu2, menu3):
    await callback.message.edit_text(text = "Выберите вашу специальность!")
    markup = await specialities_keyboard(degree)
    await callback.message.edit_reply_markup(markup)

async def list_menu1(callback: types.CallbackQuery, degree, speciality, level, menu1, menu2, menu3):
    res_text = "Выберите вопрос"

    if menu1 != "0":
        check = await check_have_child(menu1)
        if not check:
            #WHEN CLICKED BACK
            #удалить отправленный файл при нажатии назад
            message_ids = await get_message_id(callback.from_user.id, menu1)
            for message_id in message_ids:
                await delete_message(message_id[0])
                await bot.delete_message(chat_id = callback.from_user.id, message_id = message_id[0])

            await callback.message.edit_text(text = res_text)
            markup = await menu1_keyboard(degree, speciality, level, menu1)
        else:
            markup = await menu1_keyboard(degree, speciality, level, menu1)
            await callback.message.edit_text(text = res_text)
    else:
        markup = await menu1_keyboard(degree, speciality, level, menu1)
        await callback.message.edit_text(text = res_text)

    await callback.message.edit_reply_markup(markup)  

async def list_menu2(callback: types.CallbackQuery, degree, speciality, level, menu1, menu2, menu3):
    res_text = "Выберите вопрос"
    
    check_child = await check_have_child(menu1)
    if check_child:
        await callback.message.edit_text(text = res_text)

    else:
        
        await send_file(menu1, callback)
        res_text = await get_question_result(menu1)
        # await callback.message.edit_text(text = f"list_menu2_back = {res_text}")
        # markup = show_menu_back_markup(degree, speciality, int(level), menu1, menu2, menu3)

        if menu1=="qn_1":
            department_id = await get_department_id_by_speciality(speciality)
            data = await get_department_info_by_id(department_id)
            data_text = f"{data.department_name} \n\n {data.department_address} \n {data.department_url} \n Заведующий(ая) кафедрой: {data.head_of_department} \n email: {data.email_of_head} \n Тел: {data.phone_of_department} \n {data.url_of_head}"       
        elif menu1=="qn_2":
            data = await get_institute_info_by_id(INSTITUTE_ID)
            data_text = f"{data.institute_name} \n\n {data.institute_address} \n {data.institute_url} \n {data.institute_phone} \n {data.institute_manager_email} \n Директор Института: {data.inst_dir_name} \n email: {data.inst_dir_email} \n Тел: {data.inst_dir_phone} \n {data.inst_dir_url} \n Заместители директора: 1) {data.first_deputy_info} \n 2) {data.second_deputy_info} \n 3) {data.third_deputy_info}"    
        elif menu1=="qn_9":
            data_institute = await get_institute_info_by_id(INSTITUTE_ID)
            data_question = await get_question_result(menu1)
            data_text = f"{data_question} {data_institute.second_deputy_info}"

        else:
            try:
                data_text = await get_question_result(menu1)
            except Exception as e:
                print(e)

        await callback.message.edit_text(text = data_text)

    #try delete messages
    try:
        message_ids = await get_message_id(callback.from_user.id, menu2)
        for message_id in message_ids:
            await delete_message(message_id[0])
            await bot.delete_message(chat_id = callback.from_user.id, message_id = message_id[0])
    except Exception as e:
        print(e)

    markup = await menu2_keyboard(degree, speciality, level, menu1)
    await callback.message.edit_reply_markup(markup)     
    
async def list_menu3(callback: types.CallbackQuery, degree, speciality, level, menu1, menu2, menu3):
    res_text = "Выберите вопрос"

    check = await check_have_child(menu2)
    if check:
        await callback.message.edit_text(text = res_text)

        markup = await menu3_keyboard(degree, speciality, level, menu1, menu2)
    else:
        await send_file(menu2, callback)
        if menu2 == "qn_16":
            res_text = await get_differentquestion_result(INSTITUTE_ID, menu2)
        else:
            res_text = await get_question_result(menu2)
        await callback.message.edit_text(text = res_text)

        markup = show_menu_back_markup(degree, speciality, int(level), menu1, menu2, menu3)
    
    #try delete messages
    try:
        message_ids = await get_message_id(callback.from_user.id, menu3)
        for message_id in message_ids:
            await delete_message(message_id[0])
            await bot.delete_message(chat_id = callback.from_user.id, message_id = message_id[0])
    except Exception as e:
        print(e)

    await callback.message.edit_reply_markup(markup)

async def show_last_menu(callback: types.CallbackQuery, degree, speciality, level, menu1, menu2, menu3):
    res_text = await get_differentquestion_result(INSTITUTE_ID, menu3)
    markup = show_menu_back_markup(degree, speciality, int(level), menu1, menu2, menu3)
    await send_file(menu3, callback)
    await callback.message.edit_text(text = res_text)
    await callback.message.edit_reply_markup(markup)

@dp.callback_query_handler(menu_cd.filter())
async def navigate(call:types.CallbackQuery, callback_data:dict):
    current_level = callback_data.get('level')
    degree = callback_data.get('degree')
    speciality = callback_data.get('speciality')
    menu1 = callback_data.get('menu1')
    menu2 = callback_data.get('menu2')
    menu3 = callback_data.get('menu3')


    levels = {
        "0": list_degrees,
        "1": list_specialities,
        "2": list_menu1,
        "3": list_menu2,
        "4": list_menu3,
        "5": show_last_menu
    }

    current_level_function = levels[current_level]

    await current_level_function(
        call,
        level = current_level,
        degree = degree,
        speciality = speciality,
        menu1 = menu1,
        menu2 = menu2,
        menu3 = menu3,
        
    )
