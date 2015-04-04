import re

def is_reversion(comment):
    '''
    Parse a comment, and determine whether it is a reversion.
    '''


ACCOUNT = re.compile('^.*|([^\]]+)\]\]')
def account(comment):
    '''
    Determine the account whose edits were reverted.
    '''
    candidates = re.findall(r'\|([^ \]]+)\]', comment)
    if len(candidates) > 0:
        b = candidates[0]
    else:
        b = None
    return None, b
