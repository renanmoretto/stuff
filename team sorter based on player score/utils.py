import random

def sort_teams(
    players: dict[str, int],
    number_of_teams: int,
    team_size: int,
    margin: float = 0.05,
) -> list[str]:
    if len(players) < number_of_teams*team_size:
        raise ValueError(
            'number of players must be bigger than number_of_teams*team_size. '
            f'expected {number_of_teams*team_size} or more players, got {len(players)}'
        )

    tries = 0
    while True:
        available_players = players.copy()
        teams, scores = [], []
        for _ in range(1, number_of_teams+1):
            selected_players_names = random.sample(list(available_players.keys()), team_size)
            selected_players_scores = [players.get(name, 0) for name in selected_players_names]

            teams.append(selected_players_names)
            scores.append(sum(selected_players_scores))
            
            for p in selected_players_names:
                available_players.pop(p)

        tries += 1
        if (max(scores)/min(scores) - 1) < margin:
            break
    return teams