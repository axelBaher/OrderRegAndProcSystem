import logging
import os

from backend.core.config import LOG_PATH, ROOT_PATH, LOG_CONSOLE_ENABLED, LOG_FILE_ENABLED

if not os.path.exists(ROOT_PATH / "backend" / "logs"):
    os.makedirs(ROOT_PATH / "logs")

# LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_CONSOLE_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

"""

======================================================LogRecord attributes======================================================
| Attribute name | Format                                    | Description                                                     |
|----------------|-------------------------------------------|-----------------------------------------------------------------|
| args           | You shouldn't need to format this yourself| The tuple of arguments merged into msg to produce message, or a |
                                                               dict whose values are used for the merge (when there is only one|
                                                               argument, and it is a dictionary).                              |
| asctime        | %(asctime)s                               | Human-readable time when the LogRecord was created.             |
                                                               By default this is of the form '2003-07-08 16:49:45,896'        |
                                                               (the numbers after the comma are millisecond portion            |
                                                               of the time).                                                   |
| created        | %(created)f                               | Time when the LogRecord was created                             |
                                                             | (as returned by time.time_ns() / 1e9).                          |
| exc_info       | You shouldn't need to format this yourself| Exception tuple (à la sys.exc_info) or,                         |                         
                                                               if no exception has occurred, None.                             |
| filename       | %(filename)s                              | Filename portion of pathname.                                   |
| funcName       | %(funcName)s                              | Name of function containing the logging call.                   |
| levelname      | %(levelname)s                             | Text logging level for the message                              |
                                                               ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').              |
| levelno        | %(levelno)s                               | Numeric logging level for the message                           |
                                                               (DEBUG, INFO, WARNING, ERROR, CRITICAL).                        |
| lineno         | %(lineno)d                                | Source line number where the logging call was issued            |
                                                               (if available).                                                 |
| message        | %(message)s                               | The logged message, computed as msg % args.                     |
                                                               This is set when Formatter.format() is invoked.                 |
| module         | %(module)s                                | Module (name portion of filename).                              |
| msecs          | %(msecs)d                                 | Millisecond portion of the time when the LogRecord was created. |
| msg            | You shouldn't need to format this yourself| The format string passed in the original logging call.          |
                                                               Merged with args to produce message, or an arbitrary object     |
                                                               (see Using arbitrary objects as messages).                      |
| name           | %(name)s                                  | Name of the logger used to log the call.                        |
| pathname       | %(pathname)s                              | Full pathname of the source file where the                      |
                                                               logging call was issued (if available).                         |
| process        | %(process)d                               | Process ID (if available).                                      |
| processName    | %(processName)s                           | Process name (if available).                                    |
| relativeCreated| %(relativeCreated)d                       | Time in milliseconds when the LogRecord was created, relative to|
                                                               the time the logging module was loaded.                         |
| stack_info     | You shouldn't need to format this yourself| Stack frame information (where available) from the bottom of the|
                                                               stack in the current thread, up to and                          |
                                                               including the stack frame of the logging call                   |
                                                               which resulted in the creation of this record.                  |
| thread         | %(thread)d                                | Thread ID (if available).                                       |
| threadName     | %(threadName)s                            | Thread name (if available).                                     |
| taskName       | %(taskName)s                              | asyncio.Task name (if available).                               |

=======================================================Formatter Objects========================================================

fmt (str) –                             A format string in the given style for the logged output as a whole.
                                        The possible mapping keys are drawn from the LogRecord object’s LogRecord attributes.
                                        If not specified, '%(message)s' is used, which is just the logged message.

datefmt (str) –                         A format string in the given style for the date/time portion of the logged output.
                                        If not specified, the default described in formatTime() is used.

style (str)                             Can be one of '%', '{' or '$' and determines
                                        how the format string will be merged with its data:
                                        using one of printf-style String Formatting (%), str.format() ({)
                                        or string.Template ($).
                                        This only applies to fmt and datefmt (e.g. '%(message)s' versus '{message}'),
                                        not to the actual log messages passed to the logging methods.
                                        However, there are other ways to use {- and $-formatting for log messages.

validate (bool)                         If True (the default), incorrect or mismatched fmt and style will raise a ValueError;
                                        for example, logging.Formatter('%(asctime)s - %(message)s', style='{').

defaults (dict[str, Any])               A dictionary with default values to use in custom fields.
                                        For example, logging.Formatter('%(ip)s %(message)s', defaults={"ip": None})
"""

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if LOG_CONSOLE_ENABLED:
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(LOG_CONSOLE_FORMAT))
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)

if LOG_FILE_ENABLED:
    file_handler = logging.FileHandler(LOG_PATH / "axelbaher.log", mode='a')
    file_handler.setFormatter(logging.Formatter(LOG_FILE_FORMAT))
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)

# Если ни один обработчик не добавлен, добавляем NullHandler
# if not logger.handlers:
#     logger.addHandler(logging.NullHandler())
#
# logger.propagate = False
#
# Перенаправляем стандартный вывод и вывод ошибок в логгер
# class StreamToLogger:
#     def __init__(self, logger, log_level=logging.INFO):
#         self.logger = logger
#         self.log_level = log_level
#         self.linebuf = ''
#
#     def write(self, buf):
#         for line in buf.rstrip().splitlines():
#             self.logger.log(self.log_level, line.rstrip())
#
#     def flush(self):
#         pass
#
# if not LOG_CONSOLE_ENABLED:
#     sys.stdout = StreamToLogger(logger, logging.INFO)
#     sys.stderr = StreamToLogger(logger, logging.ERROR)
