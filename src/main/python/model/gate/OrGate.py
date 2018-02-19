from model.gate.Gate import Gate

class OrGate(Gate):
    def __init__(self, name, circuit):
        Gate.__init__(self, name, circuit)
        self.type = "Or Gate "

    def doGate(self, inputs):
        """
        :param inputs: the input values
        :return: true if one input value is true, otherwise false
        """
        for i in inputs:
            if i == 1:
                return self.sendConnect(1)
        return self.sendConnect(0)