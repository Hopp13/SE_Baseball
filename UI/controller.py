import flet as ft
from model.team import Team

from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        self._view.dd_squadra.options.clear()

        self._model.crea_grafo(int(self._view.dd_anno.value))
        teams = self._model.get_squadre_anno(int(self._view.dd_anno.value))

        for team in teams:
            self._view.dd_squadra.options.append(ft.DropdownOption(text = f"{team.team_code} ({team.name})", key = team.id))

        self._view.update()

    def handle_dettagli(self, e):
        self._view.txt_risultato.controls.clear()

        neighbors = self._model.get_neighbors(int(self._view.dd_squadra.value))
        for neighbor in neighbors:
            edges = self._model.get_edges()
            for edge in edges:
                if edge[0] == neighbor or edge[1] == neighbor:
                    peso = edge[2]["weight"]
            teams = self._model.get_squadre_anno(int(self._view.dd_anno.value))
            for team in teams:
                if team.id == neighbor:
                    actual_team = team
                    break
            self._view.txt_risultato.controls.append(ft.Text(f"{actual_team.team_code} ({actual_team.name}) - peso: {peso}"))

        self._view.update()

    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        # TODO

    def populate_dd_anno(self):
        years = self._model.get_years()
        for year in years:
            self._view.dd_anno.options.append(ft.DropdownOption(year))
        self._view.update()

    def handle_squadre(self, e):
        self._view.txt_out_squadre.controls.clear()

        teams = self._model.get_squadre_anno(int(self._view.dd_anno.value))

        self._view.txt_out_squadre.controls.append(ft.Text(f"Numero squadre: {str(len(teams))}"))
        for team in teams:
            self._view.txt_out_squadre.controls.append(ft.Text(f"{team.team_code} ({team.name})"))

        self._view.update()