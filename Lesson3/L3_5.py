import math

def test_speed(speed):
    if(speed <= 70):
        print("Ok")
    elif (speed > 70):
        demeritPoint = math.floor((speed - 70) / 5)
        print("Points: ", demeritPoint)
        if(demeritPoint >= 12):
            print("License suspended")

driverSpeed = eval(input("Input the speed of driver: "))
test_speed(driverSpeed)

