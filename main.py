from add_task import *
from delete_task import *
from show_tasks import *
from save_tasks import *
from mark_complete import *
from load_tasks import *  # Görev yükleme fonksiyonunu içe aktar

# Program başladığında görevleri JSON dosyasından yükle
to_do_list = load_tasks_from_file()

# Ana uygulama döngüsü
try:
    while True:
        # Kullanıcıya ana menüyü göster ve seçim yapmasını iste
        print("\nTo-Do List Uygulaması")
        print("1. Görev Ekle")
        print("2. Görevleri Göster")
        print("3. Görev Sil")
        print("4. Görevleri Kaydet")
        print("5. Görev Tamamla")
        print("6. Çıkış")

        # Kullanıcı girişini al ve seçime göre işlem yap
        choice = input("Seçiminiz (1/2/3/4/5/6): ")

        if choice == "1":
            add_task(to_do_list)
        elif choice == "2":
            show_tasks(to_do_list)
        elif choice == "3":
            delete_task(to_do_list)
        elif choice == "4":
            save_tasks_to_file(to_do_list)
        elif choice == "5":
            mark_task_complete(to_do_list)
        elif choice == "6":
            print("Uygulamadan çıkılıyor...")
            break
        else:
            # Geçersiz girişler için geri bildirim
            print("Geçersiz bir seçenek girdiniz. Lütfen 1, 2, 3, 4, 5 veya 6 seçeneklerinden birini girin.")
except Exception as e:
    print("Bir hata oluştu:")
    traceback.print_exc()