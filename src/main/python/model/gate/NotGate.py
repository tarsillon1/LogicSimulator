from model.gate.Gate import Gate

class NotGate(Gate):
     def __init__(self, name, circuit):
        Gate.__init__(self, name, circuit)
        self.type = "Not Gate "

     def doGate(self, inputs):
        """
        :param inputs: the input values
        :return: true if input values are not true, otherwise false
        """
        for i in inputs:
            if i == 0:
                return self.sendConnect(1)
            else:
                return self.sendConnect(0)