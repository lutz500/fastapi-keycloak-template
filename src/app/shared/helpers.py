import os
from .logging import logger


def get_env(name: str, log: bool = False):
    """Get environment variable or return exception."""
    try:
        var = os.environ[name]
        if log:
            logger.info(f"Loaded environment variable '{name}': {var}")
        return var
    except KeyError:
        error_msg = f"Expected environment variable '{name}' not set."
        logger.error(error_msg)
        raise EnvironmentError(error_msg)
