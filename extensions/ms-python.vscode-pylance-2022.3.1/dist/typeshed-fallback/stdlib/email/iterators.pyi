from email.message import Message
from typing import Iterator

__all__ = ["body_line_iterator", "typed_subpart_iterator", "walk"]

def body_line_iterator(msg: Message, decode: bool = ...) -> Iterator[str]: ...
def typed_subpart_iterator(msg: Message, maintype: str = ..., subtype: str | None = ...) -> Iterator[str]: ...
def walk(self: Message) -> Iterator[Message]: ...
