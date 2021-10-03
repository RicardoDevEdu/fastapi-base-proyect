def remove_item_none_of_dict(data):
    for key, value in dict(data).items():
        if value is None:
            del data[key]
    return data
