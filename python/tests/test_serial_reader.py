import pytest
import serial

from lora_processor.serial_reader import SerialReader

def test_construction():
    reader = SerialReader()
    
def test_open():
    reader = SerialReader()
    with pytest.raises(serial.serialutil.SerialException) as excinfo:
        reader.open()

def test_rssi_read():
    reader = SerialReader()
    line = 'RSSI: 85'.encode('utf-8')
    reader.process_line(line)

    assert reader.rssi == 85

def test_message_read():
    reader = SerialReader()
    line = 'Hello World # 99'.encode('utf-8')
    reader.process_line(line)
    assert reader.message == line.decode('utf-8')