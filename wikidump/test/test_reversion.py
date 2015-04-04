import pytest

from ..reversion import account

ACCOUNT_TEST_CASES = [
    (None, '189.141.247.145', 'Reverting possible vandalism by [[Special:Contributions/189.141.247.145|189.141.247.145]] to version by 62.237.63.251. False positive? [[User:ClueBot/FalsePositives|Report it]]. Thanks, [[User:ClueBot|ClueBot]]. (674366) (Bot)'),
    (None, 'Bof-mo-bot', 'Reverted edits by [[Special:Contributions/Bof-mo-bot|Bof-mo-bot]] ([[User talk:Bof-mo-bot|talk]]) to last version by ClueBot'),
    (None, None, 'revert non encyclopedic content referenced to primary source'),
    ('522511957', None, 'Reverted to revision 522511957 by Katharineamy: vandalism. ([[WP:TW|TW]])'),
    (None, '82.43.7.206', 'Reverted edits by 82.43.7.206 identified as vandalism ([[WP:HG|HG 3]])'),
    (None, '86.42.138.172', 'Reverted edits by [[Special:Contributions/86.42.138.172|86.42.138.172]] ([[User talk:86.42.138.172|talk]]) to last version by SchfiftyThree'),
    (None, 'Jasoneverett2@msn.com', 'Reverted [[WP:AGF|good faith]] edits by [[Special:Contributions/Jasoneverett2@msn.com|Jasoneverett2@msn.com]] ([[User talk:Jasoneverett2@msn.com|talk]]): Revert unreferenced promotional sounding edit. ([[WP:TW|TW]])'),
]

@pytest.mark.parametrize('expected_revision, expected_account, comment', ACCOUNT_TEST_CASES)
def test_account(expected_revision, expected_account, comment):
    assert (expected_revision, expected_account) == account(comment)
