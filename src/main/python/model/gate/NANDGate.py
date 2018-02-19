from model.gate.Gate import Gate

class NANDGate(Gate):
     def __init__(self, name, circuit):
        Gate.__init__(self, name, circuit)
        self.type = "NAND Gate "

     def doGate(self, inputs):
        """
        :param inputs: the input values
        :return: true if input values are both not true, otherwise false
        """
        for i in inputs:
            if i == 0:
                return self.sendConnect(1)
        return self.sendConnect(0)