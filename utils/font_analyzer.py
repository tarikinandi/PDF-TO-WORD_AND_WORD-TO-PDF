"""
PDF dosyalarındaki yazı tiplerini analiz etmek için yardımcı fonksiyonlar
"""

import fitz  # PyMuPDF kütüphanesi

def analyze_pdf_fonts(pdf_path):
    """
    PDF dosyasındaki yazı tiplerini analiz eder
    
    Args:
        pdf_path (str): PDF dosyasının yolu
        
    Returns:
        dict: Yazı tipi adları ve kullanım sayıları
    """
    try:
        fonts = {}
        doc = fitz.open(pdf_path)
        
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

def get_font_statistics(pdf_path):
    """
    PDF dosyasındaki yazı tipi istatistiklerini döndürür
    
    Args:
        pdf_path (str): PDF dosyasının yolu
        
    Returns:
        tuple: (toplam_yazı_tipi_sayısı, en_çok_kullanılan_yazı_tipi)
    """
    fonts = analyze_pdf_fonts(pdf_path)
    
    if not fonts:
        return 0, None
    
    total_fonts = len(fonts)
    most_used_font = max(fonts.items(), key=lambda x: x[1])[0]
    
    return total_fonts, most_used_font 