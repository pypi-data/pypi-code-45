# Flask imports
from flask import request, abort, make_response, jsonify

# JSON SChema Imports
from jsonschema import validate
from jsonschema.exceptions import ValidationError


def validate_json(f):
    # Validate the json
    try:
        request.get_json()
    except Exception:
        msg = "payload must be a valid json"
        return abort(400, {"error": msg})


def validate_schema(schema=None, force=False, data=None):
    if not data:
        # Validate the schema of the json
        data = request.get_json(force=force)

    if data is None:
        return abort(400, 'Failed to decode JSON object')

    try:
        validate(data, schema)
    except ValidationError as e:
        return abort(make_response(jsonify(e), 400))
