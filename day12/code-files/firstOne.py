from turtle import Turtle, Screen
from prettytable import PrettyTable

timmy = Turtle()
# my_screen = Screen()

# creating object from external library
table = PrettyTable()
# table.field_names = ["field1", "field2", "field3", "field4", ]
#
# table.add_row(["row1col1", "row1col2", "row1col3", "row1col4", ])
# table.add_row(["row2col1", "row2col2", "row2col3", "row3col4", ])
# table.add_row(["row3col1", "row3col2", "row3col3", "row3col4", ])
#

table.add_column("somedummytitlecol1", ["row1col1", "somedummyrow2col1", "row3col1"])
table.add_column("titlecol2", ["row1col2", "row2col2", "row3col2somedummy"])
table.add_column("titlecol3somedummy", ["somedummyrow1col3", "row2col3", "row3col3"])

# table.align["somedummytitlecol1"] = "l"
# table.align["titlecol3somedummy"] = "r"

table.align = "l"

print(table)

# my_screen.exitonclick()
