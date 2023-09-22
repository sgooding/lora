import pytest
import serial

from lora_processor.serial_reader import SerialReader

def test_construction():
    reader = SerialReader()
    
def test_open():
    reader = SerialReader()
    with pytest.raises(serial.serialutil.SerialException) as excinfo:
        reader.open()