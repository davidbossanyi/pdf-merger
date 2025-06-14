from pathlib import Path
from typing import Annotated

import typer
from pypdf import PdfWriter

cli = typer.Typer(pretty_exceptions_show_locals=False)


@cli.command(name="merge", help="Merge PDFs into a single document")
def merge_pdfs(
    folder: Annotated[str, typer.Argument(..., help="Folder containing PDFs to merge", show_default=False)],
    output: Annotated[str, typer.Option("--output", "-o", help="Output filename")] = "merged.pdf",
) -> None:
    pdf_folder = Path(folder).absolute()
    if not pdf_folder.exists():
        typer.secho(f"Folder {pdf_folder.as_uri()} does not exist.", fg="red")
        raise typer.Exit()
    pdf_files = list(pdf_folder.glob("*.pdf"))
    if not pdf_files:
        typer.secho(f"No PDFs found in {pdf_folder.as_uri()}.", fg="red")
        raise typer.Exit()
    output = output + ".pdf" if not output.endswith(".pdf") else output
    output_file = pdf_folder / output
    writer = PdfWriter()
    for pdf in sorted(pdf_files):
        writer.append(pdf)
    writer.write(output_file)
    writer.close()
    typer.secho(f"Merged {len(pdf_files)} PDFs to {output_file.as_uri()}.", fg="green")
