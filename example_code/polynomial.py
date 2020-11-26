from numbers import Number


class Polynomial:

    def __init__(self, coefs):

        self.coefficients = coefs

    def degree(self):

        return len(self.coefficients) - 1

    def __str__(self):

        coefs = self.coefficients
        terms = []

        # Degree 0 and 1 terms conventionally have different representation.
        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() > 0 and coefs[1]:
            terms.append(f"{coefs[1]}x")

        # Remaining terms look like cx^d, though factors of 1 are dropped.
        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        # Sum polynomial terms from high to low exponent.
        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):

        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __add__(self, other):

        if isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        elif isinstance(other, Polynomial):
            # Work out how many coefficient places the two polynomials have in
            # common.
            common = min(self.degree(), other.degree()) + 1
            # Sum the common coefficient positions.
            coefs = tuple(a + b for a, b in zip(self.coefficients[:common],
                                                other.coefficients[:common]))

            # Append the high degree coefficients from the higher degree
            # summand.
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        else:
            return NotImplemented

    def __radd__(self, other):

        return self + other
