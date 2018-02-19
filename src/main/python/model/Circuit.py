import turtle


class Circuit(object):
    def __init__(self, name):
        self.name = name
        self.gates = {}
        self.inputs = []
        self.outputs = []

    def fire(self):
        """
        Fire the circuit.
        """
        for input in self.inputs:
            input.doGate([])

        for output in self.outputs:
            print(output.name + ": " + str(output.val))

    def drawCircuit(self):
        """
        Draw the circuit.
        """
        drawing = turtle.Turtle()
        drawing.penup()
        drawing.hideturtle()
        drawing.clear()

        for input in self.inputs:
            input.doGate([])

        self.resetDepth()
        self.calculateDepths(self.inputs)

        for gate in self.gates.values():
            gate.draw(drawing)

        turtle.done()

    def calculateDepths(self, inputs):
        """
        Calculate depths of the circuit.
        """
        y = 0
        for input in self.inputs:
            input.depthY = y
            y += 1

        self.depthX(inputs, 0)
        self.depthY(inputs)

        max = 0
        for output in self.outputs:
            if max < output.depthX:
                max = output.depthX

        for output in self.outputs:
            output.depthX = max

        self.adjustDepth()

    def depthX(self, inputs, currentDepth):
        maxDepth = currentDepth
        tempDepth = 0

        for input in inputs:

            if (input.depthX < currentDepth):
                input.depthX = currentDepth

            if (len(input.outConnections) != 0):
                tempDepth = self.depthX(input.outConnections, currentDepth + 1)

            if tempDepth > maxDepth:
                maxDepth = tempDepth

        return maxDepth

    def depthY(self, inputs):
        for input in inputs:
            if input not in self.inputs:
                cons = []
                for con in input.inConnections:
                    cons.append(con.depthY)
                input.depthY = int(self.average(cons))

        outs = []
        for input in inputs:
            for out in input.outConnections:
                outs.append(out)

        if len(outs) != 0:
            self.depthY(outs)

    def adjustDepth(self):
        for gate1 in self.gates.values():
            for gate2 in self.gates.values():
                if (gate1.depthX == gate2.depthX and gate1.depthY == gate2.depthY and gate1 != gate2):
                    gate1.depthY += 1
                    self.adjustDepth()

    def resetDepth(self):
        for gate in self.gates.values():
            gate.depthX = 0
            gate.depthY = 0

    def average(self, nums):
        avr = 0
        for num in nums:
            avr += num
        avr /= len(nums)
        return avr

    def addGate(self, name, gate):
        """
        Add gate to the circuit.
        :param name: the name of the gate
        :param gate: the gate
        """
        self.gates[name] = gate

    def removeGate(self, name):
        """
        Remove gate to the circuit.
        :param name: the name of the gate
        :param gate: the gate
        """
        del self.gates[name]

    def getGate(self, name):
        """
        Get a gate from the circuit.
        :param name: the name of the gate
        """
        return self.gates[name]

    def addInput(self, gate):
        """
        Add input gate to the circuit.
        :param gate: the input gate
        """
        self.inputs.append(gate)

    def removeInput(self, gate):
        """
        Remove input gate to the circuit.
        :param gate: the input gate
        """
        self.inputs.remove(gate)

    def addOutput(self, gate):
        """
        Add output gate to the circuit.
        :param gate: the output gate
        """
        self.outputs.append(gate)

    def removeOutput(self, gate):
        """
        Remove output gate to the circuit.
        :param gate: the output gate
        """
        self.outputs.remove(gate)

    def hasGate(self, name):
        """
        Check if circuit has gate.
        :param name: the name of the gate
        """
        return (name in self.gates)
