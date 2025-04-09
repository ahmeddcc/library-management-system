import sys
import os

# معلومات التطبيق
APP_NAME = "نظام إدارة المكتبات"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Your Company"
APP_DESCRIPTION = "نظام متكامل لإدارة المكتبات والمبيعات"

# المسارات
MAIN_SCRIPT = "main.py"
ICON_PATH = "assets/icons/app.ico"

# الملفات المطلوبة
REQUIRED_FILES = [
    "assets/",  # مجلد الأصول
    "templates/",  # مجلد القوالب
    "LICENSE",
    "README.md"
]

# المكتبات الإضافية
REQUIRED_PACKAGES = [
    "PyQt6",
    "pandas",
    "matplotlib",
    "reportlab",
    "xlsxwriter",
    "python-barcode",
    "Pillow",
    "cryptography"
]