from model.gate.Gate import Gate

class NORGate(Gate):
     def __init__(self, name, circuit):
        Gate.__init__(self, name, circuit)
        self.type = "NOR Gate "

     def doGate(self, inputs):
        """
        :param inputs: the input values
        :return: true if input values are false, otherwise false
        """
        for i in inputs:
            if i == 1:
                return self.sendConnect(0)
        return self.sendConnect(1)