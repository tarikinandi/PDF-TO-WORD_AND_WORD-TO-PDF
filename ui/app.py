"""
Ana uygulama sınıfı
"""

import os
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from core.pdf_to_word import PDFToWordConverter
from core.word_to_pdf import WordToPDFConverter
from ui.components import (
    TitleSection, 
    FileSelectionSection, 
    OutputSection, 
    FormatOptionsSection, 
    ButtonSection, 
    StatusSection
)
from utils.file_utils import (
    browse_file, 
    get_file_extension, 
    get_file_name_without_extension, 
    confirm_overwrite
)
from utils.font_analyzer import analyze_pdf_fonts

class FileConverterApp:
    """
    Ana uygulama sınıfı
    """
    
    def __init__(self, root):
        """
        Ana uygulamayı oluşturur
        
        Args:
            root: Ana pencere
        """
        self.root = root
        
        # Dönüştürücüleri oluştur
        self.pdf_to_word_converter = PDFToWordConverter()
        self.word_to_pdf_converter = WordToPDFConverter()
        
        # Ana çerçeve
        main_frame = ttk.Frame(root, padding=20)
        main_frame.pack(fill=BOTH, expand=YES)
        
        # Başlık bölümü
        self.title_section = TitleSection(
            main_frame, 
            "PDF ve Word Dönüştürücü", 
            "Dosyalarınızı orijinal formatını koruyarak dönüştürün"
        )
        
        # Ayırıcı çizgi
        separator = ttk.Separator(main_frame)
        separator.pack(fill=X, pady=15)
        
        # Dosya seçim bölümü
        self.file_section = FileSelectionSection(main_frame, self.browse_file)
        
        # Çıktı ayarları bölümü
        self.output_section = OutputSection(main_frame)
        
        # Format koruma seçenekleri bölümü
        self.format_section = FormatOptionsSection(main_frame)
        
        # Buton bölümü
        self.button_section = ButtonSection(
            main_frame, 
            self.pdf_to_word, 
            self.word_to_pdf
        )
        
        # Durum bölümü
        self.status_section = StatusSection(main_frame)
    
    def browse_file(self):
        """
        Dosya seçme iletişim kutusunu açar
        """
        file_path = browse_file()
        if file_path:
            self.file_section.file_path_var.set(file_path)
            
            # Çıktı adını otomatik olarak ayarla
            file_name = get_file_name_without_extension(file_path)
            self.output_section.output_name_var.set(file_name)
    
    def pdf_to_word(self):
        """
        PDF'den Word'e dönüştürme işlemini başlatır
        """
        pdf_path = self.file_section.file_path_var.get()
        output_name = self.output_section.output_name_var.get()
        
        # Giriş doğrulama
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
            self.status_section.status_var.set("Dönüştürülüyor...")
            self.status_section.progress["value"] = 0
            self.root.update()
            
            # Çıktı dosya yolunu oluştur
            output_dir = os.path.dirname(pdf_path)
            output_path = os.path.join(output_dir, f"{output_name}.docx")
            
            # Dosya zaten varsa sor
            if not confirm_overwrite(output_path):
                self.status_section.status_var.set("İşlem iptal edildi.")
                return
            
            # Gelişmiş yazı tipi analizi
            if self.format_section.advanced_font_var.get():
                self.status_section.status_var.set("Yazı tipleri analiz ediliyor...")
                self.status_section.progress["value"] = 10
                self.root.update()
                fonts = analyze_pdf_fonts(pdf_path)
                print("PDF'de bulunan yazı tipleri:", fonts)
            
            # PDF'yi Word'e dönüştür
            self.status_section.status_var.set("PDF içeriği dönüştürülüyor...")
            self.status_section.progress["value"] = 20
            self.root.update()
            
            # Dönüşüm seçeneklerini hazırla
            conversion_options = {
                # Yazı tipi koruması
                'preserve_font_style': self.format_section.preserve_font_var.get(),
                'preserve_font_size': self.format_section.preserve_font_var.get(),
                'preserve_font_family': self.format_section.preserve_font_var.get(),
                
                # Düzen koruması
                'preserve_paragraph_spacing': self.format_section.preserve_layout_var.get(),
                'preserve_line_spacing': self.format_section.preserve_layout_var.get(),
                'preserve_text_alignment': self.format_section.preserve_layout_var.get(),
                'preserve_indentation': self.format_section.preserve_layout_var.get(),
                
                # Resim koruması
                'preserve_images': self.format_section.preserve_images_var.get(),
                
                # Gelişmiş ayarlar
                'debug': False,
                'multi_processing': True,
                'ignore_page_error': True,
                'ignore_text_error': True,
            }
            
            # Dönüşümü başlat
            success = self.pdf_to_word_converter.convert(pdf_path, output_path, conversion_options)
            
            if success:
                self.status_section.progress["value"] = 100
                self.status_section.status_var.set(f"Dönüştürme tamamlandı: {output_path}")
                messagebox.showinfo("Başarılı", f"PDF dosyası Word'e dönüştürüldü!\nKonum: {output_path}")
            else:
                self.status_section.progress["value"] = 0
                self.status_section.status_var.set("Dönüştürme başarısız oldu!")
                messagebox.showerror("Hata", "Dönüştürme işlemi sırasında bir hata oluştu!")
                
        except Exception as e:
            self.status_section.progress["value"] = 0
            self.status_section.status_var.set("Hata oluştu!")
            messagebox.showerror("Hata", f"Dönüştürme sırasında bir hata oluştu:\n{str(e)}")
    
    def word_to_pdf(self):
        """
        Word'den PDF'e dönüştürme işlemini başlatır
        """
        word_path = self.file_section.file_path_var.get()
        output_name = self.output_section.output_name_var.get()
        
        # Giriş doğrulama
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
            self.status_section.status_var.set("Dönüştürülüyor...")
            self.status_section.progress["value"] = 0
            self.root.update()
            
            # Çıktı dosya yolunu oluştur
            output_dir = os.path.dirname(word_path)
            output_path = os.path.join(output_dir, f"{output_name}.pdf")
            
            # Dosya zaten varsa sor
            if not confirm_overwrite(output_path):
                self.status_section.status_var.set("İşlem iptal edildi.")
                return
            
            # Word'ü PDF'ye dönüştür
            self.status_section.status_var.set("Word içeriği dönüştürülüyor...")
            self.status_section.progress["value"] = 20
            self.root.update()
            
            # Dönüşümü başlat (Word->PDF için özel seçenekler gerekmez)
            success = self.word_to_pdf_converter.convert(word_path, output_path)
            
            if success:
                self.status_section.progress["value"] = 100
                self.status_section.status_var.set(f"Dönüştürme tamamlandı: {output_path}")
                messagebox.showinfo("Başarılı", f"Word dosyası PDF'e dönüştürüldü!\nKonum: {output_path}")
            else:
                self.status_section.progress["value"] = 0
                self.status_section.status_var.set("Dönüştürme başarısız oldu!")
                messagebox.showerror("Hata", "Dönüştürme işlemi sırasında bir hata oluştu!")
                
        except Exception as e:
            self.status_section.progress["value"] = 0
            self.status_section.status_var.set("Hata oluştu!")
            messagebox.showerror("Hata", f"Dönüştürme sırasında bir hata oluştu:\n{str(e)}")