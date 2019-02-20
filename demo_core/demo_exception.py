from math import log2


def entropy(probabilities):
    if sum(probabilities) != 1:
        raise ValueError('probabilities must have sum 1')
    if not all(0 <= p <= 1 for p in probabilities):
        raise ValueError('all probabilities must be between 0 and 1')

    return -sum(p*log2(p) for p in probabilities if p != 0)


assert entropy([0.25]*4) == 2

while True:
    try:
        p = float(input('enter the probability:'))
        q = 1-p
        entr = entropy([p, q])
    except ValueError as e:
        print('invalid input ('+str(e)+')')
    else:
        break

print(f'entropy of {p}: {entr}')
