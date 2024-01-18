from typing import Any, Dict, Iterable

from _typeshed import Incomplete

from ..core import BaseRenderer as BaseRenderer
from ..core import BlockState as BlockState
from ..util import strip_end as strip_end
from ._list import render_list as render_list

fenced_re: Incomplete

class MarkdownRenderer(BaseRenderer):
    NAME: str
    def __call__(self, tokens: Iterable[Dict[str, Any]], state: BlockState) -> str: ...
    def render_referrences(self, state: BlockState) -> Iterable[str]: ...
    def render_children(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def text(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def emphasis(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def strong(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def link(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def image(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def codespan(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def linebreak(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def softbreak(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def blank_line(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def inline_html(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def paragraph(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def heading(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def thematic_break(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def block_text(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def block_code(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def block_quote(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def block_html(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def block_error(self, token: Dict[str, Any], state: BlockState) -> str: ...
    def list(self, token: Dict[str, Any], state: BlockState) -> str: ...
