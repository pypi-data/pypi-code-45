from jsonschema import validate

from superwise.exceptions.superwise_exceptions import SuperwiseRequestFormatError


def valid_trace_emit_prediction(data):
    """
    validate trace request from user
    :param data:
    :return: return if the data format is valid or not
    """
    schema = {
        "type": "object",
        "properties": {
            "record": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "ts": {"type": "string"},
                    "features": {
                        "type": "object"
                    },
                    "prediction_value": {"type": "string"},
                    "prediction_probability": {"type": "number"}
                },
                "required": ["id", "ts", "features", "prediction_probability"],
                "additionalProperties": False
            },
            "version_id": {"type": "integer"},
        },
        "required": ["record", "version_id"],
        "additionalProperties": False
    }
    try:
        res = validate(instance=data, schema=schema)
        return res is None
    except Exception:
        raise SuperwiseRequestFormatError("Request not in the right format...")


def valid_trace_batch_predictions(data):
    """
    validate trace batch requests from user
    :param data:
    :return: return if the data format is valid or not
    """
    schema = {
        "type": "object",
        "properties": {
            "records": {
                "type": "array",
                "items": [
                    {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string"
                            },
                            "ts": {
                                "type": "string"
                            },
                            "features": {
                                "type": "object"
                            },
                            "prediction_value": {
                                "type": "string"
                            },
                            "prediction_probability": {
                                "type": "number"
                            },

                        },
                        "required": [
                            "id",
                            "ts",
                            "features",
                            "prediction_probability"
                        ],
                        "additionalProperties": False
                    }
                ]
            },
            "version_id": {
                "type": "integer"
            }
        },
        "required": [
            "records", "version_id"
        ],
        "additionalProperties": False

    }
    try:
        res = validate(instance=data, schema=schema)
        return res is None
    except Exception:
        raise SuperwiseRequestFormatError("Request not in the right format...")


def valid_trace_file_predictions(data):
    """
    validate trace request from user
    :param data:
    :return: return if the data format is valid or not
    """
    schema = {
        "type": "object",
        "properties": {
            "file_url": {"type": "string"},
            "version_id": {"type": "integer"}
        },
        "required": ["file_url", "version_id"],
        "additionalProperties": False
    }
    try:
        res = validate(instance=data, schema=schema)
        return res is None
    except Exception:
        raise SuperwiseRequestFormatError("Request not in the right format...")


def valid_trace_emit_label(data):
    """
    validate trace request from user
    :param data:
    :return: return if the data format is valid or not
    """
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "ts": {"type": "string"},
            "label": {"type": "string"},
        },
        "required": ["id", "ts", "label"],
        "additionalProperties": False
    }
    try:
        res = validate(instance=data, schema=schema)
        return res is None
    except Exception:
        raise SuperwiseRequestFormatError("Request not in the right format...")


def valid_trace_batch_labels(data):
    """
    validate trace batch requests from user
    :param data:
    :return: return if the data format is valid or not
    """
    schema = {
        "type": "object",
        "properties": {
            "records": {
                "type": "array",
                "items": [
                    {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string"
                            },
                            "ts": {
                                "type": "string"
                            },
                            "label": {
                                "type": "string"
                            },

                        },
                        "required": [
                            "id",
                            "ts",
                            "label",
                        ],
                        "additionalProperties": False
                    }
                ]
            }
        },
        "required": [
            "records"
        ],
        "additionalProperties": False
    }
    try:
        res = validate(instance=data, schema=schema)
        return res is None
    except Exception:
        raise SuperwiseRequestFormatError("Request not in the right format...")


def valid_trace_file_labels(data):
    """
    validate trace request from user
    :param data:
    :return: return if the data format is valid or not
    """
    schema = {
        "type": "object",
        "properties": {
            "file_url": {"type": "string"}
        },
        "required": ["file_url"],
        "additionalProperties": False
    }
    try:
        res = validate(instance=data, schema=schema)
        return res is None
    except Exception:
        raise SuperwiseRequestFormatError("Request not in the right format...")
