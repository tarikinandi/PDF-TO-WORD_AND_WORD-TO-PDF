# PDF ve Word Dönüştürücü

Modern, kullanıcı dostu bir PDF ve Word dönüştürücü uygulaması. PDF dosyalarını Word'e ve Word dosyalarını PDF'e, orijinal formatlarını koruyarak dönüştürün.


## Özellikler

- **PDF'den Word'e Dönüştürme**: PDF dosyalarını DOCX formatına dönüştürün  
- **Word'den PDF'e Dönüştürme**: DOCX dosyalarını PDF formatına dönüştürün  
- **Format Koruma**: Yazı tipleri, düzen ve resimleri koruma seçenekleri  
- **Gelişmiş Yazı Tipi İşleme**: Daha iyi yazı tipi koruması için gelişmiş analiz  
- **Modern Arayüz**: Bootstrap tarzı, kullanıcı dostu arayüz  
- **İlerleme Takibi**: Dönüştürme işlemi sırasında gerçek zamanlı ilerleme gösterimi  

## Kurulum

### Gereksinimler

- Python 3.6 veya daha yeni bir sürüm
- pip (Python paket yöneticisi)
- Microsoft Word (Word'den PDF'e dönüşüm için)

### Adımlar

1. Bu depoyu klonlayın:
   ```bash
   git clone https://github.com/kullaniciadi/pdf-word-donusturucu.git
   cd pdf-word-donusturucu
   ```

2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

3. Uygulamayı çalıştırın:
   ```bash
   python main.py
   ```

## Kullanım

1. **Dosya Seçimi**:  
   - "Gözat" butonuna tıklayarak dönüştürmek istediğiniz dosyayı seçin  
   - PDF'den Word'e dönüştürmek için bir PDF dosyası seçin  
   - Word'den PDF'e dönüştürmek için bir Word dosyası seçin  

2. **Çıktı Ayarları**:  
   - "Çıktı Adı" alanına, oluşturulacak dosyanın adını girin  
   - Uzantı (.pdf veya .docx) otomatik olarak eklenecektir  

3. **Format Koruma Seçenekleri**:  
   - "Yazı tiplerini koru" seçeneği, yazı tiplerinin korunmasını sağlar  
   - "Sayfa düzenini koru" seçeneği, sayfa düzeninin korunmasını sağlar  
   - "Resimleri koru" seçeneği, resimlerin korunmasını sağlar  
   - "Gelişmiş yazı tipi işleme" seçeneği, daha iyi yazı tipi koruması sağlar  

4. **Dönüştürme**:  
   - PDF'den Word'e dönüştürmek için "PDF → Word" butonuna tıklayın  
   - Word'den PDF'e dönüştürmek için "Word → PDF" butonuna tıklayın  

## Proje Yapısı

```
pdf_word_converter/
│
├── main.py                  # Ana uygulama başlatıcı
├── requirements.txt         # Bağımlılıklar
│
├── config/                  # Konfigürasyon dosyaları
│   ├── __init__.py
│   └── settings.py          # Uygulama ayarları
│
├── core/                    # Çekirdek dönüştürücü modülleri
│   ├── __init__.py
│   ├── converter.py         # Dönüştürme işlemleri için soyut sınıf
│   ├── pdf_to_word.py       # PDF'den Word'e dönüştürücü
│   └── word_to_pdf.py       # Word'den PDF'e dönüştürücü
│
├── ui/                      # Kullanıcı arayüzü modülleri
│   ├── __init__.py
│   ├── app.py               # Ana uygulama sınıfı
│   ├── components.py        # UI bileşenleri
│   └── styles.py            # UI stilleri
│
└── utils/                   # Yardımcı fonksiyonlar
    ├── __init__.py
    ├── file_utils.py        # Dosya işlemleri
    └── font_analyzer.py     # Yazı tipi analizi
```

## Mimari

Bu proje, SOLID prensiplerine ve Clean Code yaklaşımına uygun olarak tasarlanmıştır:

- **Single Responsibility Principle (SRP)**: Her sınıf ve modül yalnızca bir sorumluluğa sahiptir  
- **Open/Closed Principle (OCP)**: Kod, genişletmeye açık ancak değiştirmeye kapalıdır  
- **Liskov Substitution Principle (LSP)**: Alt sınıflar, üst sınıfların yerine geçebilir  
- **Interface Segregation Principle (ISP)**: Sınıflar, ihtiyaç duymadıkları arayüzlere bağımlı değildir  
- **Dependency Inversion Principle (DIP)**: Yüksek seviyeli modüller, düşük seviyeli modüllere bağımlı değildir  

## Bağımlılıklar

- [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap): Bootstrap tarzı arayüz için  
- [pdf2docx](https://github.com/dothinking/pdf2docx): PDF'den Word'e dönüştürme için  
- [docx2pdf](https://github.com/AlJohri/docx2pdf): Word'den PDF'e dönüştürme için  
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF): PDF yazı tipi analizi için  

## Sorun Giderme

### Modül Bulunamadı Hatası
- `ModuleNotFoundError` alırsanız, gerekli kütüphaneleri yüklediğinizden emin olun  
- `pip install -r requirements.txt` komutunu tekrar çalıştırın  

### Word'den PDF'e Dönüşüm Hatası
- Microsoft Word'ün yüklü ve çalışır durumda olduğundan emin olun  
- Word'ün otomatik makroları çalıştırmasına izin verildiğinden emin olun  

### PDF'den Word'e Dönüşüm Sorunları
- Karmaşık formatlı PDF'lerde bazı yazı tipleri veya düzen özellikleri tam olarak korunamayabilir  
- Daha iyi sonuçlar için "Gelişmiş yazı tipi işleme" seçeneğini etkinleştirin  


**Not**: Bu uygulama, PDF ve Word dönüşümlerinin mükemmel olacağını garanti etmez. Karmaşık formatlı dosyalarda bazı özellikler tam olarak korunamayabilir.
