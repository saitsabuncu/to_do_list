import json
import traceback

def save_tasks_to_file(task_data, filename="completed_tasks.json"):
    """
    Görevleri JSON dosyasına kaydeder.
    Kullanıcıya kaydetme işlemi hakkında geri bildirim sağlar.
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            # Görevleri JSON formatında dosyaya yaz
            json.dump(task_data, file, indent=4, ensure_ascii=False)
            print(f"Görevler '{filename}' dosyasına başarıyla kaydedildi.")
    except Exception as e:
        print("Görevler kaydedilirken bir hata oluştu:")
        traceback.print_exc()
