
import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Input Data Siswa", layout="centered")
st.title("📝 Form Input Data Siswa")

# Inisialisasi session state untuk menyimpan data input sementara
if "data_siswa" not in st.session_state:
    st.session_state["data_siswa"] = []

# Form input
with st.form("form_input_siswa"):
    nama = st.text_input("Nama Siswa")
    sekolah = st.text_input("Nama Sekolah")
    kelas = st.text_input("Kelas")
    alamat = st.text_area("Alamat Siswa")

    submitted = st.form_submit_button("➕ Tambahkan Data")

    if submitted:
        if nama and sekolah and kelas and alamat:
            st.session_state["data_siswa"].append({
                "Nama": nama,
                "Sekolah": sekolah,
                "Kelas": kelas,
                "Alamat": alamat
            })
            st.success("✅ Data siswa berhasil ditambahkan.")
        else:
            st.warning("⚠️ Semua kolom harus diisi.")

# Tampilkan tabel data yang sudah diinput
if st.session_state["data_siswa"]:
    df_siswa = pd.DataFrame(st.session_state["data_siswa"])
    st.markdown("### 📋 Data Siswa yang Telah Diinput")
    st.dataframe(df_siswa)

    # Tombol download
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df_siswa.to_excel(writer, index=False, sheet_name='Data Siswa')
    output.seek(0)

    st.download_button("⬇️ Download Data Siswa (.xlsx)", data=output, file_name="data_siswa.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
else:
    st.info("Belum ada data siswa yang dimasukkan.")
