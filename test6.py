from projectq import MainEngine
from projectq.backends import ResourceCounter, _resource, ClassicalSimulator, CommandPrinter
from projectq.meta import Uncompute, Compute
from projectq.ops import H, Tdag, CNOT, T, X, Toffoli, Measure, All, Allocate

eng=MainEngine()

Qureg1=eng.allocate_qureg(2)
Qureg2=eng.allocate_qureg(2)
Qureg3=eng.allocate_qureg(2)
Qureg4=eng.allocate_qureg(2)
Qureg5=eng.allocate_qureg(2)
Qureg6=eng.allocate_qureg(2)
Qureg7=eng.allocate_qureg(2)
Qureg8=eng.allocate_qureg(2)
Qureg9=eng.allocate_qureg(2)
Qureg10=eng.allocate_qureg(2)

AllQureg = [Qureg1, Qureg2, Qureg3, Qureg4, Qureg5, Qureg6, Qureg7, Qureg8, Qureg9, Qureg10]
for oneset in AllQureg:
    X | oneset[1]

def swap1(qubit1, qubit2, tem_qubit):
    CNOT | (qubit1, tem_qubit)
    CNOT | (tem_qubit, qubit1)
    CNOT | (qubit2, qubit1)
    CNOT | (qubit1, qubit2)
    CNOT | (tem_qubit, qubit2)
    CNOT | (qubit2, tem_qubit)

TEMQUBIT = eng.allocate_qureg(1)

# 交换
for oneset in AllQureg:
    swap1(oneset[0], oneset[1], TEMQUBIT)

# 测量
for oneset in AllQureg:
    All(Measure) | oneset

# 测量临时变量TEMQUBIT
All(Measure) | TEMQUBIT

# 冲洗
eng.flush()

# 打印
for oneset in AllQureg:
    print("qubit0: {}, qubit1: {}".format(int(oneset[0]), int(oneset[1])))
print("temqubit: {}".format(int(TEMQUBIT)))