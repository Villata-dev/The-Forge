from systems.stealth import StealthSystem
from systems.pickpocket import PickpocketSystem

def test_stealth_chance():
    sys = StealthSystem()
    chance = sys.calculate_detection_chance(100, 0.2, 0.0, 50)
    assert chance < 50.0 # Alta habilidad y poca luz deben mantener deteccion baja

def test_pickpocket_limits():
    result = PickpocketSystem.attempt_theft(100, 100.0, 5000) # Muy pesado y valioso
    assert result["chance_had"] == 5.0 # Debe ser capado al minimo 5%
