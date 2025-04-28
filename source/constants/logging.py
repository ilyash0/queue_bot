from pathlib import Path


class LoggingConstants(str):
    CONSOLE_LEVEL = "INFO"
    FILE_LEVEL = "DEBUG"
    CONSOLE_MESSAGE = False
    FILE_MESSAGE = True
    FILE_FULL = True
    FILE_ERROR = True

    BASE_LOG_DIR = Path("source") / "data"
    ERROR_LOG_DIR = BASE_LOG_DIR / "error_logs"
    FULL_LOG_DIR = BASE_LOG_DIR / "full_logs"

    CONSOLE_LOG_FORMAT = (
        "<blue>{time:YYYY-MM-DD HH:mm:ss.SSS}</blue> <white>|</white> "
        "<level>{level: <8}</level> <white>|</white> "
        "<light-blue>{name}</light-blue>:<light-blue>{function}</light-blue>:<light-blue>{line}</light-blue> <white>-</white> <level>{message}</level>"
    )
    FILE_LOG_FORMAT = (
        "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | "
        "{name}:{function}:{line} - {message}"
    )

    USER_MESSAGE_MARKER_START = "Update id="
    USER_MESSAGE_MARKER_END = "is handled."
