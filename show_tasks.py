import traceback


def show_tasks(task_data):
    """
    Yapılacaklar listesindeki tüm görevleri kategorilere ve öncelik sırasına göre gösterir.
    Tamamlanmış görevlerin durumunu ve tamamlama tarihini belirtir.
    Kullanıcı belirli bir kategoriyi seçerek filtreleme yapabilir.
    Liste boşsa, kullanıcıya bilgi verir.
    """
    try:
        print("\nYapılacaklar Listesi:")
        if not task_data:
            print("Liste şu anda boş.")
            return

        # Kullanıcıdan geçerli bir yanıt alana kadar tekrar sor
        while True:
            filter_choice = input("Görevleri belirli bir kategoriye göre filtrelemek ister misiniz? (E/H): ").lower()
            if filter_choice in ["e", "h"]:
                break
            else:
                print("Geçersiz giriş. Lütfen 'E' (evet) veya 'H' (hayır) girin.")

        if filter_choice == "e":
            category = input("Görüntülemek istediğiniz kategoriyi girin: ")
            if category in task_data:
                print(f"\nKategori: {category}")
                tasks = task_data[category]

                # Görevleri öncelik sırasına göre sıralamak
                sorted_tasks = sorted(tasks, key=lambda x: ["yüksek", "orta", "düşük"].index(x["priority"]))

                for i, task_info in enumerate(sorted_tasks, 1):
                    task = task_info["task"]
                    priority = task_info["priority"]
                    completed = task_info.get("completed", False)
                    completion_date = task_info.get("completion_date", "Henüz tamamlanmadı")
                    status = "Tamamlandı" if completed else "Devam Ediyor"
                    print(f"{i}. {task} (Öncelik: {priority}) - Durum: {status} - Tamamlama Tarihi: {completion_date}")
            else:
                print(f"'{category}' kategorisi mevcut değil.")
        else:
            # Tüm görevleri göster
            for category, tasks in task_data.items():
                print(f"\nKategori: {category}")
                sorted_tasks = sorted(tasks, key=lambda x: ["yüksek", "orta", "düşük"].index(x["priority"]))

                for i, task_info in enumerate(sorted_tasks, 1):
                    task = task_info["task"]
                    priority = task_info["priority"]
                    completed = task_info.get("completed", False)
                    completion_date = task_info.get("completion_date", "Henüz tamamlanmadı")
                    status = "Tamamlandı" if completed else "Devam Ediyor"
                    print(f"{i}. {task} (Öncelik: {priority}) - Durum: {status} - Tamamlama Tarihi: {completion_date}")
    except Exception as e:
        print("Bir hata oluştu:")
        traceback.print_exc()
