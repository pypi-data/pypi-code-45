from functools import wraps

from flask import request, jsonify, current_app

from jsonschema import validate
from jsonschema.exceptions import ValidationError


def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            request.get_json()
        except Exception:
            msg = "payload must be a valid json"
            return jsonify({"error": msg}), 400
        return f(*args, **kw)
    return wrapper


def validate_schema(schema):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            try:
                validate(request.json, schema)
            except ValidationError as e:
                return jsonify({"error": e.message}), 400
            return f(*args, **kw)
        return wrapper
    return decorator
