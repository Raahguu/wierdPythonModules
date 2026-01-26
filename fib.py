import sys
from types import ModuleType

class _fib(ModuleType):
    def __init__(self, iter=False, zeroth=0, first=1, max=None):
        self.__zeroth = zeroth
        self.__first = first
        self.__values = []

        self.__iter = iter

        if isinstance(max, int) or max is None:
            self.max = max
        else:
            raise ValueError("The 'max' property must be of type 'int' or 'NoneType'")

        if self.__iter == False:
            self.__values = [self.__zeroth, self.__first]

        super().__init__('fib')

    def __calc_next(self):
        if len(self.__values) == 0:
            self.__values.append(self.__zeroth)
        elif len(self.__values) == 1:
            self.__values.append(self.__first)
        else:
            self.__values.append(self.__values[-1] + self.__values[-2])

    def __getitem__(self, pos : int):
        if not isinstance(pos, int):
            raise ValueError("The index must be of type 'int'")

        while True:
            if len(self.__values) > pos:
                return self.__values[pos]

            self.__calc_next()

    def __contains__(self, value):
        while True:
            if self.max != None and len(self.__values) >= self.max:
                return value in self.__values

            if self.__values[-1] > value:
                return value in self.__values

            self.__calc_next()

    # Iterator stuff
    def __call__(self, max):
        """
            returns an iterator with the specified max
        """
        return _fib(True, max=max)

    def __iter__(self):
        if self.__iter == False:
            return _fib(True)
        else:
            return self

    def __next__(self):
        if self.max != None and len(self.__values) >= self.max:
            raise StopIteration

        self.__calc_next()

        return self.__values[-1]

sys.modules[__name__] = _fib()

del sys
del ModuleType
