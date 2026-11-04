# ==========================================
# Nama: Farel Ilyasa Habbi Pratama 
# NIM: 25041450138 
# Kelas: 2583E
# Deskripsi: Program utama untuk menguji struktur graf dan deteksi siklus
# ==========================================

from module import Graph

if __name__ == "__main__":
    # Inisialisasi graf dengan 7 titik (vertex)
    jumlah_vertex = 7
    g = Graph(jumlah_vertex)
    
    # Penamaan vertex
    nama_vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    for i, nama in enumerate(nama_vertex):
        g.add_vertex_data(i, nama)

    # Menambahkan hubungan antar vertex (edges)
    edges = [
        (1, 0), (0, 3), (0, 2), (2, 3), 
        (3, 4), (3, 5), (3, 6), (4, 5)
    ]
    
    for u, v in edges:
        g.add_edge(u, v)

    # Menampilkan struktur
    g.print_graph()
    
    # Menjalankan deteksi siklus
    print("--- Pengecekan Siklus ---")
    status_siklus = g.is_cyclic()
    print(f"Hasil: Apakah graf memiliki siklus? {status_siklus}")