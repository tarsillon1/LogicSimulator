from model.gate.Gate import Gate

class XNORGate(Gate):
     def __init__(self, name, circuit):
        Gate.__init__(self, name, circuit)
        self.type = "XNOR Gate "

     def doGate(self, inputs):
        """
        :param inputs: the input values
        :return: true if input values are the same, otherwise false
        """
        val = inputs[0]
        for i in inputs:
            if i != val:
                return self.sendConnect(0)
        return self.sendConnect(1)