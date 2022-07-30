import logging
from json import JSONDecodeError
from flask import render_template, Blueprint, request
from functions import add_post, upload_post
from loader.utils import picture_valid

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')



@loader_blueprint.route('/post')
def page_post_form():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=["POST"])
def page_post_upload():
    picture = request.files.get("picture")
    if picture:
        if picture_valid(picture):

            # Получаем имя файла у загруженного файла
            filename = picture.filename
            try:
                # Сохраняем картинку под родным именем в папку uploads
                picture_save = f"./uploads/images/{filename}"
                picture.save(picture_save)
                picture_path = '/' + picture_save
                content = request.form['content']
                new_post = add_post(picture_path, content)
            except FileNotFoundError:
                # Будет выполнено, если файл не найден
                logging.error("Файл не найден")
                return f"Файл не найден"
            except JSONDecodeError:
                # Будет выполнено, если файл найден, но не превращается из JSON
                return f"Файл не удается преобразовать"

            return render_template('post_uploaded.html', new_post=new_post)

        else:
            logging.info("файл не является картинкой")
            return f"файл не является картинкой"
    else:
        logging.error("ошибка загрузки")
        return f"ошибка загрузки"
