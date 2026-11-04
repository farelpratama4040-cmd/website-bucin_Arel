Nama    ; Kms Muhammad Al Qodri
NIM     : 25041450145
Kelas   : 2583E

<?php
// ==========================================
// 1. DEKLARASI KONSTANTA
// ==========================================
define("PHI", 3.14159);

$hasil = null;

// Cek jika tombol submit ditekan
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // 2. INPUT DATA DARI FORM (VARIABEL)
    $nama = htmlspecialchars($_POST['nama'] ?? '');
    $nim  = htmlspecialchars($_POST['nim'] ?? '');
    $r    = (float) ($_POST['r'] ?? 0);
    $t    = (float) ($_POST['t'] ?? 0);

    // 3. PROSES ARITMATIKA BANGUN RUANG (TABUNG)
    $volume = PHI * ($r ** 2) * $t;
    $luas_permukaan = 2 * PHI * $r * ($r + $t);

    $hasil = [
        'nama' => $nama,
        'nim' => $nim,
        'r' => $r,
        't' => $t,
        'volume' => $volume,
        'luas_permukaan' => $luas_permukaan
    ];
}
?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Latihan Variabel, Konstanta & Aritmatika</title>
    <style>
        body { font-family: sans-serif; margin: 30px; background-color: #f4f6f9; }
        .container { max-width: 500px; background: #fff; padding: 25px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin: auto; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input[type="text"], input[type="number"] { width: 100%; padding: 8px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px; }
        button { background-color: #007bff; color: white; border: none; padding: 10px 15px; border-radius: 4px; cursor: pointer; width: 100%; font-size: 16px; }
        button:hover { background-color: #0056b3; }
        .result-box { margin-top: 25px; padding: 15px; background: #e9ecef; border-left: 5px solid #007bff; border-radius: 4px; }
        .result-box table { width: 100%; border-collapse: collapse; }
        .result-box td { padding: 4px 0; }
    </style>
</head>
<body>

<div class="container">
    <h2>Form Perhitungan Tabung</h2>
    <form action="" method="POST">
        <div class="form-group">
            <label>Nama Lengkap:</label>
            <input type="text" name="nama" required>
        </div>
        <div class="form-group">
            <label>NIM:</label>
            <input type="text" name="nim" required>
        </div>
        <div class="form-group">
            <label>Jari-jari (r) cm:</label>
            <input type="number" step="any" name="r" required>
        </div>
        <div class="form-group">
            <label>Tinggi (t) cm:</label>
            <input type="number" step="any" name="t" required>
        </div>
        <button type="submit">Hitung & Cetak Data</button>
    </form>

    <?php if ($hasil): ?>
        <!-- 4. CETAK SEMUA DATA YANG DIINPUT & DIPROSES -->
        <div class="result-box">
            <h3>Hasil Perhitungan:</h3>
            <table>
                <tr><td><strong>Nama Lengkap</strong></td><td>: <?= $hasil['nama']; ?></td></tr>
                <tr><td><strong>NIM</strong></td><td>: <?= $hasil['nim']; ?></td></tr>
                <tr><td><strong>Konstanta PHI</strong></td><td>: <?= PHI; ?></td></tr>
                <tr><td><strong>Jari-jari (r)</strong></td><td>: <?= $hasil['r']; ?> cm</td></tr>
                <tr><td><strong>Tinggi (t)</strong></td><td>: <?= $hasil['t']; ?> cm</td></tr>
                <tr><td colspan="2"><hr></td></tr>
                <tr><td><strong>Volume Tabung</strong></td><td>: <?= number_format($hasil['volume'], 2); ?> cm³</td></tr>
                <tr><td><strong>Luas Permukaan</strong></td><td>: <?= number_format($hasil['luas_permukaan'], 2); ?> cm²</td></tr>
            </table>
        </div>  
    <?php endif; ?>
</div>

</body>
</html>