import json
import math

def round_well(num):
    return math.ceil(num)

def meta_paginate(data_filter ,params, query_set):
    item_per_page = int(params.get("item_per_page", 15))
    page = int(params.get("page", 1))
    order = params.get("order", "DESC")
    skip = (page-1) * item_per_page
    key_orders = {
        "ASC": "+",
        "DESC": "-"
    }
    str_order = "{}created_at".format(key_orders.get(order))

    total = query_set.all(data_filter).count()

    total_page = round_well(total/item_per_page)

    query_result = query_set.filter_all(
        data_filter,
        skip,
        item_per_page,
        str_order,
    )

    meta = {
        "current_page": page,
        "item_per_page": item_per_page,
        "total_page": total_page,
        "available_orders": [
            "ASC",
            "DESC"
        ]
    }

    output = {
        "data":json.loads(query_result.to_json())
    } 

    output['meta'] = meta

    return output