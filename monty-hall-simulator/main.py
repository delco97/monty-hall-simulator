import random
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class MontyHallSimulationInputs:
    num_simulations: int
    num_doors: int

@dataclass
class MontyHallSimulationOutputs:
    stay_wins: int
    stay_loses: int
    switch_wins: int
    switch_loses: int

@dataclass
class MontyHallSimulation:
    inputs: MontyHallSimulationInputs
    outputs: MontyHallSimulationOutputs

    def __str__(self):
        return (
            f"Numero di porte: {self.inputs.num_doors}; Simulazioni: {self.inputs.num_simulations}\n"
            f"    Vittorie mantenendo la scelta iniziale: {self.outputs.stay_wins} ({(self.outputs.stay_wins / self.inputs.num_simulations) * 100:.2f}%)\n"
            f"    Sconfitte mantenendo la scelta iniziale: {self.outputs.stay_loses} ({(self.outputs.stay_loses / self.inputs.num_simulations) * 100:.2f}%)\n"
            f"    Vittorie cambiando la scelta iniziale: {self.outputs.switch_wins} ({(self.outputs.switch_wins / self.inputs.num_simulations) * 100:.2f}%)\n"
            f"    Sconfitte cambiando la scelta iniziale: {self.outputs.switch_loses} ({(self.outputs.switch_loses / self.inputs.num_simulations) * 100:.2f}%)\n"
        )

def monty_hall_simulation(
        num_simulations: int,
        num_doors: int = 3
) -> MontyHallSimulation:
    stay_wins = 0
    stay_loses = 0
    switch_wins = 0
    switch_loses = 0

    for _ in range(num_simulations):
        # Si posiziona il premio dietro una delle tre porte
        doors = [0] * num_doors
        prize_door = random.randint(0, len(doors) - 1)
        doors[prize_door] = 1

        # Il giocatore sceglie una porta a caso
        player_choice = random.randint(0, len(doors) - 1)

        # Il conduttore apre una porta vuota
        loosing_doors = [
            i for i in range(len(doors))
            if i != player_choice and doors[i] == 0
        ]
        monty_opens = random.choice(loosing_doors)

        # Se giocatore decide di cambiare, ne sceglie una tra le porte rimanenti
        remaining_doors = [
            i for i in range(len(doors))
            if i != player_choice and i != monty_opens
        ]
        switch_door = random.choice(remaining_doors)

        # Verificare il risultato
        if doors[player_choice] == 1:
            stay_wins += 1
        else:
            stay_loses += 1
        if doors[switch_door] == 1:
            switch_wins += 1
        else:
            switch_loses += 1

    return MontyHallSimulation(
        inputs=MontyHallSimulationInputs(
            num_simulations=num_simulations,
            num_doors=num_doors,
        ),
        outputs=MontyHallSimulationOutputs(
            stay_wins=stay_wins,
            stay_loses=stay_loses,
            switch_wins=switch_wins,
            switch_loses=switch_loses,
        )
    )

def plot_simulations(num_simulations: int, doors_start: int, doors_end: int):
    """
    Show a plot built as follows:
    - x axis: number of doors simulated
    - y axis: win percentage by stying and win percentage by switching
    """

    fig, ax = plt.subplots()
    ax.set_xlabel("Doors")
    ax.set_ylabel("% wins")
    ax.set_title("Monty Hall Simulation")
    x_doors = []
    y_stay_win_percentage = []
    y_switch_win_percentage = []
    epsilon = 0.1
    for doors in range(doors_start, doors_end + 1, 1):
        result = monty_hall_simulation(num_simulations=num_simulations, num_doors=doors)
        x_doors.append(doors)
        y_stay_win_percentage.append(result.outputs.stay_wins / result.inputs.num_simulations * 100)
        y_switch_win_percentage.append(result.outputs.switch_wins / result.inputs.num_simulations * 100)

    ax.plot(x_doors, y_stay_win_percentage, label="% wins by staying")
    ax.plot(x_doors, y_switch_win_percentage, label="% wins by switching")
    ax.legend()
    plt.show(block=False)


if __name__ == "__main__":
    plot_simulations(num_simulations=10000, doors_start=3, doors_end=20)
