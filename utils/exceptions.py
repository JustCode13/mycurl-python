import typing

class CurlError(Exception):
    def __init__(self, message: str) -> None:
        if not isinstance(message, str):
            raise TypeError("message must be a string")
        
        if not message.strip():
            raise ValueError("message cannot be empty")
        
        self.message = message
        super().__init__(message)

    