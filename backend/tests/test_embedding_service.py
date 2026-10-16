
import pytest

from backend.app.services.embedding_service import (
    EmbeddingService,
    EmbeddingServiceError,
)


def test_empty_text_is_rejected():
    service = EmbeddingService()

    with pytest.raises(ValueError):
        service.embed_text("")


def test_whitespace_text_is_rejected():
    service = EmbeddingService()

    with pytest.raises(ValueError):
        service.embed_text("   ")


def test_ollama_failure_is_reported(monkeypatch):
    service = EmbeddingService()

    def fake_embed(**kwargs):
        raise RuntimeError("Ollama indisponible")

    monkeypatch.setattr(
        "backend.app.services.embedding_service.ollama.embed",
        fake_embed,
    )

    with pytest.raises(EmbeddingServiceError):
        service.embed_text("Contenu d'une facture")
