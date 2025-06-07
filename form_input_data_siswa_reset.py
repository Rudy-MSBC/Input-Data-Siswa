
import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Input Data Siswa", layout="centered")
st.title("📝 Form Input Data Siswa")

# Inisialisasi session state
if "data_siswa" not in st.session_state:
    st.session_state["data_siswa"] = []

if "nama" not in st.session_state:
    st.session_state["nama"] = ""
if "sekolah" not in st.session_state:
    st.session_state["sekolah"] = ""
if "kelas" not in st.session_state:
    st.session_state["kelas"] = ""
if "alamat" not in st.session_state:
    st.session_state["alamat"] = ""

# Form input
with st.form("form_input_siswa"):
    nama = st.text_input("Nama Siswa", value=st.session_state["nama"], key="nama_input")
    sekolah = st.text_input("Nama Sekolah", value=st.session_state["sekolah"], key="sekolah_input")
    kelas = st.text_input("Kelas", value=st.session_state["kelas"], key="kelas_input")
    alamat = st.text_area("Alamat Siswa", value=st.session_state["alamat"], key="alamat_input")

    submitted = st.form_submit_button("➕ Simpan Data")

    if submitted:
        if nama and sekolah and kelas and alamat:
            st.session_state["data_siswa"].append({
                "Nama": nama,
                "Sekolah": sekolah,
                "Kelas": kelas,
                "Alamat": alamat
            })
            st.success(f"✅ Data untuk {nama} berhasil disimpan.")

            # Reset form values
            st.session_state["nama_input"] = ""
            st.session_state["sekolah_input"] = ""
            st.session_state["kelas_input"] = ""
            st.session_state["alamat_input"] = ""
        else:
            st.warning("⚠️ Semua kolom harus diisi.")

# Tampilkan data
if st.session_state["data_siswa"]:
    df_siswa = pd.DataFrame(st.session_state["data_siswa"])
    st.markdown("### 📋 Data Siswa yang Telah Disimpan")
    st.dataframe(df_siswa)

    # Tombol download Excel
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df_siswa.to_excel(writer, index=False, sheet_name='Data Siswa')
    output.seek(0)

    st.download_button("⬇️ Download Data Siswa (.xlsx)", data=output, file_name="data_siswa.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
else:
    st.info("Belum ada data siswa yang dimasukkan.")
