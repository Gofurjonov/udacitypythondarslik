month = 1
paid_months = 0
while month <= 12:
    status = input(f"{month}-oy ijarani to‘ladingizmi? (ha/yo‘q): ")
    try:
        if status.lower() not in ["ha", "yo'q"]:
            raise ValueError("Noto‘g‘ri javob! Faqat 'ha' yoki 'yo‘q' kiriting.")
    except ValueError as e:
        print(e)
        continue
    if status.lower() == "ha":
        paid_months +=1
    month +=1

print(f"Siz {paid_months} oy ijarani to‘ladingiz.")