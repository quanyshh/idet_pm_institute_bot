#from utils.db_api.models import Degree, Department,  Institute, Question, Speciality, Message, Differentquestion
from models import Degree, Department, Institute, Speciality, Question, Message, Differentquestion

from typing import List
from sqlalchemy import and_

#from utils.db_api.database import db
from database import db


async def add_degrees(**kwargs):
    new_degree = await Degree(**kwargs).create()
    return new_degree

async def get_degrees() -> List[Degree]:
    return await Degree.query.gino.all()

async def get_degree_id(degree_callbackdata):
    return await Degree.select('id').where(Degree.degree_callbackdata==degree_callbackdata).gino.scalar()
#----------------------------------------------------------

async def add_institutes(**kwargs):
    new_institute = await Institute(**kwargs).create()
    return new_institute

async def get_institutes() -> List[Institute]:
    return await Institute.query.gino.all()

async def get_institute_id_by_code(institute_calbackdata):
    return await Institute.query.where(Institute.institute_callbackdata == institute_calbackdata).gino.first()

async def get_institute_info_by_id(institute_id):
    return await Institute.query.where(Institute.id == institute_id).gino.first()

#----------------------------------------------------------

async def add_departments(**kwargs):
    new_department = await Department(**kwargs).create()
    return new_department

async def get_departments_ids(institute_id):
    return await Department.select('id').where(Department.institute_id == institute_id).gino.all()

async def get_department_info_by_id(department_id):
    return await Department.query.where(Department.id == department_id).gino.first()
#----------------------------------------------------------

async def add_specialities(**kwargs):
    return await Speciality(**kwargs).create()

async def get_specialities(department_ids_list, degree_id) -> List[Speciality]:
    return await Speciality.query.where(
        and_(
            Speciality.department_id.in_(department_ids_list),
            Speciality.degree_id == degree_id
        )
    ).gino.all()

async def get_department_id_by_speciality(speciality_callbackdata):
    return await Speciality.select('department_id').where(Speciality.speciality_callbackdata == speciality_callbackdata).gino.scalar()

#----------------------------------------------------------


async def add_question(**kwargs):
    return await Question(**kwargs).create()

async def get_questions():
    return await Question.query.gino.all()

async def get_menu_data(menu_level, parent=None):
    if parent:
        return await Question.query.where(
            and_(
                Question.menu_level == menu_level,
                Question.parent_callbackdata == parent
            )
        ).gino.all()
    else:
        return await Question.query.where(
            Question.menu_level == menu_level
        ).gino.all()

async def check_have_child(question_callbackdata):
    return await Question.select('have_child').where(
            Question.question_callbackdata == question_callbackdata
        ).gino.scalar()

async def check_have_file(question_callbackdata):
    return await Question.select('have_file').where(
            Question.question_callbackdata == question_callbackdata
        ).gino.scalar()

async def get_question_result(question_callbackdata):
    return await Question.select('question_result').where(
            Question.question_callbackdata == question_callbackdata
        ).gino.scalar()

async def get_file_names(question_callbackdata):
    return await Question.select('file_name').where(
        Question.question_callbackdata == question_callbackdata
        ).gino.scalar()


#----------------------------------------------------------

async def add_message(**kwargs):
    return await Message(**kwargs).create()

async def get_message_id(chat_id, question_callbackdata):
    return await Message.select('message_id').where(
        and_(
            Message.chat_id == chat_id,
            Message.question_callbackdata == question_callbackdata
        )
    ).gino.all()

async def delete_message(message_id):
    return await Message.delete.where(Message.message_id == message_id).gino.status()

#----------------------------------------------------------

async def add_different_question(**kwargs):
    return await Differentquestion(**kwargs).create()

async def get_differentquestion_result(INSTITUTE_ID, question_callbackdata):
    return await Differentquestion.select('question_result').where(
            and_(
                Differentquestion.institute_id == INSTITUTE_ID,
                Differentquestion.question_callbackdata == question_callbackdata
            )
        ).gino.scalar()