"""Harbor 0.13.x writes ``"step_results": null`` for single-step tasks."""

from skillevaluator.tier3.harbor.collector import _constituent_default_reward_failure


def _result(step_results):
    return {"verifier_result": {"rewards": {"overall": 1.0}}, "step_results": step_results}


def test_null_step_results_is_not_malformed() -> None:
    assert _constituent_default_reward_failure(_result(None)) == ""


def test_non_list_step_results_is_still_malformed() -> None:
    assert "malformed" in _constituent_default_reward_failure(_result({"bad": 1}))


def test_absent_step_results_is_fine() -> None:
    assert _constituent_default_reward_failure({"verifier_result": {"rewards": {"overall": 1.0}}}) == ""
