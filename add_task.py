import traceback

class Task:
    """Bir görevi temsil eden sınıf."""
    def __init__(self, description, category, priority="orta"):
        self.description = description
        self.category = category
        self.priority = priority.lower() if priority in ["yüksek", "orta", "düşük"] else "orta"

    def __str__(self):
        return f"{self.description} ({self.priority} öncelik)"

class TaskManager:
    """Görev yönetimi için sınıf."""
    def __init__(self):
        self.tasks = {}  # Görevleri kategori bazında saklayan sözlük
        self.last_added_task = None  # Geri alma işlemi için son eklenen görev

    def add_task(self):
        """Kullanıcıdan görev bilgilerini alıp ekler."""
        try:
            description = input("Eklemek istediğiniz görevi girin: ")
            category = input("Bu görevi hangi kategoriye eklemek istiyorsunuz?: ")
            priority = input("Bu görevin önceliğini girin (yüksek, orta, düşük): ").lower()

            # Geçersiz öncelik seviyesini 'orta' olarak ayarla
            if priority not in ["yüksek", "orta", "düşük"]:
                print("Geçersiz öncelik seviyesi girildi. Otomatik olarak 'orta' olarak ayarlandı.")
                priority = "orta"

            # Yeni kategori oluştur
            if category not in self.tasks:
                self.tasks[category] = []
                print(f"Yeni kategori '{category}' oluşturuldu.")

            # Yeni görevi oluştur ve listeye ekle
            new_task = Task(description, category, priority)
            self.tasks[category].append(new_task)
            self.last_added_task = (category, new_task)

            print(f"Görev eklendi: {new_task}")

            # Geri alma seçeneği
            self.undo_task()

        except Exception:
            print("Bir hata oluştu:")
            traceback.print_exc()

    def undo_task(self):
        """Son eklenen görevi geri alma işlemi."""
        if self.last_added_task:
            category, task = self.last_added_task
            while True:
                undo = input(f"'{task.description}' görevini geri almak ister misiniz? (E/H): ").lower()
                if undo == "e":
                    self.tasks[category].remove(task)
                    print(f"'{task.description}' görevi geri alındı.")
                    self.last_added_task = None
                    break
                elif undo == "h":
                    print("Görev kaydedildi.")
                    break
                else:
                    print("Geçersiz giriş. Lütfen 'E' (evet) veya 'H' (hayır) girin.")

    def list_tasks(self):
        """Tüm görevleri listele."""
        if not self.tasks:
            print("Henüz eklenmiş bir görev bulunmuyor.")
            return
        
        print("\nGörev Listesi:")
        for category, tasks in self.tasks.items():
            print(f"\nKategori: {category}")
            for idx, task in enumerate(tasks, 1):
                print(f"  {idx}. {task}")
        print()

    def start(self):
        """Ana menüyü çalıştırır."""
        while True:
            print("\n1. Görev Ekle")
            print("2. Görevleri Listele")
            print("3. Çıkış")
            choice = input("Seçiminizi yapın: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçerli bir seçenek girin.")

# Uygulamayı başlat
if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.start()
