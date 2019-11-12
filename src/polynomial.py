from numbers import Number

class Polynomial:

    def __init__(self, coefs):

        self.coefficients = coefs

    def degree(self):

        return len(self.coefficients) - 1

    def __str__(self):

        coefs = self.coefficients
        terms = []
        # Process the higher degree terms in reverse order.
        for d in range(self.degree(), 1, -1):
            if coefs[d]:
                terms.append(str(coefs[d]) + "x^" + str(d))
        # Degree 1 and 0 terms traditionally have different representation.
        if self.degree() > 0 and coefs[1]:
            terms.append(str(coefs[1]) + "x")
        if coefs[0]:
            terms.append(str(coefs[0]))

        return " + ".join(terms) or "0"

    def __repr__(self):

        return "Polynomial(" + repr(self.coefficients) + ")"

    def __add__(self, other):
        if isinstance(other, Number):
            
            return Polynomial((self.coefficients[0] + other,) + self.coefficients[1:])
        
        elif isinstance(other, Polynomial):
# This is wrong
            mindegree = min(self.degree(), other.degree())
            # Start with the high degree coefficients from the higher degree summand.
            coefs += self.coefficients[:other.degree()+1] + other.coefficients[:self.degree()+1:]
            
            # First sum the coefficients up to the lower degree.
            coefs = tuple(a + b for a, b in zip(self.coefficients, other.coefficients))
            return Polynomial(coefs)

        else:

            return NotImplemented
            
