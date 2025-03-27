class NumeralConverter():
    def __init__(self):
        pass

    def _N_valid(self, N: int) -> bool:
        if type(N) != int:
            return False
        if N < 0:
            return False
        return True

    def _base_valid(self, base: int) -> bool:
        if type(base) != int:
            return False
        if base < 2:
            return False
        return True

    def _digits_valid(self, base: int, digits: list[int]) -> bool:
        if self._base_valid(base) == False:
            return False
        if type(digits) != list:
            return False
        for digit in digits:
            if type(digit) != int:
                return False
            if digit < 0:
                return False
            if digit >= base:
                return False
        return True

    def _get_value(self, base: int, digits: list[int]) -> int:
        nd = len(digits)
        n = 0

        for i in range(0, nd):
            n += digits[i] * (base ** (nd - (i + 1)))
        return n

    def get_value(self, base: int, digits: list[int]) -> int:
        if self._digits_valid(base, digits) == False:
            raise Exception(f"digits {digits} should all be int >= 0 and < base {base}")
        if self._base_valid(base) == False:
            raise Exception(f"base {base} should be int >= 2")
        
        return self._get_value(base, digits)

    def _convert_to_base(self, base: int, N: int) -> list[int]:
        digits = []

        nd = 0
        while base ** (nd + 1) <= N:
            nd += 1

        j = 0

        while j <= nd:
            k = N // (base ** (nd - j))
            digits.append(k)
            N -= k * (base ** (nd - j))
            j += 1
        
        return digits

    def convert_to_base(self, base: int, N: int) -> list[int]:
        if self._N_valid(N) == False:
            raise Exception(f"N {N} should be int >= 0")
        if self._base_valid(base) == False:
            raise Exception(f"base {base} should be int >= 2")

        return self._convert_to_base(base, N)
