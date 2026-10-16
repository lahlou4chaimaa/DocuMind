
import fitz
import pytest

from backend.app.services.pdf_service import (
    PDFExtractionError,
    extract_pdf_text,
)


def test_extract_pdf_text(tmp_path):
    pdf_path = tmp_path / "facture_test.pdf"

    document = fitz.open()
    page = document.new_page()
    page.insert_text(
        (72, 72),
        "Facture numero FAC-2026-001",
    )
    document.save(pdf_path)
    document.close()

    result = extract_pdf_text(pdf_path)

    assert result["filename"] == "facture_test.pdf"
    assert result["page_count"] == 1
    assert "FAC-2026-001" in result["full_text"]
    assert result["pages"][0]["page_number"] == 1


def test_missing_pdf_raises_error(tmp_path):
    missing_path = tmp_path / "inexistant.pdf"

    with pytest.raises(PDFExtractionError):
        extract_pdf_text(missing_path)


def test_non_pdf_file_raises_error(tmp_path):
    text_path = tmp_path / "document.txt"
    text_path.write_text("Test", encoding="utf-8")

    with pytest.raises(PDFExtractionError):
        extract_pdf_text(text_path)
