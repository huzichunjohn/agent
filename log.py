import logging

from ..config import LOG_DIR, LOG_LEVEL
print LOG_DIR, LOG_LEVEL

LOG = logging.basicConfig()

console = logging.StreamHandler()
formatter = logging.Formatter("%(levelname)s %(message)s")
console.setFormatter(formatter)

LOG.addHandler(console)

