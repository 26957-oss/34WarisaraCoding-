# 1. รับค่าคะแนน 3 วิชาจากผู้ใช้งาน (แปลงเป็นทศนิยมด้วย float เพื่อรองรับคะแนนที่มีเศษ)
subject1 = float(input("กรอกคะแนนวิชาที่ 1: "))
subject2 = float(input("กรอกคะแนนวิชาที่ 2: "))
subject3 = float(input("กรอกคะแนนวิชาที่ 3: "))

# 2. คำนวณคะแนนรวม
total_score = subject1 + subject2 + subject3

# 3. ตรวจสอบเงื่อนไขระดับคะแนน
if total_score >= 80:
    grade = "ดีเยี่ยม"
elif total_score >= 60:  # ช่วง 60 ถึง 79
    grade = "ผ่าน"
else:                    # ต่ำกว่า 60
    grade = "ควรปรับปรุง"

# 4. แสดงผลลัพธ์
print("------------------------")
print(f"คะแนนรวมทั้งหมด: {total_score:.2f} คะแนน")
print(f"ระดับคะแนนที่ได้: {grade}")
print("------------------------")
