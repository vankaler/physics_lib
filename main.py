
def calculate_speed(distance, time):
    return distance / time


def calculate_acceleration(change_in_velocity, time):
    return change_in_velocity / time


def calculate_force(mass, acceleration):
    return mass * acceleration


def calculate_work(force, distance):
    return force * distance


def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity**2


if __name__ == "__main__":
    
    print("Testing physics functions:")
    distance = 100  # meters
    time = 20  # seconds
    velocity = calculate_speed(distance, time)
    print("Velocity:", velocity, "m/s")

    change_in_velocity = 30  # m/s
    acceleration_time = 10  # seconds
    acceleration = calculate_acceleration(change_in_velocity, acceleration_time)
    print("Acceleration:", acceleration, "m/s^2")

    mass = 5  # kilograms
    force = calculate_force(mass, acceleration)
    print("Force:", force, "N")

    work_distance = 50  # meters
    work_done = calculate_work(force, work_distance)
    print("Work done:", work_done, "J")

    # Testing with different values
    mass_2 = 2  # kilograms
    velocity_2 = 15  # m/s
    kinetic_energy = calculate_kinetic_energy(mass_2, velocity_2)
    print("Kinetic energy:", kinetic_energy, "J")




