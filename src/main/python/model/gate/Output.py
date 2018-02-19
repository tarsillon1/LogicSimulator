from model.gate.Gate import Gate

class Output(Gate):
    def __init__(self, name, circuit):
        Gate.__init__(self, name, circuit)
        circuit.addOutput(self)
        self.type = "Output Gate "

    def doGate(self, inputs):
        self.val = inputs[0]
        return self.val

    def destroy(self):
        Gate.destroy()
        self.circuit.removeOutput(self)