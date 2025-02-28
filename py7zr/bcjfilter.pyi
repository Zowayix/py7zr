from typing import Any, Union

class BCJFilter:
    is_encoder: Any = ...
    prev_mask: int = ...
    prev_pos: int = ...
    current_position: int = ...
    stream_size: Any = ...
    buffer: Any = ...
    def __init__(self, func: Any, readahead: int, is_encoder: bool, stream_size: int=...) -> None: ...
    def sparc_code(self): ...
    def ppc_code(self): ...
    def armt_code(self) -> int: ...
    def arm_code(self) -> int: ...
    def x86_code(self) -> int: ...
    def decode(self, data: Union[bytes, bytearray, memoryview], max_length: int=...) -> bytes: ...
    def encode(self, data: Union[bytes, bytearray, memoryview]) -> bytes: ...
    def flush(self): ...

class BCJDecoder(BCJFilter):
    def __init__(self, size: int) -> None: ...

class BCJEncoder(BCJFilter):
    def __init__(self) -> None: ...

class SparcDecoder(BCJFilter):
    def __init__(self, size: int) -> None: ...

class SparcEncoder(BCJFilter):
    def __init__(self) -> None: ...

class PpcDecoder(BCJFilter):
    def __init__(self, size: int) -> None: ...

class PpcEncoder(BCJFilter):
    def __init__(self) -> None: ...

class ArmtDecoder(BCJFilter):
    def __init__(self, size: int) -> None: ...

class ArmtEncoder(BCJFilter):
    def __init__(self) -> None: ...

class ArmDecoder(BCJFilter):
    def __init__(self, size: int) -> None: ...

class ArmEncoder(BCJFilter):
    def __init__(self) -> None: ...
