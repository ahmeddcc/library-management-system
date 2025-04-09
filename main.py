from utils.system_mode_manager import SystemModeManager

def main():
    # إنشاء مدير وضع النظام
    system_mode_manager = SystemModeManager(db.conn)
    
    # الحصول على الوضع الحالي
    current_mode = system_mode_manager.get_current_mode()
    
    # التحقق من الترخيص فقط إذا كان الوضع المرخص نشطاً
    if current_mode['mode'] == 'licensed':
        license_validator = LicenseValidator(db.conn)
        if not license_validator.check_license():
            activation_dialog = LicenseActivationDialog(license_validator)
            if activation_dialog.exec() != QDialog.DialogCode.Accepted:
                sys.exit(0)
    
    # ... باقي الكود
    
    # تحديث النافذة الرئيسية
    window = MainWindow(
        system_mode_manager=system_mode_manager,
        license_validator=license_validator if current_mode['mode'] == 'licensed' else None,
        # ... باقي المعاملات
    )