from click.testing import CliRunner

from .main import main

runner = CliRunner()


def test_app():
    result = runner.invoke(main, ["Camila", "--city", "Berlin"])
    assert result.exit_code == 0
    assert "Hello Camila" in result.stdout
    assert "Let's have a coffee in Berlin" in result.stdout

def test_help():
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "--city" in result.stdout
