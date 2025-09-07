import qrcode

def main():
    data = 'https://www.geeksforgeeks.org/python/generate-qr-code-using-qrcode-in-python/'

    qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

    qr.add_data(data)

    qr.make(fit = True)

    img = qr.make_image(fill_color = 'black', back_color = 'white')

    nimi = input("qrcode nimi: ")

    img.save(f'{nimi}.png')

if __name__=="__main__":
    main()