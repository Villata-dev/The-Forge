from ui.fog_of_war import FogOfWar

def test_fow_reveal():
    fow = FogOfWar(1000, 1000, 32)
    fow.reveal((100, 100), 2)
    assert len(fow.visited) > 0
    assert (int(100/32), int(100/32)) in fow.visited
