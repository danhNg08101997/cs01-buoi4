# Viết chương trình nhập vào 1 số n in ra tam giác vuông n tương ứng.

print('---------------Ứng dụng in ra tam giác vuông-------------------------')

# Input
so_n = int(input("Nhập vào số n: "))
bieu_tuong = str(input("Nhập vào biểu tượng: "))
# Output
tam_giac_vuong = ''
# Process
hang = 1
while hang <= so_n:
    # Xử lý từng hàng
    so_cot = 1
    while so_cot <= hang:
        tam_giac_vuong += bieu_tuong + " "
        so_cot += 1
    tam_giac_vuong += '\n'
    hang += 1

print(tam_giac_vuong)