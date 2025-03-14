"""
Dosya işlemleri için yardımcı fonksiyonlar
"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_file(file_types=None):
    """
    Dosya seçme iletişim kutusunu açar
    
    Args:
        file_types (list, optional): Dosya türleri listesi
        
    Returns:
        str: Seçilen dosyanın yolu veya iptal edilirse boş string
    """
    if file_types is None:
        file_types = [
            ("Tüm Dosyalar", "*.*"),
            ("PDF Dosyaları", "*.pdf"),
            ("Word Dosyaları", "*.docx")
        ]
    
    file_path = filedialog.askopenfilename(
        title="Dosya Seç",
        filetypes=file_types
    )
    
    return file_path

def get_file_extension(file_path):
    """
    Dosya uzantısını döndürür
    
    Args:
        file_path (str): Dosya yolu
        
    Returns:
        str: Dosya uzantısı (nokta dahil, örn: '.pdf')
    """
    _, extension = os.path.splitext(file_path)
    return extension.lower()

def get_file_name_without_extension(file_path):
    """
    Uzantısız dosya adını döndürür
    
    Args:
        file_path (str): Dosya yolu
        
    Returns:
        str: Uzantısız dosya adı
    """
    base_name = os.path.basename(file_path)
    name_without_ext = os.path.splitext(base_name)[0]
    return name_without_ext

def check_file_exists(file_path):
    """
    Dosyanın var olup olmadığını kontrol eder
    
    Args:
        file_path (str): Dosya yolu
        
    Returns:
        bool: Dosya varsa True, yoksa False
    """
    return os.path.isfile(file_path)

def confirm_overwrite(file_path):
    """
    Dosyanın üzerine yazma onayı ister
    
    Args:
        file_path (str): Dosya yolu
        
    Returns:
        bool: Kullanıcı onaylarsa True, onaylamazsa False
    """
    if check_file_exists(file_path):
        return messagebox.askyesno(
            "Dosya Mevcut", 
            f"{os.path.basename(file_path)} dosyası zaten mevcut. Üzerine yazmak istiyor musunuz?"
        )
    return True 