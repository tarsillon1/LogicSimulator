from common.Constants import Constants
import random


class Gate:
    def __init__(self, name, circuit):
        self.name = name;
        self.outConnections = []
        self.inConnections = []
        self.connectionVals = []
        self.depthX = 0
        self.depthY = 0
        self.val = 0
        self.type = "Gate "
        self.circuit = circuit

    def sendConnect(self, val):
        """
        When fired, send the output value of this gate to all output gates.
        :param val: the calculated value of this gate
        :return: the val of this gate
        """
        self.val = val
        for connection in self.outConnections:
            connection.connect(val)
        return val

    def connect(self, val):
        """
        Receive output value from input gate. Record value.
        :param val:  the output value of the input gate.
        """
        self.connectionVals.append(val)
        if (len(self.connectionVals) == len(self.inConnections)):
            self.doGate(self.connectionVals)
            self.connectionVals = []

    def doGate(self, inputs):
        """
        Process the input values based on the gate.
        :param inputs: the input values.
        """
        for connection in self.outConnections:
            connection.connect(0)
        return 0

    def addOutConnection(self, gate):
        """
        Add an out connection.
        :param gate: the gate to add
        """
        self.outConnections.append(gate)

    def removeOutConnection(self, gate):
        """
        Remove an out connection.
        :param gate: the gate to remove
        """
        self.outConnections.remove(gate)

    def addInConnection(self, gate):
        """
        Add an in connection.
        :param gate: the gate to add
        """
        self.inConnections.append(gate)

    def removeInConnection(self, gate):
        """
        Remove an in connection.
        :param gate: the gate to remove
        """
        self.inConnections.remove(gate)

    def destroy(self):
        """
        Destroy this gate
        """
        for connection in self.outConnections:
            connection.removeInConnection(self)

        for connection in self.inConnections:
            connection.removeOutConnection(self)

    def reconnectAll(self):
        """
        Reconnect out connection and in connection to this gate.
        """
        for connection in self.outConnections:
            connection.addInConnection(self)

        for connection in self.inConnections:
            connection.addOutConnection(self)

    def draw(self, turtle):
        """
        Draw this gate.
        """
        x = (self.depthX * Constants.GATE_SEPERATION_X) + Constants.GATE_START_X
        y = (-self.depthY * Constants.GATE_SEPERATION_Y) + Constants.GATE_START_Y

        turtle.setpos(x, y)
        turtle.write(self.type + self.name, move=False, align="center", font=("Arial", 16, "normal"))
        turtle.setpos(x, y - Constants.NUM_DISTANCE)
        turtle.write(self.val, move=False, align="center", font=("Arial", 14, "normal"))

        tup = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        turtle.pencolor(tup)
        for output in self.outConnections:
            turtle.penup()
            turtle.setpos(x + Constants.NUM_DISTANCE, y - (Constants.NUM_DISTANCE / 2))
            turtle.pendown()
            x2 = (output.depthX * Constants.GATE_SEPERATION_X) + Constants.GATE_START_X
            y2 = (-output.depthY * Constants.GATE_SEPERATION_Y) + Constants.GATE_START_Y
            turtle.setpos(x2 - Constants.NUM_DISTANCE, y2 - (Constants.NUM_DISTANCE / 2))

        turtle.pencolor("black")
        turtle.penup()
