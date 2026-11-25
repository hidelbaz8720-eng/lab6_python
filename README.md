
# TP 6 – Dataclasses en Python

## Présentation

Ce TP porte sur les dataclasses en Python dans le cadre de la programmation orientée objet. Il contient deux exercices : la modélisation d'un livre et la modélisation d'un film.

## Exercice 1 : Classe Livre

### Objectifs
- Créer une classe `Livre` avec les attributs :
  - `titre`
  - `auteur`
  - `annee`
  - `prix`
- Utiliser `@dataclass(frozen=True, slots=True)`.
- Rendre les objets immuables.
- Convertir un objet en JSON avec `to_json()`.

### Extensions
- Ajouter une méthode `promo(prix_reduit)`.
- Reconstituer un livre depuis une chaîne JSON.
- Comparer deux livres selon leur prix croissant.

<img width="1920" height="1080" alt="Screenshot 2026-11-25 084812" src="https://github.com/user-attachments/assets/a7db7e73-c821-4045-9437-58422ae4532a" />


## Exercice 2 : Classe Film

### Objectifs
- Créer une classe `Film` avec les attributs :
  - `titre`
  - `realisateur`
  - `annee`
  - `note` (entre 0 et 10)
- Utiliser `@dataclass(frozen=True, slots=True)`.
- Implémenter la méthode `to_json()`.
- Implémenter la méthode `est_classique()` qui retourne `True` si l'année est avant 2000.

### Extensions
- Comparer les films selon leur note.
- Ajouter une méthode `from_json(str)`.
- Gérer une liste de films favoris.
- Sérialiser plusieurs films en JSON.
- Écrire des tests unitaires dans un fichier séparé.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d3a9abbc-1939-40fa-8451-682e5cd02271" />

## Notions étudiées

- Programmation orientée objet (POO).
- Décorateur `@dataclass`.
- Immutabilité avec `frozen=True`.
- Optimisation mémoire avec `slots=True`.
- Sérialisation et désérialisation JSON.
- Comparaison d'objets.
- Tests unitaires avec `unittest`.


## Conclusion

Ce TP permet de maîtriser les dataclasses Python et de comprendre comment créer des objets immuables, les sérialiser en JSON et les comparer.

---
**Technologie :** Python 3  
**Module :** Programmation orientée objet  
**TP :** 6 – Dataclasses
