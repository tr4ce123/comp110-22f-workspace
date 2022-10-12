"""Testing the dictionary functions for correct functionality."""

__author__ = "730567386"

from dictionary import invert


def test_invert() -> None:
    """Test."""
    initial_dict: dict[str, str] = {"h": "i", "j": "k"}
    assert invert(initial_dict) == {"i": "h", "k": "j"}