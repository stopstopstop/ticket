def sleep(s: int) -> None: ...
def sleep_ms(ms: int) -> None: ...
def sleep_us(us: int) -> None: ...
def ticks_ms() -> int: ...
def ticks_us() -> int: ...
def ticks_cpu() -> int: ...
def ticks_add(ticks_in: int, delta_in: int) -> int: ...
def ticks_diff(old: int, new: int) -> int: ...
