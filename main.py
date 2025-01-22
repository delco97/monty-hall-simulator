import random

def monty_hall_simulation(num_simulations: int, num_doors: int = 3):
    stay_wins = 0
    switch_wins = 0

    for _ in range(num_simulations):
        # Si posiziona il premio dietro una delle tre porte
        doors = [0] * num_doors
        prize_door = random.randint(0, 2)
        doors[prize_door] = 1

        # Il giocatore sceglie una porta a caso
        player_choice = random.randint(0, 2)

        # Il conduttore apre una porta vuota
        loosing_doors = [
            i for i in range(len(doors))
            if i != player_choice and doors[i] == 0
        ]
        monty_opens = random.choice(loosing_doors)

        # Se giocatore decide di cambiare, ne scegli una tra le porte rimanenti
        remaining_doors = [
            i for i in range(len(doors))
            if i != player_choice and i != monty_opens
        ]
        switch_door = random.choice(remaining_doors)

        # Verificare il risultato
        if doors[player_choice] == 1:
            stay_wins += 1  # Vincita mantenendo la scelta iniziale
        elif doors[switch_door] == 1:
            switch_wins += 1  # Vincita cambiando scelta

    # Risultati finali
    print(f"Numero di simulazioni: {num_simulations}")
    print(f"Vittorie mantenendo la scelta iniziale: {stay_wins} ({stay_wins / num_simulations:.2%})")
    print(f"Vittorie cambiando scelta: {switch_wins} ({switch_wins / num_simulations:.2%})")

monty_hall_simulation(10000, 4)