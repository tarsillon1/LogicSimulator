from model.gate.Gate import Gate


class Input(Gate):
    def __init__(self, name, circuit):
        Gate.__init__(self, name, circuit)
        circuit.addInput(self)
        self.type = "Input Gate "

    def doGate(self, inputs):
        self.sendConnect(self.val)

    def destroy(self):
        Gate.destroy(self)
        self.circuit.removeInput(self)