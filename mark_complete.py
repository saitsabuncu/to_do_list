import traceback
from datetime import datetime

def mark_task_complete(task_data):
    """
    Kullanıcının belirli bir görevi tamamlanmış olarak işaretlemesini sağlar ve tamamlama tarihini ekler.
    Görevin durumu 'Tamamlandı' olarak güncellenir ve tarih bilgisi eklenir.
    """
    try:
        while True:
            # Kullanıcıdan tamamlamak istediği görevi sor
            category = input("Hangi kategoriden bir görevi tamamlanmış olarak işaretlemek istiyorsunuz?: ")
            if category in task_data:
                task = input(f"{category} kategorisinden tamamlanmış olarak işaretlemek istediğiniz görevi girin: ")
                found = False
                for t in task_data[category]:
                    if t["task"] == task:
                        # Görevi tamamlanmış olarak işaretle ve tarih ekle
                        t["completed"] = True
                        t["completion_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        found = True
                        print(f"'{task}' görevi '{category}' kategorisinde tamamlandı olarak işaretlendi.")
                        break
                if not found:
                    print(f"'{task}' görevi '{category}' kategorisinde bulunamadı.")
            else:
                print("Bu kategori mevcut değil.")

            # Kullanıcıya başka bir görev işaretleyip işaretlemeyeceğini sor
            another = input("Başka bir görevi tamamlanmış olarak işaretlemek ister misiniz? (E/H): ").lower()
            if another == "e":
                continue
            else:
                print("Ana menüye dönülüyor...")
                break
    except Exception as e:
        print("Bir hata oluştu:")
        traceback.print_exc()
