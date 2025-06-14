from pathlib import Path

from typer.testing import CliRunner

from pdf_merger import cli

runner = CliRunner()


def test_non_existant_folder_exits_with_message(tmp_path: Path) -> None:
    result = runner.invoke(cli, [(tmp_path / "i-dont-exist").as_posix()])
    assert result.exit_code == 0
    assert f"Folder {(tmp_path / 'i-dont-exist').as_uri()} does not exist." in result.stdout


def test_no_files_exits_with_message(tmp_path: Path) -> None:
    result = runner.invoke(cli, [tmp_path.as_posix()])
    assert result.exit_code == 0
    assert f"No PDFs found in {tmp_path.as_uri()}." in result.stdout
