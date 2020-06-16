import png, pyqrcode
from pyqrcode import QRCode

stringToBeConvertedToQRCode = 'www.geeksforgeeks.org'

qcode = pyqrcode.create(stringToBeConvertedToQRCode)
qcode.svg("myqr.svg", scale=8)
qcode.png('myqr.png', scale=6)  

