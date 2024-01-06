# Viết chương trình cho phép người dùng nhập vào 1 số n, tính tổng bình phương từ 1 -> n
# Ví dụ: n=5 => tổng bình phương = 1^2 + 2^2 + ... + n^2

# Input
so_n = int(input("Nhập số n: "))
while so_n < 0:
    so_n = int(input("Nhập số n: "))
# Output
tong_binh_phuong = 0
# Process
so_hang = 1
while so_hang <= so_n:
    so_hang *= so_hang
    tong_binh_phuong += so_hang
    so_hang += 1

print(f'Tổng bình phương của {so_n} là: {tong_binh_phuong}')