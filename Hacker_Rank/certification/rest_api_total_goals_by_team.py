import requests

def retrieve_goals(data, team_text):
    goals = 0
    for d in data:
        goals += int(d[team_text])
    return goals

def get_team_goals(team, year, team_type, team_text):
    team_goals = 0
    base_url = f"https://jsonmock.hackerrank.com/api/football_matches?"
    url = base_url + f"year={year}&{team_type}={team}&page=1"
    res = requests.get(url)
    json_res = res.json()
    total_pages = json_res["total_pages"]
    if total_pages == 1:
        data = json_res["data"]
        team_goals = retrieve_goals(data, team_text)
    else:
        for page in range(1,total_pages+1):
            new_url = base_url + f"year={year}&{team_type}={team}&page={page}"
            res = requests.get(new_url)
            json_res = res.json()
            data = json_res["data"]
            goals = retrieve_goals(data, team_text)
            team_goals += goals
    return team_goals

def getTotalGoals(team, year):
    # Write your code here
    team1_goals = get_team_goals(team, year, "team1", "team1goals")
    team2_goals = get_team_goals(team, year, "team2", "team2goals")
    total_goals = team1_goals + team2_goals
    return total_goals


if __name__ == '__main__':

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)

    print(result)