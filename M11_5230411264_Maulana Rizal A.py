import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import mean_squared_error, accuracy_score
import os

# Fungsi untuk memproses data
def preprocess_data(file_name, target_column):
    try:
        # Memuat data
        data = pd.read_excel(file_name)
        print("\nData berhasil dimuat!")
        print("5 baris pertama data:\n", data.head())

        # Memastikan kolom target ada
        if target_column not in data.columns:
            print(f"\nKolom '{target_column}' tidak ditemukan dalam data.")
            return None, None, None, None

        # Memisahkan fitur dan target
        X = data.drop(columns=[target_column])
        y = data[target_column]

        # Membagi data menjadi data latih dan uji
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        print("\nPreprocessing selesai. Data siap digunakan.")
        return X_train, X_test, y_train, y_test

    except Exception as e:
        print(f"\nTerjadi kesalahan saat memproses data: {e}")
        return None, None, None, None

# Fungsi untuk analisis menggunakan algoritma tertentu
def analyze_data(algorithm, X_train, X_test, y_train, y_test):
    try:
        if algorithm == 'LinearRegression':
            model = LinearRegression()
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)
            mse = mean_squared_error(y_test, predictions)
            print(f"\nAnalisis selesai menggunakan {algorithm}.")
            print(f"Mean Squared Error: {mse}")
        elif algorithm == 'NaiveBayes':
            model = GaussianNB()
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)
            accuracy = accuracy_score(y_test, predictions)
            print(f"\nAnalisis selesai menggunakan {algorithm}.")
            print(f"Accuracy: {accuracy}")
        else:
            print("\nAlgoritma tidak dikenali. Pilih 'LinearRegression' atau 'NaiveBayes'.")
            return

    except Exception as e:
        print(f"\nTerjadi kesalahan selama analisis: {e}")

# Menu utama berbasis terminal
def main_menu():
    while True:
        print("\nMenu Utama:")
        print("1. Preprocessing Data")
        print("2. Analisis Data")
        print("3. Keluar")

        choice = input("Pilih menu (1/2/3): ")

        if choice == '1':
            file_name = input("Masukkan nama file (dengan ekstensi .xlsx): ")
            target_column = input("Masukkan nama kolom target: ")
            global X_train, X_test, y_train, y_test
            X_train, X_test, y_train, y_test = preprocess_data(file_name, target_column)
        elif choice == '2':
            if X_train is None or X_test is None or y_train is None or y_test is None:
                print("\nHarap lakukan preprocessing terlebih dahulu.")
            else:
                algorithm = input("Pilih algoritma ('LinearRegression' atau 'NaiveBayes'): ")
                analyze_data(algorithm, X_train, X_test, y_train, y_test)
        elif choice == '3':
            print("\nKeluar dari program. Terima kasih!")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = None, None, None, None
    main_menu()
