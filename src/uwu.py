import random, re

faces = list(set(open("./src/faces.txt", encoding='utf-8').read().split()))

def stutter(s: str) -> str:
    ix = random.randint(1, len(s))
    return s[:ix] + '-' + s[ix:]

def uwu(s: str, S: float = 0.1, F: float = 0.1) -> str:
    '''
        1: l | r => w
        2: th => d
        3: stutter with probability S
        4: add face after a word with probability F
    '''
    # replace l, r with w and th with d
    x = re.sub(r"th","d",re.sub(r"l|r","w",s.lower()))
    # add stutter
    x = map(lambda s: stutter(s) if random.random() < S else s, x.split())
    # add faces
    x = map(lambda s: s + ' ' + random.choice(faces) if random.random() < F else s, list(x))

    return ' '.join(x)