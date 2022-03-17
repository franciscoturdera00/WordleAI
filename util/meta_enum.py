from enum import EnumMeta, Enum


class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True

    def __contains_all__(cls, lst):
        return all(map(cls.__contains__, lst))


class BaseEnum(Enum, metaclass=MetaEnum):
    pass
