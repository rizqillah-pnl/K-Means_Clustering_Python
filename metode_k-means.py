
import numpy as np
import os


def get_dataset():
    # dataset klasterisasi
    filename = os.path.dirname(__file__) + "\dataset.csv"
    dataset = np.genfromtxt(filename, delimiter=",")
    print("DATA POINT :\n", dataset)
    return dataset


def get_centroids():
    centroids = []
    centroids.append([0.92, 1.00])  # (C1)
    centroids.append([1.00, 0.46])  # (C2)
    centroids.append([0.35, 0.63])  # (C3)
    centroids.append([0.58, 0.13])  # (C4)
    centroids.append([0, 0.08])    # (C5)
    return np.array(centroids)


def hitung_euclidean_distance(dataset, centroid):
    return np.sqrt(np.sum((dataset - centroid)**2))


def iterasi_k_means(dataset, centroid):
    panjang_dataset = len(dataset)
    panjang_centroid = len(centroid)
    dataset_label = []
    label_cluster = []
    for i in range(panjang_dataset):  # 50 X
        hasil_euclid = []
        for j in range(panjang_centroid):  # 5 X
            hasil_euclid.append(
                hitung_euclidean_distance(dataset[i], centroid[j]))

        # nilai_terkecil = min(hasil_euclid)
        index_nilai_terkecil = hasil_euclid.index(min(hasil_euclid))
        label_cluster.append(index_nilai_terkecil)
        # array dua dimensi diappend lagi sehingga jadi array 3 dimensi
        dataset_label.append([[i], [index_nilai_terkecil]])

    # mendapatkan indeks label centroid
    indeks_label = []
    for i in range(panjang_centroid):
        for j in range(panjang_dataset):
            if i in dataset_label[j][1]:
                indeks_label.append([i, j])

    # mencari centroid baru
    new_centroid = []
    for y in range(panjang_centroid):
        centroidbaru = 0
        for x in range(panjang_dataset):
            if indeks_label[x][0] == y:
                # dataset[indeks_label[x][1] adalah array dua dimensi, sehingga otomatis variabel centroid baru berubah jadi array dua dimensi juga
                centroidbaru = centroidbaru + dataset[indeks_label[x][1]]

        # count() untuk mendapatkan jumlah masing2 label/cluster
        temp = centroidbaru/(label_cluster.count(y))
        new_centroid.append(temp)

    print("CENTROID BARU :", new_centroid)
    return new_centroid, label_cluster


if __name__ == '__main__':
    dataset = get_dataset()
    centroid = get_centroids()

    print("CENTROID AWAL :\n", centroid)

    temp_centroid = np.array("")

    while True:
        [centroid, label_cluster] = iterasi_k_means(
            dataset, centroid)
        # jika centroid lama SAMA DENGAN centroid baru
        # maka variabel ulang akan False ataupun perulangan while berhenti
        if np.array_equal(centroid, temp_centroid) == True:
            break
        temp_centroid = centroid

    print("\n----------------------------------------------------")
    print("------------------ HASIL CLUTERING -----------------")
    print("----------------------------------------------------")

    for i in range(len(dataset)):
        print("DATASET Ke{", i, "} :", dataset[i],
              "| Cluster :", label_cluster[i])
