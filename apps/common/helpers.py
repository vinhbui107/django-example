from rest_framework.serializers import Serializer


def validate_data(schema_cls: Serializer, data: dict):
    """
    Validate data using Marshmallow schema
    Return validated data if success, raise ValidationError if failed
    """

    schema = schema_cls(data=data)
    schema.is_valid(raise_exception=True)
    return schema.validated_data


def add_request_data(request, key, value):
    request_data = request.data.copy()
    query_params = request.query_params.dict()
    request_data.update(query_params)
    request_data[key] = value
    return request_data
