import json
import traceback
from datetime import datetime


class Task:
    """Bir görevi temsil eden sınıf."""

    def __init__(self, description, category, priority="orta", completed=False, completion_date=None):
        self.description = description
        self.category = category
        self.priority = priority.lower() if priority in ["yüksek", "orta", "düşük"] else "orta"
        self.completed = completed
        self.completion_date = completion_date

    def mark_completed(self):
        """Görevi tamamlandı olarak işaretler ve tarih ekler."""
        self.completed = True
        self.completion_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """Nesneyi JSON'a uygun bir sözlük formatına çevirir."""
        return {
            "task": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "completion_date": self.completion_date if self.completed else "Henüz tamamlanmadı"
        }

    def __str__(self):
        status = "Tamamlandı" if self.completed else "Devam Ediyor"
        return f"{self.description} ({self.priority} öncelik) - Durum: {status} - Tamamlama Tarihi: {self.completion_date or 'Henüz tamamlanmadı'}"


class TaskManager:
    """Görev yönetimi için sınıf."""

    def __init__(self, filename="tasks.json"):
        self.filename = filename  # JSON dosya adı
        self.tasks = self.load_tasks_from_file()  # Başlangıçta görevleri yükle

    def load_tasks_from_file(self):
        """JSON dosyasından görevleri yükler ve bir sözlük olarak döndürür."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return {category: [Task(**task) for task in tasks] for category, tasks in data.items()}
        except FileNotFoundError:
            print(f"'{self.filename}' dosyası bulunamadı, boş bir görev listesiyle başlatılıyor.")
            return {}
        except json.JSONDecodeError:
            print(f"'{self.filename}' dosyasında okuma hatası. Boş bir görev listesiyle başlatılıyor.")
            return {}
        except Exception:
            print("Görevler yüklenirken bir hata oluştu:")
            traceback.print_exc()
            return {}

    def save_tasks_to_file(self):
        """Görevleri JSON dosyasına kaydeder."""
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump({category: [task.to_dict() for task in tasks] for category, tasks in self.tasks.items()},
                          file, indent=4, ensure_ascii=False)
            print(f"Görevler başarıyla '{self.filename}' dosyasına kaydedildi.")
        except Exception:
            print("Görevler kaydedilirken bir hata oluştu:")
            traceback.print_exc()

    def add_task(self, category, task_description, priority="orta"):
        """Yeni bir görev ekler ve kaydeder."""
        if category not in self.tasks:
            self.tasks[category] = []

        new_task = Task(task_description, category, priority)
        self.tasks[category].append(new_task)
        print(f"'{task_description}' görevi '{category}' kategorisine eklendi.")

        self.save_tasks_to_file()  # Her eklemeden sonra dosyayı güncelle

    def list_tasks(self, category_filter=None):
        """Tüm görevleri listele veya belirli bir kategoriyi göster."""
        try:
            print("\nYapılacaklar Listesi:")
            if not self.tasks:
                print("Liste şu anda boş.")
                return

            if category_filter:
                if category_filter in self.tasks:
                    print(f"\nKategori: {category_filter}")
                    tasks = sorted(self.tasks[category_filter],
                                   key=lambda x: ["yüksek", "orta", "düşük"].index(x.priority))
                    for i, task in enumerate(tasks, 1):
                        print(f"{i}. {task}")
                else:
                    print(f"'{category_filter}' kategorisi mevcut değil.")
            else:
                # Tüm görevleri göster
                for category, tasks in self.tasks.items():
                    print(f"\nKategori: {category}")
                    sorted_tasks = sorted(tasks, key=lambda x: ["yüksek", "orta", "düşük"].index(x.priority))
                    for i, task in enumerate(sorted_tasks, 1):
                        print(f"{i}. {task}")

        except Exception:
            print("Görevleri listelerken bir hata oluştu:")
            traceback.print_exc()

    def complete_task(self, category, task_number):
        """Belirli bir görevi tamamlanmış olarak işaretler."""
        try:
            if category in self.tasks and 1 <= task_number <= len(self.tasks[category]):
                task = self.tasks[category][task_number - 1]
                task.mark_completed()
                print(f"'{task.description}' görevi tamamlandı olarak işaretlendi.")
                self.save_tasks_to_file()
            else:
                print("Geçersiz kategori veya görev numarası!")
        except Exception:
            print("Görevi tamamlarken bir hata oluştu:")
            traceback.print_exc()

    def start(self):
        """Ana menüyü çalıştırır."""
        while True:
            print("\n1. Görev Ekle")
            print("2. Görevleri Listele")
            print("3. Belirli Kategorideki Görevleri Listele")
            print("4. Görev Tamamla")
            print("5. Çıkış")
            choice = input("Seçiminizi yapın: ")

            if choice == "1":
                category = input("Kategori adı: ")
                task_description = input("Görev açıklaması: ")
                priority = input("Öncelik (yüksek, orta, düşük): ").lower()
                self.add_task(category, task_description, priority)
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                category_filter = input("Görüntülemek istediğiniz kategori: ")
                self.list_tasks(category_filter)
            elif choice == "4":
                category = input("Hangi kategorideki görevi tamamlamak istiyorsunuz?: ")
                self.list_tasks(category)
                try:
                    task_number = int(input("Tamamlamak istediğiniz görevin numarasını girin: "))
                    self.complete_task(category, task_number)
                except ValueError:
                    print("Lütfen geçerli bir sayı girin!")
            elif choice == "5":
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçerli bir seçenek girin.")


# Uygulamayı başlat
if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.start()
