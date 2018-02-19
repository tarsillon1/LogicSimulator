from model.gate.Gate import Gate


class AndGate(Gate):
    def __init__(self, name, circuit):
        Gate.__init__(self, name, circuit)
        self.type = "And Gate "

    def doGate(self, inputs):
        """
        :param inputs: the input values to process
        :return: true if all the values are true, otherwise false
        """
        for i in inputs:
            if i == 0:
                return self.sendConnect(0)
        return self.sendConnect(1)
