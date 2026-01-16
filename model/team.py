from dataclasses import dataclass


@dataclass
class Team:
    id : int
    team_code : str
    name : str

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id
