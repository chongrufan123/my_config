from typing import Any

class Environment:
    data: Any
    def __init__(self, config, prefix) -> None: ...
    def load(self): ...
