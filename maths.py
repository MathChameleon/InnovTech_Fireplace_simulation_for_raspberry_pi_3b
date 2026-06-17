from collections.abc import AsyncGenerator
import asyncio


def lerp(a: int, b: int, t: float) -> float:
    """Linear interpolate on the scale given by a to b, using t as the point on that scale.
    Examples
    --------
        50 == lerp(0, 100, 0.5)
        4.2 == lerp(1, 5, 0.8)
    """
    return (1 - t) * a + t * b


async def lerp_over_time(
    a: int, b: int, second: float, sleep_time: float
) -> AsyncGenerator[float]:
    """_summary_

    Args:
        a (int): Start value
        b (int): Destination value
        second (float): Duration
        sleep_time (float): Time for each iterations

    Yields:
        Iterator[float]: Lerped value
    """
    last = a
    t = 0
    inc = sleep_time / second
    while last != b:
        last = lerp(a, b, t)
        t = min(t + inc, 1)
        await asyncio.sleep(sleep_time)
        yield last
