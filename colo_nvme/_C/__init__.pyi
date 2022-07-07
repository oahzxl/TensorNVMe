from torch import Tensor
from typing import Callable, Optional, List


class Offloader:
    def __init__(self, filename: str, n_entries: int, backend: str = 'uring') -> None: ...
    def async_write(self, tensor: Tensor, key: str, callback: Optional[Callable[[], None]] = None) -> None: ...
    def async_read(self, tensor: Tensor, key: str, callback: Optional[Callable[[], None]] = None) -> None: ...
    def sync_write(self, tensor: Tensor, key: str) -> None: ...
    def sync_read(self, tensor: Tensor, key: str) -> None: ...
    def sync_write_events(self) -> None: ...
    def sync_read_events(self) -> None: ...
    def synchronize(self) -> None: ...
    def async_writev(self, tensors: List[Tensor], key: str, callback: Optional[Callable[[], None]] = None) -> None: ...
    def async_readv(self, tensors: List[Tensor], key: str, callback: Optional[Callable[[], None]] = None) -> None: ...
    def sync_writev(self, tensors: List[Tensor], key: str) -> None: ...
    def sync_readv(self, tensors: List[Tensor], key: str) -> None: ...