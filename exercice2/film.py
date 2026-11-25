from dataclasses import dataclass
from functools import total_ordering
import json


@total_ordering
@dataclass(frozen=True, slots=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float

    def __post_init__(self):
        if not isinstance(self.titre, str) or not self.titre.strip():
            raise ValueError("Le titre doit être une chaîne non vide.")

        if not isinstance(self.realisateur, str) or not self.realisateur.strip():
            raise ValueError("Le réalisateur doit être une chaîne non vide.")

        if isinstance(self.annee, bool) or not isinstance(self.annee, int):
            raise TypeError("L'année doit être un entier.")

        if isinstance(self.note, bool) or not isinstance(self.note, (int, float)):
            raise TypeError("La note doit être numérique.")

        if not 0 <= self.note <= 10:
            raise ValueError("La note doit être comprise entre 0 et 10.")

    def est_classique(self):
        return self.annee < 2000

    def to_json(self):
        return json.dumps({
            "titre": self.titre,
            "realisateur": self.realisateur,
            "annee": self.annee,
            "note": self.note
        }, ensure_ascii=False)

    @classmethod
    def from_json(cls, chaine):
        donnees = json.loads(chaine)

        if not isinstance(donnees, dict):
            raise ValueError("Le JSON doit contenir un objet.")

        champs = {"titre", "realisateur", "annee", "note"}

        if set(donnees.keys()) != champs:
            raise ValueError("Les champs JSON sont invalides.")

        return cls(**donnees)

    def __lt__(self, autre):
        if not isinstance(autre, Film):
            return NotImplemented
        return self.note < autre.note   