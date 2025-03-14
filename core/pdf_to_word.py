"""
PDF'den Word'e dönüştürme işlemleri
"""

import os
from pdf2docx import Converter as PDFtoWordConverter
from core.converter import Converter
from config.settings import DEFAULT_CONVERSION_OPTIONS

class PDFToWordConverter(Converter):
    """
    PDF dosyalarını Word formatına dönüştüren sınıf
    """
    
    def convert(self, input_path, output_path, options=None):
        """
        PDF dosyasını Word formatına dönüştürür
        
        Args:
            input_path (str): PDF dosyasının yolu
            output_path (str): Çıktı Word dosyasının yolu
            options (dict, optional): Dönüşüm seçenekleri
            
        Returns:
            bool: Dönüşüm başarılı ise True, değilse False
        """
        try:
            # Varsayılan seçenekleri kullan ve kullanıcı seçenekleriyle birleştir
            conversion_options = DEFAULT_CONVERSION_OPTIONS.copy()
            if options:
                conversion_options.update(options)
            
            # Dönüştürücüyü başlat
            converter = PDFtoWordConverter(input_path)
            
            # Dönüşümü gerçekleştir
            converter.convert(output_path, **conversion_options)
            converter.close()
            
            return True
        except Exception as e:
            print(f"PDF'den Word'e dönüştürme hatası: {str(e)}")
            return False
    
    def get_supported_input_formats(self):
        """
        Desteklenen giriş formatlarını döndürür
        
        Returns:
            list: Desteklenen giriş formatlarının listesi
        """
        return [".pdf"]
    
    def get_supported_output_formats(self):
        """
        Desteklenen çıkış formatlarını döndürür
        
        Returns:
            list: Desteklenen çıkış formatlarının listesi
        """
        return [".docx"] 