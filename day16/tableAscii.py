from table2ascii import table2ascii,PresetStyle



pokeTable = table2ascii(
    header=["Pokemon_Name","Type"],
    body=[["pikachu","electric"],["charmander","fire"]],
    style=PresetStyle.ascii_box
)
print()
print(
    pokeTable
)