# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.building.api import *
from PyInstaller.building.build_main import *
import os

# استيراد إعدادات البناء
import build_config as config

block_cipher = None

# تجميع الملفات المطلوبة
added_files = []
for file_path in config.REQUIRED_FILES:
    if os.path.isdir(file_path):
        # إذا كان مجلد، أضف جميع ملفاته
        for root, dirs, files in os.walk(file_path):
            for file in files:
                full_path = os.path.join(root, file)
                added_files.append((full_path, os.path.dirname(full_path)))
    else:
        # إذا كان ملف، أضفه مباشرة
        added_files.append((file_path, '.'))

a = Analysis(
    [config.MAIN_SCRIPT],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=config.APP_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=config.ICON_PATH,
    version='file_version_info.txt',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=config.APP_NAME,
)