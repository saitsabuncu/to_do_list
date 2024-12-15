# Yapılacaklar Listesi Uygulaması (To-Do List)

Bu uygulama, kullanıcıların yapılacak görevlerini yönetebilmeleri için bir komut satırı tabanlı yapılacaklar listesi sistemidir. Görev ekleme, silme, tamamlanmış olarak işaretleme ve listeleme gibi temel özellikler içerir.

## Özellikler

- **Görev Ekleme**: Yeni bir görev ekleyebilir ve kategorilere ayırabilirsiniz.
- **Görev Listeleme**: Görevleri kategori ve öncelik seviyelerine göre görüntüleyebilirsiniz.
- **Görev Silme**: Belirli bir kategoriden istenilen görevi silebilirsiniz.
- **Görev Tamamlama**: Görevleri tamamlanmış olarak işaretleyebilir ve tamamlama tarihlerini kaydedebilirsiniz.
- **Görev Kaydetme ve Yükleme**: Görevler otomatik olarak bir JSON dosyasına kaydedilir ve yüklenir.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki yazılımlara ihtiyacınız vardır:

- Python 3.7 veya üzeri
- `json`, `traceback`, `datetime` (Python ile birlikte gelir)

## Kurulum

1. Proje dosyalarını bilgisayarınıza indirin.
2. Terminal veya komut istemcisinde projenin bulunduğu dizine gidin.
3. Aşağıdaki komutu çalıştırarak uygulamayı başlatın:
   ```bash
   python main.py
   ```

## Kullanım

Program başladığında, aşağıdaki menü karşınıza çıkacaktır:
```
To-Do List Uygulaması
1. Görev Ekle
2. Görevleri Göster
3. Görev Sil
4. Görevleri Kaydet
5. Görev Tamamla
6. Çıkış
```

### Örnek İş Akışı

1. Görev eklemek için **1** tuşuna basarak "Görev Ekle" seçeneğini seçin.
2. Görevleri görüntülemek için **2** tuşuna basarak "Görevleri Göster" seçeneğini kullanın.
3. Bir görevi silmek için **3** tuşuna basarak ilgili görevi kategorisinden çıkarabilirsiniz.
4. Görevlerinizi kaydetmek için **4** tuşuna basarak JSON dosyasına kaydedin.
5. Görevlerinizi tamamlanmış olarak işaretlemek için **5** tuşuna basın.

### JSON Dosya Yapısı

Görevleriniz `completed_tasks.json` dosyasında saklanır. Dosya yapısı şu şekildedir:
```json
{
    "Kişisel": [],
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

## Proje Yapısı

- **`main.py`**: Ana menü ve uygulamanın giriş noktası.
- **`add_task.py`**: Yeni görev ekleme işlevi.
- **`delete_task.py`**: Görev silme işlevi.
- **`show_tasks.py`**: Görevleri listeleme ve görüntüleme işlevi.
- **`mark_complete.py`**: Görevleri tamamlanmış olarak işaretleme işlevi.
- **`save_tasks.py`**: Görevleri JSON dosyasına kaydetme işlevi.
- **`load_tasks.py`**: Görevleri JSON dosyasından yükleme işlevi.

## Katkıda Bulunma

Proje hakkında öneri ve geliştirmeler için pull request'ler kabul edilir. Lütfen önerileriniz için bir **issue** açmayı unutmayın.

## Lisans

Bu proje [MIT Lisansı](https://opensource.org/licenses/MIT) altında lisanslanmıştır.
