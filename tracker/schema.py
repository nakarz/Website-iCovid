update_filter_api_request = {
    'type': 'object',
    'properties': {
        'username': {'type': 'string'},
        'chart_type': {'type': 'string'},
        'number_of_data': {'type': 'string'},
    },
    'required': ['username', 'chart_type', 'number_of_data'],
}

get_filter_api_request = {
    'type': 'object',
    'properties': {
        'username': {'type': 'string'},
    },
    'required': ['username'],
}