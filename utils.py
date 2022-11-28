import json

from config import FILE


def load_candidates(filename):
    """
    Загружает данные из файла
    :param filename: путь к файлу
    :return:список кандидатов
    """
    with open(filename, 'r', encoding='utf-8') as file:
        json_file = json.load(file)
        return json_file


def get_candidate(pk):
    """
        поиск кандидата по рк
        :param pk:ноумен кандидата
        :return:данные кандидата
        """
    list_of_candidates = load_candidates(FILE)
    for candidat in list_of_candidates:
        if candidat['id'] == pk:
            return candidat
    return None



def get_candidates_by_name(candidate_name):
    list_of_candidates = load_candidates(FILE)
    result = []
    for candidat in list_of_candidates:
        if candidate_name in candidat.lower().split(' '):
            result.append(candidat)
    return result



def get_candidates_by_skill(skill_name):
    #– возвращает кандидатов по навыку
    pass

