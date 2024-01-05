# Viết chương trình cho phép người dùng nhập vào số n, yêu cầu tính n!, trong trường hợp người dùng nhập vào số nhỏ hơn 1 thì in ra 1.
# Ví dụ: 5 => 1*2*3*4*5

# Input
so_n = int(input("Nhập vào số n: "))
while so_n < 0:
    so_n = int(input("Nhập vào số n: "))
# Output
gia_thua = 1
# Process
so_hang = 1
while so_hang <= so_n:
    gia_thua *= so_hang
    so_hang += 1

print(f'{so_n}! = {gia_thua}')
