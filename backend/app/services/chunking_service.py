
from dataclasses import dataclass


@dataclass
class TextChunk:
    text: str
    chunk_index: int
    page_number: int


def chunk_pdf_pages(
    pages: list[dict],
    chunk_size: int = 1000,
    overlap: int = 150,
) -> list[TextChunk]:
    """
    Découpe le texte des pages PDF en passages avec chevauchement.

    chunk_size : nombre approximatif de caractères par passage.
    overlap : nombre de caractères répétés entre deux passages.
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size doit être supérieur à zéro.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError(
            "overlap doit être positif et inférieur à chunk_size."
        )

    chunks: list[TextChunk] = []
    chunk_index = 0
    step = chunk_size - overlap

    for page in pages:
        page_number = int(page["page_number"])
        text = page["text"].strip()

        if not text:
            continue

        start = 0

        while start < len(text):
            end = min(start + chunk_size, len(text))
            piece = text[start:end].strip()

            if piece:
                chunks.append(
                    TextChunk(
                        text=piece,
                        chunk_index=chunk_index,
                        page_number=page_number,
                    )
                )
                chunk_index += 1

            if end == len(text):
                break

            start += step

    return chunks
