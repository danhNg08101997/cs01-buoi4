# Viết chương trình cho phép người dùng nhập vào 1 số n, kiểm tra xem n có phải là số nguyên tố hay không, in ra màn hình kết quả

print('---------------Ứng dụng kiểm tra số nguyên tố-------------------------')
# Input
so_n = int(input("Nhập vào số n: "))
# Output
so_luong_uoc = 0
ket_qua = ''
# Process
so_chia = 1
while so_chia <= so_n:
    if so_n % so_chia == 0:
        so_luong_uoc += 1
    so_chia += 1

if so_luong_uoc == 2:
    ket_qua = f'{so_n} là số nguyên tố'
else:
    ket_qua = f'{so_n} không phải là số nguyên tố'

print(ket_qua)