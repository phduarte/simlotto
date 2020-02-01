from random import randint

def generate(bets, dezenas, numbers):
    ret = []
    for a in range(bets):

        balls = list(range(1,numbers+1))
        drawn = []

        for d in range(dezenas):
            i = randint(0,len(balls)-1)
            drawn.append(balls[i])
            balls.pop(i)

        ret.append(sorted(drawn))

    return ret

def generate_sena(bets = 1):
    return generate(bets, 6, 60)

def generate_quina(bets=1):
    return generate(bets, 5, 80)

def simulate_sena(*numbers):
    bet = generate_sena()
    bet = set(*bet)
    hit = bet.intersection(numbers)

    if not hit:
        return "Bad luck! You didn't hit any."

    if len(hit) == 6:
        return "Congrats! You're the Winner!"
    
    sequence = ', '.join(str(i) for i in hit)

    return f"Congrats! You hit {len(hit)} ball's on sequence {sequence}."
