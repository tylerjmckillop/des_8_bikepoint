from modules.loginitialise import setup_logging
from datetime import datetime as dt

logger = setup_logging('logs', dt.now().strftime('%Y-%m-%d %H-%M-%S'))