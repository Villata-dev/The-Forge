from systems.alchemy import AlchemySystem
import json

def test_potion_crafting():
    # Simulando ingredientes compatibles
    ing1 = {"effects": ["Damage Health", "Invisibility"]}
    ing2 = {"effects": ["Invisibility", "Restore Magicka"]}
    
    result = AlchemySystem.craft_potion(ing1, ing2)
    assert result["success"] == True
    assert "Invisibility" in result["effects"]

def test_failed_potion():
    ing1 = {"effects": ["Restore Health"]}
    ing2 = {"effects": ["Invisibility"]}
    
    result = AlchemySystem.craft_potion(ing1, ing2)
    assert result["success"] == False
