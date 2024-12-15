import json
import traceback

def load_tasks_from_file(filename="completed_tasks.json"):
    """
    JSON dosyasından görevleri yükler ve bir sözlük olarak döner.
    Eğer dosya yoksa veya okunamazsa, kullanıcıya bilgi verilir ve boş bir görev listesi döner.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            # JSON dosyasını yükle ve döndür
            return json.load(file)
    except FileNotFoundError:
        print(f"'{filename}' dosyası bulunamadı, boş bir görev listesiyle başlatılıyor.")
        return {}
    except json.JSONDecodeError:
        print(f"'{filename}' dosyasında okuma hatası. Boş bir görev listesiyle başlatılıyor.")
        return {}
    except Exception as e:
        print("Görevler yüklenirken bir hata oluştu:")
        traceback.print_exc()
        return {}
