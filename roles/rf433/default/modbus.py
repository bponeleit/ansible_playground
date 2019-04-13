import time
import traceback
import serial

from pymodbus.client.sync import ModbusSerialClient as pyRtu

slavesArr = [2]
iterSp = 100
regsSp = 10
portNbr = '/dev/ttyUSB0'
portName = 'com22'
baudrate = 9600

pymc = pyRtu(method='rtu', port=portNbr, baudrate=baudrate, timeout=timeoutSp)

errCnt = 0
startTs = time.time()
for i in range(iterSp):
  for slaveId in slavesArr: 
    try:
        pymc.read_holding_registers(0,regsSp,unit=slaveId)
    except:
        errCnt += 1
        tb = traceback.format_exc()


stopTs = time.time()
timeDiff = stopTs  - startTs
print "pymodbus:\ttime to read %s x %s (x %s regs): %.3f [s] / %.3f [s/req]" % (len(slavesArr),iterSp, regsSp, timeDiff, timeDiff/iterSp)
if errCnt >0:
    print "   !pymodbus:\terrCnt: %s; last tb: %s" % (errCnt, tb)


pymc.close()