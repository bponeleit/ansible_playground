import time
import traceback
import serial

from pymodbus.client.sync import ModbusSerialClient as pyRtu

slavesArr = [1]
iterSp = 100
regsSp = 10
#portNbr = '/dev/ttyUSB0'
portNbr = '/dev/cu.usbserial-1420'
portName = 'com22'
#baudrate = 9600
baudrate = 19200
timeoutSp = 10

pymc = pyRtu(method='rtu', port=portNbr, baudrate=baudrate, timeout=timeoutSp)

errCnt = 0
startTs = time.time()
for i in range(iterSp):
  for slaveId in slavesArr: 
    try:
        hr = pymc.read_holding_registers(0,regsSp,unit=slaveId)
        print(hr)
    except:
        errCnt += 1
        tb = traceback.format_exc()


stopTs = time.time()
timeDiff = stopTs  - startTs
print('pymodbus:\ttime to read %s x %s (x %s regs): %.3f [s] / %.3f [s/req]' % (len(slavesArr),iterSp, regsSp, timeDiff, timeDiff/iterSp))
if errCnt >0:
    print('   !pymodbus:\terrCnt: %s; last tb: %s' % (errCnt, tb))


pymc.close()
pymodbus.console serial --port /dev/cu.usbserial-1420 --baudrate 9600 --timeout 2
pymodbus.console serial --port /dev/ttyUSB0 --baudrate 9600 --timeout 2