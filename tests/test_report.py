import pytest

from dominions_watchdog import turn_report 


@pytest.fixture
def test_log_string():
    return "(Er) (Ul) Mav+ Sa- Ca- Ct+ Ni+ Ka+ (Rl)"


@pytest.fixture
def malformed_log_string():
    return "(Er) (Ul) Mav= Sa- Ca- Ct+ Ni+ Ka+ (Rl)"


def test_normal_log_string_parsed(test_log_string):
    report = turn_report.Dominions5TurnReport.from_log_string(test_log_string)
    
    assert "Ermor" in report.ai_turns
    assert "Marverni" in report.turns_done
    assert "Sauromatia" in report.turns_pending


def test_malformed_log_string_raises(malformed_log_string):
    with pytest.raises(RuntimeError):
        report = turn_report.Dominions5TurnReport.from_log_string(malformed_log_string)
