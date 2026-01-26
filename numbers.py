import sys
from types import ModuleType
import one

class _numberContextManager(ModuleType):
    def __init__(self):
        super().__init__('numbers')

    @staticmethod
    def str_to_num(s):
        # Replace underscores with spaces so we can parse normally
        s = s.replace('_', ' ').strip()

        num_groups = {
            'thousand': 10**3,
            'million': 10**6,
            'billion': 10**9,
            'trillion': 10**12,
            'quadrillion': 10**15,
            'quintillion': 10**18,
            'sextillion': 10**21,
            'septillion': 10**24,
            'octillion': 10**27,
            'nonillion': 10**30,
            'decillion': 10**33,
            'undecillion': 10**36,
        }

        singles = {
            'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
        }

        teens = {
            'ten': 10,
            'eleven': 11,
            'twelve': 12,
            'thirteen': 13,
            'fourteen': 14,
            'fifteen': 15,
            'sixteen': 16,
            'seventeen': 17,
            'eighteen': 18,
            'nineteen': 19,
        }

        tens = {
            'twenty': 20,
            'thirty': 30,
            'forty': 40,
            'fifty': 50,
            'sixty': 60,
            'seventy': 70,
            'eighty': 80,
            'ninety': 90,
        }

        words = s.split()
        total = 0
        current = 0
        negative = False

        for word in words:
            if word == 'negative':
                negative = True
            elif word in singles:
                current += singles[word]
            elif word in teens:
                current += teens[word]
            elif word in tens:
                current += tens[word]
            elif word == 'hundred':
                current *= 100
            elif word in num_groups:
                total += current * num_groups[word]
                current = 0
            else:
                raise ValueError(f"Unknown number: {word}")

        total += current
        return -total if negative else total

    def __getattr__(self, num):
        value = _numberContextManager.str_to_num(num)
        new_num = one.__class__(value)
        return new_num

sys.modules[__name__] = _numberContextManager()
del sys
del ModuleType
