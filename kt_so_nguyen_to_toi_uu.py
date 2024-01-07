import math
# Viết chương trình cho phép người dùng nhập vào 1 số n, kiểm tra xem n có phải là số nguyên tố hay không, in ra màn hình kết quả

print('---------------Ứng dụng kiểm tra số nguyên tố tối ưu------------------')

# Input
so_n = int(input("Nhập vào số n: "))
# Output
ket_luan = True
# Process
so_chia = 2
while so_chia <= math.sqrt(so_n):
    if so_n % so_chia == 0:
        ket_luan = False
        break
    so_chia += 1

if ket_luan and so_n > 1:
    print(f'{so_n} là số nguyên tố')
else:
    print(f'{so_n} không phải là số nguyên tố')