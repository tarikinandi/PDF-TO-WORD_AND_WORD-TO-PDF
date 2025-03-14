"""
Dönüştürücü sınıflar için temel soyut sınıf
"""

from abc import ABC, abstractmethod

class Converter(ABC):
    """
    Dönüştürücü sınıflar için temel soyut sınıf.
    Single Responsibility Principle: Her dönüştürücü sınıfı sadece bir tür dönüşümden sorumludur.
    Open/Closed Principle: Yeni dönüştürücü türleri eklemek için bu sınıfı genişletebiliriz.
    """
    
    @abstractmethod
    def convert(self, input_path, output_path, options=None):
        """
        Dosyayı dönüştürür
        
        Args:
            input_path (str): Giriş dosyasının yolu
            output_path (str): Çıkış dosyasının yolu
            options (dict, optional): Dönüşüm seçenekleri
            
        Returns:
            bool: Dönüşüm başarılı ise True, değilse False
        """
        pass
    
    @abstractmethod
    def get_supported_input_formats(self):
        """
        Desteklenen giriş formatlarını döndürür
        
        Returns:
            list: Desteklenen giriş formatlarının listesi
        """
        pass
    
    @abstractmethod
    def get_supported_output_formats(self):
        """
        Desteklenen çıkış formatlarını döndürür
        
        Returns:
            list: Desteklenen çıkış formatlarının listesi
        """
        pass 