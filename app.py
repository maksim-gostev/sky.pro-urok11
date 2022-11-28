from flask import Flask, request, render_template

from config import FILE
import utils

app = Flask(__name__)



@app.route("/")
def get_all():
    """
    Выводит всех кандидатов
    :return: список кондидатов
    """
    list_of_candidates: object = utils.load_candidates(FILE)

    return render_template('list.html', list_of_candidates=list_of_candidates)


@app.route("/candidates/<int:pk>")
def get_by_pk(pk):
    """
    выводит кондидата по рк
    :param pk: int
    :return: данные кандидата
    """
    candidat = utils.get_candidate(pk)
    return render_template('single.html', candidat=candidat)


@app.route("/candidates/<candidate_name>")
def get_by_name(candidate_name):
    """
    возвращает кондидатов по имени
    :param candidate_name: имя
    :return: список кондидатов
    """
    lower_name = candidate_name.lower()
    list_candidate_name = utils.get_candidates_by_name(lower_name)

    number_of_candidates = len(list_candidate_name)
    return render_template('search.html', list_candidate_name=list_candidate_name,
                           number_of_candidates=number_of_candidates)


@app.route("/skill/<skill>")
def get_by_skills(skill):
    """
    возвращает кандидатов по навыку
    :param skill:навык
    :return:список кандидатов
    """
    skill_lower = skill.lower()
    candidates = utils.get_candidates_by_skill(skill_lower)
    len_candidates = len(candidates)
    return render_template('skill.html', candidates=candidates, len_candidates=len_candidates,
                           skill=skill.capitalize())


app.run()
