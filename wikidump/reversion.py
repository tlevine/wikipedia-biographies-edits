import re

def is_reversion(comment):
    '''
    Parse a comment, and determine whether it is a reversion.
    '''


def account(comment):
    '''
    Determine the account whose edits were reverted.
    '''
    a = b = None
    candidates = re.findall(r'\|([^ \]]+)\]', comment)
    if len(candidates) > 0:
        b = candidates[0]
    else:
        candidates = re.findall(r'by ([0-9.]+)', comment)
        if len(candidates) > 0:
            b = candidates[0]
    return a, b
