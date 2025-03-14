"""
Yeniden kullanılabilir UI bileşenleri
"""

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ui.styles import Styles

class TitleSection:
    """
    Başlık bölümü bileşeni
    """
    
    def __init__(self, parent, title, subtitle):
        """
        Başlık bölümünü oluşturur
        
        Args:
            parent: Ebeveyn widget
            title (str): Ana başlık
            subtitle (str): Alt başlık
        """
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill=X, pady=(0, 20))
        
        # Logo/İkon (emoji kullanarak basit bir logo)
        logo_label = ttk.Label(self.frame, text="🔄", font=("Arial", 28))
        logo_label.pack(pady=(0, 5))
        
        # Başlık
        title_label = ttk.Label(
            self.frame, 
            text=title, 
            **Styles.get_title_style()
        )
        title_label.pack()
        
        # Alt başlık
        subtitle_label = ttk.Label(
            self.frame, 
            text=subtitle, 
            **Styles.get_subtitle_style()
        )
        subtitle_label.pack(pady=(5, 0))

class FileSelectionSection:
    """
    Dosya seçim bölümü bileşeni
    """
    
    def __init__(self, parent, browse_command):
        """
        Dosya seçim bölümünü oluşturur
        
        Args:
            parent: Ebeveyn widget
            browse_command: Gözat butonuna tıklandığında çağrılacak fonksiyon
        """
        self.frame = ttk.Labelframe(
            parent, 
            text="Dosya Seçimi", 
            **Styles.get_labelframe_style()
        )
        self.frame.pack(fill=X, pady=10)
        
        content = ttk.Frame(self.frame)
        content.pack(fill=X)
        
        ttk.Label(content, text="Dosya:").grid(row=0, column=0, padx=5, pady=10, sticky="w")
        
        self.file_path_var = tk.StringVar()
        file_entry = ttk.Entry(content, textvariable=self.file_path_var, width=50)
        file_entry.grid(row=0, column=1, padx=5, pady=10)
        
        browse_button = ttk.Button(
            content, 
            text="Gözat", 
            command=browse_command, 
            **Styles.get_button_style("info")
        )
        browse_button.grid(row=0, column=2, padx=5, pady=10)

class OutputSection:
    """
    Çıktı ayarları bölümü bileşeni
    """
    
    def __init__(self, parent):
        """
        Çıktı ayarları bölümünü oluşturur
        
        Args:
            parent: Ebeveyn widget
        """
        self.frame = ttk.Labelframe(
            parent, 
            text="Çıktı Ayarları", 
            **Styles.get_labelframe_style()
        )
        self.frame.pack(fill=X, pady=10)
        
        content = ttk.Frame(self.frame)
        content.pack(fill=X)
        
        ttk.Label(content, text="Çıktı Adı:").grid(row=0, column=0, padx=5, pady=10, sticky="w")
        
        self.output_name_var = tk.StringVar()
        output_entry = ttk.Entry(content, textvariable=self.output_name_var, width=50)
        output_entry.grid(row=0, column=1, padx=5, pady=10, columnspan=2)

class FormatOptionsSection:
    """
    Format koruma seçenekleri bölümü bileşeni
    """
    
    def __init__(self, parent):
        """
        Format koruma seçenekleri bölümünü oluşturur
        
        Args:
            parent: Ebeveyn widget
        """
        self.frame = ttk.Labelframe(
            parent, 
            text="Format Koruma Seçenekleri", 
            **Styles.get_labelframe_style()
        )
        self.frame.pack(fill=X, pady=10)
        
        content = ttk.Frame(self.frame)
        content.pack(fill=X)
        
        # Yazı tipi koruma seçeneği
        self.preserve_font_var = tk.BooleanVar(value=True)
        font_check = ttk.Checkbutton(
            content, 
            text="Yazı tiplerini koru", 
            variable=self.preserve_font_var,
            bootstyle="round-toggle"
        )
        font_check.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        # Düzen koruma seçeneği
        self.preserve_layout_var = tk.BooleanVar(value=True)
        layout_check = ttk.Checkbutton(
            content, 
            text="Sayfa düzenini koru", 
            variable=self.preserve_layout_var,
            bootstyle="round-toggle"
        )
        layout_check.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Resim koruma seçeneği
        self.preserve_images_var = tk.BooleanVar(value=True)
        images_check = ttk.Checkbutton(
            content, 
            text="Resimleri koru", 
            variable=self.preserve_images_var,
            bootstyle="round-toggle"
        )
        images_check.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
        # Gelişmiş yazı tipi işleme seçeneği
        self.advanced_font_var = tk.BooleanVar(value=True)
        advanced_font_check = ttk.Checkbutton(
            content, 
            text="Gelişmiş yazı tipi işleme", 
            variable=self.advanced_font_var,
            bootstyle="round-toggle"
        )
        advanced_font_check.grid(row=1, column=1, padx=5, pady=5, sticky="w")

class ButtonSection:
    """
    Buton bölümü bileşeni
    """
    
    def __init__(self, parent, pdf_to_word_command, word_to_pdf_command):
        """
        Buton bölümünü oluşturur
        
        Args:
            parent: Ebeveyn widget
            pdf_to_word_command: PDF'den Word'e dönüştürme komutu
            word_to_pdf_command: Word'den PDF'e dönüştürme komutu
        """
        self.frame = ttk.Frame(parent)
        self.frame.pack(pady=20)
        
        # PDF'den Word'e dönüştürme butonu
        pdf_to_word_button = ttk.Button(
            self.frame, 
            text="PDF → Word", 
            command=pdf_to_word_command, 
            **Styles.get_button_style("success")
        )
        pdf_to_word_button.pack(side=LEFT, padx=10)
        
        # Word'den PDF'e dönüştürme butonu
        word_to_pdf_button = ttk.Button(
            self.frame, 
            text="Word → PDF", 
            command=word_to_pdf_command, 
            **Styles.get_button_style("primary")
        )
        word_to_pdf_button.pack(side=LEFT, padx=10)

class StatusSection:
    """
    Durum bölümü bileşeni
    """
    
    def __init__(self, parent):
        """
        Durum bölümünü oluşturur
        
        Args:
            parent: Ebeveyn widget
        """
        self.frame = ttk.Labelframe(
            parent, 
            text="Durum", 
            **Styles.get_labelframe_style()
        )
        self.frame.pack(fill=X, pady=10)
        
        content = ttk.Frame(self.frame)
        content.pack(fill=X, pady=10)
        
        # Durum metni
        self.status_var = tk.StringVar(value="Hazır")
        status_label = ttk.Label(
            content, 
            textvariable=self.status_var
        )
        status_label.pack(pady=(0, 10))
        
        # İlerleme çubuğu
        self.progress = ttk.Progressbar(
            content, 
            **Styles.get_progress_style()
        )
        self.progress.pack(pady=5) 