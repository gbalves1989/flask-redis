from api import redis_client


def redis_set(key: str, data: any) -> None:
    redis_client.__setitem__(key, data)


def redis_get(key: str) -> bytes:
    return redis_client.__getitem__(key)


def redis_remove(key: str) -> None:
    redis_client.__delitem__(key)
