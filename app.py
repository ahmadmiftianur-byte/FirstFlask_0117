from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    nama_terakhir = ""

    if request.method == "POST":
        nama_terakhir = request.form.get("nama", "").strip()
        if nama_terakhir:
            hasil = f"Halo, {nama_terakhir}! Parameter berhasil diproses lewat POST."
        else:
            hasil = "Nama tidak boleh kosong. Silakan isi terlebih dahulu."

    