from model.LogicSimulator import LogicSimulator

logicSim = LogicSimulator()

"""
Command line processing.
"""
while 1:
    user_input = input()
    user_input = user_input.strip()

    if user_input.lower()[:7] == "connect" and " to " in user_input.lower():
        name1 = user_input[8:user_input.index(" to ")]
        name2 = user_input[user_input.index(" to ") + 4:]
        logicSim.connect(name1, name2)

    if user_input.lower()[:10] == "disconnect" and " from " in user_input.lower():
        name1 = user_input[11:user_input.index(" from ")]
        name2 = user_input[user_input.index(" from ") + 6:]
        logicSim.disconnect(name1, name2)

    if user_input.lower()[:6] == "create" and " gate " in user_input.lower():
        type = user_input[7:user_input.index(" gate ")]
        name = user_input[user_input.index(" gate ") + 6:]
        logicSim.create(name, type)

    if user_input.lower()[:15] == "create circuit ":
        name = user_input[15:]
        logicSim.createCircuit(name)

    if user_input.lower()[:12] == "set circuit ":
        name = user_input[12:]
        logicSim.setCircuit(name)

    if user_input.lower()[:7] == "delete ":
        name = user_input[7:]
        logicSim.delete(name)

    if user_input.lower()[:3] == "set" and " to " in user_input.lower():
        name = user_input[4:user_input.index(" to ")]
        val = user_input[user_input.index(" to ") + 4:]
        logicSim.set(name, int(val))

    if user_input.lower()[:6] == "change" and " to " in user_input.lower():
        name = user_input[7:user_input.index(" to ")]
        type = user_input[user_input.index(" to ") + 4:]
        logicSim.change(name, type)

    if user_input.lower()[:12] == "fire circuit":
        name = user_input[12:]
        logicSim.fire()

    if user_input.lower() == "draw circuit":
        logicSim.draw()