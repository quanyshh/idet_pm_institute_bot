import asyncio
from database import create_db
from db_commands import add_degrees, add_institutes, add_departments, add_question, add_specialities, add_different_question



async def add_data():

    #backelor
    await add_degrees(
        degree_name="Бакалавриат",
        degree_callbackdata="backhelor"
    )

    #master
    await add_degrees(
        degree_name="Магистратура",
        degree_callbackdata="master"
    )

    #phd
    await add_degrees(
        degree_name="Докторантура",
        degree_callbackdata="phd"
    )

    #-----------------------------------

    #oilgas
    await add_institutes(
        institute_name = "Институт геологии и нефтегазового дела им. К. Турысова",
        institute_callbackdata = "inst_oilgas",
        institute_address = "Ваша Дирекция Института (Деканат) находится по адресу Сатпаева 22. Этаж 3. Кабинет 325. (Здание - Главный учебный корпус)",
        institute_url = "https://satbayev.university/ru/institutes/geology-oil-gas-business",
        institute_phone = "+7(727) 2577171 (7220)",
        institute_manager_email = "l.adilbekova@satbayev.university",
        inst_dir_name = "Сыздыков Аскар Хамзаевич",
        inst_dir_email = "a.syzdykov@satbayev.university",
        inst_dir_url = "https:// official.satbayev.university/ru/teachers/syzdykov-askar-khamzaevich",
        inst_dir_phone = "+7(727) 320-40-31",
        first_deputy_info = "Аршамов Ялкунжан Камалович (Курирует академическую часть) \n email: y.arshamov@satbayev.university \n https://official.satbayev.university/ru/teachers/arshamov-yalkunzhan \n Тел: +7(727) 2577171 (7412) \n",
        second_deputy_info = "Макыжанова Асыл Темиртаевна (Курирует учебно-воспитательную часть) \n email: a.makyzhanova@satbayev.university \n https://official.satbayev.university/ru/teachers/makyzhanova-asyl-temirtaevna \n Тел: +7(727)320-41-79 \n",
        third_deputy_info = "Нарбаев Марс Турсынбекович (Курирует научную часть) \n email: m.narbayev@satbayev.university \n Тел: +7(727)320-40-41"
    )

    await add_institutes(
        institute_name = "Горно-металлургический институт имени О.А. Байконурова",
        institute_callbackdata = "inst_gmi",
        institute_address = "Институт находится в Горно-металлургическом корпусе (ГМК) по адресу Сатпаева 22, угол Масанчи. Этаж 2. Кабинет 232",
        institute_url = "https://official.satbayev.university/ru/mining-metallurgy",
        institute_phone = "+7(727)320-41-35",
        institute_manager_email = "n.toregali@satbayev.university \n a.kerimbek@satbayev.university",
        inst_dir_name = "Рысбеков Канай Бахытович",
        inst_dir_email = "k.rysbekov@satbayev.university",
        inst_dir_url = "",
        inst_dir_phone = "",
        first_deputy_info = "Айтенов Кенесбай Джолдасбаевич (Курирует учебную часть ) \n Email: k.aitenov@satbayev.university \n Тел: +7(727)320-40-43",
        second_deputy_info = "Куандыков Тилепбай Алимбаевич (Курирует Воспитательную часть) \n Email: t.kuandykov@satbayev.university \n Тел: +7(727)320-40-45",
        third_deputy_info = "Мырзахметов Сайфилмалик Серикбаевич (Курирует научную часть) \n Email: s.myrzakhmetov@satbayev.university \n Тел: +7(727)320-40-43",
    )

    await add_institutes(
        institute_name = "Институт архитектуры и строительства им. Т.К.Басенова",
        institute_callbackdata = "inst_ac",
        institute_address = "МУК 202",
        institute_url = "",
        institute_phone = "+7 (727) 292-09-16, +7 (727) 320-40-37",
        institute_manager_email = "t.matveyeva@satbayev.university",
        inst_dir_name = "Куспангалиев Болат Урайханович",
        inst_dir_email = "b.kuspangaliyev@satbayev.university",
        inst_dir_url = "",
        inst_dir_phone = "",
        first_deputy_info = "Батесова Фируза Кайсарбековна \n f.batessova@satbayev.university \n Тел: +7 (727) 320-40-47 \n МУК 201",
        second_deputy_info = "Шевцова Владлена Степановна \n v.shevtsova@satbayev.university \n +7 (727) 320-40-47 \n МУК 201",
        third_deputy_info = "Зам. директора по науке Жұмаділова Жанар Оразбекқызы \n  z.zhumadilova@satbayev.university \n  +7 (727) 320-41-91 \n МУК 200",
    )

    await add_institutes(
        institute_name = "Институт управления проектами имени Е Туркебаева",
        institute_callbackdata = "inst_pn",
        institute_address = "Ваша Дирекция Института управления проектами имени Е Туркебаева (Деканат) находится по адресу Сатпаева 22. Главный учебный корпус (ГУК) этаж 4. Кабинет 415.",
        institute_url = "https://official.satbayev.university/ru/project-management",
        institute_phone = "+7(727)320-41-38 ",
        institute_manager_email = "a.kulbayeva@satbayev.university",
        inst_dir_name = "Амралинова Бакытжан Базарбековна",
        inst_dir_email = "b.amralinova@satbayev.university",
        inst_dir_url = "",
        inst_dir_phone = "",
        first_deputy_info = "Абенова Майра Хомаровна \n Email: m.abenova@satbayev.university \n Тел: +7(727)320-40-48 \n",
        second_deputy_info = "Иманкулова Бахыткуль Борисовна (Курирует Воспитательную работу) \n Email: b.imankulova@satbayev.university \n Тел: +7(727)320-40-48 \n",
        third_deputy_info = "Кулбаева Акерке Тиналовна  (гл. менеджер) \n Email: a.kulbayeva@satbayev.university \n Тел: +7(727)320-41-38 \n",
    )


    # await add_institutes(
    #     institute_name = "",
    #     institute_callbackdata = "",
    #     institute_address = "",
    #     institute_url = "",
    #     institute_phone = "",
    #     institute_manager_email = "",
    #     inst_dir_name = "",
    #     inst_dir_email = "",
    #     inst_dir_url = "",
    #     inst_dir_phone = "",
    #     first_deputy_info = "",
    #     second_deputy_info = "",
    #     third_deputy_info = "",
    # )

    #-----------------------------------

    #departments of oilgas institute_id = 1,
    await add_departments(
        department_name = "Кафедра Геологической съемки, поиска и разведки месторождений полезных ископаемых",
        department_callbackdata = "inst1_dep1",
        institute_id = 1,
        department_address = "Ваша Кафедра находится по адресу Сатпаева 22. Этаж 4. Кабинет 439. (Здание ГУК)",
        department_url = "https:// official.satbayev.university/ru/geology-oil-gas-business/gspemd",
        head_of_department = "Бекботаева Алма Анарбековна",
        email_of_head = "a.bekbotayeva@satbayev.university",
        phone_of_department = "+7(727)257-71-71 (внут 7327)",
        url_of_head = "https://official.satbayev.university/ru/teachers/bekbotaeva-alma-anarbekovna",
    )

    await add_departments(
        department_name = "Кафедра Нефтяной инженерии",
        department_callbackdata = "inst1_dep2",
        institute_id = 1,
        department_address = "Ваша Кафедра находится по адресу Сатпаева 22. Этаж 7. Кабинет 711. (Здание Нефтяного корпуса)",
        department_url = "https:// official.satbayev.university/ru/geology-oil-gas-business/kafedra-neftyanoy-inzhenerii",
        head_of_department = "Елигбаева Гульжахан Жакпаровна",
        email_of_head = "y.sarsenbayev@satbayev.university",
        phone_of_department = "+7(727) 320-40-58",
        url_of_head = "https://official.satbayev.university/ru/teachers/eligbaeva-gulzhakhan-zhakparovna",
    )

    await add_departments(
        department_name = "Кафедра Геофизики",
        department_callbackdata = "inst1_dep3",
        institute_id = 1,
        department_address = "Ваша Кафедра находится по адресу Сатпаева 22. Этаж 5. Кабинет 523. (Здание ГУК)",
        department_url = "https:// official.satbayev.university/ru/geology-oil-gas-business/gph",
        head_of_department = "Абетов Ауэз Егембердыевич",
        email_of_head = "a.abetov@satbayev.university",
        phone_of_department = "+7(727) 320-41-57",
        url_of_head = "https://official.satbayev.university/ru/teachers/abetov-auez-egemberdyev",
    )

    await add_departments(
        department_name = "Кафедра Гидрогеология, инженерная и нефтегазовая геология",
        department_callbackdata = "inst1_dep4",
        institute_id = 1,
        department_address = "Ваша Кафедра находится по адресу Сатпаева 22. Этаж 4,5. Кабинет 407, 513 ГУК",
        department_url = "https:// official.satbayev.university/ru/geology-oil-gas-business/gog",
        head_of_department = "Енсепбаев Талгат Аблаевич",
        email_of_head = "t.yensepbayev@satbayev.university",
        phone_of_department = "+7(727)257-71-71 (внут 7401)",
        url_of_head = "https://official.satbayev.university/ru/teachers/ensepbaev-talgat-ablaevich_1",
    )

    await add_departments(
        department_name = "Кафедра химической и биохимической инженерии",
        department_callbackdata = "inst1_dep5",
        institute_id = 1,
        department_address = "Ваша Кафедра находится по адресу Сатпаева 22. Этаж 10. Кабинет 1016 ГУК",
        department_url = "https://official.satbayev.university/ru/chemical-biological-technologies/cht",
        head_of_department = "Амитова Айгуль Амантаевна",
        email_of_head = "a.amitova@satbayev.university",
        phone_of_department = "+7(727)257-71-71 (внут 7061)",
        url_of_head = "https://official.satbayev.university/ru/teachers/amitova-aygul-amantaevna",
    )

    await add_departments(
        department_name = "Кафедра химических процессов и промышленной экологии",
        department_callbackdata = "inst1_dep6",
        institute_id = 1,
        department_address = "Ваша Кафедра находится по адресу Сатпаева 22. Этаж 4,5. Кабинет 140а ГМК",
        department_url = "https://official.satbayev.university/ru/chemical-biological-technologies/kafedra-khimicheskikh-protsessov-i-promyshlennoy-ekologii",
        head_of_department = "Кубекова Шолпан Накишбековна",
        email_of_head = "s.kubekova@satbayev.university",
        phone_of_department = "+7(727)257-71-71 (внут 7469)",
        url_of_head = "https://official.satbayev.university/ru/teachers/kubekova-sholpan-nakishbekovna",
    )

    #departments of mining and metallurgy institute_id = 2,
    await add_departments(
        department_name = "Кафедра Горное дело",
        department_callbackdata = "inst2_dep1",
        institute_id = 2,
        department_address = "Кафедра находится в Горно-металлургическом корпусе (ГМК) по адресу Сатпаева 22, угол Масанчи. Этаж 2. Кабинет 234, 115, 242",
        department_url = "",
        head_of_department = "Молдабаев Серик Курашович",
        email_of_head = "s.moldabayev@satbayev.university",
        phone_of_department = "только внутрений 72-45",
        url_of_head = "",
    )

    await add_departments(
        department_name = "Кафедра Маркшейдерское дело и геодезия",
        department_callbackdata = "inst2_dep2",
        institute_id = 2,
        department_address = "Кафедра находится в Горно-металлургическом корпусе (ГМК) по адресу Сатпаева 22, угол Масанчи. Этаж 2. Кабинет 238.",
        department_url = "",
        head_of_department = "Орынбасарова Эльмира Орынбасаровна",
        email_of_head = "e.orynbassarova@satbayev.university",
        phone_of_department = "+7 (727) 320-40-64",
        url_of_head = "",
    )

    await add_departments(
        department_name = "Кафедра Материаловедение, нанотехнологии и инженерная физика",
        department_callbackdata = "inst2_dep3",
        institute_id = 2,
        department_address = "Кафедра находится в Горно-металлургическом корпусе (ГМК) по адресу Сатпаева 22, угол Масанчи. Этаж 3. Кабинет 328.",
        department_url = "",
        head_of_department = "Какимов Улан Кадырханулы",
        email_of_head = "u.kakimov@satbayev.university",
        phone_of_department = "+7 (727) 292-54-51",
        url_of_head = "",
    )

    await add_departments(
        department_name = "Кафедра Металлургия и обогащение полезных ископаемых",
        department_callbackdata = "inst2_dep4",
        institute_id = 2,
        department_address = "Кафедра находится в Горно-металлургическом корпусе (ГМК) по адресу Сатпаева 22, угол Масанчи. Этаж 1. Кабинет 121.",
        department_url = "",
        head_of_department = "Барменшинова Мадина Богембаевна",
        email_of_head = "m.barmenshinova@satbayev.university",
        phone_of_department = "только внутрений 72-52",
        url_of_head = "",
    )
    
    await add_departments(
        department_name = "Кафедра Металлургические процессы, теплотехника и технологии специальных материалов",
        department_callbackdata = "inst2_dep5",
        institute_id = 2,
        department_address = "Кафедра находится в Горно-металлургическом корпусе (ГМК) по адресу Сатпаева 22, угол Масанчи. Этаж 3. Кабинет 311.",
        department_url = "",
        head_of_department = "Чепуштанова Татьяна Александровна",
        email_of_head = "t.chepushtanova@satbayev.university",
        phone_of_department = "только внутрений 73-46",
        url_of_head = "",
    )


    #departments of architecture institute_id = 3,
    await add_departments(
        department_name = "Кафедра Архитектура",
        department_callbackdata = "inst3_dep1",
        institute_id = 3,
        department_address = "ИМС 409",
        department_url = "",
        head_of_department = "Султанова Камиля Рамазановна",
        email_of_head = "k.sultanova@satbayev.university",
        phone_of_department = "+7 (727) 292-57-03",
        url_of_head = "",
    )

    await add_departments(
        department_name = "Кафедра Инженерные системы и сети",
        department_callbackdata = "inst3_dep2",
        institute_id = 3,
        department_address = "МУК 205",
        department_url = "",
        head_of_department = "Алимова Куляш Кабпасовна",
        email_of_head = "k.alimova@satbayev.university",
        phone_of_department = "+7 (727) 292-73-04",
        url_of_head = "",
    )

    await add_departments(
        department_name = "Кафедра Строительство и строительные материалы",
        department_callbackdata = "inst3_dep3",
        institute_id = 3,
        department_address = "МУК 301",
        department_url = "",
        head_of_department = "Наширалиев Жанкелди Туртемирович",
        email_of_head = "zh.nashiraliyev@satbayev.university",
        phone_of_department = "+7 (701) 907-97-43",
        url_of_head = "",
    )
    

    #departments of project management institute_id = 4,
    await add_departments(
        department_name = "Кафедра Логистика",
        department_callbackdata = "inst4_dep1",
        institute_id = 4,
        department_address = "Ваша Кафедра находится по адресу Сатпаева 22. Этаж 4. Кабинет 410. (Здание ГУК)",
        department_url = "",
        head_of_department = "Муханова Гульмира Самудиновна",
        email_of_head = "g.mukhanova@satbayev.university",
        phone_of_department = "+7 701 993 7718",
        url_of_head = "",
    )
    
    await add_departments(
        department_name = "Кафедра Менеджмент и математическая экономика",
        department_callbackdata = "inst4_dep2",
        institute_id = 4,
        department_address = "Ваша Кафедра находится по адресу Сатпаева 22, угол А.Байтурсынова. Этаж 4. Кабинет 408.",
        department_url = "",
        head_of_department = "Турегельдинова Алия Жумабековна",
        email_of_head = "management@satbayev.university",
        phone_of_department = "+7(727)320-40-91",
        url_of_head = "",
    )
    
    # await add_departments(
    #     department_name = "",
    #     department_callbackdata = "inst1_dep7",
    #     institute_id = 1,
    #     department_address = "",
    #     department_url = "",
    #     head_of_department = "",
    #     email_of_head = "",
    #     phone_of_department = "",
    #     url_of_head = "",
    # )

    #-----------------------------------


    #intitute 1 department 1
    await add_specialities(
        speciality_name = "ОП 6В07202, 6В05201 – Геология и разведка месторождений полезных ископаемых",
        speciality_callbackdata = "inst1_dep1_spec1",
        department_id = 1,
        degree_id = 1
    )
    
    await add_specialities(
        speciality_name = "ОП 7M07206 – Геология и разведка месторождений полезных ископаемых",
        speciality_callbackdata = "inst1_dep1_spec2",
        department_id = 1,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "ОП 8D07205 – Геология и разведка месторождений твердых полезных ископаемых",
        speciality_callbackdata = "inst1_dep1_spec3",
        department_id = 1,
        degree_id = 3
    )

    #intitute 1 department 2
    await add_specialities(
        speciality_name = "ОП 6В07204 – Petroleum engineering",
        speciality_callbackdata = "inst1_dep2_spec1",
        department_id = 2,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "ОП 6В07204 – Магистральные сети и инфраструктура",
        speciality_callbackdata = "inst1_dep2_spec2",
        department_id = 2,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "ОП 7M07202 – Нефтяная инженерия",
        speciality_callbackdata = "inst1_dep2_spec3",
        department_id = 2,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "ОП 8D07202 – Нефтяная инженерия",
        speciality_callbackdata = "inst1_dep2_spec4",
        department_id = 2,
        degree_id = 3
    )

    #intitute 1 department 3
    await add_specialities(
        speciality_name = "ОП 6В07201 – Нефтегазовая и рудная геофизика",
        speciality_callbackdata = "inst1_dep3_spec1",
        department_id = 3,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "ОП 7M07105 – Нефтегазовая и рудная геофизика",
        speciality_callbackdata = "inst1_dep3_spec2",
        department_id = 3,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "ОП 7M05302 – Сейсмология",
        speciality_callbackdata = "inst1_dep3_spec3",
        department_id = 3,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "ОП 8D07104 – Нефтегазовая и рудная геофизика",
        speciality_callbackdata = "inst1_dep3_spec4",
        department_id = 3,
        degree_id = 3
    )

    await add_specialities(
        speciality_name = "ОП 7 D05302 – Сейсмология",
        speciality_callbackdata = "inst1_dep3_spec5",
        department_id = 3,
        degree_id = 3
    )

    #intitute 1 department 4
    await add_specialities(
        speciality_name = "ОП 6В07202, 6В05201 – Геология и разведка месторождений полезных ископаемых",
        speciality_callbackdata = "inst1_dep4_spec1",
        department_id = 4,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "ОП 6В07211, 6В05202, 6В05104 – Гидрогеология и инженерная геология",
        speciality_callbackdata = "inst1_dep4_spec2",
        department_id = 4,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "ОП 6В08601 – Водные ресурсы и водопользование",
        speciality_callbackdata = "inst1_dep4_spec3",
        department_id = 4,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "ОП 7M07207 – Геология нефти и газа",
        speciality_callbackdata = "inst1_dep4_spec4",
        department_id = 4,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "ОП 7M05203 – Гидрогеология и инженерная геология",
        speciality_callbackdata = "inst1_dep4_spec5",
        department_id = 4,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "ОП 7М08601 – Водные ресурсы и водопользование",
        speciality_callbackdata = "inst1_dep4_spec6",
        department_id = 4,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "ОП 8D07206 – Геология нефти и газа",
        speciality_callbackdata = "inst1_dep4_spec7",
        department_id = 4,
        degree_id = 3
    )

    await add_specialities(
        speciality_name = "ОП 8D05202– Гидрогеология и инженерная геология",
        speciality_callbackdata = "inst1_dep4_spec8",
        department_id = 4,
        degree_id = 3
    )

    #intitute 1 department 5
    await add_specialities(
        speciality_name = "ОП 6В05101, 6B05102, 6B07110 – Химическая и биохимическая инженерия",
        speciality_callbackdata = "inst1_dep5_spec1",
        department_id = 5,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "ОП 6В07117 – Химическая технология нефтегазохимической продукции",
        speciality_callbackdata = "inst1_dep5_spec2",
        department_id = 5,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "ОП 7M07110 – Химические процессы и производство химических материалов",
        speciality_callbackdata = "inst1_dep5_spec3",
        department_id = 5,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "ОП 7M07109 – Химическая инженерия углеводородных соединений",
        speciality_callbackdata = "inst1_dep5_spec4",
        department_id = 5,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "ОП 8D07108 – Основные процессы синтеза и производства новых органических и полимерных материалов",
        speciality_callbackdata = "inst1_dep5_spec5",
        department_id = 5,
        degree_id = 3
    )

    await add_specialities(
        speciality_name = "ОП 8D07107 – Химическая инженерия углеводородных соединений",
        speciality_callbackdata = "inst1_dep5_spec6",
        department_id = 5,
        degree_id = 3
    )

    #intitute 1 department 6
    await add_specialities(
        speciality_name = "ОП 6В05101, 6B05102, 6B07110 – Химическая и биохимическая инженерия",
        speciality_callbackdata = "inst1_dep6_spec1",
        department_id = 6,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "ОП 6В05103 – Инженерная экология",
        speciality_callbackdata = "inst1_dep6_spec2",
        department_id = 6,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "ОП 6В07116 – Технология основных производств и новые материалы",
        speciality_callbackdata = "inst1_dep6_spec3",
        department_id = 6,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "ОП 7M07110 – Химические процессы и производство химических материалов",
        speciality_callbackdata = "inst1_dep6_spec4",
        department_id = 6,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "ОП 7M05101, 7М05202 – Биоэкологическая инженерия",
        speciality_callbackdata = "inst1_dep6_spec5",
        department_id = 6,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "ОП 7М07116, 7М05102, 7М05201 – Computation in chemical and biochemical engineering",
        speciality_callbackdata = "inst1_dep6_spec6",
        department_id = 6,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "ОП 8D07109 – Инновационные технологии и новые неорганические материалы",
        speciality_callbackdata = "inst1_dep6_spec7",
        department_id = 6,
        degree_id = 3
    )

    await add_specialities(
        speciality_name = "ОП 8D05201 – Биоэкологическая инженерия",
        speciality_callbackdata = "inst1_dep6_spec8",
        department_id = 6,
        degree_id = 3
    )


    #intitute 2 department 7
    await add_specialities(
        speciality_name = "6В07205 – Горная инженерия",
        speciality_callbackdata = "inst2_dep7_spec1",
        department_id = 7,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "7М07203 – Горная инженерия",
        speciality_callbackdata = "inst2_dep7_spec2",
        department_id = 7,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "7М07215 – Горная инженерия",
        speciality_callbackdata = "inst2_dep7_spec3",
        department_id = 7,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "8D07203 – Горная инженерия",
        speciality_callbackdata = "inst2_dep7_spec4",
        department_id = 7,
        degree_id = 3
    )

    #intitute 2 department 8
    await add_specialities(
        speciality_name = "6В07303 – Геопространственная цифровая инженерия",
        speciality_callbackdata = "inst2_dep8_spec1",
        department_id = 8,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "6В07304 – Геопространственная цифровая инженерия",
        speciality_callbackdata = "inst2_dep8_spec2",
        department_id = 8,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "7М07210 – Геопространственная цифровая инженерия",
        speciality_callbackdata = "inst2_dep8_spec3",
        department_id = 8,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "7М07306 – Геопространственная цифровая инженерия",
        speciality_callbackdata = "inst2_dep8_spec4",
        department_id = 8,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "8D07306 – Геопространственная цифровая инженерия",
        speciality_callbackdata = "inst2_dep8_spec5",
        department_id = 8,
        degree_id = 3
    )

    #intitute 2 department 9
    await add_specialities(
        speciality_name = "6В07109 - Инженерная физика и материаловедение",
        speciality_callbackdata = "inst2_dep9_spec1",
        department_id = 9,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "6В07207 - Инженерная физика и материаловедение",
        speciality_callbackdata = "inst2_dep9_spec2",
        department_id = 9,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "7M07103 – Материаловедение и технология новых материалов",
        speciality_callbackdata = "inst2_dep9_spec3",
        department_id = 9,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "7М05301 – Прикладная и инженерная физика",
        speciality_callbackdata = "inst2_dep9_spec4",
        department_id = 9,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "8D07103 Материаловедение и инженерия",
        speciality_callbackdata = "inst2_dep9_spec5",
        department_id = 9,
        degree_id = 3
    )

    await add_specialities(
        speciality_name = "8D05301 Прикладная и инженерная физика",
        speciality_callbackdata = "inst2_dep9_spec6",
        department_id = 9,
        degree_id = 3
    )

    #intitute 2 department 10
    await add_specialities(
        speciality_name = "6B07203 Металлургия и обогащение полезных ископаемых",
        speciality_callbackdata = "inst2_dep10_spec1",
        department_id = 10,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "7M07223 Металлургия и обогащение полезных ископаемых",
        speciality_callbackdata = "inst2_dep10_spec2",
        department_id = 10,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "7M07204 Металлургия и обогащение полезных ископаемых",
        speciality_callbackdata = "inst2_dep10_spec3",
        department_id = 10,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "8D07204 Металлургическая инженерия",
        speciality_callbackdata = "inst2_dep10_spec4",
        department_id = 10,
        degree_id = 3
    )

    await add_specialities(
        speciality_name = "8D07201 – Обогащение полезных ископаемых",
        speciality_callbackdata = "inst2_dep10_spec5",
        department_id = 10,
        degree_id = 3
    )

    #intitute 2 department 11
    await add_specialities(
        speciality_name = "6B07203 Металлургия и обогащение полезных ископаемых",
        speciality_callbackdata = "inst2_dep11_spec1",
        department_id = 11,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "7M07204 Металлургия и обогащение полезных ископаемых",
        speciality_callbackdata = "inst2_dep11_spec2",
        department_id = 11,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "8D07204 Металлургическая инженерия",
        speciality_callbackdata = "inst2_dep11_spec3",
        department_id = 11,
        degree_id = 3
    )

    #intitute 3 department 12
    await add_specialities(
        speciality_name = "6В02102 Дизайн",
        speciality_callbackdata = "inst3_dep12_spec1",
        department_id = 12,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "6В07307 Архитектура",
        speciality_callbackdata = "inst3_dep12_spec2",
        department_id = 12,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "6В07301 Архитектура и дизайн",
        speciality_callbackdata = "inst3_dep12_spec3",
        department_id = 12,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "6В02101 Архитектура и дизайн",
        speciality_callbackdata = "inst3_dep12_spec4",
        department_id = 12,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "5В042000 Архитектура",
        speciality_callbackdata = "inst3_dep12_spec5",
        department_id = 12,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "5В042100 Дизайн",
        speciality_callbackdata = "inst3_dep12_spec6",
        department_id = 12,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "7М07302 Архитектура и градостроительство",
        speciality_callbackdata = "inst3_dep12_spec7",
        department_id = 12,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "8D07302 Архитектура и градостроительство",
        speciality_callbackdata = "inst3_dep12_spec8",
        department_id = 12,
        degree_id = 3
    )

    #intitute 3 department 13
    await add_specialities(
        speciality_name = "6B07306 Инженерные системы и сети",
        speciality_callbackdata = "inst3_dep13_spec1",
        department_id = 13,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "6B11201 Гигиена и охрана труда на производстве",
        speciality_callbackdata = "inst3_dep13_spec2",
        department_id = 13,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "6В07302 Строительная инженерия",
        speciality_callbackdata = "inst3_dep13_spec3",
        department_id = 13,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "7M07304 Инженерные системы и сети (2 года)",
        speciality_callbackdata = "inst3_dep13_spec4",
        department_id = 13,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "7M07311 Инженерные системы и сети (1,5 год)",
        speciality_callbackdata = "inst3_dep13_spec5",
        department_id = 13,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "7M07312 Инженерные системы и сети (1 год)",
        speciality_callbackdata = "inst3_dep13_spec6",
        department_id = 13,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "7M11201 Гигиена и охрана труда на производстве",
        speciality_callbackdata = "inst3_dep13_spec7",
        department_id = 13,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "8D07304 Инженерные системы и сети",
        speciality_callbackdata = "inst3_dep13_spec8",
        department_id = 13,
        degree_id = 3
    )

    #intitute 3 department 14
    await add_specialities(
        speciality_name = "5B079200 - Строительство",
        speciality_callbackdata = "inst3_dep14_spec1",
        department_id = 14,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "5B073000 - Производство строительных материалов изделии и конструкции",
        speciality_callbackdata = "inst3_dep14_spec2",
        department_id = 14,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "6В07305 - Транспортное строительство",
        speciality_callbackdata = "inst3_dep14_spec3",
        department_id = 14,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "6В07118- Транспортное сооружения",
        speciality_callbackdata = "inst3_dep14_spec4",
        department_id = 14,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "7М07303 Строительство и производство строительных материалов, изделий и конструкций",
        speciality_callbackdata = "inst3_dep14_spec5",
        department_id = 14,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "7М07308 Строительство и производство строительных материалов, изделий и конструкций",
        speciality_callbackdata = "inst3_dep14_spec6",
        department_id = 14,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = " 7М07320, 7М07321, 7М07322- Транспортное строительство",
        speciality_callbackdata = "inst3_dep14_spec7",
        department_id = 14,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "8D07303 - Строительство и производство строительных материалов и конструкции",
        speciality_callbackdata = "inst3_dep14_spec8",
        department_id = 14,
        degree_id = 3
    )

    await add_specialities(
        speciality_name = "8В07305 - Строительство и производство строительных материалов и конструкции",
        speciality_callbackdata = "inst3_dep14_spec9",
        department_id = 14,
        degree_id = 3
    )

    #intitute 4 department 15
    await add_specialities(
        speciality_name = "6В11301- Транспортные услуги",
        speciality_callbackdata = "inst4_dep15_spec1",
        department_id = 15,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "7М11302- Логистика",
        speciality_callbackdata = "inst4_dep15_spec2",
        department_id = 15,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "8D11301 - Транспортные услуги",
        speciality_callbackdata = "inst4_dep15_spec3",
        department_id = 15,
        degree_id = 3
    )

    #intitute 4 department 16
    await add_specialities(
        speciality_name = "6B06101 - Математическая экономика и анализ данных",
        speciality_callbackdata = "inst4_dep16_spec1",
        department_id = 16,
        degree_id = 1
    )

    await add_specialities(
        speciality_name = "7М04101 – «Проектный менеджмент» (2 года)",
        speciality_callbackdata = "inst4_dep16_spec2",
        department_id = 16,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "7М04102 – «Проектный менеджмент» (1,5 года)",
        speciality_callbackdata = "inst4_dep16_spec3",
        department_id = 16,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "7М04103 – «Проектный менеджмент» (1 год)",
        speciality_callbackdata = "inst4_dep16_spec4",
        department_id = 16,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "7M04104  - Executive MBA",
        speciality_callbackdata = "inst4_dep16_spec5",
        department_id = 16,
        degree_id = 2
    )

    await add_specialities(
        speciality_name = "8D04101 - Управление проектами",
        speciality_callbackdata = "inst4_dep16_spec6",
        department_id = 16,
        degree_id = 3
    )

    await add_specialities(
        speciality_name = "8D04102 - Менеджмент",
        speciality_callbackdata = "inst4_dep16_spec7",
        department_id = 16,
        degree_id = 3
    )

    # await add_specialities(
    #     speciality_name = "",
    #     speciality_callbackdata = "",
    #     department_id = ,
    #     degree_id = 
    # )


    #-----------------------------------

    #questions #menu level 1
    await add_question(
        question_name = "Где находиться моя кафедра",
        question_callbackdata = "qn_1",
        question_result = "",
        menu_level = 1
    )

    await add_question(
        question_name = "Где находится мой институт",
        question_callbackdata = "qn_2",
        question_result = "",
        menu_level = 1
    )

    await add_question(
        question_name = "У меня вопрос по учебе",
        question_callbackdata = "qn_3",
        question_result = "",
        menu_level = 1,
        have_child = True
    )

    await add_question(
        question_name = "У меня финансовый вопрос",
        question_callbackdata = "qn_4",
        question_result = "",
        menu_level = 1,
        have_child = True
    )

    await add_question(
        question_name = "Где получить ID карту",
        question_callbackdata = "qn_5",
        question_result = "",
        menu_level = 1,
        have_child = True
    )

    await add_question(
        question_name = "Вопрос по военкомату/военная кафедра",
        question_callbackdata = "qn_6",
        question_result = "",
        menu_level = 1,
        have_child = True
    )

    await add_question(
        question_name = "Онай/Медстраховка",
        question_callbackdata = "qn_7",
        question_result = "",
        menu_level = 1,
        have_child = True
    )

    await add_question(
        question_name = "Справка с места учебы",
        question_callbackdata = "qn_8",
        question_result = "<b>СПРАВКИ С МЕСТО УЧЕБЫ</b> \n\n Университет выдает справки с места учебы, которые подтверждают их академическую занятость в ВУЗе. Справки с места учебы выдаются только после издания Приказа о зачислении.\n\n Cправка с места учебы можно получить оставив заявку в личном кабинете (раздел <b>справка</b>)",
        menu_level = 1
    )

    await add_question(
        question_name = "Активист(хочу участвовать в социальной жизни)",
        question_callbackdata = "qn_9",
        question_result = "<b>Я АКТИВИСТ (ХОЧУ УЧАСТВОВАТЬ В СОЦИАЛЬНОЙ ЖИЗНИ)</b> \n\n Если у вас есть таланты и желаете стать активистом нашего университета, то вы можете связаться с заместителем директора по воспитательной части \n",
        menu_level = 1
    )

    await add_question(
        question_name = "Вопрос по общежитию",
        question_callbackdata = "qn_10",
        question_result = "<b>ВОПРОС ПО ОБЩЕЖИТИЮ</b> \n\n 1) Напишите заявление на имя проректора \n 2) Предоставьте заявление в общежитие №1 \n Тел: +7(727)320-41-43 ",
        menu_level = 1
    )

    await add_question(
        question_name = "Обходной лист",
        question_callbackdata = "qn_11",
        question_result = "<b>ОБХОДНОЙ ЛИСТ</b> \n\n После приказа об отчислении вы запускаете обходной лист (онлайн) на портале sso.satbayev.university . Отследить процесс подписание обходного листа можно увидеть нажав на номер <b>обходного листа.</b>",
        menu_level = 1,
        have_file = True,
        file_name = "['Заявление на место в общежитии.pdf']"
    )

    #menu level 2 question 3
    await add_question(
        question_name = "Я хочу подать на аппеляцию",
        question_callbackdata = "qn_12",
        question_result = "<b>Я ХОЧУ ПОДАТЬ НА АППЕЛЯЦИЮ</b> \n\n Заявление на апелляцию подается в течение 24 часов после объявлений результатов на имя заведующей кафедры дисциплины (на имя председателя апелляционной комиссии). Например: если у вас вопрос по Математики, то вы подаете заявление на имя зав. кафедры <b>Высшей математики</b> \n 1) Кафедра <b>Высшей математики</b> находится в ГУК 801 каб. \n Заведующий кафедры Уалиев Жомарт Разханович \n Email: zh.ualiyev@satbayev.university \n\n 2) Кафедра <b>Общая физика</b> находится в ГУК 917 каб. \n Заведующий кафедры Лесбаев Айдос Бакытжанович \n Email: a.lesbayev@satbayev.university \n\n 3) Кафедра <b>Казахский и русский языки</b> находится в ГУК 512 каб. \n Заведующий кафедры Удербаев Алмас Жауынбаевич \n Email: a.uderbayev@satbayev.university \n Тел: +7 (727) 320-40-9721:45 \n\n 4) Кафедра <b>Английский язык</b> находится в ГУК 823 каб. \n Заведующая кафедры Турлыбекова Анар Орымбаевна \n Email: a.o.turlybekova@satbayev.university \n\n 5) Кафедра <b>Физическая культура</b> находится в ГМК 101 каб. \n Заведующий кафедры Иматалиев Талап Сайпуллаевич \n Email: t.imataliyev@satbayev.university \n Тел: +7 (727) 320-40-85 \n\n 6)	Кафедра <b>Общественные дисциплины</b> находится в ГУК 814 каб. \n Заведующая кафедры Анасова Каламкас Темиркуловна \n Email: k.anasova@satbayev.university \n Тел: +7 (727) 320-40-95",
        menu_level = 2,
        parent_callbackdata = "qn_3"
    )

    await add_question(
        question_name = "ИУП, Расписание",
        question_callbackdata = "qn_13",
        question_result = "<b>ИУП, РАСПИСАНИЕ</b> \n\n ИУП (индивидуальный учебный план) и расписание составляется до начала учебного семестра. \n ИУП составляется совместно с эдвайзером (Положение об эдвайзера) и нужно сдать в Офис регистратор. ОР Находится на 1 этаже ГУК. \n Email: or-help@satbayev.university \n Тел: +7 (727) 320-41-16 \n\n Период перерегистрации (Add/Drop неделя), корректировка ИУПов проходит в первые недели учебного семестра. В этот период можно корректировать расписание, ИУПы и отложить предмет на поздний срок (W- withdrawal).\n Withdrawal предметов после завершении периода бесплатного снятия будет на платной основе.",
        menu_level = 2,
        parent_callbackdata = "qn_3"
    )

    await add_question(
        question_name = "Поменять преподователя",
        question_callbackdata = "qn_14",
        question_result = "<b>ПОМЕНЯТЬ ПРЕПОДОВАТЕЛЯ</b> \n\n Поменять преподавателя можно только в период перерегистрации (Add/Drop неделя) в начале семестра",
        menu_level = 2,
        parent_callbackdata = "qn_3"
    )

    await add_question(
        question_name = "Хочу подать на вакантный грант",
        question_callbackdata = "qn_15",
        question_result = "<b>ХОЧУ ПОДАТЬ НА ВАКАНТНЫЙ ГРАНТ</b> \n\n Подать на вакантный государственный образовательный грант можно в каникулярный период после окончательных оценок. На вакантный грант можно подать с GPA 2.5 и выше. \n Заявление на вакантный грант подается в Офис регистратор. ОР Находится на 1 этаже ГУК.  \n Email: or-help@satbayev.university \n Тел: +7 (727) 320-41-16",
        menu_level = 2,
        parent_callbackdata = "qn_3"
    )

    await add_question(
        question_name = "Академический отпуск",
        question_callbackdata = "qn_16",
        question_result = "<b>АКАДЕМИЧЕСКИЙ ОТПУСК</b> \n\n Академический отпуск могут получить студенты, которые: \n 1) Призываются в армию \n 2) По беременностью (от 24 неделя, Железодефицитная анемия (ЖДА), угроза прерывания беременности (УПБ), ВКК от гинеколога Форма 037/у) \n 3) По уходу за маленьким ребёнком \n 4) По состоянию здоровья (при наличии справки ВКК из мед. учреждения) \n Заявление подается с копией удостоверения личности и справками \n Нельзя получить академический отпуск по семейным обстоятельствам и финансовому положению. \n Заявление пишется на имя Проректора по академическим вопросам с подписью студента и визами эдвайзера, зав. кафедры, директора института (27 МСК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)). \n К заявлению прилагаете Представление от Дирекции института и сдаете документы в канцелярию 201 НК (Нефтяной корпус)",
        menu_level = 2,
        parent_callbackdata = "qn_3",
        have_file = True,
        file_name = "['Пример заполнения каз.pdf', 'Пример заполнения русс.pdf', 'Форма заявления Жаутиков Б.A. рус.pdf', 'Форма заявления Жаутиков Б.A.каз.pdf']"
    )

    await add_question(
        question_name = "Перевод между вузами",
        question_callbackdata = "qn_17",
        question_result = "",
        menu_level = 2,
        parent_callbackdata = "qn_3",
        have_child = True
    )

    await add_question(
        question_name = "Я хочу восстановиться/отчислиться",
        question_callbackdata = "qn_18",
        question_result = "",
        menu_level = 2,
        parent_callbackdata = "qn_3",
        have_child = True
    )

    #menu level 2 question 4
    await add_question(
        question_name = "Я хочу получить скидку",
        question_callbackdata = "qn_19",
        question_result = "<b>Я ХОЧУ ПОЛУЧИТЬ СКИДКУ</b> \n\n Satbayev University предоставляет скидки студентам на обучение по определённым категориям студентов: социально-уязвимым студентам, отличникам, мастерам спорта. А также материально поощряет победителей международных олимпиад и конкурсов. Предоставление скидок осуществляется согласно Положению на образовательные услуги и материальному стимулированию (поощрению) обучающихся по социальным и другим категориям:\n 1) Сироты; \n 2) Студенты-инвалиды (или оба родители инвалиды);\n 3) Многодетная семья (дети в возрасте до 18 лет); \n 4) Дети из неполной семьи и других социально-уязвимых слоев населения (GPA не менее 2.67). \n 5) Отличники учебы (GPA не менее 3.67) (2-4 курс); \n 6) Спортсмены имеющий спортивный разряд мастера спорта РК; \n 7) Мастер спорта международного класса РК.22:12 \n\n Курирует данный вопрос Отдел по социальной работе 408 НК (Нефтяной корпус) \n Тел: +7(727)320-40-75. \n E-mail: zh.ibragimova@satbayev.university \n\n Заявку на скидку вы можете подать онлайн \n https://official.satbayev.university/ru/department-for-student-affairs/skidki-na-obuchenie",
        menu_level = 2,
        parent_callbackdata = "qn_4"
    )

    await add_question(
        question_name = "Оплата по частям",
        question_callbackdata = "qn_20",
        question_result = "<b>ОПЛАТА ПО ЧАСТЯМ</b> \n\n Если у вас сложилась трудность с оплатой за обучение или задолженности, то вы можете заполнить заявление на оплату по частям или равными долями. Заявление рассматривается руководством университета. \n 1) Пишете заявление на имя Проректора с подписью студента и визами эдвайзера, зав. кафедры и директора института (27 МСК). В заявлений указываете четкий график оплаты с конкретными датами месяца. \n 2) Прилагаете необходимые подтверждающие документы (Например если у вас многодетная семья, вы прилагаете копии свидетельство о рождении детей, копию удостоверения личности мамы и справку о многодетной семьи с ЦОНа) \n 3) Прилагаете письмо в свободной форме от родителя о том, что они дают согласие на составленный вами график и копию удостоверение личности родителя \n 4) Составляете и подписываете Соглашение с графиком оплаты в дирекции Института 27 МСК \n 5) После необходимо сдать документы в канцелярию 201 НК (Нефтяной корпус)",
        menu_level = 2,
        parent_callbackdata = "qn_4",
        have_file = True,
        file_name = "['Форма заявления Кульдеев Е.И.каз.pdf', 'Формы заявлений Кульдеев Е.И. русc.pdf']"
    )

    await add_question(
        question_name = "Я получил грант, хочу вернуть деньги",
        question_callbackdata = "qn_21",
        question_result = "<b>Я ПОЛУЧИЛ ГРАНТ, ХОЧУ ВЕРНУТЬ ДЕНЬГИ</b> \n\n Если вы во время учебы на платиной основе получили грант и хотите вернуть оплаченные средства, то вы можете написать заявление на имя Проректора \n 1) Пишете заявление на имя Проректора с подписью студента и визами эдвайзера, зав. кафедры, директора института  (МСК 27) и бухгалтерией (203 НК (Нефтяной корпус)). В заявлений указываете IBAN карточного счета. \n 2) Прилагаете распечатанную версию реквизита карточного счета и копию удостоверение личности \n 3) После сдаете документы в канцелярию 201 НК (Нефтяной корпус)",
        menu_level = 2,
        parent_callbackdata = "qn_4"
    )

    await add_question(
        question_name = "Я вернул стипендию, когда поступят деньги",
        question_callbackdata = "qn_22",
        question_result = "<b>Я ВЕРНУЛ СТИПЕНДИЮ, КОГДА ПОСТУПЯТЬ ДЕНЬГИ</b> \n\n Если в конце учебного семестра вы набрали 70 и выше по всем предметам и вернули стипендию, то ваша стипендия вернется вам после приказа и на втором месяце следующего семестра.",
        menu_level = 2,
        parent_callbackdata = "qn_4"
    )

    #menu level 2 question 5
    await add_question(
        question_name = "Я потерял карту",
        question_callbackdata = "qn_24",
        question_result = "<b>Я ПОТЕРЯЛ ID-КАРТУ</b> \n\n Если вы потеряли ID-карту, то перевыпуск ID-карты будет стоить 1000 тг. \n 1) Для перевыпуска ID-карты вам необходимо запросить служебную записку в дирекции Института 27 МСК \n 2) Служебную записку необходимо сдать в ЦОД 342, 344 ГМК и приложить чек оплаты за перевыпуск",
        menu_level = 2,
        parent_callbackdata = "qn_5"
    )

    await add_question(
        question_name = "Я не получил карту",
        question_callbackdata = "qn_25",
        question_result = "<b>Я НЕ ПОЛУЧИЛ ID-КАРТУ</b> \n\n 1)Для выпуска ID-карты вам необходимо запросить служебную записку в дирекции Института 27 МСК. \n 2) Служебную записку необходимо сдать в ЦОД 342, 344 ГМК",
        menu_level = 2,
        parent_callbackdata = "qn_5"
    )

    #menu level 2 question 6
    await add_question(
            question_name = "Вопрос по военкомату",
            question_callbackdata = "qn_26",
            question_result = "<b>ВОПРОС ПО ВОЕНКОМАТУ</b> \n\n Университет выдает справки с места учебы, которые подтверждают их академическую занятость в ВУЗе. Справки с места учебы выдаются только после издания Приказа о зачислении. \n Cправка по воинскому учету (для отсрочки от армии) занимается Сектор воинского учета 341 каб. ГУК Тел: +7 (727)292-77-97",
            menu_level = 2,
            parent_callbackdata = "qn_6",
    )

    await add_question(
            question_name = "Справка для военной кафедры",
            question_callbackdata = "qn_27",
            question_result = "<b>СПРАВКА ДЛЯ ВОЕННОЙ КАФЕДРЫ</b> \n\n При Satbayev University есть Институт военного дела (ИВД). Всю необходимую информацию ИВД публикуют на официальном сайте университета https://official.satbayev.university/, https://satbayev.university/ \n Ответы на все вопросы по военной кафедре можете найти в отдельном телеграм боте: \n @Idet_military_department_bot \n Институт военного дела находится ул. Байтурсынова 140 \n Тел: +7(727)292-04-82, 292-08-45 \n Cправка для ИВД можно получить на портале https://sso.satbayev.university/",
            menu_level = 2,
            parent_callbackdata = "qn_6",
    )

    #menu level 2 question 7
    await add_question(
        question_name = "Мне нужен Онай",
        question_callbackdata = "qn_28",
        question_result = "<b>МНЕ НУЖЕН ОНАЙ</b> \n\n По вопросам Оңай вы можете обратиться в Отдел по социальной работе 408 НК \n Тел: +7(727)320-40-75 \n https://instagram.com/onay.satbayev?utm_medium=copy_link ",
        menu_level = 2,
        parent_callbackdata = "qn_7",
    )

    await add_question(
            question_name = "Вопрос по мед. страховке",
            question_callbackdata = "qn_29",
            question_result = "<b>ВОПРОС ПО МЕД.СТРАХОВКИ</b> \n\n По вопросам мед. страховки вы можете обратиться в Офис регистратор 1 этаж ГУК \n Тел: +7 (727) 320-41-16 \n Email: or-help@satbayev.university",

            menu_level = 2,
            parent_callbackdata = "qn_7",
    )
    #menu level 3 question 17
    await add_question(
            question_name = "Перевод в Satbayev University",
            question_callbackdata = "qn_30",
            question_result = "<b>ПЕРЕВОД В SATBAYEV UNIVERSITY</b> \n\n Если вы обучаетесь на гранте и переводитесь на схожую специальность, то ваш грант сохраняется, в противном случае вы будете обучаться на платной основе. \n В первую очередь вам необходимо получить разрешение из вашего университета написав заявление на перевод. После вы пишете заявление в наш университет предоставив разрешительные документы, копию удостоверения личности и официальный транскрипт. \n Все документы нужно предоставить в дирекцию института по адресу Сатпаева 22В Этаж 2. Кабинет 27. (Здание МСК) или направить на Email: e.nugman@satbayev.university \n Мы принимаем ваши документы и издаём приказ о переводе. А вы в это время заполняете анкету студента на kb.satbayev.university",
            menu_level = 3,
            parent_callbackdata = "qn_17",
            have_file = True,
            file_name = "['Форма заявления Жаутиков Б.A русс.pdf', 'Форма Заявления Жаутиков Б.A.pdf']"
    )

    await add_question(
            question_name = "Перевод из Satbayev University в другой ВУЗ",
            question_callbackdata = "qn_31",
            question_result = "<b>ПЕРЕВОД С SU В ДРУГОЙ ВУЗ</b> \n\n Подумайте, нужно ли вам переводится с Национального технического ВУЗа в другие университеты. \n Если вы обучаетесь на гранте и переводитесь на схожую специальность, то ваш грант сохраняется, в противном случае вы будете обучаться на платной основе. \n Если у вас есть весомые причины для перевода в другой ВУЗ, то алгоритм такой:\n 1) Вы пишете заявление на имя Проректора по академическим вопросам с подписью студента и визами эдвайзера, зав. кафедры, директора института (27 МСК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)) (*если у вас имеется финансовая задолженность, то необходимо оплатить задолженность и приложить чек оплаты). \n 2) После того как вы собрали все необходимые подписи сдаете в приемную 302 НК (Нефтяной корпус) \n 3) Вы получаете университетский печать на ваше заявление с разрешением в бухгалтерии 217 НК (Нефтяной корпус) \n 4) В офис регистраторе запрашиваете официальный транскрипт \n 5) После зачисления в другой ВУЗ не забудьте заполнить обходной лист в Satbayev University на портале (SSO)",
            menu_level = 3,
            parent_callbackdata = "qn_17",
            have_file = True,
            file_name = "['Форма заявления Жаутиков Б.A русс.pdf', 'Форма Заявления Жаутиков Б.A.pdf']",
    )

    await add_question(
            question_name = "Я хочу восстановиться",
            question_callbackdata = "qn_32",
            question_result = "<b>Я ХОЧУ ВОССТАНОВИТЬСЯ</b> \n\n Для восстановления на учебу в университет у студента должны отсутствовать не закрытые дисциплины в 1-м семестре (F) и иметь общий бал ЕНТ 65 с предметами физика и математика. \n 1) Вы пишете заявление на имя Проректора по академическим вопросам с подписью студента и визами зав. кафедры, директора института (27 МСК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)) (*если у вас имеется финансовая задолженность, то необходимо оплатить задолженность и приложить чек оплаты). \n 2) К заявлению прилагаете Представление от Дирекции института 27 (МСК) и сдаете документы в канцелярию 201 НК (Нефтяной корпус)",
            menu_level = 3,
            parent_callbackdata = "qn_18",
            have_file = True,
            file_name = "['Форма заявления Жаутиков Б.A. рус.pdf','Форма заявления Жаутиков Б.A.каз.pdf']"
    )

    await add_question(
            question_name = "Я хочу отчислиться",
            question_callbackdata = "qn_33",
            question_result = "<b>Я ХОЧУ ОТЧИСЛИТЬСЯ</b> \n\n Для отчисления с университета по собственному желанию вы пишите заявление на имя Проректора по академическим вопросам. После приказа об отчислении вы запускаете обходной лист (онлайн) на портале sso.satbayev.university . Отследить процесс подписание обходного листа можно увидеть нажав на номер обходного листа. \n 1) Вы пишете заявление на имя Проректора по академическим вопросам с подписью студента и визами эдвайзера, зав. кафедры, директора института (27 МСК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)) (*если у вас имеется финансовая задолженность, то необходимо оплатить задолженность и приложить чек оплаты). \n 2) К заявлению прилагаете Представление от Дирекции института 27 (МСК) и сдаете документы в канцелярию 201 НК (Нефтяной корпус)",
            menu_level = 3,
            parent_callbackdata = "qn_18",
            have_file = True,
            file_name = "['Форма заявления Жаутиков Б.A. рус.pdf','Форма заявления Жаутиков Б.A.каз.pdf']"
    )

    #menu level 3 differentquestion results for institute 1 oilgas
    await add_different_question(
        institute_id = 1,
        question_callbackdata = "qn_24",
        question_result = "<b>Я ПОТЕРЯЛ ID-КАРТУ</b> \n\n Если вы потеряли ID-карту, то перевыпуск ID-карты будет стоить 1000 тг. \n 1) Для перевыпуска ID-карты вам необходимо запросить служебную записку в дирекции Института 325 ГУК \n 2) Служебную записку необходимо сдать в ЦОД 342, 344 ГМК и приложить чек оплаты за перевыпуск",
    )

    await add_different_question(
        institute_id = 1,
        question_callbackdata = "qn_25",
        question_result = "<b>Я НЕ ПОЛУЧИЛ ID-КАРТУ</b> \n\n 1)Для выпуска ID-карты вам необходимо запросить служебную записку в дирекции Института 325 ГУК. \n 2) Служебную записку необходимо сдать в ЦОД 342, 344 ГМК",
    )

    await add_different_question(
        institute_id = 1,
        question_callbackdata = "qn_30",
        question_result = "<b>ПЕРЕВОД В SATBAYEV UNIVERSITY</b> \n\n Если вы обучаетесь на гранте и переводитесь на схожую специальность, то ваш грант сохраняется, в противном случае вы будете обучаться на платной основе. \n В первую очередь вам необходимо получить разрешение из вашего университета написав заявление на перевод. После вы пишете заявление в наш университет предоставив разрешительные документы, копию удостоверения личности и официальный транскрипт. \n Все документы нужно предоставить в дирекцию института по адресу Сатпаева 22,  3 этаж. Кабинет 325 (здание ГУК) или направить на Emails: a.makyzhanova@satbayev.university, igngd@satbayev.university \n Мы принимаем ваши документы и издаём приказ о переводе. А вы в это время заполняете анкету студента на kb.satbayev.university",
            
    )

    await add_different_question(
        institute_id = 1,
        question_callbackdata = "qn_31",
        question_result = "<b>ПЕРЕВОД С SU В ДРУГОЙ ВУЗ</b> \n\n Подумайте, нужно ли вам переводится с Национального технического ВУЗа в другие университеты. \n Если вы обучаетесь на гранте и переводитесь на схожую специальность, то ваш грант сохраняется, в противном случае вы будете обучаться на платной основе. \n Если у вас есть весомые причины для перевода в другой ВУЗ, то алгоритм такой:\n 1) Вы пишете заявление на имя Проректора по академическим вопросам с подписью студента и визами эдвайзера, зав. кафедры, директора института (325 ГУК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)) (*если у вас имеется финансовая задолженность, то необходимо оплатить задолженность и приложить чек оплаты). \n 2) После того как вы собрали все необходимые подписи сдаете в приемную 302 НК (Нефтяной корпус) \n 3) Вы получаете университетский печать на ваше заявление с разрешением в бухгалтерии 217 НК (Нефтяной корпус) \n 4) В офис регистраторе запрашиваете официальный транскрипт \n 5) После зачисления в другой ВУЗ не забудьте заполнить обходной лист в Satbayev University на портале (SSO)",
    )

    await add_different_question(
        institute_id = 1,
        question_callbackdata = "qn_32",
        question_result = "<b>Я ХОЧУ ВОССТАНОВИТЬСЯ</b> \n\n Для восстановления на учебу в университет у студента должны отсутствовать не закрытые дисциплины в 1-м семестре (F) и иметь общий бал ЕНТ 65 с предметами физика и математика. \n 1) Вы пишете заявление на имя Проректора по академическим вопросам с подписью студента и визами зав. кафедры, директора института (325 ГУК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)) (*если у вас имеется финансовая задолженность, то необходимо оплатить задолженность и приложить чек оплаты). \n 2) К заявлению прилагаете Представление от Дирекции института (325 ГУК)) и сдаете документы в канцелярию 201 НК (Нефтяной корпус)",
    )

    await add_different_question(
        institute_id = 1,
        question_callbackdata = "qn_33",
        question_result = "<b>Я ХОЧУ ОТЧИСЛИТЬСЯ</b> \n\n Для отчисления с университета по собственному желанию вы пишите заявление на имя Проректора по академическим вопросам. После приказа об отчислении вы запускаете обходной лист (онлайн) на портале sso.satbayev.university . Отследить процесс подписание обходного листа можно увидеть нажав на номер обходного листа. \n 1) Вы пишете заявление на имя Проректора по академическим вопросам с подписью студента и визами эдвайзера, зав. кафедры, директора института (325 ГУК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)) (*если у вас имеется финансовая задолженность, то необходимо оплатить задолженность и приложить чек оплаты). \n 2) К заявлению прилагаете Представление от Дирекции института (325 ГУК) и сдаете документы в канцелярию 201 НК (Нефтяной корпус)",
    )

    await add_different_question(
        institute_id = 1,
        question_callbackdata = "qn_16",
        question_result = "<b>АКАДЕМИЧЕСКИЙ ОТПУСК</b> \n\n Академический отпуск могут получить студенты, которые: \n 1) Призываются в армию \n 2) По беременностью (от 24 неделя, Железодефицитная анемия (ЖДА), угроза прерывания беременности (УПБ), ВКК от гинеколога Форма 037/у) \n 3) По уходу за маленьким ребёнком \n 4) По состоянию здоровья (при наличии справки ВКК из мед. учреждения) \n Заявление подается с копией удостоверения личности и справками \n Нельзя получить академический отпуск по семейным обстоятельствам и финансовому положению. \n Заявление пишется на имя Проректора по академическим вопросам с подписью студента и визами эдвайзера, зав. кафедры, директора института (325 ГУК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)). \n К заявлению прилагаете Представление от Дирекции института и сдаете документы в канцелярию 201 НК (Нефтяной корпус)",
    )

    #menu level 3 differentquestion results for institute 2 metallurgy
    await add_different_question(
        institute_id = 2,
        question_callbackdata = "qn_24",
        question_result = "<b>Я ПОТЕРЯЛ ID-КАРТУ</b> \n\n Если вы потеряли ID-карту, то перевыпуск ID-карты будет стоить 1000 тг. \n 1) Для перевыпуска ID-карты вам необходимо запросить служебную записку в дирекции Института 232 ГМК \n 2) Служебную записку необходимо сдать в ЦОД 342, 344 ГМК и приложить чек оплаты за перевыпуск",
    )

    await add_different_question(
        institute_id = 2,
        question_callbackdata = "qn_25",
        question_result = "<b>Я НЕ ПОЛУЧИЛ ID-КАРТУ</b> \n\n 1)Для выпуска ID-карты вам необходимо запросить служебную записку в дирекции Института 232 ГМК. \n 2) Служебную записку необходимо сдать в ЦОД 342, 344 ГМК",
    )

    await add_different_question(
        institute_id = 2,
        question_callbackdata = "qn_30",
        question_result = "<b>ПЕРЕВОД В SATBAYEV UNIVERSITY</b> \n\n Если вы обучаетесь на гранте и переводитесь на схожую специальность, то ваш грант сохраняется, в противном случае вы будете обучаться на платной основе. \n В первую очередь вам необходимо получить разрешение из вашего университета написав заявление на перевод. После вы пишете заявление в наш университет предоставив разрешительные документы, копию удостоверения личности и официальный транскрипт. \n Все документы нужно предоставить в дирекцию института по адресу Сатпаева 22В Этаж 2. Кабинет 232. (Здание ГМК) \n Мы принимаем ваши документы и издаём приказ о переводе. А вы в это время заполняете анкету студента на kb.satbayev.university",
            
    )

    await add_different_question(
        institute_id = 2,
        question_callbackdata = "qn_31",
        question_result = "<b>ПЕРЕВОД С SU В ДРУГОЙ ВУЗ</b> \n\n Подумайте, нужно ли вам переводится с Национального технического ВУЗа в другие университеты. \n Если вы обучаетесь на гранте и переводитесь на схожую специальность, то ваш грант сохраняется, в противном случае вы будете обучаться на платной основе. \n Если у вас есть весомые причины для перевода в другой ВУЗ, то алгоритм такой:\n 1) Вы пишете заявление на имя Проректора по академическим вопросам с подписью студента и визами эдвайзера, зав. кафедры, директора института (232 ГМК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)) (*если у вас имеется финансовая задолженность, то необходимо оплатить задолженность и приложить чек оплаты). \n 2) После того как вы собрали все необходимые подписи сдаете в приемную 302 НК (Нефтяной корпус) \n 3) Вы получаете университетский печать на ваше заявление с разрешением в бухгалтерии 217 НК (Нефтяной корпус) \n 4) В офис регистраторе запрашиваете официальный транскрипт \n 5) После зачисления в другой ВУЗ не забудьте заполнить обходной лист в Satbayev University на портале (SSO)",
    )

    await add_different_question(
        institute_id = 2,
        question_callbackdata = "qn_32",
        question_result = "<b>Я ХОЧУ ВОССТАНОВИТЬСЯ</b> \n\n Для восстановления на учебу в университет у студента должны отсутствовать не закрытые дисциплины в 1-м семестре (F) и иметь общий бал ЕНТ 65 с предметами физика и математика. \n 1) Вы пишете заявление на имя Проректора по академическим вопросам с подписью студента и визами зав. кафедры, директора института (232 ГМК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)) (*если у вас имеется финансовая задолженность, то необходимо оплатить задолженность и приложить чек оплаты). \n 2) К заявлению прилагаете Представление от Дирекции института (232 ГМК) и сдаете документы в канцелярию 201 НК (Нефтяной корпус)",
    )

    await add_different_question(
        institute_id = 2,
        question_callbackdata = "qn_33",
        question_result = "<b>Я ХОЧУ ОТЧИСЛИТЬСЯ</b> \n\n Для отчисления с университета по собственному желанию вы пишите заявление на имя Проректора по академическим вопросам. После приказа об отчислении вы запускаете обходной лист (онлайн) на портале sso.satbayev.university . Отследить процесс подписание обходного листа можно увидеть нажав на номер обходного листа. \n 1) Вы пишете заявление на имя Проректора по академическим вопросам с подписью студента и визами эдвайзера, зав. кафедры, директора института (232 ГМК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)) (*если у вас имеется финансовая задолженность, то необходимо оплатить задолженность и приложить чек оплаты). \n 2) К заявлению прилагаете Представление от Дирекции института (232 ГМК) и сдаете документы в канцелярию 201 НК (Нефтяной корпус)",
    )

    await add_different_question(
        institute_id = 2,
        question_callbackdata = "qn_16",
        question_result = "<b>АКАДЕМИЧЕСКИЙ ОТПУСК</b> \n\n Академический отпуск могут получить студенты, которые: \n 1) Призываются в армию \n 2) По беременностью (от 24 неделя, Железодефицитная анемия (ЖДА), угроза прерывания беременности (УПБ), ВКК от гинеколога Форма 037/у) \n 3) По уходу за маленьким ребёнком \n 4) По состоянию здоровья (при наличии справки ВКК из мед. учреждения) \n Заявление подается с копией удостоверения личности и справками \n Нельзя получить академический отпуск по семейным обстоятельствам и финансовому положению. \n Заявление пишется на имя Проректора по академическим вопросам с подписью студента и визами эдвайзера, зав. кафедры, директора института (232 ГМК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)). \n К заявлению прилагаете Представление от Дирекции института и сдаете документы в канцелярию 201 НК (Нефтяной корпус)",
    )

    #menu level 3 differentquestion results for institute 3 architecture
    await add_different_question(
        institute_id = 3,
        question_callbackdata = "qn_24",
        question_result = "<b>Я ПОТЕРЯЛ ID-КАРТУ</b> \n\n Если вы потеряли ID-карту, то перевыпуск ID-карты будет стоить 1000 тг. \n 1) Для перевыпуска ID-карты вам необходимо запросить служебную записку в дирекции Института 201 МУК \n 2) Служебную записку необходимо сдать в ЦОД 342, 344 ГМК и приложить чек оплаты за перевыпуск",
    )

    await add_different_question(
        institute_id = 3,
        question_callbackdata = "qn_25",
        question_result = "<b>Я НЕ ПОЛУЧИЛ ID-КАРТУ</b> \n\n 1)Для выпуска ID-карты вам необходимо запросить служебную записку в дирекции Института 201 МУК. \n 2) Служебную записку необходимо сдать в ЦОД 342, 344 ГМК",
    )

    await add_different_question(
        institute_id = 3,
        question_callbackdata = "qn_30",
        question_result = "<b>ПЕРЕВОД В SATBAYEV UNIVERSITY</b> \n\n Если вы обучаетесь на гранте и переводитесь на схожую специальность, то ваш грант сохраняется, в противном случае вы будете обучаться на платной основе. \n В первую очередь вам необходимо получить разрешение из вашего университета написав заявление на перевод. После вы пишете заявление в наш университет предоставив разрешительные документы, копию удостоверения личности и официальный транскрипт. \n Все документы нужно предоставить в дирекцию института по адресу Сатпаева 22а Этаж 2. Кабинет 201. (Здание МУК) или направить на Email: e.nugman@satbayev.university \n Мы принимаем ваши документы и издаём приказ о переводе. А вы в это время заполняете анкету студента на kb.satbayev.university",
            
    )

    await add_different_question(
        institute_id = 3,
        question_callbackdata = "qn_31",
        question_result = "<b>ПЕРЕВОД С SU В ДРУГОЙ ВУЗ</b> \n\n Подумайте, нужно ли вам переводится с Национального технического ВУЗа в другие университеты. \n Если вы обучаетесь на гранте и переводитесь на схожую специальность, то ваш грант сохраняется, в противном случае вы будете обучаться на платной основе. \n Если у вас есть весомые причины для перевода в другой ВУЗ, то алгоритм такой:\n 1) Вы пишете заявление на имя Проректора по академическим вопросам с подписью студента и визами эдвайзера, зав. кафедры, директора института (201 МУК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)) (*если у вас имеется финансовая задолженность, то необходимо оплатить задолженность и приложить чек оплаты). \n 2) После того как вы собрали все необходимые подписи сдаете в приемную 302 НК (Нефтяной корпус) \n 3) Вы получаете университетский печать на ваше заявление с разрешением в бухгалтерии 217 НК (Нефтяной корпус) \n 4) В офис регистраторе запрашиваете официальный транскрипт \n 5) После зачисления в другой ВУЗ не забудьте заполнить обходной лист в Satbayev University на портале (SSO)",
    )

    await add_different_question(
        institute_id = 3,
        question_callbackdata = "qn_32",
        question_result = "<b>Я ХОЧУ ВОССТАНОВИТЬСЯ</b> \n\n Для восстановления на учебу в университет у студента должны отсутствовать не закрытые дисциплины в 1-м семестре (F) и иметь общий бал ЕНТ 65 с предметами физика и математика. \n 1) Вы пишете заявление на имя Проректора по академическим вопросам с подписью студента и визами зав. кафедры, директора института (201 МУК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)) (*если у вас имеется финансовая задолженность, то необходимо оплатить задолженность и приложить чек оплаты). \n 2) К заявлению прилагаете Представление от Дирекции ИАиС 201 (МУК) и сдаете документы в канцелярию 201 НК (Нефтяной корпус)",
    )

    await add_different_question(
        institute_id = 3,
        question_callbackdata = "qn_33",
        question_result = "<b>Я ХОЧУ ОТЧИСЛИТЬСЯ</b> \n\n Для отчисления с университета по собственному желанию вы пишите заявление на имя Проректора по академическим вопросам. После приказа об отчислении вы запускаете обходной лист (онлайн) на портале sso.satbayev.university . Отследить процесс подписание обходного листа можно увидеть нажав на номер обходного листа. \n 1) Вы пишете заявление на имя Проректора по академическим вопросам с подписью студента и визами эдвайзера, зав. кафедры, директора института (201 МУК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)) (*если у вас имеется финансовая задолженность, то необходимо оплатить задолженность и приложить чек оплаты). \n 2) К заявлению прилагаете Представление от Дирекции ИАиС 201 (МУК) и сдаете документы в канцелярию 201 НК (Нефтяной корпус)",
    )

    await add_different_question(
        institute_id = 3,
        question_callbackdata = "qn_16",
        question_result = "<b>АКАДЕМИЧЕСКИЙ ОТПУСК</b> \n\n Академический отпуск могут получить студенты, которые: \n 1) Призываются в армию \n 2) По беременностью (от 24 неделя, Железодефицитная анемия (ЖДА), угроза прерывания беременности (УПБ), ВКК от гинеколога Форма 037/у) \n 3) По уходу за маленьким ребёнком \n 4) По состоянию здоровья (при наличии справки ВКК из мед. учреждения) \n Заявление подается с копией удостоверения личности и справками \n Нельзя получить академический отпуск по семейным обстоятельствам и финансовому положению. \n Заявление пишется на имя Проректора по академическим вопросам с подписью студента и визами эдвайзера, зав. кафедры, директора института (201 МУК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)). \n К заявлению прилагаете Представление от Дирекции института и сдаете документы в канцелярию 201 НК (Нефтяной корпус)",
    )

    #menu level 3 differentquestion results for institute 4 project management
    await add_different_question(
        institute_id = 4,
        question_callbackdata = "qn_24",
        question_result = "<b>Я ПОТЕРЯЛ ID-КАРТУ</b> \n\n Если вы потеряли ID-карту, то перевыпуск ID-карты будет стоить 1000 тг. \n 1) Для перевыпуска ID-карты вам необходимо запросить служебную записку в дирекции Института 415,408,401 ГУК \n 2) Служебную записку необходимо сдать в ЦОД 342, 344 ГМК и приложить чек оплаты за перевыпуск",
    )

    await add_different_question(
        institute_id = 4,
        question_callbackdata = "qn_25",
        question_result = "<b>Я НЕ ПОЛУЧИЛ ID-КАРТУ</b> \n\n 1)Для выпуска ID-карты вам необходимо запросить служебную записку в дирекции Института 415,408,401 ГУК. \n 2) Служебную записку необходимо сдать в ЦОД 342, 344 ГМК",
    )

    await add_different_question(
        institute_id = 4,
        question_callbackdata = "qn_30",
        question_result = "<b>ПЕРЕВОД В SATBAYEV UNIVERSITY</b> \n\n Если вы обучаетесь на гранте и переводитесь на схожую специальность, то ваш грант сохраняется, в противном случае вы будете обучаться на платной основе. \n В первую очередь вам необходимо получить разрешение из вашего университета написав заявление на перевод. После вы пишете заявление в наш университет предоставив разрешительные документы, копию удостоверения личности и официальный транскрипт. \n Все документы нужно предоставить в дирекцию института по адресу Сатпаева 22В Этаж 4. Кабинет 415,408,401. (Здание ГУК) \n Мы принимаем ваши документы и издаём приказ о переводе. А вы в это время заполняете анкету студента на kb.satbayev.university",
            
    )

    await add_different_question(
        institute_id = 4,
        question_callbackdata = "qn_31",
        question_result = "<b>ПЕРЕВОД С SU В ДРУГОЙ ВУЗ</b> \n\n Подумайте, нужно ли вам переводится с Национального технического ВУЗа в другие университеты. \n Если вы обучаетесь на гранте и переводитесь на схожую специальность, то ваш грант сохраняется, в противном случае вы будете обучаться на платной основе. \n Если у вас есть весомые причины для перевода в другой ВУЗ, то алгоритм такой:\n 1) Вы пишете заявление на имя Проректора по академическим вопросам с подписью студента и визами эдвайзера, зав. кафедры, директора института (415,408,401 ГУК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)) (*если у вас имеется финансовая задолженность, то необходимо оплатить задолженность и приложить чек оплаты). \n 2) После того как вы собрали все необходимые подписи сдаете в приемную 302 НК (Нефтяной корпус) \n 3) Вы получаете университетский печать на ваше заявление с разрешением в бухгалтерии 217 НК (Нефтяной корпус) \n 4) В офис регистраторе запрашиваете официальный транскрипт \n 5) После зачисления в другой ВУЗ не забудьте заполнить обходной лист в Satbayev University на портале (SSO)",
    )

    await add_different_question(
        institute_id = 4,
        question_callbackdata = "qn_32",
        question_result = "<b>Я ХОЧУ ВОССТАНОВИТЬСЯ</b> \n\n Для восстановления на учебу в университет у студента должны отсутствовать не закрытые дисциплины в 1-м семестре (F) и иметь общий бал ЕНТ 65 с предметами физика и математика. \n 1) Вы пишете заявление на имя Проректора по академическим вопросам с подписью студента и визами зав. кафедры, директора института (415,408,401 ГУК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)) (*если у вас имеется финансовая задолженность, то необходимо оплатить задолженность и приложить чек оплаты). \n 2) К заявлению прилагаете Представление от Дирекции института (415,408,401 ГУК) и сдаете документы в канцелярию 201 НК (Нефтяной корпус)",
    )

    await add_different_question(
        institute_id = 4,
        question_callbackdata = "qn_33",
        question_result = "<b>Я ХОЧУ ОТЧИСЛИТЬСЯ</b> \n\n Для отчисления с университета по собственному желанию вы пишите заявление на имя Проректора по академическим вопросам. После приказа об отчислении вы запускаете обходной лист (онлайн) на портале sso.satbayev.university . Отследить процесс подписание обходного листа можно увидеть нажав на номер обходного листа. \n 1) Вы пишете заявление на имя Проректора по академическим вопросам с подписью студента и визами эдвайзера, зав. кафедры, директора института (415,408,401 ГУК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)) (*если у вас имеется финансовая задолженность, то необходимо оплатить задолженность и приложить чек оплаты). \n 2) К заявлению прилагаете Представление от Дирекции института (415,408,401 ГУК) и сдаете документы в канцелярию 201 НК (Нефтяной корпус)",
    )

    await add_different_question(
        institute_id = 4,
        question_callbackdata = "qn_16",
        question_result = "<b>АКАДЕМИЧЕСКИЙ ОТПУСК</b> \n\n Академический отпуск могут получить студенты, которые: \n 1) Призываются в армию \n 2) По беременностью (от 24 неделя, Железодефицитная анемия (ЖДА), угроза прерывания беременности (УПБ), ВКК от гинеколога Форма 037/у) \n 3) По уходу за маленьким ребёнком \n 4) По состоянию здоровья (при наличии справки ВКК из мед. учреждения) \n Заявление подается с копией удостоверения личности и справками \n Нельзя получить академический отпуск по семейным обстоятельствам и финансовому положению. \n Заявление пишется на имя Проректора по академическим вопросам с подписью студента и визами эдвайзера, зав. кафедры, директора института (415,408,401 ГУК), директора ОР (офис регистратор) и бухгалтерией (203 НК (Нефтяной корпус)). \n К заявлению прилагаете Представление от Дирекции института и сдаете документы в канцелярию 201 НК (Нефтяной корпус)",
    )

    
loop = asyncio.get_event_loop()
loop.run_until_complete(create_db())
loop.run_until_complete(add_data())