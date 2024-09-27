# import minimalmodbus
# instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1)  # port name, slave address (in decimal)
#
# ## Read temperature (PV = ProcessValue) ##
# temperature = instrument.read_register(289, 1)  # Registernumber, number of decimals
# print(temperature)
#
# ## Change temperature setpoint (SP) ##
# NEW_TEMPERATURE = 95
# instrument.write_register(24, NEW_TEMPERATURE, 1)  # Registernumber, value, number of decimals for storage
#
import minimalmodbus
import serial

try:
    instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1)  # port name, slave address (in decimal)
    #instrument.serial.baudrate = 9600  # Baud rate
    instrument.serial.timeout = 1      # Timeout in seconds

    # Read temperature (PV = ProcessValue)
    temperature = instrument.read_register(289, 1)  # Registernumber, number of decimals
    print(f"Current Temperature: {temperature}°C")

    # Change temperature setpoint (SP)
    NEW_TEMPERATURE = 95
    instrument.write_register(24, NEW_TEMPERATURE, 1)  # Registernumber, value, number of decimals for storage
    print(f"Setpoint Temperature changed to: {NEW_TEMPERATURE}°C")

except (IOError, ValueError) as e:
    print(f"Failed to read from the instrument, error: {e}")
