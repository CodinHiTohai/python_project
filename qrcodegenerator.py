import qrcode
url=input("enter you url")
filename=input("enter your filename to save as it is")
if not(filename.endswith(".png")):
    filename=filename+".png"
img=qrcode.make(url)
img.save(filename)
