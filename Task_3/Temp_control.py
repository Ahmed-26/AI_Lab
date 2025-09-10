class MAgent:
    def __init__(self, desired_temp):
        self.desired_temp = desired_temp
        self.previous_actions = {}  

    def perceive(self, room, current_temp):
        return current_temp

    def act(self, room, current_temp):
        prev_action = self.previous_actions.get(room)
        if current_temp < self.desired_temp:
            action = "Turn on heater"
        else:
            action = "Turn off heater"

        if action == prev_action:
            action = f"Keep heater {'on' if action == 'Turn on heater' else 'off'}"
        self.previous_actions[room] = action if "Turn" in action else prev_action
        return action

rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}
desired_temp = 22
agent = MAgent(desired_temp)

for cycle in range(2):
    print(f"\nCycle {cycle+1}:")
    for room, temperature in rooms.items():
        action = agent.act(room, temperature)
        print(f"{room}: Current temperature = {temperature}°C. {action}.")