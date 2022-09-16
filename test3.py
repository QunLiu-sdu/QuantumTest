from projectq import MainEngine
from projectq.backends import ResourceCounter, _resource, ClassicalSimulator, CommandPrinter
from projectq.meta import Uncompute, Compute
from projectq.ops import H, Tdag, CNOT, T, X, Toffoli, Measure, All, Allocate

#*****************检查电路时，输入值需要赋值，采取1就过NOT门的思路*******************
def allocation_input_qubits(INPUT, qinput):
    def hextobin(ahex):
        if ahex == '0':
            return '0000'
        elif ahex == '1':
            return '1000'
        elif ahex == '2':
            return '0100'
        elif ahex == '3':
            return '1100'
        elif ahex == '4':
            return '0010'
        elif ahex == '5':
            return '1010'
        elif ahex == '6':
            return '0110'
        elif ahex == '7':
            return '1110'
        elif ahex == '8':
            return '0001'
        elif ahex == '9':
            return '1001'
        elif ahex == 'A':
            return '0101'
        elif ahex == 'B':
            return '1101'
        elif ahex == 'C':
            return '0011'
        elif ahex == 'D':
            return '1011'
        elif ahex == 'E':
            return '0111'
        elif ahex == 'F':
            return '1111'
    for site in range(16):
        thisstr = INPUT[site]
        binstr = hextobin(thisstr[1])
        binstr += hextobin(thisstr[0])
        for bit in range(8):
            if binstr[bit] == '1':
                X | qinput[8*site+bit]

def print_all_qubits(allqubits):
    def bintohex(abin4):
        if abin4 == '0000':
            return '0'
        elif abin4 == '1000':
            return '1'
        elif abin4 == '0100':
            return '2'
        elif abin4 == '1100':
            return '3'
        elif abin4 == '0010':
            return '4'
        elif abin4 == '1010':
            return '5'
        elif abin4 == '0110':
            return '6'
        elif abin4 == '1110':
            return '7'
        elif abin4 == '0001':
            return '8'
        elif abin4 == '1001':
            return '9'
        elif abin4 == '0101':
            return 'A'
        elif abin4 == '1101':
            return 'B'
        elif abin4 == '0011':
            return 'C'
        elif abin4 == '1011':
            return 'D'
        elif abin4 == '0111':
            return 'E'
        elif abin4 == '1111':
            return 'F'

    for each_qubits in allqubits:
        bit_str = ''
        hex_str = ''
        for i in range(len(each_qubits)):
            if i != 0 and i % 8 == 0:
                bit_str += ' '
            thisqubit = str(int(each_qubits[i]))
            bit_str += thisqubit
        print(bit_str)

        hexnum = len(bit_str) // 9
        for thishex in range(hexnum + 1):
            thisstr = bit_str[thishex*9:thishex*9+8]
            hex_str += bintohex(thisstr[4:8])
            hex_str += bintohex(thisstr[0:4])
            hex_str += ' '
        print(hex_str)

eng = MainEngine(backend=ClassicalSimulator())


INPUT = ['01', '23', '45', '67',
         '89', 'AB', 'CD', 'EF',
         'FE', 'DC', 'BA', '98',
         '76', '54', '32', '10']
# 0 1 2 3
# 4 5 6 7
# 8 9 10 11
# 12 13 14 15

input_qibuts = eng.allocate_qureg(128)  # 输入明文

allocation_input_qubits(INPUT, input_qibuts)

All(Measure) | input_qibuts

allqubits = [input_qibuts]

print_all_qubits(allqubits)