"""
VÉROLIS PMV-1.0 - Procédure Mathématique VÉROLIS
Copyright (c) 2023 Dany Tshiseleka Thoka
Licence : CC-BY-SA 4.0 | Dépôt BnF 31/01/2023

Axiomatique des Lois Fondamentales
DOUM... silence... DOUM... | Φ = 3
"""

import math

def verolis_pmv(n: int) -> dict:
    """
    Calcule PMV-1.0 pour un entier n > 0
    Retourne : dict avec portes, phi, theta, omega, I
    """
    if n <= 0:
        raise ValueError("n doit être > 0")
    
    # Khor : compression +2Δ9
    portes = []
    temp = n
    while temp % 2 == 0:
        portes.append(2)
        temp //= 2
    i = 3
    while i * i <= temp:
        while temp % i == 0:
            portes.append(i)
            temp //= i
        i += 2
    if temp > 1:
        portes.append(temp)
    
    # Râ : rotations 120°
    phi = len(portes) % 3
    theta = sum(portes) % 9
    omega = 120 * phi
    
    # Unité sacrée I = 1
    I = 1
    
    return {
        "n": n,
        "portes_premieres": portes,
        "phi": phi,
        "theta": theta,
        "omega_deg": omega,
        "I": I,
        "doum": "DOUM... silence... DOUM..."
    }

if __name__ == "__main__":
    # Test: 12 = 2*2*3
    resultat = verolis_pmv(12)
    print(f"VÉROLIS PMV-1.0 | n={resultat['n']}")
    print(f"Portes: {resultat['portes_premieres']}")
    print(f"Φ={resultat['phi']} | θ={resultat['theta']} | Ω={resultat['omega_deg']}°")
    print(f"I={resultat['I']} | {resultat['doum']}")
