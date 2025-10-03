from turtle import Screen

import Learn
print(Learn.vishal)

import turtle
x = turtle.Turtle()
print(x)
x.shape("turtle")
x.color("Darkorchid2")
x.forward(100)
x.circle(10)

y = Screen()
print(y.canvheight)
print(y.exitonclick())

from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])
print(x[0])

table = PrettyTable()
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)

table.add_column("City name",
["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
1554769])
table.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
869.4])

# print(table)

x = PrettyTable()
x.field_names = ["PokemonName","Type"]
rows_to_add = [
    ['Pikachu', 'Electric'],
    ['Charmander', 'Fire'],
    ['Bulbasaur', 'Grass']
]
x.add_rows(rows_to_add)
x._rows[0][1] = 'vishal'
print(x)

