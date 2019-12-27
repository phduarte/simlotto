from lotto import generate_sena, generate_quina, simulate_sena

print("+-- SENA --------------+")
for i in generate_sena(10):
    """test for Mega Sena"""
    print(i)

print("+-- QUINA -------------+")
for i in generate_quina(10):
    """test for Quina"""
    print(i)

print("+-- SIMULATOR ---------+")

result_game1 = simulate_sena(1,2,3,4,5,6)
print(result_game1)
result_game2 = simulate_sena(22,24,32,50,51,58)
print(result_game2)
result_game3 = simulate_sena(21,23,31,49,50,57)
print(result_game3)
result_game4 = simulate_sena(1,2,3,4,5,6)
print(result_game4)