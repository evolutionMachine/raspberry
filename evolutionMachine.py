import control
import serial
class EvolutionMachine:
    # deviceController = control.DeviceController
    arduino = {}
    evolutionState = 0

    def getData(self):
        _ret = {}
        _ret["visual_sensor"] = float(self.readLine());
        _ret["evolution_state"] = 0.2
        _ret["pump1"] = 0.3
        _ret["pump2"] = 0.4
        _ret["pump3"] = 0.5

        return _ret

    def __init__(self):
        self.arduino = serial.Serial('/dev/ttyACM0')

    def readLine(self):
        line = self.arduino.readline();
        return line;

if __name__ == '__main__':
    evm = EvolutionMachine()
    print evm
    print evm.getData()