# Chapter 02-03 BluePrint Route Function Management
# https://wikidocs.net/81510

from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
#    return 'Pybo index from myproject/pybo/views/main_views.py'
    return redirect(url_for('question._list'))


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo! from myproject/pybo/views/main_views.py'

