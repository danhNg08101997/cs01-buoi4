# Viết chương trình cho phép người dùng nhập vào 1 số n, tính tổng bình phương từ 1 -> n
# Ví dụ: n=5 => tổng bình phương = 1^2 + 2^2 + ... + n^2

# Input
so_n = int(input("Nhập số n: "))
while so_n < 0:
    so_n = int(input("Nhập số n: "))
# Output
tong_binh_phuong = 0
# Process
temp = so_n
while temp >= 1:
    tong_binh_phuong += temp**2
    temp -= 1

print(f'Tổng bình phương của {so_n} là: {tong_binh_phuong}')