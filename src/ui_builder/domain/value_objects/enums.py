from enum import Enum


class TypeAlert(Enum):
    ALERT = "alert"
    INFO = "alert alert-info"
    SUCCESS = "alert alert-success"
    WARNING = "alert alert-warning"
    ERROR = "alert alert-error"


class IconOutline(Enum):
    INFORMATION_CIRCLE = """<path
    stroke-linecap="round"
    stroke-linejoin="round"
    stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>"""


class Stroke(Enum):
    INFO = "stroke-info"
    CURRENT = "stroke-current"


class TypeTextInput(Enum):
    TEXT = "text"
    PASSWORD = "password"
    EMAIL = "email"

class TypeInputColor(Enum):
    DEFAULT = ''
    PRIMARY = 'input-primary'
    SECONDARY = 'input-secondary'
    ACCENT = 'input-accent'
    INFO = 'input-info'
    SUCCESS = 'input-success'
    WARNING = 'input-warning'
    ERROR = 'input-error'

class TypeInputSize(Enum):
    DEFAULT = ''
    XS = 'input-xs'
    SM = 'input-sm'
    MD = 'input-md'
    LG = 'input-lg'

class TypeInputIconPosition(Enum):
    NONE = 'none'
    RIGHT = 'right'
    LEFT = 'left'

class TypeButton(Enum):
    DEFAULT = ''
    NEUTRAL = 'btn-neutral'
    PRIMARY = 'btn-primary'
    SECONDARY = 'btn-secondary'
    ACCENT = 'btn-accent'
    GHOST = 'btn-ghost'
    LINK = 'btn-link'

class TypeButtonSize(Enum):
    DEFAULT = ''
    XS = 'btn-xs'
    SM = 'btn-sm'
    LG = 'btn-lg'