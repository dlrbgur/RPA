import qrcode
a=input('이름을 입력하세요')
b=input('학번을 입력하세요')
c=input('과를 입력하세요')
qr_data=a,b,c
qr_img=qrcode.make(qr_data)

save_path='my_info_data.png'
qr_img.save(save_path)