from numbers import Number

class Polynomial:

    def __init__(self, coefs):

        self.coefficients = coefs

    def degree(self):

        return len(self.coefficients) - 1

    def __str__(self):

        coefs = self.coefficients
        terms = []

        # It is conventional to omit factors of 1.
        str1 = lambda n: '' if n == 1 else str(n)
        
        # Process the higher degree terms in reverse order.
        for d in range(self.degree(), 1, -1):
            if coefs[d]:
                terms.append(str1(coefs[d]) + "x^" + str(d))
        # Degree 1 and 0 terms conventionally have different representation.
        if self.degree() > 0 and coefs[1]:
            terms.append(str1(coefs[1]) + "x")
        if coefs[0]:
            terms.append(str(coefs[0]))

        return " + ".join(terms) or "0"

    def __repr__(self):

        return "Polynomial(" + repr(self.coefficients) + ")"

    def __add__(self, other):
        
        if isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,) + self.coefficients[1:])
        
        elif isinstance(other, Polynomial):
            # Work out how many coefficient places the two polynomials have in common.
            common = min(self.degree(), other.degree()) + 1
            # Sum the common coefficient positions.
            coefs = tuple(a + b for a, b in zip(self.coefficients[:common],
                                                other.coefficients[:common]))
            
            # Append the high degree coefficients from the higher degree summand.
            coefs += self.coefficients[common:] + other.coefficients[common:]
            
            return Polynomial(coefs)

        else:
            return NotImplemented

    def __radd__(self, other):

        return self + other
