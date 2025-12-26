import qrcode

url = input("Enter the url to convert to Qr Code:\n")
filename = input("Enter the name of the file:\n")

img = qrcode.make(url)
img.save(filename+".png")