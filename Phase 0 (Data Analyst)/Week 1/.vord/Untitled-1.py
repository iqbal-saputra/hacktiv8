def penghasilan(jabatan, jam_kerja):
    perhitungan_gaji = {"Manager": 10_000_000, "Staff": 5_000_000, "Kasir": 4_000_000}

    if jabatan not in perhitungan_gaji:
        raise ValueError(
            f"Jabatan '{jabatan}' tidak terdaftar. Input jabatan yang valid"
        )
    # if jabatan not in perhitungan_gaji:
    #     raise ValueError(f"Jabatan '{jabatan}' tidak terdaftar. Jabatan yang valid adalah: {', '.join(perhitungan_gaji.keys())}")

    total_gaji = 0
    hasil_lembur = 20_000

    if jam_kerja > 40:
        total_gaji = perhitungan_gaji[jabatan] + ((jam_kerja - 40) * hasil_lembur)
    else:
        total_gaji += perhitungan_gaji[jabatan]

    return total_gaji


# hasil = penghasilan("Manager", 35)
# print(hasil)

# hasil = penghasilan("Staff", 20)
# print(hasil)


def total_operasional(karyawan):

    total_biaya = 0

    for i in karyawan:
        jabatan, jam_kerja = i
        total_biaya += penghasilan(jabatan, jam_kerja)

    return total_biaya


karyawan = (["Manager", 50], ["Staff", 50], ["Kasir", 50])

# hasil = total_operasional(karyawan)
# print(hasil)

import unittest

class UnitTest(unittest.TestCase):
    def karyawan(self):
        karyawan = {
            
        }