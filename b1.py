branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

data = {}

for branch in range(1, branch_count + 1):
    data[branch] = {}
    print(f"Chi nhánh {branch}:")
    for month in range(1, month_count + 1):
        revenue = int(
            input(f"  Tháng {month}: ")
        )
        data[branch][month] = revenue

print()
print("─" * 16 + " Kết quả " + "─" * 16)

for branch in range(1, branch_count + 1):
    for month in range(1, month_count + 1):
        print(f"Chi nhánh {branch}, tháng {month}: {data[branch][month]} triệu đồng")