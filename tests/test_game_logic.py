import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_update_score_win():
    # Test scoring for a win on the first attempt
    points = update_score(0, "Win", 1)
    assert points == 80  # 100 - 10*(1+1) = 80
    # Wait, in code, attempt_number is st.session_state.attempts, which is incremented to 1 for first guess.
    # 100 - 10*(1 + 1) = 80
    # But let's check the code.

# In the code: points = 100 - 10 * (attempt_number + 1)
# For attempt_number=1 (first guess), 100 - 10*2 = 80
# For attempt_number=6 (last), 100 - 10*7 = 30, but min 10.

# But in the test, for attempt_number=1, 80.

# But perhaps adjust.

# Also, test for not win.

def test_update_score_lose():
    points = update_score(0, "Too High", 1)
    assert points == 0

def test_update_score_win_last_attempt():
    # For hard, limit=5, attempt_number=5, points = 100 - 10*(5+1)=40, >10
    points = update_score(0, "Win", 5)
    assert points == 40

def test_update_score_win_min_score():
    # If attempt_number is high, say 10, 100 - 10*11 = 0, but min 10
    points = update_score(0, "Win", 9)  # 100 - 10*10 = 0, min 10
    assert points == 10

def test_parse_guess_valid():
    ok, guess, err = parse_guess("50")
    assert ok == True
    assert guess == 50
    assert err is None

def test_parse_guess_invalid():
    ok, guess, err = parse_guess("abc")
    assert ok == False
    assert guess is None
    assert err == "That is not a number."

def test_parse_guess_empty():
    ok, guess, err = parse_guess("")
    assert ok == False
    assert guess is None
    assert err == "Enter a guess."
