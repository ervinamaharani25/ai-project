# from app_v1.rag_engine import ask_ai

# if __name__ == "__main__":
#     ticket_no = '12312022026'
#     question = "Error downloading Orange Report"
#     result = ask_ai(question)
#     print(result)



import requests

queries = [
    "Update Approval",
    "Tidak Tercantum Size women",
    "Tidak Shipping Out Tablet",
    "Tidak bisa unduh report lotmaterialdetail",
    "Tidak bisa receipt b2b dan muncul notifikasi Not Have need receipt shipment data",
    "Tidak bisa melalukan input order OA saat akan melakukan Order Summary",
    "Tidak bisa LPB",
    "TIDAK BISA LOGIN SERP DI EDGE",
    "Tidak bisa ke buka aplikasi atau nge blank",
    "Tidak bisa input QTY pada menu sample order list",
    "Tidak bisa export data di menu Bussines MM- Comprehensive Po Data di PC SliProduksi 11",
    "Tidak bisa buat dokumen invesment plan",
    "TIDAK BISA BOOKING LAPTOP DI MENU BOOKING",
    "Tidak ada technology stitching pada style DH2987-002 model NIKE COURT VISION LO NN",
    "Tidak ada data fluxion sample yang muncul",
    "There a different data between finance mm and wh in receiving mold me",
    "SLI-FS12 WAREHOUSE FACILITY SUPPOTY (Tidak ditemukan data LPB pada receiving list)",
    "Setting SERP",
    "Revisi day type ramadhan (kebutuhan RPL OranHR)",
    "purchase mold tidak bisa add attachment",
    "Public usage dan Ir berbeda",
    "Perubahan Reason",
    "Penghapusan Double Data",
    "penambahan kategori capex untuk akun 22308016",
    "Penambahan Intercompany Account pada FS",
    "No Notification Request Repair Machine to Wechat",
    "MTLCode tidak muncul",
    "menu pr error di pc sli prod 6 a.n indrayana susendi",
    "Medical Adjustment-SKIPAYROLL5",
    "Lotcode not changes after receive change notice",
    "Lotcode F12U518 & F12U519 visual line tidak muncul pada hasil print",
    "Lot Unpublished on menu Bucket Management when MRP Already publish",
    "LOT CODE TIDAK BERHASIL DI REFRESH",
    "Local Amount not record",
    "Komponen tidak muncul dengan lengkap",
    "Install JCS mes dan J2 mess pada pc ppic7",
    "Instalasi SERP di PC SLI STOCKFIT6",
    "Instalasi JIT di PC SLI STOCKFIT6",
    "Input BM material ROLLBACK TRANSACTION",
    "FS bulan Desember ini masih ada selisih, dan untuk STI Salary FOH (Adjust)",
    "Disponse Price in JCS SERP",
    "Deleting employee clocking on Employee Clocking Detail menu",
    "Data output scanner pada tarikan data rework stitching tidak ada",
    "Custem report operating statement monthly",
    "COLOR TIDAK TER UPDATE SEMUA",
    "cannot upload data LFC",
    "Can not send PO automatically by email in Computer Sli-purchasing2",
    "Can not generate development list on PPR order material",
    "Blank error SERP mengganti w rate date",
    "belum muncul nilai ActualFee 202601 dan TotalActualFee",
    "B2B barcode input vendor PT sunjin qty input data sudah balace tetapi hasil apload barcoad selisi",
    "Audit PR Laste",
    "Assign Dept code baru",
    "Assign COA 211040 - INTERCOMPANY ACCOUNT ke A/R Event",
    "Adjust Price pada Incoming bill",
    "Addition of Employee to Orang-e Account",
    "Abnormal Issue J2 Lot Working Hour Report Janaury 2026"
]

for q in queries:
    response = requests.post(
        "http://127.0.0.1:8000/ai/recommendation",
        json={"query": q}
    )
    print("Query:", q)
    print("Response:", response.json())
    print("-" * 50)