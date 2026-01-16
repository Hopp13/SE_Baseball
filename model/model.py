from database.dao import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.dao = DAO
        self.G = nx.Graph()

    def get_years(self):
        return self.dao.read_years()

    def get_squadre_anno(self, year):
        return self.dao.read_squadre_anno(year)

    def crea_grafo(self, year):
        self.G.clear()

        salaries = self.dao.read_salary()
        teams = self.dao.read_squadre_anno(year)

        teams_weights = dict()
        for team in teams:
            team_weight = 0
            for salary in salaries:
                if salary.team_id == team.id:
                    team_weight += salary.salary
            teams_weights[team.id] = team_weight

        for team1 in teams:
            for team2 in teams:
                self.G.add_edge(team1.id, team2.id, weight = teams_weights[team1.id] + teams_weights[team2.id])

    def get_neighbors(self, team):
        return self.G.neighbors(team)

    def get_edges(self):
        return list(self.G.edges(data=True))
