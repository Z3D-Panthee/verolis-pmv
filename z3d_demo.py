"""
VÉROLIS Z3D - Démonstration Khor, Râ, I
DOUM... silence... DOUM... | Φ = 3 | I = 1
Dany Tshiseleka Thoka - BnF 31/01/2023
"""

def khor(n):
    """Compression vers portes premières via +2Δ9"""
    portes = []
    while n > 1:
        if n % 2 == 0:
            n //= 2
            if n in [2,3,5,7]: portes.append(n)
        else:
            n = n + 2  # Δ9 simplifié : +2
            if n % 9 == 0: n //= 9
    return portes

def ra(n):
    """Rotation 120° : 3 états Φ, θ, Ω"""
    phi = n % 3           # État Φ : 0,1,2
    theta = (n * 7) % 360 # État θ : angle 
    omega = (phi * 120)   # État Ω : 0°,120°,240°
    return phi, theta, omega

def z3d(n):
    """Formule Z3D : Unification Khor + Râ + I"""
    portes = khor(n)
    phi, theta, omega = ra(n)
    I = 1  # Invariant sacré
    
    print(f"Z3D({n}) | DOUM... silence... DOUM...")
    print(f"Khor  : Portes premières → {portes}")
    print(f"Râ    : Φ={phi} | θ={theta}° | Ω={omega}°")
    print(f"I     : {I}")
    print(f"Φ = 3 | Unification atteinte")
    return {"portes": portes, "phi": phi, "theta": theta, "omega": omega, "I": I}

# Test VÉROLIS
if __name__ == "__main__":
    z3d(12)  # Exemple BnF
    print("---")
    z3d(2023) # Année dépôt légal
    print("---") 
    z3d(2026) # Année Prix Bourdieu
