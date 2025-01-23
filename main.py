import random

def monty_hall_simulation(num_simulations: int, num_doors: int = 3):
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

    # Risultati finali
    print(f"Numero di simulazioni: {num_simulations}\n")
    print(f"Vittorie mantenendo la scelta iniziale: {stay_wins} ({(stay_wins / num_simulations) * 100:.2f}%)")
    print(f"Sconfitte mantenendo la scelta iniziale: {stay_loses} ({(stay_loses / num_simulations) * 100:.2f}%)\n")
    print(f"Vittorie cambiando la scelta iniziale: {switch_wins} ({(switch_wins / num_simulations) * 100:.2f}%)")
    print(f"Sconfitte cambiando la scelta iniziale: {switch_loses} ({(switch_loses / num_simulations) * 100:.2f}%)")

monty_hall_simulation(100000, 4)