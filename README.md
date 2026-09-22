# Théorème C — Classification des premiers non-ordinaires universels

Famille : $\mathcal C_\sigma : y^2 = x^7 + \sigma x + 1$ (genre 3), matrice de Cartier–Manin $M_p(\sigma)$.

**Énoncé.** $\det M_p(\sigma) \equiv 0$ dans $\mathbf F_p[\sigma]$ ssi $p \in \{3, 7, 11, 23\}$.

## Contenu

- `theoreme_C.tex` / `theoreme_C.pdf` — énoncé, méthodologie, démonstration complète (3 étapes : structurel / asymptotique universel / raccord fini).
- `scripts/verification_theoreme_C.py` — certificat de calcul indépendant, brute force, arithmétique exacte.
- `sorties/verification_p_jusqua_157.txt` — sortie de référence du script ci-dessus.

## Reproduire

```bash
python3 scripts/verification_theoreme_C.py
```

Aucune dépendance externe (Python 3 standard uniquement — listes d'entiers pour les polynômes, pas de `sympy`, pas de `sage`). Durée : quelques secondes pour $p \le 157$.

Le script :
1. construit $(x^7+\sigma x+1)^{(p-1)/2}$ par exponentiation rapide dans $\mathbf F_p[\sigma][x]$ (représentation : dict `{exposant_en_x: liste_coeffs_en_sigma}`) ;
2. en extrait $M_p(\sigma)$ et son déterminant par la formule explicite des permutations (Leibniz, $3\times3$) ;
3. cherche le terme non nul de plus bas degré ;
4. vérifie que la liste des $p$ à déterminant nul est exactement `[3, 7, 11, 23]` (`assert` en fin de script).

## Statut de vérification

| Étape de la preuve | Nature | Statut |
|---|---|---|
| I. $p\in\{3,7,11,23\}$ | argument structurel fini | ✅ prouvé, revérifié par calcul brute force |
| II. $p\ge101$ | argument algébrique universel (6 valeurs $R_a$ fixes) | 🟡 prouvé sous réserve — les $R_a$ sont repris d'une dérivation externe (Pochhammer), pas re-dérivés ici ; cohérence vérifiée sur 21+758 premiers indépendamment |
| III. $5\le p\le97$ | fini, calcul direct | ✅ prouvé, revérifié |

**Ce qui rend cette classification différente d'une simple accumulation numérique :** l'étape II est une identité algébrique valable pour une infinité de premiers à la fois (tous les facteurs premiers des 6 valeurs $R_a$ sont $<101$), pas une vérification cas par cas. C'est ce qui permet de qualifier le théorème de *clôturé* plutôt que de *fortement corroboré*.

## Limite honnête

Les 6 valeurs numériques de $R_a$ (§ étape II) n'ont pas été re-dérivées symboliquement depuis les coefficients multinomiaux dans cette session — elles ont été prises comme données et vérifiées par leurs conséquences (non-annulation testée indépendamment sur de nombreux premiers, aucun désaccord). Une reprise complète re-dérivant ces 6 constantes à la main fermerait la dernière réserve.

## Portée

Ce théorème concerne un invariant géométrique (ordinarité/superspécialité en caractéristique $p$) de la courbe $y^2=x^7+\sigma x+1$, **distinct** du groupe de Galois de $x^7+\sigma x+1$ sur $\mathbb Q$ (objet d'un autre document de ce projet). Les deux ne se déduisent pas l'un de l'autre sans démonstration ; un lien potentiel (superspécialité en $p=7$ et groupe de décomposition en 7 pour $7\nmid\sigma$) est noté mais non exploité ailleurs dans ce projet.
