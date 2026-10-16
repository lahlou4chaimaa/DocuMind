
from pathlib import Path

import pymupdf


class PDFExtractionError(Exception):
    """Erreur lors de l'extraction du texte d'un PDF."""


def extract_pdf_text(file_path: str | Path) -> dict:
    path = Path(file_path)

    if not path.exists() or not path.is_file():
        raise PDFExtractionError("Le fichier PDF est introuvable.")

    if path.suffix.lower() != ".pdf":
        raise PDFExtractionError("Le fichier fourni n'est pas un PDF.")

    try:
        pages = []

        with pymupdf.open(path) as document:
            if document.is_encrypted:
                raise PDFExtractionError(
                    "Le PDF est protégé par un mot de passe."
                )

            for number, page in enumerate(document, start=1):
                pages.append({
                    "page_number": number,
                    "text": page.get_text("text").strip(),
                })

        full_text = "\n\n".join(
            f"[Page {page['page_number']}]\n{page['text']}"
            for page in pages
            if page["text"]
        )

        return {
            "filename": path.name,
            "page_count": len(pages),
            "pages": pages,
            "full_text": full_text,
        }

    except PDFExtractionError:
        raise
    except Exception as exc:
        raise PDFExtractionError(
            "Impossible de lire ce PDF."
        ) from exc
