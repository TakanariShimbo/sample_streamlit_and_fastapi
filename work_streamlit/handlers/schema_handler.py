from typing import Any, Dict

from pydantic import ValidationError

from handlers.response_handler import ResponseHandler


class SchemaHandler:
    @staticmethod
    def create_instance(schema_class: Any, kwargs: Dict[str, Any]) -> ResponseHandler:
        try:
            schema_instance = schema_class(**kwargs)
            return ResponseHandler(is_success=True, contents={"created_instance": schema_instance})
        
        except ValidationError as e:
            for error in e.errors():
                field = error['loc'][0]
                msg = error['msg']
                error_message = f"{field}: {msg}"
                return ResponseHandler(is_success=False, detail=error_message)
            
        raise Exception("An unexpected error occurred while trying to create a schema instance.")