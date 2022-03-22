import qrcode
data = 'HydraLearn'
img = qrcode.make(data)
img.save('MyQRCode.png')