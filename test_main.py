import main

def test_calculate_speed():
    assert main.calculate_speed(100, 20) == 5

def test_calculate_acceleration():
    assert main.calculate_acceleration(30, 10) == 3

def test_calculate_force():
    assert main.calculate_force(5, 3) == 15

def test_calculate_work():
    assert main.calculate_work(15, 50) == 750

def test_calculate_kinetic_energy():
    assert main.calculate_kinetic_energy(2, 15) == 225