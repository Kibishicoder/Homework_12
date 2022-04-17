from flask import Blueprint, request, render_template
from functions import load_posts
import logging

logging.basicConfig(encoding='utf8', level=logging.INFO)

main_blueprint = Blueprint('main', __name__, template_folder='templates')

@main_blueprint.route('/')
def main():
    return render_template('index.html')


@main_blueprint.route('/search')
def search():
    search_by_request = request.args['s']
    logging.info(f'Будем искать по {search_by_request}')
    posts = [x for x in load_posts() if search_by_request.lower() in x['content'].lower()]
    return render_template('post_list.html', search_by_request=search_by_request, posts=posts)