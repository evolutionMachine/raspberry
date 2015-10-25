import RPi.GPIO as GPIO
import random as rnd
import time

class Log:
    values = [];
    limit  = 100;

    def __init__(self, _limit):
        values     = [];
        self.limit = _limit

    def add(self, _value):
        self.values.append(_value)
        if len(self.values) > self.limit:
            self.values.pop(0);

    def average(self):
        return self.sum() / len(self.values)

    def sum(self):
        sum    = 0
        for value in self.values:
            sum += value

        return sum

    def extremes(self, _start, _stop):
        min    = self.values[0]
        max    = self.values[0]
        for value in self.values:
            if value < min:
                min = value
            if value > max:
                max = value

        return {"min": min, "max": max}



class Device:
    pin   = 0
    input = True
    value = False

    def __init__(self, _pin, _input):
        self.pin   = _pin
        self.input = _input

        GPIO.setup(self.pin, self.input if GPIO.IN else GPIO.OUT)

    def start(self):
        if self.input:
            print "not an output"
            return

        self.value = True
        GPIO.output(self.pin, True)

    def stop(self):
        if self.input:
            print "not an output"
            return

        self.value = False
        GPIO.output(self.pin, False)


    def read(self):
        return GPIO.input

    def __str__(self):
        return "On pin " + str(self.pin) + " is " + str(self.input) if "input" else "output"

class Motor(Device):
    def start(self):
        Device.start(self);

    def stop(self):
        Device.stop(self);


class irCounter(Device):
    input  = True
    counter = 0
    log    = None
    event  = None

    def __init__(self, _pin, _log):
        Device.__init__(self, _pin, True)
        self.log = _log


    def callback(self):
        self.counter += 1

    def start(self):
        self.event = GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.callback, bouncetime=1)

    def stop(self):
        GPIO.remove_event_detect(self.pin)


class DeviceController:
    devices = {};

    def stopMotor(self, _motor):
        self.devices["motor"][_motor].stop()

    def startMotor(self, _motor):
        self.devices["motor"][_motor].start()

    def __init__(self):
        self.devices["motor"] = {}

        self.devices["irLed"] = Device(10, True);
        self.devices["irCounter"] = irCounter(15,Log(100))

        self.devices["motor"]["food"    ] = Motor(13, False)
        self.devices["motor"]["poison"  ] = Motor(12, False)
        self.devices["motor"]["rejector"] = Motor(11, False)

        for key, _motor in self.devices["motor"].iteritems():
            GPIO.setup(_motor.pin, GPIO.OUT)



if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    dc = DeviceController();
    dc.startMotor("food");
    log = Log(10)

    for x in range(0,10):
        log.add(rnd.uniform(1,100))

    print "Values"
    print log.values
    print "Average"
    print log.average();
    print "extremes"
    print log.extremes(0,10)

    for key, _device in dc.devices["motor"].iteritems():
        print "start motor " + str(key)
        _device.start()
        time.sleep(2)

        print "stop motor " + str(key)
        _device.stop()

    print "Start ir Led"
    dc.devices["irLed"].start();
    print "Start ir Counter"
    dc.devices["irCounter"].start();

    time.sleep(1)

    dc.devices["irCounter"].stop();

    print "collected " + str(dc.devices["irCounter"].log.sum())

    print "Stop ir Led"
    dc.devices["irLed"].stop();

    print "Start ir Counter"
    dc.devices["irCounter"].start();

    print "collected " + str(dc.devices["irCounter"].log.sum())


    time.sleep(1)

    print "collected " + str(dc.devices["irCounter"].log.sum())

    for key, _device in dc.devices.iteritems():
        print str(key) + " " + str(_device)

    GPIO.cleanup()
