def uzer_info(name, sname, born, sity, email, tel):
    """
    Функция uzer_info принимает данные о пользователе и выводит их на экран одной строкой
    :param name: Имя
    :param sname: Фамилия
    :param born: год рождения
    :param sity: город
    :param email: электронная почта
    :param tel: телефон
    """
    print(f'{name} {sname}, родился в {born} году, проживает в городе {sity}. Контакты {email}, {tel}')
uzer_info(name="Фидель", born="1936", sname="Кастро", email="fidel@bk.ru", sity="Гаванна", tel=5555555)