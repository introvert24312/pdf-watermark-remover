from PyQt5.QtWidgets import QFileDialog

from modules.interfaces.interfaces import FileHandlerInterface
from modules.model.base_model import BaseModel
from modules.utils import load_pdf, save_images
import os



class FileHandler(FileHandlerInterface):
    def __init__(self, model):
        self.model: BaseModel = model

    def load_images(self, path=None, dpi=175):
        path, _ = QFileDialog.getOpenFileName(
            None,
            "Load PDF",
            "",
            "PDF files (*.pdf);;All files (*.*)"
        )
        if path:
            images = load_pdf(path, self.model.image_model.image_data.dpi)
            self.model.update_data(images)

    def save_images(self):
        """Save processed images to specified path"""
        try:
            output_path, _ = QFileDialog.getSaveFileName(
                None,
                "Save images as PDF",
                "output.pdf",
                "PDF files (*.pdf);;All files (*.*)"
            )
            if output_path:
                # Remove extension if provided, save_images will add .pdf
                if output_path.endswith('.pdf'):
                    output_path = output_path[:-4]
                save_images(self.model.image_model.get_original_sized_images(), output_path)
                return True
            return False
        except Exception as e:
            print(f"Error saving images: {str(e)}")
            return False

    def load_mask(self, path=None):
        """Load mask from file"""
        try:
            path, _ = QFileDialog.getOpenFileName(
                None,
                "Load mask",
                "",
                "PNG files (*.png);;All files (*.*)"
            )
            if path:
                self.model.load_mask(path)
        except Exception as e:
            print(f"Error loading mask: {str(e)}")


    def save_mask(self):
        try:
            path, _ = QFileDialog.getSaveFileName(
                None,
                "Save mask",
                "mask.png",
                "PNG files (*.png);;All files (*.*)"
            )
            if path:
                self.model.mask_model.save_mask(path)
        except Exception as e:
            print(f"Error saving mask: {str(e)}")
