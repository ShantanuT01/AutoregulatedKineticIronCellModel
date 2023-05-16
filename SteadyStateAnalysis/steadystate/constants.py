# state changing variables
OXYGEN = "OXYGEN"
IRON = "IRON"
KISU = "kisu"

# components
FC = "FC"
CIA = "CIA"
F2 = "F2"
F3 = "F3"
FM = "FM"
FS = "FS"
MP = "MP"
O2 = "O2"
COMPONENTS = [FC,CIA,F2,F3,FM,FS,MP,O2]

# regression variables
SENSED_SPECIES = "Sensed Species"
RATE_CONSTANT = "Rate Constant"


# State Variables
STATES = dict()
STATES[FC] = [20, 10, 5]
STATES[CIA] = [80, 70, 68]
STATES[F2] = [200, 30, 20]
STATES[F3] = [3400, 420, 60]
STATES[FM] = [100, 200, 50]
STATES[FS] = [500, 150, 300]
STATES[MP] = [50, 8500, 20]
STATES[O2] = [1.0, 0.481333, 1.22222]
