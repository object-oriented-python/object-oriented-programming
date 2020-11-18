from functools import singledispatch
import expressions


@singledispatch
def evaluate(expr, *o, map={}):
    raise NotImplementedError(
        f"Cannot evaluate a {type(expr).__name__}")


@evaluate.register(expressions.Number)
def _(expr, *o, map={}):
    return expr.value


@evaluate.register(expressions.Symbol)
def _(expr, *o, map={}):
    return map[expr.value]


@evaluate.register(expressions.Add)
def _(expr, *o, map={}):
    return o[0] + o[1]


@evaluate.register(expressions.Sub)
def _(expr, *o, map={}):
    return o[0] - o[1]


@evaluate.register(expressions.Mul)
def _(expr, *o, map={}):
    return o[0] * o[1]


@evaluate.register(expressions.Div)
def _(expr, *o, map={}):
    return o[0] / o[1]


@evaluate.register(expressions.Pow)
def _(expr, *o, map={}):
    return o[0] ** o[1]
