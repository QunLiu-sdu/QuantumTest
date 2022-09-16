from projectq import MainEngine

from projectq.ops import H, Measure, All

#初始化引擎，这里使用默认引擎

eng=MainEngine()

#初始化qureg（qubit的list）

Qureg=eng.allocate_qureg(1)

#执行你需要的门

H | Qureg[0]


All(Measure) | Qureg

#冲一下引擎（需要注意的，有些引擎不冲也会跑，有些需要冲一下,下次再讲）

eng.flush()

#取出测量结果，简单的int就可以

c0=int(Qureg[0])


print(c0)


#最终结果0或者1