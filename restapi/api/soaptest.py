from zeep import Client

client = Client(wsdl='http://dev.usbooking.org/us/UnitedSolutions?wsdl')

print(client.service.SectorCode(24))

# install "pip install zeep"
# python soaptest.py
# python -mzeep http://dev.usbooking.org/us/UnitedSolutions?wsdl
# run >>python soaptest.py