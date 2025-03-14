"""
Uygulama ayarları ve sabitleri
"""

# Uygulama ayarları
APP_TITLE = "PDF ve Word Dönüştürücü"
APP_THEME = "litera"  # ttkbootstrap teması

# Varsayılan değerler
DEFAULT_PADDING = 20
DEFAULT_FONT = ("Helvetica", 10)
DEFAULT_TITLE_FONT = ("Helvetica", 22, "bold")
DEFAULT_SUBTITLE_FONT = ("Helvetica", 11)

# Renk şeması
COLORS = {
    "primary": "primary",
    "secondary": "secondary",
    "success": "success",
    "info": "info",
    "warning": "warning",
    "danger": "danger",
}

# Dönüşüm ayarları
DEFAULT_CONVERSION_OPTIONS = {
    # Yazı tipi koruması
    'preserve_font_style': True,
    'preserve_font_size': True,
    'preserve_font_family': True,
    
    # Düzen koruması
    'preserve_paragraph_spacing': True,
    'preserve_line_spacing': True,
    'preserve_text_alignment': True,
    'preserve_indentation': True,
    
    # Resim koruması
    'preserve_images': True,
    
    # Gelişmiş ayarlar
    'debug': False,
    'multi_processing': True,
    'ignore_page_error': True,
    'ignore_text_error': True,
} 