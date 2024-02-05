# from smartcard.System import readers
# from smartcard.util import toHexString

# def read_desfire(reader):
#     connection = reader.createConnection()
#     connection.connect()

#     # TODO: Use DESFire commands to read data in NDEF format
#     data = connection.transmit([0x90, 0xBD, 0x00, 0x04, 0x00])

#     print("Data read from MIFARE DESFire:", toHexString(data))

#     connection.disconnect()

# def write_desfire(reader, data_to_write):
#     connection = reader.createConnection()
#     connection.connect()

#     # TODO: Use DESFire commands to write data in NDEF format
#     connection.transmit([0x90, 0xAF, 0x00, 0x04, 0x00, data_to_write])

#     print("Data written to MIFARE DESFire.")

#     connection.disconnect()

# # def main():
#     # Get the list of available smart card readers
# r = readers()
# if not r:
#     print("No smart card readers found.")

# reader = r[0]  # Assuming the first reader, adjust if needed

#     # Uncomment the function calls based on your requirement
# read_desfire(reader)
# # write_desfire(reader, "Hello, NDEF on DESFire!")

# # if _name_ == "_main_":
# #     main()






# import nfcpy

# def read_ndef_data(tag):
#     ndef_data = None
#     try:
#         ndef_records = tag.ndef.records
#         ndef_data = [record.text for record in ndef_records]
#     except Exception as e:
#         print(f"Error reading NDEF data: {e}")

#     return ndef_data

# def on_connect(tag):
#     ndef_data = read_ndef_data(tag)
#     if ndef_data:
#         print("NDEF Data:")
#         for data in ndef_data:
#             print(data)
#     else:
#         print("No NDEF data found.")

# # Replace 'usb' with the correct connection method for your NFC reader
# with nfcpy.ContactlessFrontend('usb') as clf:
#     print("Waiting for an NFC card...")
#     clf.connect(rdwr={'on-connect': on_connect})














# from smartcard.System import readers
# from smartcard.util import toHexString

# def read_desfire(reader):
#     connection = reader.createConnection()
#     connection.connect()

#     # TODO: Use DESFire commands to select the application and file
#     # Example: 
#     # Select application
#     select_application_apdu = [0x90, 0x5A, 0x00, 0x00, 0x03, 0x01, 0x00, 0x00, 0x00]
#     _, _, _ = connection.transmit(select_application_apdu)
    
#     # Select file
#     select_file_apdu = [0x90, 0x5C, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x00]
#     _, _, _ = connection.transmit(select_file_apdu)

#     # Read data
#     read_data_apdu = [0x90, 0xBD, 0x00, 0x00, 0xFF]  # Assuming FF bytes length, adjust accordingly
#     data, _, _ = connection.transmit(read_data_apdu)

#     # Convert the response to a list of bytes
#     data_bytes = list(data)

#     print("Data read from MIFARE DESFire:", toHexString(data_bytes))

#     connection.disconnect()

# # Get the list of available smart card readers
# r = readers()
# if not r:
#     print("No smart card readers found.")
# else:
#     reader = r[0]  # Assuming the first reader, adjust if needed

#     # Uncomment the function calls based on your requirement
# read_desfire(reader)


# from smartcard.System import readers

# def write_desfire(reader, ndef_data_to_write):
#     connection = reader.createConnection()
#     connection.connect()

#     # TODO: Use DESFire commands to select the application and file
#     # Example: 
#     # Select application
#     select_application_apdu = [0x90, 0x5A, 0x00, 0x00, 0x03, 0x01, 0x00, 0x00, 0x00]
#     _, _, _ = connection.transmit(select_application_apdu)
    
#     # Select file
#     select_file_apdu = [0x90, 0x5C, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x00]
#     _, _, _ = connection.transmit(select_file_apdu)

#     # Write data
#     write_data_apdu = [0x90, 0xD0, 0x00, 0x00, 0x00] + ndef_data_to_write
#     _, _, _ = connection.transmit(write_data_apdu)

#     print("NDEF Data written to MIFARE DESFire.")

#     connection.disconnect()

# # Get the list of available smart card readers
# r = readers()
# if not r:
#     print("No smart card readers found.")
# else:
#     reader = r[0]  # Assuming the first reader, adjust if needed

#     # Example NDEF data to write
#     ndef_data_to_write = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06]

#     # Uncomment the function calls based on your requirement
#     write_desfire(reader, ndef_data_to_write)




# from smartcard.System import readers
# from smartcard.util import toHexString

# def authenticate(reader):
#     connection = reader.createConnection()
#     connection.connect()

#     # Authenticate with the default key (0x00)
#     auth_apdu = [0x90, 0x0A, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00]
#     _, sw1, sw2 = connection.transmit(auth_apdu)

#     if sw1 == 0x90 and sw2 == 0x00:
#         print("Authentication successful.")
#         return True
#     else:
#         print("Authentication failed.")
#         return False

# def read_ndef_data(reader):
#     connection = reader.createConnection()
#     connection.connect()

#     # Select the application and file where NDEF data is stored
#     select_application_apdu = [0x90, 0x5A, 0x00, 0x00, 0x03, 0x01, 0x00, 0x00, 0x00]
#     _, _, _ = connection.transmit(select_application_apdu)

#     select_file_apdu = [0x90, 0x5C, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x00]
#     _, _, _ = connection.transmit(select_file_apdu)

#     # Read NDEF data
#     # Read NDEF data with dynamic length
#     read_apdu = [0x90, 0xBD, 0x00, 0x00, 0x00]
#     length = 0xFF  # You might need to adjust this based on your application
#     read_apdu += [length]
#     data, _, _ = connection.transmit(read_apdu)


#     # Convert the response to a list of bytes
#     data_bytes = list(data)

#     print("NDEF Data read from MIFARE DESFire:", toHexString(data_bytes))

#     connection.disconnect()

# def write_ndef_data(reader, ndef_data):
#     connection = reader.createConnection()
#     connection.connect()

#     # Select the application and file where NDEF data is stored
#     select_application_apdu = [0x90, 0x5A, 0x00, 0x00, 0x03, 0x01, 0x00, 0x00, 0x00]
#     _, _, _ = connection.transmit(select_application_apdu)

#     select_file_apdu = [0x90, 0x5C, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x00]
#     _, _, _ = connection.transmit(select_file_apdu)

#     # Write NDEF data
#     write_apdu = [0x90, 0xD0, 0x00, 0x00, 0x00] + ndef_data
#     _, _, _ = connection.transmit(write_apdu)

#     print("NDEF Data written to MIFARE DESFire.")

#     connection.disconnect()

# # Get the list of available smart card readers
# r = readers()
# if not r:
#     print("No smart card readers found.")
# else:
#     reader = r[0]  # Assuming the first reader, adjust if needed

#     # Example NDEF data to write
#     ndef_data_to_write = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06]

#     # Uncomment the function calls based on your requirement
#     # if authenticate(reader):
#     read_ndef_data(reader)
#     # write_ndef_data(reader, ndef_data_to_write)


from smartcard.System import readers
from smartcard.util import toHexString

def authenticate(reader):
    connection = reader.createConnection()
    connection.connect()

    # Authenticate with the default key (0x00)
    auth_apdu = [0x90, 0x0A, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00]
    _, sw1, sw2 = connection.transmit(auth_apdu)

    if sw1 == 0x90 and sw2 == 0x00:
        print("Authentication successful.")
        return True
    else:
        print("Authentication failed.")
        return False

def read_ndef_data(reader):
    connection = reader.createConnection()
    connection.connect()

    # Select the application and file where NDEF data is stored
    select_application_apdu = [0x90, 0x5A, 0x00, 0x00, 0x03, 0x01, 0x00, 0x00, 0x00]
    _, _, _ = connection.transmit(select_application_apdu)

    select_file_apdu = [0x90, 0x5C, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x00]
    _, _, _ = connection.transmit(select_file_apdu)

    # Read NDEF data with dynamic length
    read_apdu = [0x90, 0xBD, 0x00, 0x00, 0x00, 0xFF]  # Assuming FF bytes length, adjust accordingly
    data, _, _ = connection.transmit(read_apdu)

    # Convert the response to a list of bytes
    data_bytes = list(data)

    print("NDEF Data read from MIFARE DESFire:", toHexString(data_bytes))

    connection.disconnect()

def write_ndef_data(reader, ndef_data):
    connection = reader.createConnection()
    connection.connect()

    # Select the application and file where NDEF data is stored
    select_application_apdu = [0x90, 0x5A, 0x00, 0x00, 0x03, 0x01, 0x00, 0x00, 0x00]
    _, _, _ = connection.transmit(select_application_apdu)

    select_file_apdu = [0x90, 0x5C, 0x00, 0x00, 0x04, 0x00, 0x01, 0x00, 0x00]
    _, _, _ = connection.transmit(select_file_apdu)

    # Convert string to bytes
    ndef_data_bytes = [ord(char) for char in ndef_data]

    # Write NDEF data
    write_apdu = [0x90, 0xD0, 0x00, 0x00, 0x00] + ndef_data_bytes
    _, _, _ = connection.transmit(write_apdu)

    print("NDEF Data written to MIFARE DESFire.")

    connection.disconnect()

# Get the list of available smart card readers
r = readers()
if not r:
    print("No smart card readers found.")
else:
    reader = r[0]  # Assuming the first reader, adjust if needed

    # Example NDEF data to write (as a string)
    ndef_data_to_write = "Hello, NFC!"

    # Uncomment the function calls based on your requirement
    # if authenticate(reader):
    # read_ndef_data(reader)
    write_ndef_data(reader, ndef_data_to_write)
