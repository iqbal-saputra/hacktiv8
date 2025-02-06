def hitung_penghasilan(role, jam_kerja):
    perhitungan_gaji = {
        "Manager": 10_000_000,  # keys, values
        "Staff": 5_000_000,
        "Kasir": 4_000_000,
    }

    total_gaji = 0
    gaji_lembur = 20_000

    if jam_kerja > 40:
        total_gaji += gaji_lembur * (jam_kerja - 40)
        total_gaji += perhitungan_gaji[role]
    else:
        total_gaji += perhitungan_gaji[role]

    return total_gaji


# hasil = hitung_penghasilan("Manager", 45)
# print(hasil)

karyawan = [("Manager", 50), ("Staff", 50), ("Kasir", 50)]


def total_pengeluaran(karyawan):
    total_operasional = 0

    for i in karyawan:
        role, jam_kerja = i
        # print(type(i))
        total_operasional += hitung_penghasilan(role, jam_kerja)

    return total_operasional


hasil = total_pengeluaran(karyawan)
print(hasil)

import unittest


class UnitTest(unittest.TestCase):
    def karyawan1(self):
        karyawan = (
            ["Manager", 45],
            ["Staff", 35],
            ["Kasir", 50],
        )
        expected_Result = 19_300_000
        self.assertEqual(total_pengeluaran(karyawan), expected_Result)

    def karyawan2(self):
        karyawan = (["Manager", 50], ["Staff", 50], ["Kasir", 50])
        expectedResult = 19_600_000
        self.assertEqual(total_pengeluaran(karyawan), expectedResult)


if __name__ == "__main__":
    unittest.main()
