import os
import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pdf2docx import Converter as PDFtoWordConverter
from docx2pdf import convert as word_to_pdf_convert
import fitz  # PyMuPDF kütüphanesi

class FileConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF ve Word Dönüştürücü")
        self.root.geometry("700x700")
        
        # Ana çerçeve
        main_frame = ttk.Frame(root, padding=20)
        main_frame.pack(fill=BOTH, expand=YES)
        
        # Başlık
        title_frame = ttk.Frame(main_frame)
        title_frame.pack(fill=X, pady=(0, 20))
        
        # Logo/İkon (emoji kullanarak basit bir logo)
        logo_label = ttk.Label(title_frame, text="🔄", font=("Arial", 28))
        logo_label.pack(pady=(0, 5))
        
        title_label = ttk.Label(
            title_frame, 
            text="PDF ve Word Dönüştürücü", 
            font=("Helvetica", 22, "bold"),
            bootstyle="primary"
        )
        title_label.pack()
        
        subtitle_label = ttk.Label(
            title_frame, 
            text="Dosyalarınızı orijinal formatını koruyarak dönüştürün", 
            font=("Helvetica", 11),
            bootstyle="secondary"
        )
        subtitle_label.pack(pady=(5, 0))
        
        # Ayırıcı çizgi
        separator = ttk.Separator(main_frame)
        separator.pack(fill=X, pady=15)
        
        # Dosya seçme bölümü
        file_frame = ttk.Labelframe(
            main_frame, 
            text="Dosya Seçimi", 
            padding=15,
            bootstyle="primary"
        )
        file_frame.pack(fill=X, pady=10)
        
        file_content = ttk.Frame(file_frame)
        file_content.pack(fill=X)
        
        ttk.Label(file_content, text="Dosya:").grid(row=0, column=0, padx=5, pady=10, sticky="w")
        
        self.file_path_var = tk.StringVar()
        file_entry = ttk.Entry(file_content, textvariable=self.file_path_var, width=50)
        file_entry.grid(row=0, column=1, padx=5, pady=10)
        
        browse_button = ttk.Button(
            file_content, 
            text="Gözat", 
            command=self.browse_file, 
            bootstyle="info",
            width=10
        )
        browse_button.grid(row=0, column=2, padx=5, pady=10)
        
        # Çıktı adı bölümü
        output_frame = ttk.Labelframe(
            main_frame, 
            text="Çıktı Ayarları", 
            padding=15,
            bootstyle="primary"
        )
        output_frame.pack(fill=X, pady=10)
        
        output_content = ttk.Frame(output_frame)
        output_content.pack(fill=X)
        
        ttk.Label(output_content, text="Çıktı Adı:").grid(row=0, column=0, padx=5, pady=10, sticky="w")
        
        self.output_name_var = tk.StringVar()
        output_entry = ttk.Entry(output_content, textvariable=self.output_name_var, width=50)
        output_entry.grid(row=0, column=1, padx=5, pady=10, columnspan=2)
        
        # Format koruma seçenekleri
        format_frame = ttk.Labelframe(
            main_frame, 
            text="Format Koruma Seçenekleri", 
            padding=15,
            bootstyle="primary"
        )
        format_frame.pack(fill=X, pady=10)
        
        format_content = ttk.Frame(format_frame)
        format_content.pack(fill=X)
        
        # Yazı tipi koruma seçeneği
        self.preserve_font_var = tk.BooleanVar(value=True)
        font_check = ttk.Checkbutton(
            format_content, 
            text="Yazı tiplerini koru", 
            variable=self.preserve_font_var,
            bootstyle="round-toggle"
        )
        font_check.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        # Düzen koruma seçeneği
        self.preserve_layout_var = tk.BooleanVar(value=True)
        layout_check = ttk.Checkbutton(
            format_content, 
            text="Sayfa düzenini koru", 
            variable=self.preserve_layout_var,
            bootstyle="round-toggle"
        )
        layout_check.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Resim koruma seçeneği
        self.preserve_images_var = tk.BooleanVar(value=True)
        images_check = ttk.Checkbutton(
            format_content, 
            text="Resimleri koru", 
            variable=self.preserve_images_var,
            bootstyle="round-toggle"
        )
        images_check.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
        # Gelişmiş yazı tipi işleme seçeneği
        self.advanced_font_var = tk.BooleanVar(value=True)
        advanced_font_check = ttk.Checkbutton(
            format_content, 
            text="Gelişmiş yazı tipi işleme", 
            variable=self.advanced_font_var,
            bootstyle="round-toggle"
        )
        advanced_font_check.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        # BUTONLAR - ÖNEMLİ BÖLÜM
        # Dönüşüm butonları için ayrı bir çerçeve
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        # PDF'den Word'e dönüştürme butonu
        self.pdf_to_word_button = ttk.Button(
            button_frame, 
            text="PDF → Word", 
            command=self.pdf_to_word,
            bootstyle="success",
            width=20,
            padding=10
        )
        self.pdf_to_word_button.pack(side=LEFT, padx=10)
        
        # Word'den PDF'e dönüştürme butonu
        self.word_to_pdf_button = ttk.Button(
            button_frame, 
            text="Word → PDF", 
            command=self.word_to_pdf,
            bootstyle="primary",
            width=20,
            padding=10
        )
        self.word_to_pdf_button.pack(side=LEFT, padx=10)
        
        # İlerleme çubuğu
        progress_frame = ttk.Frame(main_frame, padding=(0, 10))
        progress_frame.pack(fill=X)
        
        self.progress = ttk.Progressbar(
            progress_frame, 
            orient="horizontal", 
            length=650, 
            mode="determinate",
            bootstyle="success-striped"
        )
        self.progress.pack(pady=5)
        
        # Durum bilgisi
        self.status_var = tk.StringVar()
        self.status_var.set("Hazır")
        status_label = ttk.Label(
            main_frame, 
            textvariable=self.status_var,
            font=("Helvetica", 10),
            bootstyle="secondary"
        )
        status_label.pack(pady=5)
        
        # Alt bilgi
        footer_frame = ttk.Frame(main_frame)
        footer_frame.pack(fill=X, side=BOTTOM, pady=10)
        
        footer_label = ttk.Label(
            footer_frame, 
            text="© 2023 PDF ve Word Dönüştürücü", 
            font=("Helvetica", 8),
            bootstyle="secondary"
        )
        footer_label.pack(side=RIGHT)
    
    def browse_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("PDF Dosyaları", "*.pdf"), ("Word Dosyaları", "*.docx")]
        )
        if file_path:
            self.file_path_var.set(file_path)
            # Dosya adını çıktı adı olarak ayarla (uzantısız)
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            self.output_name_var.set(file_name)
    
    def analyze_pdf_fonts(self, pdf_path):
        """PDF dosyasındaki yazı tiplerini analiz eder"""
        try:
            doc = fitz.open(pdf_path)
            fonts = {}
            
            for page_num in range(len(doc)):
                page = doc[page_num]
                font_dict = page.get_fonts()
                
                for font in font_dict:
                    font_name = font[3]
                    if font_name not in fonts:
                        fonts[font_name] = 1
                    else:
                        fonts[font_name] += 1
            
            doc.close()
            return fonts
        except Exception as e:
            print(f"Yazı tipi analizi sırasında hata: {str(e)}")
            return {}
    
    def pdf_to_word(self):
        pdf_path = self.file_path_var.get()
        output_name = self.output_name_var.get()
        
        if not pdf_path:
            messagebox.showerror("Hata", "Lütfen bir PDF dosyası seçin!")
            return
        
        if not pdf_path.lower().endswith('.pdf'):
            messagebox.showerror("Hata", "Seçilen dosya bir PDF dosyası değil!")
            return
        
        if not output_name:
            messagebox.showerror("Hata", "Lütfen çıktı dosyası için bir isim girin!")
            return
        
        try:
            self.status_var.set("Dönüştürülüyor...")
            self.progress["value"] = 0
            self.root.update()
            
            # Çıktı dosya yolunu oluştur
            output_dir = os.path.dirname(pdf_path)
            output_path = os.path.join(output_dir, f"{output_name}.docx")
            
            # Dosya zaten varsa sor
            if os.path.exists(output_path):
                if not messagebox.askyesno("Dosya Mevcut", 
                                          f"{output_name}.docx dosyası zaten mevcut. Üzerine yazmak istiyor musunuz?"):
                    self.status_var.set("İşlem iptal edildi.")
                    return
            
            # Gelişmiş yazı tipi analizi
            if self.advanced_font_var.get():
                self.status_var.set("Yazı tipleri analiz ediliyor...")
                self.progress["value"] = 10
                self.root.update()
                fonts = self.analyze_pdf_fonts(pdf_path)
                print("PDF'de bulunan yazı tipleri:", fonts)
            
            # PDF'yi Word'e dönüştür
            self.progress["value"] = 20
            self.status_var.set("PDF içeriği dönüştürülüyor...")
            self.root.update()
            
            # Dönüşüm seçeneklerini ayarla
            converter = PDFtoWordConverter(pdf_path)
            
            # Dönüşüm parametrelerini hazırla
            convert_options = {
                # Yazı tipi koruması
                'preserve_font_style': self.preserve_font_var.get(),
                'preserve_font_size': self.preserve_font_var.get(),
                'preserve_font_family': self.preserve_font_var.get(),
                
                # Düzen koruması
                'preserve_paragraph_spacing': self.preserve_layout_var.get(),
                'preserve_line_spacing': self.preserve_layout_var.get(),
                'preserve_text_alignment': self.preserve_layout_var.get(),
                'preserve_indentation': self.preserve_layout_var.get(),
                
                # Resim koruması
                'preserve_images': self.preserve_images_var.get(),
                
                # Gelişmiş ayarlar
                'debug': False,
                'multi_processing': True,  # Çoklu işlem ile daha iyi sonuç
                'ignore_page_error': True,  # Sayfa hatalarını yoksay
                'ignore_text_error': True,  # Metin hatalarını yoksay
            }
            
            # Dönüşümü başlat
            converter.convert(output_path, **convert_options)
            converter.close()
            
            self.progress["value"] = 100
            self.status_var.set(f"Dönüştürme tamamlandı: {output_path}")
            messagebox.showinfo("Başarılı", f"PDF dosyası Word'e dönüştürüldü!\nKonum: {output_path}")
        except Exception as e:
            self.progress["value"] = 0
            self.status_var.set("Hata oluştu!")
            messagebox.showerror("Hata", f"Dönüştürme sırasında bir hata oluştu:\n{str(e)}")
    
    def word_to_pdf(self):
        word_path = self.file_path_var.get()
        output_name = self.output_name_var.get()
        
        if not word_path:
            messagebox.showerror("Hata", "Lütfen bir Word dosyası seçin!")
            return
        
        if not word_path.lower().endswith('.docx'):
            messagebox.showerror("Hata", "Seçilen dosya bir Word dosyası değil!")
            return
        
        if not output_name:
            messagebox.showerror("Hata", "Lütfen çıktı dosyası için bir isim girin!")
            return
        
        try:
            self.status_var.set("Dönüştürülüyor...")
            self.progress["value"] = 0
            self.root.update()
            
            # Çıktı dosya yolunu oluştur
            output_dir = os.path.dirname(word_path)
            output_path = os.path.join(output_dir, f"{output_name}.pdf")
            
            # Dosya zaten varsa sor
            if os.path.exists(output_path):
                if not messagebox.askyesno("Dosya Mevcut", 
                                          f"{output_name}.pdf dosyası zaten mevcut. Üzerine yazmak istiyor musunuz?"):
                    self.status_var.set("İşlem iptal edildi.")
                    return
            
            # Word'ü PDF'ye dönüştür
            self.progress["value"] = 20
            self.root.update()
            
            # docx2pdf kütüphanesi Microsoft Word'ü kullanır, bu nedenle yazı tipleri otomatik olarak korunur
            word_to_pdf_convert(word_path, output_path)
            
            self.progress["value"] = 100
            self.status_var.set(f"Dönüştürme tamamlandı: {output_path}")
            messagebox.showinfo("Başarılı", f"Word dosyası PDF'e dönüştürüldü!\nKonum: {output_path}")
        except Exception as e:
            self.progress["value"] = 0
            self.status_var.set("Hata oluştu!")
            messagebox.showerror("Hata", f"Dönüştürme sırasında bir hata oluştu:\n{str(e)}")

if __name__ == "__main__":
    root = ttk.Window(themename="litera")  # Bootstrap teması
    app = FileConverterApp(root)
    root.mainloop()
