from engine.time_system import DayNightCycle
def test_midnight_rollover():
    clock = DayNightCycle(time_scale=3600.0) # 1 segundo = 1 hora
    clock.time_of_day = 23.5
    clock.update(1.0)
    assert clock.time_of_day == 0.5 # Debe reiniciar al pasar las 24
