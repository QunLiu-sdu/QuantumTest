from projectq import MainEngine

from projectq.ops import H, Measure, CNOT, All


def f1(Qureg):

    H | Qureg[0]

    CNOT | (Qureg[0],Qureg[1])

    All(Measure) | Qureg

#普通的函数调用

eng=MainEngine()

Qureg=eng.allocate_qureg(2)

f1(Qureg)

eng.flush()

c0=int(Qureg[0])

c1=int(Qureg[1])

print(c0)

print(c1)