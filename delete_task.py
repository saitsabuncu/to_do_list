import traceback

def delete_task(task_data):
    """
    Kullanıcının belirli bir kategoriden bir görevi silmesini sağlar.
    Kullanıcıdan kategori ve görev adı istenir. Eğer görev ve kategori bulunamazsa, anlamlı geri bildirim verilir.
    """
    try:
        while True:
            # Kullanıcıdan silmek istediği kategoriyi ve görevi al
            category = input("Hangi kategoriden görev silmek istiyorsunuz?: ")
            if category in task_data:
                task = input(f"{category} kategorisinden silmek istediğiniz görevi girin: ")
                # Görevin listede olup olmadığını kontrol et
                if task in [t["task"] for t in task_data[category]]:
                    # Görevi kategoriden sil
                    task_data[category] = [t for t in task_data[category] if t["task"] != task]
                    print(f"'{task}' görevi '{category}' kategorisinden silindi.")
                else:
                    print(f"'{task}' görevi '{category}' kategorisinde bulunamadı.")
            else:
                print("Bu kategori mevcut değil.")

            # Kullanıcıya başka bir görev silmek isteyip istemediğini sor
            another = input("Başka bir görev silmek ister misiniz? (E/H): ").lower()
            if another == "e":
                continue
            else:
                print("Ana menüye dönülüyor...")
                break
    except Exception as e:
        print("Bir hata oluştu:")
        traceback.print_exc()  # Hatanın detaylarını gösterir