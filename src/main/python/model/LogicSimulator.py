from model.Circuit import Circuit
from model.gate.AndGate import AndGate
from model.gate.OrGate import OrGate
from model.gate.NotGate import NotGate
from model.gate.XORGate import XORGate
from model.gate.NORGate import NORGate
from model.gate.XNORGate import XNORGate
from model.gate.NANDGate import NANDGate
from model.gate.Output import Output
from model.gate.Input import Input


class LogicSimulator:

    def __init__(self):
        self.circuits = {}
        self.currentCircuit = Circuit("")
        self.currentCircuitName = ""

    def createCircuit(self, name):
        """
        Create a circuit.
        :param name: name of the circuit
        """
        self.circuits[name] = Circuit(name)
        print("Created circuit " + name + ".")

    def setCircuit(self, name):
        """
        Set the current circuit.
        :param name: the name of the circuit.
        """
        if name in self.circuits:
            self.currentCircuit = self.circuits[name]
            self.currentCircuitName = name
            print("Circuit set to " + self.currentCircuitName + ".")
        else:
            print("Circuit does not exist.")

    def create(self, name, type):
        """
        Create a gate of type.
        :param name: the name of the gate
        :param type: the type of the gate
        """
        if self.currentCircuitName != "":
            if name not in self.currentCircuit.gates:
                options = {"and": AndGate,
                           "or": OrGate,
                           "not": NotGate,
                           "xor": XORGate,
                           "xnor": XNORGate,
                           "nor": NORGate,
                           "nand": NANDGate,
                           "output": Output,
                           "input": Input}

                if type.lower() in options:
                    self.currentCircuit.addGate(name, options[type.lower()](name, self.currentCircuit))
                    print("Created " + type + " gate, " + name + ".")
                else:
                    print("Gate type is unknown.")
            else:
                print("Name already exists.")
        else:
            print("No circuit open.")

    def connect(self, name1, name2):
        """
        Connect two gates together.
        :param name1: the name of the gate
        :param name2: the name of the other gate
        """
        if self.currentCircuitName != "":
            if self.currentCircuit.hasGate(name1) and self.currentCircuit.hasGate(name2):
                gate1 = self.currentCircuit.getGate(name1)
                gate2 = self.currentCircuit.getGate(name2)

                gate1.addOutConnection(gate2)
                gate2.addInConnection(gate1)

                print("Connected output of " + name1 + " to input of " + name2 + ".")
            else:
                print("A gate could not be found or has not been created.")
        else:
            print("No circuit open.")

    def disconnect(self, name1, name2):
        """
        Disconnect gates.
        :param name1: the name of the gate
        :param name2: the name of the other gate.
        """
        if self.currentCircuitName != "":
            if self.currentCircuit.hasGate(name1) and self.currentCircuit.hasGate(name2):
                gate1 = self.currentCircuit.getGate(name1)
                gate2 = self.currentCircuit.getGate(name2)

                gate1.removeOutConnection(gate2)
                gate2.removeInConnection(gate1)

                print("Disconnected output of " + name1 + " from input of " + name2 + ".")
            else:
                print("A gate could not be found or has not been created.")
        else:
            print("No circuit open.")

    def delete(self, name):
        """
        Delete gate.
        :param name: the name of the gate.
        """
        if self.currentCircuitName != "":
            if self.currentCircuit.hasGate(name):
                gate = self.currentCircuit.getGate(name)
                gate.destroy()
                self.currentCircuit.removeGate(name)
                print("Deleted " + name + ".")
            else:
                print("A gate could not be found or has not been created.")
        else:
            print("No circuit open.")

    def change(self, name, type):
        """
        Change the type of gate.
        :param name: the name of the gate to change
        :param type: the type to change the gate to
        """
        if (self.currentCircuitName != ""):
            if (self.currentCircuit.hasGate(name)):
                gate = self.currentCircuit.getGate(name)
                self.currentCircuit.removeGate(name)
                self.create(name, type)

                newGate = self.currentCircuit.getGate(name)
                newGate.inConnections = gate.inConnections
                newGate.outConnections = gate.outConnections

                gate.destroy()
                newGate.reconnectAll()
                print("Changed " + name + " to type " + type + ".")
            else:
                print("A gate could not be found or has not been created.")
        else:
            print("No circuit open.")

    def set(self, name, val):
        """
        Set the value of the gate.
        :param name: the name of the gate
        :param val: the value
        """
        if self.currentCircuitName != "":
            if name in self.currentCircuit.gates and self.currentCircuit.gates[name] in self.currentCircuit.inputs:
                self.currentCircuit.gates[name].val = val
                print("Set " + name + " to " + str(val) + ".")
            else:
                print("Cannot set gate.")
        else:
            print("No circuit open.")

    def fire(self):
        """
        Fire the current circuit.
        """
        if self.currentCircuitName != "":
            print("Fired circuit.")
            self.currentCircuit.fire()
        else:
            print("No circuit open.")

    def draw(self):
        """
        Draw the current circuit.
        """
        self.currentCircuit.drawCircuit()
