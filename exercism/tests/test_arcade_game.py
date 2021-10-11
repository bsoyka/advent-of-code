from ..arcade_game import eat_ghost, lose, score, win


def test_ghost_gets_eaten():
    assert eat_ghost(True, True) is True


def test_ghost_does_not_get_eaten_because_no_power_pellet_active():
    assert eat_ghost(False, True) is False


def test_ghost_does_not_get_eaten_because_not_touching_ghost():
    assert eat_ghost(True, False) is False


def test_score_when_eating_dot():
    assert score(False, True) is True


def test_score_when_eating_power_pellet():
    assert score(True, False) is True


def test_no_score_when_nothing_eaten():
    assert score(False, False) is False


def test_lose_if_touching_a_ghost_without_a_power_pellet_active():
    assert lose(False, True) is True


def test_dont_lose_if_touching_a_ghost_with_a_power_pellet_active():
    assert lose(True, True) is False


def test_dont_lose_if_not_touching_a_ghost():
    assert lose(True, False) is False


def test_win_if_all_dots_eaten():
    assert win(True, False, False) is True


def test_dont_win_if_all_dots_eaten_but_touching_a_ghost():
    assert win(True, False, True) is False


def test_win_if_all_dots_eaten_and_touching_a_ghost_with_a_power_pellet_active():
    assert win(True, True, True) is True


def test_dont_win_if_not_all_dots_eaten():
    assert win(False, True, True) is False
