#16-02-2026 | 19-02-2026

''' given:   name of the teams with their number of wins, losses, overtime win, overtime losses
    problem: find the qualifying team (first 4 teams) and genereate semifinal match pairs accordign to their ranking.
    rule:    "W" is the number of wins in regulation, worth 3 points each
             "OTW" is the number of overtime wins, worth 2 points each
             "OTL" is the number of overtime losses, worth 1 point each
             "L" is the number of losses, worth 0 points each
    return:  "The semi-final games will be (1st) vs (4th) and (2nd) vs (3rd)."
    example: get_semifinal_matchups(["CAN: 2-2-0-1", "FIN: 2-2-1-0", "GER: 1-0-1-3", "SUI: 0-1-3-1", "SWE: 1-1-2-1", "USA: 2-1-0-2"])
             should return "The semi-final games will be FIN vs SWE and CAN vs USA.".   '''

def get_semifinal_matchups(teams):
    team_scores = []
    for i in range(len(teams)):
        team_name, records = map(str,teams[i].split(":"))
        w, otw, otl, l = map(int,records.split("-"))
        total_scores = (w * 3) + (otw *2) + otl
        team_scores.append(f"{team_name}={total_scores}")
    
    team_scores.sort(key=lambda x: int(x.split("=")[1]), reverse=True)

    team_names = []
    for i in range(len(team_scores)):
        team = team_scores[i].split("=")[0]
        team_names.append(team)
    return f"The semi-final games will be {team_names[0]} vs {team_names[3]} and {team_names[1]} vs {team_names[2]}."

    
