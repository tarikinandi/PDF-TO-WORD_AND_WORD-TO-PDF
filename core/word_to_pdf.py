"""
Word'den PDF'e dönüştürme işlemleri
"""

import os
from docx2pdf import convert as word_to_pdf_convert
from core.converter import Converter

class WordToPDFConverter(Converter):
    """
    Word dosyalarını PDF formatına dönüştüren sınıf
    """
    
    def convert(self, input_path, output_path, options=None):
        """
        Word dosyasını PDF formatına dönüştürür
        
        Args:
            input_path (str): Word dosyasının yolu
            output_path (str): Çıktı PDF dosyasının yolu
            options (dict, optional): Dönüşüm seçenekleri (Word->PDF için kullanılmaz)
            
        Returns:
            bool: Dönüşüm başarılı ise True, değilse False
        """
        try:
            # docx2pdf kütüphanesi Microsoft Word'ü kullanır
            # Bu nedenle yazı tipleri otomatik olarak korunur
            word_to_pdf_convert(input_path, output_path)
            return True
        except Exception as e:
            print(f"Word'den PDF'e dönüştürme hatası: {str(e)}")
            return False
    
    def get_supported_input_formats(self):
        """
        Desteklenen giriş formatlarını döndürür
        
        Returns:
            list: Desteklenen giriş formatlarının listesi
        """
        return [".docx"]
    
    def get_supported_output_formats(self):
        """
        Desteklenen çıkış formatlarını döndürür
        
        Returns:
            list: Desteklenen çıkış formatlarının listesi
        """
        return [".pdf"] 