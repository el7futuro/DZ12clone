def picture_valid(picture):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    # Получаем имя файла у загруженного файла
    filename = picture.filename
    # Получаем расширение файла
    extension = filename.split(".")[-1]
    # Если расширение файла в белом списке
    if extension in ALLOWED_EXTENSIONS:
        return True
    else:
        return False