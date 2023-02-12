from typing import Callable, Dict

Producer = Callable[[str], str]


_producers: Dict[str, Producer] = dict()


def producer(name: str) -> Callable[[Producer], Producer]:
    def decorator(func: Producer) -> Producer:
        assert name not in _producers
        _producers[name] = func
        return func

    return decorator


def get_producers() -> Dict[str, Producer]:
    return dict(_producers)
