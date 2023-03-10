

# Fly and Scanning (Syncronys), FlyBy, AeroSurvalience,

is_running = True

def run(drone):
    while is_running:
        # print("Enter Input")
        update(drone)


def update(drone):
    # fly: 1. takeoff 2.
    # scan: 1. scan qr 2. put info into array 3. send info to Rover 4. go scan next qr
