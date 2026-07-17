from dataclasses import dataclass
import enum
import pathlib
import ssl 
import typing

from utils.exceptions import ConfigurationError

class RedirectPolicy(enum.Enum):
    ALWAYS = "always"
    NEVER = "never"
    MANUAL =  "manual"

    def allows_redirect(self):
        if self is RedirectPolicy.ALWAYS:
            return True
        else:
            return False
        