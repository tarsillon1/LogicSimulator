from model.gate.Gate import Gate

class XORGate(Gate):
     def __init__(self, name, circuit):
        Gate.__init__(self, name, circuit)
        self.type = "XOR Gate "

     def doGate(self, inputs):
        """
        :param inputs: the input values
        :return: true if input values are different, otherwise false
        """
        val = inputs[0]
        for i in inputs:
            if i != val:
                return self.sendConnect(1)
        return self.sendConnect(0)