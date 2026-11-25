from dataclasses import dataclass, asdict
import json


@dataclass(frozen=True, slots=True)
class Livre:
    titre: str
    auteur: str
    annee: int
    prix: float

    def to_json(self) -> str:
        """Sérialise le livre en chaîne JSON."""
        return json.dumps(asdict(self), ensure_ascii=False)

    # Extension 1 : promo immuable
    def promo(self, prix_reduit: float) -> "Livre":
        """Retourne un NOUVEAU Livre avec le prix modifié.
        L'objet original (frozen) reste inchangé."""
        return Livre(self.titre, self.auteur, self.annee, prix_reduit)

    # Extension 2 : chargement depuis JSON
    @classmethod
    def from_json(cls, chaine: str) -> "Livre":
        """Reconstruit un Livre depuis une chaîne JSON."""
        data = json.loads(chaine)
        return cls(
            titre=data["titre"],
            auteur=data["auteur"],
            annee=data["annee"],
            prix=data["prix"],
        )

    # Extension 3 : comparaison par prix (ordre croissant)
    def __lt__(self, autre: "Livre") -> bool:
        if not isinstance(autre, Livre):
            return NotImplemented
        return self.prix < autre.prix


# --- Démonstration ---
if __name__ == "__main__":
    livre = Livre("1984", "George Orwell", 1949, 9.90)
    print("JSON initial :", livre.to_json())
    # {"titre": "1984", "auteur": "George Orwell", "annee": 1949, "prix": 9.9}

    # Extension 1 : promo
    livre_promo = livre.promo(7.90)
    print("Original  :", livre.prix)         # 9.9
    print("Promo     :", livre_promo.prix)   # 7.9
    assert livre.prix == 9.90, "L'original ne doit pas changer"

    # Extension 2 : from_json
    livre_recharge = Livre.from_json(livre.to_json())
    print("Rechargé  :", livre_recharge)
    assert livre_recharge == livre

    # Extension 3 : tri par prix
    autres = [
        Livre("Le Petit Prince", "Saint-Exupéry", 1943, 6.50),
        Livre("Dune", "Frank Herbert", 1965, 12.00),
        livre,
    ]
    print("\nTriés par prix croissant :")
    for l in sorted(autres):
        print(f"  {l.prix:>5.2f} € - {l.titre}")