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

        teams = self.dao.read_squadre_anno(year)
        salaries = self.dao.read_salary()

        for team1 in teams:
            for team2 in teams:
                team1_salary = 0
                team2_salary = 0

                for salary in salaries:
                    if salary.team_id == team1.id:
                        team1_salary += salary.salary
                    elif salary.team_id == team2.id:
                        team2_salary += salary.salary

                self.G.add_edge(team1, team2, weight = team1_salary + team2_salary)

    def get_neighbors(self, team):
        return self.G.neighbors(team)

    def get_edges(self):
        return list(self.G.edges(data=True))
