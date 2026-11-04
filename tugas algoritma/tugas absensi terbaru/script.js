const form = document.getElementById('formMahasiswa');
const isiTabel = document.getElementById('isiTabel');
let dataMahasiswa = JSON.parse(localStorage.getItem('dataMaster')) || [];

// FUNGSI TAMPILKAN DATA (Ditambah efek animasi baris)
function tampilkanData(dataArray) {
    isiTabel.innerHTML = ''; 
    dataArray.forEach((mhs, index) => {
        // Bikin jeda animasi per baris biar munculnya berurutan
        let delay = index * 0.05; 
        isiTabel.innerHTML += `
            <tr class="row-animate" style="animation-delay: ${delay}s; opacity: 0;">
                <td><strong>${mhs.nim}</strong></td>
                <td>${mhs.nama}</td>
                <td><span style="background:#eee; padding:5px 10px; border-radius:5px; font-size:0.9em;">${mhs.kodeMk}</span></td>
                <td><strong style="color: ${mhs.ipk >= 3.5 ? '#2ecc71' : '#e74c3c'}">${mhs.ipk}</strong></td>
            </tr>
        `;
    });
}

// SIMPAN DATA
form.addEventListener('submit', function(e) {
    e.preventDefault(); 
    const mhsBaru = {
        nama: document.getElementById('nama').value,
        nim: document.getElementById('nim').value,
        kodeMk: document.getElementById('kodeMk').value,
        ipk: document.getElementById('ipk').value
    };
    dataMahasiswa.push(mhsBaru);
    localStorage.setItem('dataMaster', JSON.stringify(dataMahasiswa));
    tampilkanData(dataMahasiswa);
    form.reset();

    // POP-UP ANIMASI KEREN (Ganti alert standar)
    Swal.fire({
        icon: 'success',
        title: 'Berhasil!',
        text: 'Data Mahasiswa masuk ke Database.',
        timer: 2000,
        showConfirmButton: false
    });
});

// SEQUENTIAL SEARCH
document.getElementById('inputSeq').addEventListener('input', function(e) {
    let keyword = e.target.value.toLowerCase();
    let hasil = dataMahasiswa.filter(mhs => 
        mhs.nama.toLowerCase().includes(keyword) || 
        mhs.nim.includes(keyword)
    );
    tampilkanData(hasil);
});

// BINARY SEARCH
document.getElementById('btnBinary').addEventListener('click', function() {
    let targetNim = document.getElementById('inputBin').value;
    if(!targetNim) {
        Swal.fire('Oops!', 'Masukkan NIM dulu di kolom pencarian!', 'warning');
        return;
    }

    let dataUrut = [...dataMahasiswa].sort((a, b) => parseInt(a.nim) - parseInt(b.nim));
    let bawah = 0, atas = dataUrut.length - 1, ketemu = false;

    while (bawah <= atas) {
        let tengah = Math.floor((bawah + atas) / 2);
        let nimTengah = dataUrut[tengah].nim;

        if (nimTengah === targetNim) {
            tampilkanData([dataUrut[tengah]]); 
            ketemu = true;
            Swal.fire('Ketemu!', `Data ${dataUrut[tengah].nama} ditemukan.`, 'success');
            break;
        } else if (parseInt(nimTengah) < parseInt(targetNim)) {
            bawah = tengah + 1;
        } else {
            atas = tengah - 1;
        }
    }

    if(!ketemu) Swal.fire('Gagal', 'NIM tidak ada dalam sistem.', 'error');
});

// BUBBLE SORT
document.getElementById('btnBubble').addEventListener('click', function() {
    let arr = [...dataMahasiswa]; 
    let n = arr.length;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (parseInt(arr[j].nim) > parseInt(arr[j+1].nim)) {
                let temp = arr[j]; arr[j] = arr[j+1]; arr[j+1] = temp;
            }
        }
    }
    tampilkanData(arr);
    Swal.fire({ toast: true, position: 'top-end', icon: 'success', title: 'Diurutkan pakai Bubble Sort', showConfirmButton: false, timer: 1500 });
});

// SELECTION SORT
document.getElementById('btnSelection').addEventListener('click', function() {
    let arr = [...dataMahasiswa];
    let n = arr.length;
    for (let i = 0; i < n; i++) {
        let max_idx = i;
        for (let j = i + 1; j < n; j++) {
            if (parseFloat(arr[j].ipk) > parseFloat(arr[max_idx].ipk)) {
                max_idx = j;
            }
        }
        let temp = arr[i]; arr[i] = arr[max_idx]; arr[max_idx] = temp;
    }
    tampilkanData(arr);
    Swal.fire({ toast: true, position: 'top-end', icon: 'success', title: 'Diurutkan pakai Selection Sort', showConfirmButton: false, timer: 1500 });
});

// RESET TAMPILAN
document.getElementById('btnReset').addEventListener('click', function() {
    tampilkanData(dataMahasiswa); 
});

// EXPORT KE EXCEL / CSV
document.getElementById('btnExport').addEventListener('click', function() {
    if(dataMahasiswa.length === 0) {
        Swal.fire('Data Kosong', 'Tidak ada data untuk di-download.', 'info');
        return;
    }
    let csvContent = "NIM,Nama,Kode MK,IPK\n";
    dataMahasiswa.forEach(mhs => {
        csvContent += `${mhs.nim},${mhs.nama},${mhs.kodeMk},${mhs.ipk}\n`;
    });
    let blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    let link = document.createElement("a");
    link.setAttribute("href", URL.createObjectURL(blob));
    link.setAttribute("download", "Data_Absensi_Mahasiswa.csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
});

// JALANKAN SAAT WEB DIBUKA
// ==========================================
// FITUR AUTO-LOAD DATA DARI CSV
// ==========================================

async function loadDataOtomatis() {
    try {
        // Minta browser membaca file CSV yang baru aja lu bikin pakai Python
        const response = await fetch('data_mahasiswa.csv');
        const dataText = await response.text();
        
        // Pisahkan teks per baris (enter)
        const baris = dataText.split('\n').filter(row => row.trim() !== '');
        
        // Buang baris pertama karena itu cuma judul kolom (NIM, Nama, dsb)
        baris.shift();
        
        let dataBaru = [];
        
        // Olah setiap baris jadi format yang dimengerti website lu
        baris.forEach(row => {
            const kolom = row.split(','); // Pisahkan berdasarkan koma
            if(kolom.length === 4) {
                dataBaru.push({
                    nim: kolom[0].trim(),
                    nama: kolom[1].trim(),
                    kodeMk: kolom[2].trim(),
                    ipk: parseFloat(kolom[3].trim()).toFixed(2)
                });
            }
        });
        
        // Timpa data lama dengan 300 data baru ini
        dataMahasiswa = dataBaru;
        
        // Simpan ke memori laptop
        localStorage.setItem('dataMaster', JSON.stringify(dataMahasiswa));
        
        // Tampilkan ke layar dengan animasi
        tampilkanData(dataMahasiswa);
        
        Swal.fire({
            toast: true, 
            position: 'top-end', 
            icon: 'success', 
            title: '300 Data Random Berhasil Dimuat!', 
            showConfirmButton: false, 
            timer: 3000 
        });

    } catch (error) {
        console.log("Error baca CSV:", error);
        // Kalau error (misal Live Server mati), tetap tampilkan data seadanya dari memori
        tampilkanData(dataMahasiswa);
    }
}

// Cek apakah data lu masih kosong atau sedikit? 
// Kalau kurang dari 10, otomatis sedot 300 data dari CSV!
if (dataMahasiswa.length < 300) {
    loadDataOtomatis();
} else {
    tampilkanData(dataMahasiswa);
}