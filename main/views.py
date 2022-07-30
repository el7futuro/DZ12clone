import logging
from json import JSONDecodeError
from flask import render_template, Blueprint, request
from functions import load_posts, get_by_tag

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')



@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def page_tag():
 try:
    s = request.args.get('s')
    items = get_by_tag(s)
    logging.info("Произведен поиск")
    return render_template('post_list.html', s=s, items=items)

 except FileNotFoundError:
        logging.error("ошибка при загрузке файла")
        return f"Файл не найден"

 except JSONDecodeError:
        # Будет выполнено, если файл найден, но не превращается из JSON
        return f"Файл не удается преобразовать"
