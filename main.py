from task_manager import TaskManager

# TaskManager nesnesi oluştur
task_manager = TaskManager()

# Ana uygulama döngüsü
try:
    while True:
        print("\nTo-Do List Uygulaması")
        print("1. Görev Ekle")
        print("2. Görevleri Göster")
        print("3. Görevleri Kaydet")
        print("4. Görev Tamamla")
        print("5. Çıkış")

        choice = input("Seçiminiz (1/2/3/4/5): ")

        if choice == "1":
            category = input("Kategori adı: ")
            task_description = input("Görev açıklaması: ")
            priority = input("Öncelik (yüksek, orta, düşük): ").lower()
            task_manager.add_task(category, task_description, priority)

        elif choice == "2":
            task_manager.list_tasks()

        elif choice == "3":
            task_manager.save_tasks_to_file()

        elif choice == "4":
            task_manager.complete_task()

        elif choice == "5":
            print("Uygulamadan çıkılıyor...")
            break

        else:
            print("Geçersiz bir seçenek girdiniz. Lütfen 1-5 arasında bir değer girin.")

except Exception as e:
    print("Bir hata oluştu:")
    import traceback
    traceback.print_exc()
