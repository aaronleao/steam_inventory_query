import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

logger = logging.getLogger(__package__)

def validate_format(inventory: dict) -> bool:
    if not inventory or "assets" not in inventory or "descriptions" not in inventory:
        logger.error("Error: Invalid inventory data.")
        return False
    return True

def validate_size(inventory: dict) -> bool:
    if not len(inventory["assets"]):
        return False
    return True
