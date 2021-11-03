from typing import List
from app.core.commons.customtype import ImagenData


def remove_item_none_of_dict(data):
    for key, value in dict(data).items():
        if value is None:
            del data[key]
    return data
    
def get_imagen_data(image: str):
    if image is None:
        return None
    image_type = image.split(':')[1].split(';')[0].split('/')[1]
    image_mimetype = image.split(':')[1].split(';')[0]
    encode = image.split(';')[1].split(',')[0]
    content = image.split(',')[1]
    return {
        "type": image_type,
        "mimetype": image_mimetype,
        "encode": encode,
        "content": content
    }

def get_tags(tags: str):
    return list(tags.split(','))