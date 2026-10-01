from prettytable import PrettyTable


table = PrettyTable(["Id", "Name"])
table.add_rows([[1, "Chair"], [2, "Hat"]], divider=True)
print(table)
