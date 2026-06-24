from logic_utils import check_guess, parse_guess, update_score


def test_check_guess_win():
    outcome, msg = check_guess(50, 50)
    assert outcome == "Win"


def test_check_guess_too_high():
    outcome, msg = check_guess(60, 50)
    assert outcome == "Too High"


def test_check_guess_too_low():
    outcome, msg = check_guess(40, 50)
    assert outcome == "Too Low"


def test_parse_guess_valid():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42


def test_parse_guess_invalid():
    ok, value, err = parse_guess("abc")
    assert ok is False


def test_update_score_win():
    score = update_score(0, "Win", 3)
    assert score > 0