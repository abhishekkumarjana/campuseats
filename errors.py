from flask import jsonify


def problem(type_, title, status, detail):
    response = jsonify({
        "type": type_,
        "title": title,
        "status": status,
        "detail": detail
    })

    response.status_code = status
    return response