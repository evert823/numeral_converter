class MixedRadixNumeralConverter():
    def __init__(self):
        pass

    def _N_valid(self, N: int) -> bool:
        if type(N) != int:
            return False
        if N < 0:
            return False
        return True

    def _bases_valid(self, bases: list[int]) -> bool:
        if type(bases) != list:
            return False
        if len(bases) < 1:
            return False

        combined_product = 1
        for base in bases:
            if type(base) != int:
                return False
            combined_product *= base
            if base < 1:
                return False
        if combined_product <= 1:
            return False

        return True

    def _bases_digits_valid(self, bases: list[int], digits: list[int]) -> bool:
        if self._bases_valid(bases) == False:
            return False


        if type(digits) != list:
            return False

        for digit in digits:
            if type(digit) != int:
                return False
            if digit < 0:
                return False

        if len(digits) != len(bases) + 1:
            return False

        nd = len(digits)
        for i in range(nd - 1):
            if digits[i + 1] >= bases[i]:
                return False

        return True

    def _get_value(self, bases: list[int], digits: list[int]) -> int:
        nd = len(digits)
        N = digits[0]

        for i in range(1, nd):
            N = (N * bases[i - 1]) + digits[i]

        return N

    def get_value(self, bases: list[int], digits: list[int]) -> int:
        if self._bases_digits_valid(bases, digits) == False:
            raise Exception(f"bases {bases} digits {digits} validation failed")
        
        return self._get_value(bases, digits)

    def _convert_to_base(self, bases: list[int], N: int) -> list[int]:
        N_temp = N
        digits = []

        nb = len(bases)

        for i in range(nb - 1, -1, -1):
            digit = N_temp % bases[i]
            digits.insert(0, digit)
            N_temp = N_temp // bases[i]
        
        digit = N_temp
        digits.insert(0, digit)

        return digits

    def convert_to_base(self, bases: list[int], N: int) -> list[int]:
        if self._N_valid(N) == False:
            raise Exception(f"N {N} should be int >= 0")
        if self._bases_valid(bases) == False:
            raise Exception(f"bases {bases} invalid")

        return self._convert_to_base(bases, N)

