import qrcode
from PIL import Image


#  taking UPI Id is a input
upi_id= input("Enter your UPI Id = ")


phonepe_uri= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_uri= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_uri= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'


#  create qr codes for each payment app

phonepe_qr= qrcode.make(phonepe_uri)
paytm_qr=qrcode.make(paytm_uri)
google_pay_qr = qrcode.make(google_pay_uri)

#  save the qr code to image file (optional)

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#  dispplay the qr code
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show() 