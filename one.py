import sys
from types import ModuleType

class _numbers(ModuleType):
    # Create the instance, with the value
    def __init__(self, value):
        if isinstance(value, float):
            if not value.is_integer():
                raise ValueError(f"The Module's value must be of type 'int', not 'float'")
            value = int(value)

        self.__value = value
        self.__name = _numbers.num_to_str(self.__value)
        self.__module__ = self.__name
        super().__init__(self.__name)

    def __call__(self):
        print("one")
        pass

    # Convert number to string
    @staticmethod
    def num_to_str(num):
        num_groups = ['thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion', 'undecillion']
        single_num_names = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        teens_names = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
        tens_num_names = ['', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
        name = ""
        next_groups = abs(num)
        i = -1
        while True:
            if (i >= len(num_groups)):
                raise ValueError("Number too large")

            curr_group = next_groups % 1000
            next_groups = next_groups // 1000

            group_name = num_groups[i] if i >= 0 else ""
            group_name += ' '

            curr_group_name = ''
            # Hundreds
            curr_group_name += single_num_names[curr_group // 100] + ' hundred ' if curr_group // 100 > 0 else ''

            if ((curr_group % 100) // 10) == 1:
                curr_group_name += teens_names[curr_group % 10]
                curr_group_name += ' '
            else:
                curr_group_name += tens_num_names[(curr_group % 100) // 10]
                curr_group_name += ' '
                curr_group_name += single_num_names[curr_group % 10]
                curr_group_name += ' '

            curr_group_name += group_name
            name = curr_group_name + name

            if next_groups == 0:
                break
            i += 1

        if name.strip() == '':
            name = 'zero'

        if num < 0:
            name = 'negative ' + name

        return " ".join(name.strip().split())

    # Module Type Conversions
    def __int__(self):
        return self.__value

    def __float__(self):
        return float(self.__value)

    def __bool__(self):
        return bool(int(self))

    def __str__(self):
        return self.__name

    def __bytes__(self):
        return bytes(str(self), 'utf-8')

    def __complex__(self):
        return complex(float(self))

    # Module Math
    def __add__(self, other):
        if isinstance(other, int):
            return _numbers(self.__value + other)
        elif isinstance(other, _numbers):
            return _numbers(self.__value + other.__value)
        else:
            raise TypeError(f"Can't add type 'module' and type '{type(other)}'")

    def __radd__(self, other):
        if isinstance(other, int):
            return _numbers(other + self.__value)
        elif isinstance(other, _numbers):
            return _numbers(other.__value + self.__value )
        else:
            raise TypeError(f"Can't add type '{type(other)}' and type 'module'")

    def __sub__(self, other):
        if isinstance(other, int):
            return _numbers(self.__value - other)
        elif isinstance(other, _numbers):
            return _numbers(self.__value - other.__value)
        else:
            raise TypeError(f"Can't subtract type 'module' and type '{type(other)}'")

    def __rsub__(self, other):
        if isinstance(other, int):
            return _numbers(other - self.__value)
        elif isinstance(other, _numbers):
            return _numbers(other.__value - self.__value )
        else:
            raise TypeError(f"Can't subtract type '{type(other)}' and type 'module'")

    def __mul__(self, other):
        if isinstance(other, int):
            return _numbers(self.__value * other)
        elif isinstance(other, _numbers):
            return _numbers(self.__value * other.__value)
        else:
            raise TypeError(f"Can't multiply type 'module' and type '{type(other)}'")

    def __rmul__(self, other):
        if isinstance(other, int):
            return _numbers(other * self.__value)
        elif isinstance(other, _numbers):
            return _numbers(other.__value * self.__value )
        else:
            raise TypeError(f"Can't multiply type '{type(other)}' and type 'module'")

    def __mod__(self, other):
        if isinstance(other, int):
            return _numbers(self.__value % other)
        elif isinstance(other, _numbers):
            return _numbers(self.__value % other.__value)
        else:
            raise TypeError(f"Can't modulo type 'module' and type '{type(other)}'")

    def __rmod__(self, other):
        if isinstance(other, int):
            return _numbers(other % self.__value)
        elif isinstance(other, _numbers):
            return _numbers(other.__value % self.__value)
        else:
            raise TypeError(f"Can't modulo type '{type(other)}' and type 'module'")

    def __truediv__(self, other):
        if isinstance(other, int):
            return _numbers(self.__value / other)
        elif isinstance(other, _numbers):
            return _numbers(self.__value / other.__value)
        else:
            raise TypeError(f"Can't floor divide type 'module' and type '{type(other)}'")

    def __rdiv__(self, other):
        if isinstance(other, int):
            return _numbers(other / self.__value)
        elif isinstance(other, _numbers):
            return _numbers(other.__value / self.__value)
        else:
            raise TypeError(f"Can't floor divide type '{type(other)}' and type 'module'")

    def __floordiv__(self, other):
        if isinstance(other, int):
            return _numbers(self.__value // other)
        elif isinstance(other, _numbers):
            return _numbers(self.__value // other.__value)
        else:
            raise TypeError(f"Can't floor divide type 'module' and type '{type(other)}'")

    def __rfloordiv__(self, other):
        if isinstance(other, int):
            return _numbers(other // self.__value)
        elif isinstance(other, _numbers):
            return _numbers(other.__value // self.__value)
        else:
            raise TypeError(f"Can't floor divide type '{type(other)}' and type 'module'")

    def __pow__(self, other):
        if isinstance(other, int):
            return _numbers(self.__value ** other)
        elif isinstance(other, _numbers):
            return _numbers(self.__value ** other.__value)
        else:
            raise TypeError(f"Can't exponentiate type 'module' and type '{type(other)}'")

    def __rpow__(self, other):
        if isinstance(other, int):
            return _numbers(other ** self.__value)
        elif isinstance(other, _numbers):
            return _numbers(other.__value ** self.__value)
        else:
            raise TypeError(f"Can't exponentiate type '{type(other)}' and type 'module'")


    # Module Unary Arithmetic
    def __neg__(self):
        return _numbers(-self.__value)

    def __invert__(self):
        return _numbers(~self.__value)

    def __abs__(self):
        return _numbers(abs(self.__value))


    # Module Bitwise Arithmetic
    def __and__(self, other):
        if isinstance(other, int):
            return _numbers(self.__value & other)
        elif isinstance(other, _numbers):
            return _numbers(self.__value & other.__value)
        else:
            raise TypeError(f"Can't AND type 'module' and type '{type(other)}'")

    def __rand__(self, other):
        if isinstance(other, int):
            return _numbers(other & self.__value)
        elif isinstance(other, _numbers):
            return _numbers(other.__value & self.__value)
        else:
            raise TypeError(f"Can't AND type '{type(other)}' and type 'module'")

    def __or__(self, other):
        if isinstance(other, int):
            return _numbers(self.__value | other)
        elif isinstance(other, _numbers):
            return _numbers(self.__value | other.__value)
        else:
            raise TypeError(f"Can't OR type 'module' and type '{type(other)}'")

    def __ror__(self, other):
        if isinstance(other, int):
            return _numbers(other | self.__value)
        elif isinstance(other, _numbers):
            return _numbers(other.__value | self.__value)
        else:
            raise TypeError(f"Can't OR type '{type(other)}' and type 'module'")

    def __xor__(self, other):
        if isinstance(other, int):
            return _numbers(self.__value ^ other)
        elif isinstance(other, _numbers):
            return _numbers(self.__value ^ other.__value)
        else:
            raise TypeError(f"Can't OR type 'module' and type '{type(other)}'")

    def __rxor__(self, other):
        if isinstance(other, int):
            return _numbers(other ^ self.__value)
        elif isinstance(other, _numbers):
            return _numbers(other.__value ^ self.__value)
        else:
            raise TypeError(f"Can't OR type '{type(other)}' and type 'module'")

    def __rshift__(self, other):
        if isinstance(other, int):
            return _numbers(self.__value >> other)
        elif isinstance(other, _numbers):
            return _numbers(self.__value >> other.__value)
        else:
            raise TypeError(f"Can't OR type 'module' and type '{type(other)}'")

    def __rrshift__(self, other):
        if isinstance(other, int):
            return _numbers(other >> self.__value)
        elif isinstance(other, _numbers):
            return _numbers(other.__value >> self.__value)
        else:
            raise TypeError(f"Can't OR type '{type(other)}' and type 'module'")

    def __lshift__(self, other):
        if isinstance(other, int):
            return _numbers(self.__value << other)
        elif isinstance(other, _numbers):
            return _numbers(self.__value << other.__value)
        else:
            raise TypeError(f"Can't OR type 'module' and type '{type(other)}'")

    def __rlshift__(self, other):
        if isinstance(other, int):
            return _numbers(other << self.__value)
        elif isinstance(other, _numbers):
            return _numbers(other.__value << self.__value)
        else:
            raise TypeError(f"Can't OR type '{type(other)}' and type 'module'")


    # Module Equalities
    def __eq__(self, other):
        if isinstance(other, int):
            return self.__value == other
        elif isinstance(other, _numbers):
            return self.__value == other.__value
        else:
            return False

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if isinstance(other, int):
            return self.__value < other
        elif isinstance(other, _numbers):
            return self.__value < other.__value
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, int):
            return self.__value > other
        elif isinstance(other, _numbers):
            return self.__value > other.__value
        else:
            return False

    def __le__(self, other):
        if isinstance(other, int):
            return self.__value <= other
        elif isinstance(other, _numbers):
            return self.__value <= other.__value
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, int):
            return self.__value >= other
        elif isinstance(other, _numbers):
            return self.__value >= other.__value
        else:
            return False

    def __hash__(self):
        return hash(self.__value)


sys.modules[__name__] = _numbers(1)

# Cleanup namespace
del sys
del ModuleType
