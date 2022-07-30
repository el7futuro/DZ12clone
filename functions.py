import json
from json import JSONDecodeError


def load_posts(): #которая загрузит данные из файла

        with open("posts.json", encoding='utf-8') as file:
            posts_list = json.load(file)

        return posts_list




def get_by_tag(tag): #которая вернет посты с тегом
    posts_by_tag = []
    for i in load_posts():
        if tag in i['content']:
            posts_by_tag.append(i)

    return posts_by_tag


def add_post(picture_path, content): #которая добавит картинку и текст в список постов
    posts_list = load_posts()
    new_post = dict({"pic": picture_path, "content": content})
    posts_list.append(new_post)
    upload_post(posts_list)
    return new_post


def upload_post(posts_list):
    with open("posts.json", 'w', encoding='utf-8') as file:
        json.dump(posts_list, file, ensure_ascii=False)
    return





