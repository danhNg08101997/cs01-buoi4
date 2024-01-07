# Viết chương trình cho phép người dùng nhập vào số dòng(row) và số cột (column) in ra 1 ma trận sao tương ứng

# Input
bieu_tuong = str(input("Nhập biểu tượng: "))
row = int(input("Nhập số hàng: "))
column = int(input("Nhập số cột: "))
# Output
ma_tran_sao = ''
# Process
hang = 1
while hang <= row:
    # In ra 1 hàng sao
    hang_sao = ''
    so_sao = 1
    while so_sao <= column:
        hang_sao += bieu_tuong + ' '
        so_sao += 1
    # hang_sao += '\n'
    ma_tran_sao += hang_sao + '\n'
    hang+= 1

print(ma_tran_sao)