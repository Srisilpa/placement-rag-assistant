import sys
from pathlib import Path

project_root = Path(__file__).parent.parent

sys.path.append(
    str(project_root)
)

from src.memory.cache_manager import CacheManager


cache = CacheManager()

cache.set(
    "highest package",
    "42.0 LPA"
)

print(
    "Value:",
    cache.get(
        "highest package"
    )
)

print(
    "Exists:",
    cache.exists(
        "highest package"
    )
)

print(
    "Missing:",
    cache.get(
        "amazon package"
    )
)