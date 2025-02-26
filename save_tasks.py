import json
import traceback


class TaskManager:
    """Görev yönetimi için sınıf."""

    def __init__(self, filename="completed_tasks.json"):
        self.filename = filename  # JSON dosya adı
        self.tasks = self.load_tasks_from_file()  # Başlangıçta görevleri yükle

    def load_tasks_from_file(self):
        """JSON dosyasından görevleri yükler ve bir sözlük olarak döndürür."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
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
                json.dump(self.tasks, file, indent=4, ensure_ascii=False)
            print(f"Görevler başarıyla '{self.filename}' dosyasına kaydedildi.")
        except Exception:
            print("Görevler kaydedilirken bir hata oluştu:")
            traceback.print_exc()

    def add_task(self, category, task_description, priority="orta"):
        """Yeni bir görev ekler ve kaydeder."""
        if category not in self.tasks:
            self.tasks[category] = []

        new_task = {"task": task_description, "priority": priority}
        self.tasks[category].append(new_task)
        print(f"'{task_description}' görevi '{category}' kategorisine eklendi.")

        self.save_tasks_to_file()  # Her eklemeden sonra dosyayı güncelle

    def list_tasks(self):
        """Tüm görevleri listele."""
        if not self.tasks:
            print("Henüz eklenmiş bir görev bulunmuyor.")
            return

        print("\nGörev Listesi:")
        for category, tasks in self.tasks.items():
            print(f"\nKategori: {category}")
            for idx, task in enumerate(tasks, 1):
                print(f"  {idx}. {task['task']} ({task['priority']} öncelik)")
        print()


# Uygulamayı başlat
if __name__ == "__main__":
    task_manager = TaskManager()

    # Örnek kullanım
    task_manager.add_task("İş", "Raporu tamamla", "yüksek")
    task_manager.add_task("Ev", "Bulaşıkları yıka", "orta")
    task_manager.list_tasks()
