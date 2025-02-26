# ✅ Yapılacaklar Listesi Uygulaması (To-Do List)

Bu **komut satırı tabanlı To-Do List uygulaması**, kullanıcıların yapılacak görevlerini düzenlemelerine, görev ekleyip silmelerine, tamamlanan görevleri işaretlemelerine ve görevlerini JSON formatında kaydetmelerine olanak tanır.

## 📌 Öne Çıkan Özellikler:
- ✅ **Görev Ekleme:** Yeni görev ekleyebilir ve kategorilere ayırabilirsiniz.
- ✅ **Görev Listeleme:** Görevleri **kategori ve öncelik seviyelerine** göre sıralayarak listeleyebilirsiniz.
- ✅ **Görev Silme:** İstenilen kategoriden bir görevi kaldırabilirsiniz.
- ✅ **Görev Tamamlama:** Bir görevi tamamlandı olarak işaretleyebilir ve tamamlanma tarihini kaydedebilirsiniz.
- ✅ **Veri Kaydetme:** Tüm görevleriniz **JSON dosyasında otomatik olarak saklanır ve yüklenir**.

---

## 📌 Kurulum

### **1️⃣ Gerekli Yazılımlar**
- **Python 3.7 veya üstü**  
- `json`, `traceback`, `datetime` (Python’un içinde gömülü olarak gelir)

### **2️⃣ Depoyu Klonlayın**
```bash
git clone https://github.com/saitsabuncu/to_do_list.git
cd to_do_list
```

### **3️⃣ Sanal Ortam (Virtual Environment) Kurun**
```bash
python -m venv .venv
```
### **4️⃣ Sanal Ortamı Aktif Edin**
**Windows için:**
```bash
.venv\Scripts\activate
```
**Mac/Linux için:**
```bash
source .venv/bin/activate
```

### **5️⃣ Bağımlılıkları Yükleyin (Eğer Gerekliyse)**
```bash
pip install -r requirements.txt
```

### **6️⃣ Uygulamayı Başlatın**
```bash
python main.py
```

---

## 📌 Kullanım

Program başladığında, aşağıdaki **ana menü** görüntülenecektir:

```
To-Do List Uygulaması
1. Görev Ekle
2. Görevleri Göster
3. Görev Sil
4. Görevleri Kaydet
5. Görev Tamamla
6. Çıkış
```

### **Örnek Kullanım Akışı**
- **Yeni görev eklemek için** `1` seçeneğini seçin, ardından kategori ve görev detaylarını girin.
- **Tüm görevleri görmek için** `2` seçeneğini kullanın.
- **Belirli bir görevi silmek için** `3` seçeneğini seçin ve kategori içinden silmek istediğiniz görevi girin.
- **JSON dosyasına kaydetmek için** `4` seçeneğini seçin.
- **Bir görevi tamamlandı olarak işaretlemek için** `5` seçeneğini seçin.

---

## 📌 JSON Veri Yapısı

Tüm görevler **completed_tasks.json** dosyasında saklanır.  
📌 **Örnek JSON yapısı:**
```json
{
    "Kişisel": [
        {
            "task": "Kitap oku",
            "priority": "orta",
            "completed": false,
            "completion_date": "Henüz tamamlanmadı"
        }
    ],
    "Dini": [
        {
            "task": "Sabah namazını kıl",
            "priority": "yüksek",
            "completed": true,
            "completion_date": "2024-11-17 06:44:09"
        }
    ]
}
```

---

## 📌 Proje Yapısı

📂 **Proje dizininde yer alan dosyalar:**  
```
to_do_list/
│── main.py              # Uygulamayı başlatan ana dosya
│── add_task.py          # Görev ekleme işlevleri
│── delete_task.py       # Görev silme işlevleri
│── show_tasks.py        # Görevleri listeleme ve gösterme
│── mark_complete.py     # Görevleri tamamlanmış olarak işaretleme
│── save_tasks.py        # Görevleri JSON dosyasına kaydetme
│── load_tasks.py        # Görevleri JSON dosyasından yükleme
   task_manager.py
│── completed_tasks.json # Görevlerin kaydedildiği dosya
```

---

## 📌 Katkıda Bulunma

🎯 **Projeye katkı sağlamak ister misiniz?** Yeni özellikler eklemek veya hataları düzeltmek için pull request gönderebilirsiniz!  

### **1️⃣ Katkı Süreci**
1. **Projeyi fork edin** ve kendi GitHub hesabınıza alın.
2. **Yeni bir branch açın** (`git checkout -b yeni-ozellik`).
3. **Değişiklikleri yapıp commitleyin** (`git commit -m "Yeni özellik eklendi"`).
4. **Değişikliklerinizi kendi deponuza push edin** (`git push origin yeni-ozellik`).
5. **Pull Request (PR) oluşturun ve katkınızı paylaşın!** 🚀

---

## 📌 Lisans

📝 **MIT Lisansı**  
Bu proje [MIT Lisansı](https://opensource.org/licenses/MIT) altında lisanslanmıştır.
