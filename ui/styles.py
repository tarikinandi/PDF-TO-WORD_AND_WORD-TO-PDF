"""
UI bileşenleri için stil tanımlamaları
"""

from config.settings import COLORS, DEFAULT_PADDING, DEFAULT_FONT

class Styles:
    """
    UI bileşenleri için stil tanımlamaları
    """
    
    @staticmethod
    def get_frame_style():
        """
        Çerçeve stili
        """
        return {
            "padding": DEFAULT_PADDING
        }
    
    @staticmethod
    def get_labelframe_style():
        """
        Etiketli çerçeve stili
        """
        return {
            "padding": 15,
            "bootstyle": COLORS["primary"]
        }
    
    @staticmethod
    def get_button_style(button_type="primary"):
        """
        Buton stili
        
        Args:
            button_type (str): Buton türü (primary, success, info, vb.)
            
        Returns:
            dict: Buton stil özellikleri
        """
        return {
            "bootstyle": COLORS.get(button_type, COLORS["primary"]),
            "width": 15
        }
    
    @staticmethod
    def get_title_style():
        """
        Başlık stili
        """
        return {
            "font": ("Helvetica", 22, "bold"),
            "bootstyle": COLORS["primary"]
        }
    
    @staticmethod
    def get_subtitle_style():
        """
        Alt başlık stili
        """
        return {
            "font": ("Helvetica", 11),
            "bootstyle": COLORS["secondary"]
        }
    
    @staticmethod
    def get_progress_style():
        """
        İlerleme çubuğu stili
        """
        return {
            "bootstyle": f"{COLORS['success']}-striped",
            "maximum": 100,
            "length": 500
        } 