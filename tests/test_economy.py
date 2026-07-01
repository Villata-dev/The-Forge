from systems.economy import EconomyManager

def test_successful_purchase():
    eco = EconomyManager(100)
    assert eco.buy_item(40) == True
    assert eco.gold == 60

def test_failed_purchase():
    eco = EconomyManager(20)
    assert eco.buy_item(50) == False
    assert eco.gold == 20
