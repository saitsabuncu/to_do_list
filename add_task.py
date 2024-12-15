import traceback

def add_task(task_data):
    """
    Yapılacaklar listesine yeni bir görev ekler.
    Kullanıcıdan eklemek istediği görevi, kategori ve öncelik seviyesini alır ve ilgili kategoride saklar.
    """
    last_added_task = None  # Son eklenen görevi kaydetmek için

    try:
        while True:
            # Kullanıcıdan görev detaylarını al
            task = input("Eklemek istediğiniz görevi girin: ")
            category = input("Bu görevi hangi kategoriye eklemek istiyorsunuz?: ")
            priority = input("Bu görevin önceliğini girin (yüksek, orta, düşük): ").lower()

            # Geçersiz öncelik seviyelerini "orta" olarak ayarla ve bilgilendir
            if priority not in ["yüksek", "orta", "düşük"]:
                print("Geçersiz öncelik seviyesi girildi. Otomatik olarak 'orta' olarak ayarlandı.")
                priority = "orta"

            # Yeni bir kategori oluşturulup oluşturulmadığını kontrol et
            if category not in task_data:
                task_data[category] = []
                print(f"Yeni kategori '{category}' oluşturuldu.")

            # Görevi listeye ekle
            new_task = {"task": task, "priority": priority}
            task_data[category].append(new_task)
            last_added_task = (category, new_task)  # Son eklenen görevi kaydet

            # Kullanıcıya eklenen görevi geri alıp almak istemediğini sor
            while True:
                undo = input("Bu görevi geri almak ister misiniz? (E/H): ").lower()
                if undo == "e":
                    task_data[category].remove(new_task)
                    print(f"'{task}' görevi geri alındı.")
                    last_added_task = None
                    break
                elif undo == "h":
                    print("Görev kaydedildi.")
                    break
                else:
                    print("Geçersiz giriş. Lütfen 'E' (evet) veya 'H' (hayır) girin.")

            # Başka bir görev eklemek isteyip istemediğini sor
            while True:
                another = input("Başka bir görev eklemek ister misiniz? (E/H): ").lower()
                if another in ["e", "h"]:
                    break
                else:
                    print("Geçerli bir yanıt girin: 'E' (evet) veya 'H' (hayır).")

            if another == "e":
                continue
            else:
                print("Ana menüye dönülüyor...")
                break
    except Exception as e:
        print("Bir hata oluştu:")
        traceback.print_exc()