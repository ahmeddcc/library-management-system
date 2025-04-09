# نظام إدارة المكتبات | Library Management System
## التوثيق الشامل | Complete Documentation

<div dir="rtl">

## 🌐 اللغة العربية

### نظرة عامة
نظام إدارة المكتبات هو برنامج شامل لإدارة المكتبات والمبيعات، يوفر حلولاً متكاملة لإدارة المخزون، المبيعات، العملاء، والتقارير.

### المتطلبات الأساسية
- نظام تشغيل: Windows 10/11
- الذاكرة: 4GB RAM على الأقل
- المساحة: 500MB
- الشاشة: 1366×768 أو أعلى

### التثبيت
1. قم بتشغيل ملف Setup.exe
2. اختر مجلد التثبيت
3. اتبع خطوات المعالج
4. انتظر اكتمال التثبيت
5. ابدأ استخدام النظام

### الأنظمة الرئيسية

#### 1. نظام المبيعات
- إنشاء فواتير جديدة
- إدارة المرتجعات
- معالجة المدفوعات
- طباعة الفواتير

#### 2. نظام المخزون
- إدارة المنتجات
- مراقبة المخزون
- تنبيهات المخزون المنخفض
- جرد المخزون

#### 3. نظام العملاء
- إدارة بيانات العملاء
- برنامج الولاء
- سجل المعاملات
- إدارة الديون

#### 4. نظام التقارير
- تقارير المبيعات
- تقارير المخزون
- التقارير المالية
- تقارير العملاء

### الإعدادات والتخصيص
- إعدادات النظام
- إدارة المستخدمين
- تخصيص الواجهة
- إعدادات الطباعة

### الدعم الفني
- البريد: support@example.com
- الهاتف: +xxx-xxx-xxxx
- ساعات العمل: 9:00 ص - 5:00 م

</div>

---

## 🌐 English

### Overview
Library Management System is a comprehensive solution for managing libraries and sales, providing integrated solutions for inventory, sales, customer management, and reporting.

### System Requirements
- OS: Windows 10/11
- Memory: 4GB RAM minimum
- Storage: 500MB
- Display: 1366×768 or higher

### Installation
1. Run Setup.exe
2. Choose installation folder
3. Follow wizard steps
4. Wait for completion
5. Start using the system

### Main Systems

#### 1. Sales System
- Create new invoices
- Manage returns
- Process payments
- Print invoices

#### 2. Inventory System
- Product management
- Stock monitoring
- Low stock alerts
- Inventory counting

#### 3. Customer System
- Customer data management
- Loyalty program
- Transaction history
- Debt management

#### 4. Reporting System
- Sales reports
- Inventory reports
- Financial reports
- Customer reports

### Settings and Customization
- System settings
- User management
- Interface customization
- Printing settings

### Technical Support
- Email: support@example.com
- Phone: +xxx-xxx-xxxx
- Hours: 9:00 AM - 5:00 PM

## API Documentation

### 1. Authentication
```python
def login(username: str, password: str) -> dict:
    """
    Authenticate user and return session token
    
    Args:
        username (str): User's username
        password (str): User's password
        
    Returns:
        dict: Session information including token
    """