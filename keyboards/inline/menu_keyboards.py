from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.db_commands import *
from utils.db_api.models import Speciality


menu_cd = CallbackData("show_menu", "level", "degree", "speciality", "menu1", "menu2", "menu3")
INSTITUTE_ID = 4

def make_callback_data(level, degree="0", speciality="0", menu1="0", menu2="0", menu3="0"):
    return menu_cd.new(
        level = level,
        degree = degree,
        speciality = speciality,
        menu1 = menu1,
        menu2 = menu2,
        menu3=menu3
    )

async def degrees_keyboard():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=1)

    degrees = await get_degrees()

    for degree in degrees:
        button_text = degree.degree_name
        callback_data = make_callback_data(
            level=CURRENT_LEVEL+1,
            degree=degree.degree_callbackdata
        )

        markup.insert(
            InlineKeyboardButton(
                text = button_text,
                callback_data=callback_data
            )
        )

    return markup

async def specialities_keyboard(degree):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup(row_width=1)

    #institute_id = get_institute_id_by_code(institute)

    departments_in_institute = await get_departments_ids(INSTITUTE_ID) #institute_id
    departments_in_institute_list = [l[0] for l in departments_in_institute]
    degree_id = await get_degree_id(degree)
    specialities_list = await get_specialities(departments_in_institute_list, degree_id)
    
    

    print(specialities_list)
    for speciality in specialities_list:
        button_text = speciality.speciality_name
        callback_data = make_callback_data(
            level=CURRENT_LEVEL+1,
            degree=degree,
            speciality=speciality.speciality_callbackdata
        )

        markup.insert(
            InlineKeyboardButton(
                text = button_text,
                callback_data=callback_data
            )
        )
    markup.row(
        InlineKeyboardButton(
            text = "Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL-1)
        )
    )
    return markup

async def menu1_keyboard(degree, speciality, level, menu1):
    CURRENT_LEVEL = 2 #int(level)
    markup = InlineKeyboardMarkup(row_width=1)

    questions_list = await get_menu_data(menu_level=1)

    for question in questions_list:
        button_text = question.question_name
        callback_data = make_callback_data(
            level = CURRENT_LEVEL+1,
            degree = degree,
            speciality = speciality,
            menu1 = question.question_callbackdata

        )
        markup.row(
            InlineKeyboardButton(
                text = button_text, callback_data=callback_data
            )
        )
    
    markup.row(
        InlineKeyboardButton(
            text = "Назад",
            callback_data=make_callback_data(
                level = CURRENT_LEVEL-1,
                degree=degree,
                speciality=speciality
            )
        )
    )

    return markup
    
async def menu2_keyboard(degree, speciality, menu_level, menu1):
    CURRENT_LEVEL = 3
    markup = InlineKeyboardMarkup(row_width=1)

    questions_list = await get_menu_data(menu_level=2, parent=menu1)

    for question in questions_list:
        button_text = question.question_name
        callback_data = make_callback_data(
            level = CURRENT_LEVEL+1,
            degree = degree,
            speciality = speciality,
            menu1 = menu1,
            menu2 = question.question_callbackdata

        )
        markup.row(
            InlineKeyboardButton(
                text = button_text, callback_data=callback_data
            )
        )
    
    markup.row(
        InlineKeyboardButton(
            text = "Назад",
            callback_data=make_callback_data(
                level = CURRENT_LEVEL-1,
                degree=degree,
                speciality=speciality,
                menu1 = menu1
            )
        )
    )

    return markup

async def menu3_keyboard(degree, speciality, menu_level, menu1, menu2):
    CURRENT_LEVEL = 4
    markup = InlineKeyboardMarkup(row_width=1)

    questions_list = await get_menu_data(menu_level=3, parent=menu2)

    for question in questions_list:
        button_text = question.question_name
        qstn_qdata = question.question_callbackdata
        callback_data = make_callback_data(
            level = CURRENT_LEVEL+1,
            degree = degree,
            speciality = speciality,
            menu1 = menu1,
            menu2 = menu2,
            menu3 = qstn_qdata

        )
        markup.row(
            InlineKeyboardButton(
                text = button_text, callback_data=callback_data
            )
        )
    
    markup.row(
        InlineKeyboardButton(
            text = "Назад",
            callback_data=make_callback_data(
                level = CURRENT_LEVEL-1,
                degree=degree,
                speciality=speciality,
                menu1 = menu1
            )
        )
    )

    return markup

def show_menu_back_markup(degree, speciality, level, menu1, menu2, menu3):
    CURRENT_LEVEL = int(level)
    markup = InlineKeyboardMarkup(row_width=1)
    markup.row(
        InlineKeyboardButton(
            text="Назад", 
            callback_data = make_callback_data(
                level = CURRENT_LEVEL-1,
                degree = degree,
                speciality = speciality,
                menu1=menu1,
                menu2 = menu2,
                menu3 = menu3
            )
        )
    )

    return markup

