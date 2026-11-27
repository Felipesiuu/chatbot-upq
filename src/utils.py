"""Funciones compartidas entre el notebook y app.py.

La limpieza debe ser EXACTAMENTE la misma al entrenar y al predecir,
por eso vive en este archivo y no copiada en dos lugares.
"""
import re
import unicodedata


def limpiar_texto(texto: str) -> str:
    """Pasa a minúsculas, quita acentos y signos, y deja un solo espacio entre palabras.

    Ejemplo: "¿Cuánto CUESTA la inscripción?" -> "cuanto cuesta la inscripcion"
    """
    texto = str(texto).lower()
    # Separa letras y acentos (á -> a + ´) y luego elimina los acentos
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    # Todo lo que no sea letra, número o espacio se vuelve espacio
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    # Varios espacios seguidos se vuelven uno
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto


    