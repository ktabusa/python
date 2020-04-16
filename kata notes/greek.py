# test of greek alphabet kata

greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')


def greek_comparator(lhs, rhs):
    if greek_alphabet.index(lhs) > greek_alphabet.index(rhs):
        return print('result should be positive')
    elif greek_alphabet.index(lhs) < greek_alphabet.index(rhs):
        return print('result should be negative')
    else:
        return 0


greek_comparator('alpha', 'beta')
greek_comparator('psi', 'psi')
greek_comparator('upsilon', 'rho')
