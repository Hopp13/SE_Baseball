from database.DB_connect import DBConnect
from model.salary import Salary
from model.team import Team

class DAO:
    @staticmethod
    def read_years():
        conn = DBConnect.get_connection()

        cursor = conn.cursor(dictionary=True)
        query = """SELECT year FROM team"""

        cursor.execute(query)

        minimum_year = 1980
        years = []
        for row in cursor:
            if int(row["year"]) >= minimum_year and int(row["year"]) not in years:
                years.append(int(row["year"]))

        cursor.close()
        conn.close()
        return years

    @staticmethod
    def read_squadre_anno(year):
        conn = DBConnect.get_connection()

        cursor = conn.cursor(dictionary=True)
        query = """SELECT id, team_code, name FROM team WHERE year = %s"""

        cursor.execute(query, (year, ))

        teams = []
        for row in cursor:
            team = Team(int(row["id"]),
                        row["team_code"],
                        row["name"])
            teams.append(team)

        cursor.close()
        conn.close()
        return teams

    @staticmethod
    def read_salary():
        conn = DBConnect.get_connection()

        cursor = conn.cursor(dictionary=True)
        query = """SELECT id, team_id, salary FROM salary"""

        cursor.execute(query)

        salaries = []
        for row in cursor:
            salary = Salary(int(row["id"]),
                            int(row["team_id"]),
                            int(row["salary"]))
            salaries.append(salary)

        cursor.close()
        conn.close()
        return salaries
