
def init():
    global working
    global max_temperature
    global min_temperature
    global fan
    global working
    global forward
    global current_temperature
    global motor_forward
    global motor_backward
    global circuit_breaker
    forward=0
    fan=0
    working=0
    max_temperature = 80
    min_temperature = 15
    current_temperature=15
    circuit_breaker=1
