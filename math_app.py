import math
import streamlit as st

# ตั้งค่าหน้าเว็บ Streamlit
st.set_page_config(
    page_title="โปรแกรมคำนวณสูตรคณิตศาสตร์", page_icon="🔢", layout="centered"
)

st.title("📐 โปรแกรมคำนวณสูตรคณิตศาสตร์ด้วย Streamlit")
st.write(
    "แอปพลิเคชันนี้รวบรวมสูตรคณิตศาสตร์สำคัญ 3 หัวข้อ พร้อมเครื่องมือคำนวณแบบอินเทอร์แอกทีฟ"
)

# สร้าง Sidebar สำหรับเลือกหัวข้อ
menu = st.sidebar.selectbox(
    "เลือกหัวข้อคณิตศาสตร์",
    [
        "1. ພື້ນທີ່ວົງມົນ (Area of a Circle)",
        "2. ທິດສະດີບົດປີທາໂກຣັສ (Pythagorean Theorem)",
        "3. ສົມຜົນກຳລັງສອງ (Quadratic Equation)",
    ],
)

st.divider()

# ----------------------------------------------------
# ຫົວຂໍ້ທີ 1: ພື້ນທີ່ວົງມົນ
# ----------------------------------------------------
if menu == "1. ພື້ນທີ່ວົງມົນ (Area of a Circle)":
  st.header("⚪ 1. ພື້ນທີ່ວົງມົນ")

  st.write("### 📜 ສູດຄຳນິດສາດ:")
  st.latex(r"A = \pi r^2")
  st.write("ໂດຍທີ່:")
  st.markdown("- **$A$** = ພື້ນທີ່ວົງມົນ")
  st.markdown("- **$r$** = ຣັດສະມີ (Radius)")
  st.markdown("- **$\pi$** $\approx 3.14159$")

  st.divider()

  st.subheader("🧮 ເຄື່ອງຄິດເລກຄຳນວນພື້ນທີ່ວົງມົນ")
  r = st.number_input(
      "ກະລຸນາໃສ່ຄ່າຣັດສະມີ ($r$):",
      min_value=0.0,
      value=5.0,
      step=0.1,
      format="%.2f",
  )

  if st.button("ຄຳນວນພື້ນທີ່"):
    area = math.pi * (r**2)
    st.success(f"✅ ຜົນລັບ: ພື້ນທີ່ວົງມົນ = **{area:.4f}** ຕารางหน่วย")

# ----------------------------------------------------
# ຫົວຂໍ້ທີ 2: ທິດສະດີບົດປີທາໂກຣັສ
# ----------------------------------------------------
elif menu == "2. ທິດສະດີບົດປີທາໂກຣັສ (Pythagorean Theorem)":
  st.header("🔺 2. ທິດສະດີບົດປີທາໂກຣັສ")

  st.write("### 📜 ສູດຄຳນິດສາດ:")
  st.latex(r"c^2 = a^2 + b^2 \quad \rightarrow \quad c = \sqrt{a^2 + b^2}")
  st.write("ໂດຍທີ່:")
  st.markdown("- **$c$** = ດ້ານກົງກຸ່ມມຸມສາກ (Hypotenuse)")
  st.markdown("- **$a$ ແລະ $b$** = ດ້ານປະກອບມຸມສາກ")

  st.divider()

  st.subheader("🧮 ເຄື່ອງຄິດເລກຫາດ້ານກົງກຸ່ມມຸມສາກ ($c$)")
  col1, col2 = st.columns(2)
  with col1:
    a = st.number_input(
        "ໃສ່ຄ່າດ້ານ $a$:", min_value=0.0, value=3.0, step=0.1, format="%.2f"
    )
  with col2:
    b = st.number_input(
        "ໃສ່ຄ່າດ້ານ $b$:", min_value=0.0, value=4.0, step=0.1, format="%.2f"
    )

  if st.button("ຄຳນວນຫາດ້ານ c"):
    c = math.sqrt(a**2 + b**2)
    st.success(f"✅ ຜົນລັບ: ດ້ານກົງກຸ່ມມຸມສາກ ($c$) = **{c:.4f}** หน่วย")

# ----------------------------------------------------
# ຫົວຂໍ້ທີ 3: ສົມຜົນກຳລັງສອງ
# ----------------------------------------------------
elif menu == "3. ສົມຜົນກຳລັງສອງ (Quadratic Equation)":
  st.header("📈 3. ສົມຜົນກຳລັງສອງ")

  st.write("### 📜 ສູດຄຳນິດສາດ:")
  st.latex(r"ax^2 + bx + c = 0")
  st.write("ສູດຄຳນວນຫາຄ່າ $x$:")
  st.latex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")

  st.divider()

  st.subheader(
      "🧮 ເຄື່ອງຄິດເລກແກ້ສົມຜົນກຳລັງສອງ ($ax^2 + bx + c = 0$)"
  )
  col1, col2, col3 = st.columns(3)
  with col1:
    a_q = st.number_input("ຄ່າ $a$:", value=1.0, step=0.1)
  with col2:
    b_q = st.number_input("ຄ່າ $b$:", value=-5.0, step=0.1)
  with col3:
    c_q = st.number_input("ຄ່າ $c$:", value=6.0, step=0.1)

  if st.button("ແກ້ສົມຜົນ"):
    if a_q == 0:
      st.error("❌ ຄ່າ $a$ ຕ້ອງບໍ່ເທົ່າກັບ 0 (ເພາະຈະບໍ່ແມ່ນສົມຜົນກຳລັງສອງ)")
    else:
      discriminant = (b_q**2) - (4 * a_q * c_q)

      if discriminant > 0:
        x1 = (-b_q + math.sqrt(discriminant)) / (2 * a_q)
        x2 = (-b_q - math.sqrt(discriminant)) / (2 * a_q)
        st.success(
            f"✅ ສົມຜົນມີ 2 ຄຳຕອບ (Real Roots):<br>• $x_1$ = **{x1:.4f}**<br>•"
            f" $x_2$ = **{x2:.4f}**",
            icon="🎉",
        )
      elif discriminant == 0:
        x = -b_q / (2 * a_q)
        st.success(
            f"✅ ສົມຜົນມີ 1 ຄຳຕອບ (Repeated Root):<br>• $x$ = **{x:.4f}**",
            icon="🎉",
        )
      else:
        real_part = -b_q / (2 * a_q)
        imag_part = math.sqrt(abs(discriminant)) / (2 * a_q)
        st.warning(
            "⚠️ ສົມຜົນມີຄຳຕອບເປັນຈຳນວນເຊິງຊ້ອນ (Complex Roots):<br>"
            f"• $x_1$ = `{real_part:.4f} + {imag_part:.4f}i`<br>"
            f"• $x_2$ = `{real_part:.4f} - {imag_part:.4f}i`"
        )