#import pymodbus
from pymodbus.client.sync import ModbusSerialClient

client = ModbusSerialClient(
    method='rtu',
    port='tty.usbserial-1420',
    baudrate=19200,
    timeout=3,
    parity='E',
    stopbits=1,
    bytesize=8
)

if client.connect():  
    res = client.read_holding_registers(address=1, count=1, unit=1)
    if not res.isError():
        print(res.registers)
    else:
        print(res)

else:
    print('Cannot connect to the Modbus Server/Slave')