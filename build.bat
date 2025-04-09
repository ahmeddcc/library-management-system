@echo off
echo Building Store System...

:: تثبيت المتطلبات
pip install -r requirements.txt
pip install pyinstaller

:: حذف مجلدات البناء السابقة
rmdir /s /q build
rmdir /s /q dist

:: بناء التطبيق
pyinstaller app.spec

echo Build completed successfully!
pause