from projectq import MainEngine
from projectq.backends import ResourceCounter, _resource, ClassicalSimulator, CommandPrinter
from projectq.meta import Uncompute, Compute
from projectq.ops import H, Tdag, CNOT, T, X, Toffoli, Measure, All, Allocate


resource_check = 1

def f1(Qureg):

    H | Qureg[0]

    CNOT | (Qureg[0],Qureg[1])

    Toffoli_gate(Qureg[0],Qureg[1],Qureg[2],resource_check)

    All(Measure) | Qureg

def Toffoli_gate(a, b, c, resource_check):
    if (resource_check):
        Tdag | a
        Tdag | b
        H | c
        CNOT | (c, a)
        T | a
        CNOT | (b, c)
        CNOT | (b, a)
        T | c
        Tdag | a
        CNOT | (b, c)
        CNOT | (c, a)
        T | a
        Tdag | c
        CNOT | (b, a)
        H | c
    else:
        Toffoli | (a, b, c)


circuit_backend = _resource.ResourceCounter()
eng = MainEngine(backend=circuit_backend)

Qureg=eng.allocate_qureg(3)

f1(Qureg)

eng.flush()

# 打印电路实现代价
print(circuit_backend)
print("depth_of_dag: {}".format(circuit_backend.depth_of_dag))