import os

import pytest

from src.decorators import log


def test_log(capsys: pytest.CaptureFixture) -> None:
    """Тест декоратора log с выводом в консоль"""

    @log()
    def func(x, y):
        return x + y

    func(1, 2)
    captured = capsys.readouterr()
    assert "func ok\n" == captured.out


def test_log_file():
    """Тест log file с записью в txt"""

    @log(filename="test_log.txt")
    def func(x, y):
        return x + y

    func(1, 2)
    with open("test_log.txt", "r", encoding="utf-8") as file:
        assert file.readline() == "func ok\n"
    os.remove("test_log.txt")


def test_logs_errors(capsys: pytest.CaptureFixture) -> None:
    """Тест log при исключении, например: переменная не == 0"""

    @log()
    def func(x, y):
        if x == 0 or y == 0:
            raise ValueError("Переменная не должна быть равна нулю")
        return x + y

    with pytest.raises(ValueError):
        func(0, 2)
    captured = capsys.readouterr()
    assert "func error: ValueError: Переменная не должна быть равна нулю. Inputs: (0, 2), {}\n" == captured.out
