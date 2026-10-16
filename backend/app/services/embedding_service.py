
import ollama


class EmbeddingServiceError(Exception):
    """Erreur lors de la génération des embeddings."""


class EmbeddingService:
    def __init__(
        self,
        model: str = "nomic-embed-text",
    ) -> None:
        self.model = model

    def embed_text(self, text: str) -> list[float]:
        """
        Transforme un texte en vecteur numérique avec Ollama.
        Le modèle doit être installé et le serveur Ollama démarré.
        """
        if not text or not text.strip():
            raise ValueError("Le texte à vectoriser est vide.")

        try:
            response = ollama.embed(
                model=self.model,
                input=text,
            )

            embeddings = response["embeddings"]

            if not embeddings or not embeddings[0]:
                raise EmbeddingServiceError(
                    "Ollama a retourné un embedding vide."
                )

            return embeddings[0]

        except EmbeddingServiceError:
            raise
        except Exception as exc:
            raise EmbeddingServiceError(
                "Impossible de générer l'embedding. "
                "Vérifie qu'Ollama fonctionne et que le modèle "
                "est installé."
            ) from exc
