from dataclasses import dataclass

@dataclass(frozen=True)
class ErrorConstants:
    INVALID_INPUT: str = "The input provided is invalid."
    NOT_FOUND: str = "The requested resource was not found."
    SERVER_ERROR: str = "An internal server error has occurred."
    UNAUTHORIZED: str = "You do not have permission to access this resource."
    TIMEOUT: str = "The request has timed out. Please try again later."
    TEXT_LEGTH_EXCEEDED: str = "The text length exceeds the maximum allowed limit."

    @staticmethod
    def PROPERTY_NOT_ALLOWED(property_name: str) -> str:
        return f"The property '{property_name}' is not allowed."