from externals import *


## Math Ops
@njit
def opNorm(A):
    G = A[:2].T[:2].T
    return np.sqrt(np.max(np.linalg.eig(G @ G.T)[0]))

def check_transformations(transformations, mode=''):
    if transformations is None:
        raise ValueError('ifsFractals: transformations cannot be NoneType.')
    failed = []
    for i in np.arange(len(transformations)):
        if opNorm(transformations[i]) >= 1:
            failed = failed + [i+1]
    if len(failed) == 0:
        if mode == 'pretty':
            print(colored('The opNorm of every transformation is less than 1 so all of the transformations are contraction mappings.','green'))
        elif mode == 'quiet':
            return True
        else:
            return 'The opNorm of every transformation is less than 1 so all of the transformations are contraction mappings.'
    elif len(failed) == 1:
        if mode == 'pretty':
            print(colored(f'The opNorm of transformation {failed[0]} is greater than or equal to 1 so is not a contraction mapping.','red'))
        elif mode == 'quiet':
            return False
        else:
            return f'The opNorm of transformation {failed[0]} is greater than or equal to 1 so is not a contraction mapping.'
    elif len(failed) > 1:
        if mode == 'pretty':
            print(colored(f'The opNorm of transformations {failed} are greater than or equal to 1 so are not contraction mappings.','red'))
        elif mode == 'quiet':
            return False
        else:
            return f'The opNorm of transformations {failed} are greater than or equal to 1 so are not contraction mappings.'

@njit
def choose_random_index(weights):
    r = rd.uniform(0, 1)
    t = 0
    sum = weights[0]
    while r > sum:
        t += 1
        sum = sum + weights[t]
    return min(t, len(weights)-1)

@njit
def make_eq_weights(n):
    return np.array([1/n]*n)
