from __future__ import annotations

import html
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SEO_CONFIG = json.loads((ROOT / "seo-config.json").read_text(encoding="utf-8"))
SITE_URL = SEO_CONFIG["siteUrl"].rstrip("/")
BUILD_DATE = datetime.now().date().isoformat()
BUILD_VERSION = datetime.now().strftime("%Y%m%d%H%M%S")
BRAND_MARK_ASSET = "/assets/branding/snapvend_logo_square.png"
BRAND_MARK_SITE_ASSET = "/assets/branding/snapvend_logo_square_web.png"
APP_ICON_ASSET = "/assets/branding/app_icon_store_512.png"
PRODUCT_NAME = "SnapVend Gallery"
PRODUCT_SHORT_NAME = "SnapVend"
GOOGLE_PLAY_URL = "https://play.google.com/store/apps/details?id=com.snapvend.gallery"
DOWNLOAD_URL = f"{SITE_URL}/download/"
DOWNLOAD_QR_ASSET = "/assets/marketing/download-qr.svg"

DOWNLOAD_ROUTE_COPY = {
    "tr": {
        "brandKicker": "Profesyonel fotoğraf teslimi",
        "headline": "Cihazınıza göre indirme",
        "intro": "Cihazınız algılanıyor ve uygun indirme kanalına güvenli şekilde yönlendiriliyorsunuz.",
        "desktopNote": "Masaüstü veya notebook kullanıyorsanız, aşağıdan aktif mağazayı seçebilirsiniz.",
        "iosPendingNote": "SnapVend Gallery’nin iPhone ve iPad sürümü şu anda kapalı test aşamasındadır. Bu nedenle iOS cihazlarda App Store aramasına yönlendirme yapılmaz. Şu an aktif indirme Android için Google Play üzerinden sunulmaktadır.",
        "googleSmall": "Android için indir",
        "appleSmall": "iOS için test aşamasında",
        "backWebsite": "Web sitesine dön",
        "pageTitle": "SnapVend Gallery | Cihaza Göre İndirme",
    },
    "en": {
        "brandKicker": "Professional photo delivery",
        "headline": "Download for your device",
        "intro": "We detect your device and route you to the right download channel securely.",
        "desktopNote": "If you are on a desktop or notebook, choose the active store below.",
        "iosPendingNote": "SnapVend Gallery for iPhone and iPad is currently in closed testing. iOS devices are not sent to App Store search during this period. The active public download is currently available on Google Play for Android.",
        "googleSmall": "Download for Android",
        "appleSmall": "iOS version in testing",
        "backWebsite": "Back to website",
        "pageTitle": "SnapVend Gallery | Device Download",
    },
    "es": {
        "brandKicker": "Entrega profesional de fotos",
        "headline": "Descarga para tu dispositivo",
        "intro": "Detectamos tu dispositivo y te dirigimos de forma segura al canal de descarga adecuado.",
        "desktopNote": "Si estás en un ordenador, elige la tienda activa abajo.",
        "iosPendingNote": "SnapVend Gallery para iPhone y iPad está actualmente en fase de prueba cerrada. Durante este periodo, los dispositivos iOS no se envían a la búsqueda de App Store. La descarga pública activa está disponible en Google Play para Android.",
        "googleSmall": "Descargar para Android",
        "appleSmall": "Versión iOS en pruebas",
        "backWebsite": "Volver al sitio web",
        "pageTitle": "SnapVend Gallery | Descarga por dispositivo",
    },
    "fr": {
        "brandKicker": "Livraison photo professionnelle",
        "headline": "Téléchargement adapté",
        "intro": "Nous détectons votre appareil et vous orientons en toute sécurité vers le bon canal de téléchargement.",
        "desktopNote": "Si vous utilisez un ordinateur, choisissez la boutique active ci-dessous.",
        "iosPendingNote": "SnapVend Gallery pour iPhone et iPad est actuellement en test fermé. Pendant cette période, les appareils iOS ne sont pas redirigés vers la recherche App Store. Le téléchargement public actif est disponible sur Google Play pour Android.",
        "googleSmall": "Télécharger pour Android",
        "appleSmall": "Version iOS en test",
        "backWebsite": "Retour au site",
        "pageTitle": "SnapVend Gallery | Téléchargement par appareil",
    },
    "de": {
        "brandKicker": "Professionelle Fotolieferung",
        "headline": "Passend zum Gerät laden",
        "intro": "Wir erkennen dein Gerät und leiten dich sicher zum passenden Download-Kanal.",
        "desktopNote": "Wenn du einen Desktop oder ein Notebook nutzt, wähle unten den aktiven Store.",
        "iosPendingNote": "SnapVend Gallery für iPhone und iPad befindet sich derzeit im geschlossenen Test. iOS-Geräte werden in dieser Zeit nicht zur App-Store-Suche weitergeleitet. Der aktive öffentliche Download ist aktuell bei Google Play für Android verfügbar.",
        "googleSmall": "Für Android herunterladen",
        "appleSmall": "iOS-Version im Test",
        "backWebsite": "Zur Website zurück",
        "pageTitle": "SnapVend Gallery | Geräte-Download",
    },
    "it": {
        "brandKicker": "Consegna fotografica professionale",
        "headline": "Scarica per il tuo dispositivo",
        "intro": "Rileviamo il dispositivo e ti indirizziamo in modo sicuro al canale di download corretto.",
        "desktopNote": "Se usi un desktop o un notebook, scegli qui sotto lo store attivo.",
        "iosPendingNote": "SnapVend Gallery per iPhone e iPad è attualmente in test chiuso. In questa fase i dispositivi iOS non vengono inviati alla ricerca su App Store. Il download pubblico attivo è disponibile su Google Play per Android.",
        "googleSmall": "Scarica per Android",
        "appleSmall": "Versione iOS in test",
        "backWebsite": "Torna al sito",
        "pageTitle": "SnapVend Gallery | Download per dispositivo",
    },
    "pt": {
        "brandKicker": "Entrega profissional de fotos",
        "headline": "Baixe para seu dispositivo",
        "intro": "Detectamos seu dispositivo e encaminhamos você com segurança para o canal de download correto.",
        "desktopNote": "Se estiver em um desktop ou notebook, escolha a loja ativa abaixo.",
        "iosPendingNote": "O SnapVend Gallery para iPhone e iPad está atualmente em teste fechado. Durante esse período, dispositivos iOS não são enviados para a busca da App Store. O download público ativo está disponível no Google Play para Android.",
        "googleSmall": "Baixar para Android",
        "appleSmall": "Versão iOS em teste",
        "backWebsite": "Voltar ao site",
        "pageTitle": "SnapVend Gallery | Download por dispositivo",
    },
    "ru": {
        "brandKicker": "Профессиональная выдача фото",
        "headline": "Скачать для устройства",
        "intro": "Мы определяем ваше устройство и безопасно направляем к подходящему каналу загрузки.",
        "desktopNote": "Если вы используете компьютер или ноутбук, выберите активный магазин ниже.",
        "iosPendingNote": "SnapVend Gallery для iPhone и iPad сейчас находится в закрытом тестировании. В этот период устройства iOS не перенаправляются в поиск App Store. Активная публичная загрузка доступна в Google Play для Android.",
        "googleSmall": "Скачать для Android",
        "appleSmall": "iOS-версия в тестировании",
        "backWebsite": "Вернуться на сайт",
        "pageTitle": "SnapVend Gallery | Загрузка по устройству",
    },
    "ar": {
        "brandKicker": "تسليم صور احترافي",
        "headline": "حمّل حسب جهازك",
        "intro": "نكتشف جهازك ونوجهك بأمان إلى قناة التنزيل المناسبة.",
        "desktopNote": "إذا كنت تستخدم جهاز كمبيوتر، اختر المتجر النشط أدناه.",
        "iosPendingNote": "تطبيق SnapVend Gallery لأجهزة iPhone و iPad حالياً في اختبار مغلق. خلال هذه الفترة لا يتم توجيه أجهزة iOS إلى بحث App Store. التنزيل العام النشط متاح حالياً على Google Play لأجهزة Android.",
        "googleSmall": "تنزيل لأجهزة Android",
        "appleSmall": "إصدار iOS قيد الاختبار",
        "backWebsite": "العودة إلى الموقع",
        "pageTitle": "SnapVend Gallery | تنزيل حسب الجهاز",
    },
    "hi": {
        "brandKicker": "पेशेवर फोटो डिलीवरी",
        "headline": "अपने डिवाइस के लिए डाउनलोड करें",
        "intro": "हम आपका डिवाइस पहचानकर सुरक्षित रूप से सही डाउनलोड चैनल पर भेजते हैं।",
        "desktopNote": "अगर आप डेस्कटॉप या नोटबुक पर हैं, तो नीचे सक्रिय स्टोर चुनें।",
        "iosPendingNote": "iPhone और iPad के लिए SnapVend Gallery अभी बंद परीक्षण चरण में है। इस अवधि में iOS डिवाइस App Store खोज पर नहीं भेजे जाते। फिलहाल सार्वजनिक डाउनलोड Android के लिए Google Play पर उपलब्ध है।",
        "googleSmall": "Android के लिए डाउनलोड करें",
        "appleSmall": "iOS संस्करण परीक्षण में",
        "backWebsite": "वेबसाइट पर वापस जाएं",
        "pageTitle": "SnapVend Gallery | डिवाइस डाउनलोड",
    },
    "ja": {
        "brandKicker": "プロ向け写真納品",
        "headline": "端末に合わせてダウンロード",
        "intro": "端末を検出し、適切なダウンロード先へ安全に案内します。",
        "desktopNote": "デスクトップまたはノートブックの場合は、下の有効なストアを選択してください。",
        "iosPendingNote": "iPhone と iPad 向け SnapVend Gallery は現在クローズドテスト中です。この期間、iOS 端末は App Store 検索へリダイレクトされません。現在公開されているダウンロードは Android 向け Google Play です。",
        "googleSmall": "Android 用にダウンロード",
        "appleSmall": "iOS 版はテスト中",
        "backWebsite": "サイトへ戻る",
        "pageTitle": "SnapVend Gallery | 端末別ダウンロード",
    },
    "zh": {
        "brandKicker": "专业照片交付",
        "headline": "根据设备下载",
        "intro": "我们会识别你的设备，并安全引导你前往正确的下载渠道。",
        "desktopNote": "如果你使用桌面电脑或笔记本，请在下方选择当前可用的商店。",
        "iosPendingNote": "适用于 iPhone 和 iPad 的 SnapVend Gallery 目前处于封闭测试阶段。在此期间，iOS 设备不会跳转到 App Store 搜索。当前公开下载仅在 Android 的 Google Play 提供。",
        "googleSmall": "下载 Android 版本",
        "appleSmall": "iOS 版本测试中",
        "backWebsite": "返回网站",
        "pageTitle": "SnapVend Gallery | 按设备下载",
    },
}


LOCALE_META = {
    "tr": {
        "path": "",
        "dir": "ltr",
        "native": "Türkçe",
        "english": "Turkish",
        "og_locale": "tr_TR",
        "app_store_country": "tr",
        "hreflang": ["tr", "tr-TR"],
    },
    "en": {
        "path": "en",
        "dir": "ltr",
        "native": "English",
        "english": "English",
        "og_locale": "en_US",
        "app_store_country": "us",
        "hreflang": ["en", "en-US", "en-GB", "en-CA", "en-AU"],
    },
    "es": {
        "path": "es",
        "dir": "ltr",
        "native": "Español",
        "english": "Spanish",
        "og_locale": "es_ES",
        "app_store_country": "es",
        "hreflang": ["es", "es-ES", "es-MX", "es-AR", "es-CO"],
    },
    "fr": {
        "path": "fr",
        "dir": "ltr",
        "native": "Français",
        "english": "French",
        "og_locale": "fr_FR",
        "app_store_country": "fr",
        "hreflang": ["fr", "fr-FR", "fr-CA", "fr-BE", "fr-CH"],
    },
    "de": {
        "path": "de",
        "dir": "ltr",
        "native": "Deutsch",
        "english": "German",
        "og_locale": "de_DE",
        "app_store_country": "de",
        "hreflang": ["de", "de-DE", "de-AT", "de-CH"],
    },
    "it": {
        "path": "it",
        "dir": "ltr",
        "native": "Italiano",
        "english": "Italian",
        "og_locale": "it_IT",
        "app_store_country": "it",
        "hreflang": ["it", "it-IT", "it-CH"],
    },
    "pt": {
        "path": "pt",
        "dir": "ltr",
        "native": "Português",
        "english": "Portuguese",
        "og_locale": "pt_BR",
        "app_store_country": "br",
        "hreflang": ["pt", "pt-BR", "pt-PT"],
    },
    "ru": {
        "path": "ru",
        "dir": "ltr",
        "native": "Русский",
        "english": "Russian",
        "og_locale": "ru_RU",
        "app_store_country": "ru",
        "hreflang": ["ru", "ru-RU", "ru-KZ"],
    },
    "ar": {
        "path": "ar",
        "dir": "rtl",
        "native": "العربية",
        "english": "Arabic",
        "og_locale": "ar_SA",
        "app_store_country": "sa",
        "hreflang": ["ar", "ar-SA", "ar-AE", "ar-EG"],
    },
    "hi": {
        "path": "hi",
        "dir": "ltr",
        "native": "हिन्दी",
        "english": "Hindi",
        "og_locale": "hi_IN",
        "app_store_country": "in",
        "hreflang": ["hi", "hi-IN"],
    },
    "ja": {
        "path": "ja",
        "dir": "ltr",
        "native": "日本語",
        "english": "Japanese",
        "og_locale": "ja_JP",
        "app_store_country": "jp",
        "hreflang": ["ja", "ja-JP"],
    },
    "zh": {
        "path": "zh",
        "dir": "ltr",
        "native": "中文 (简体)",
        "english": "Chinese (Simplified)",
        "og_locale": "zh_CN",
        "app_store_country": "cn",
        "hreflang": ["zh", "zh-CN", "zh-SG"],
    },
}


LOCALE_ORDER = ["tr", "en", "es", "fr", "de", "it", "pt", "ru", "ar", "hi", "ja", "zh"]

SCHEMA_PRICING = {
    "tr": {"currency": "TRY", "monthly": 399.99, "yearly": 3999.99},
    "en": {"currency": "USD", "monthly": 8.95, "yearly": 89.54},
    "es": {"currency": "EUR", "monthly": 7.65, "yearly": 76.46},
    "fr": {"currency": "EUR", "monthly": 7.65, "yearly": 76.46},
    "de": {"currency": "EUR", "monthly": 7.65, "yearly": 76.46},
    "it": {"currency": "EUR", "monthly": 7.65, "yearly": 76.46},
    "pt": {"currency": "BRL", "monthly": 45.26, "yearly": 452.58},
    "ru": {"currency": "RUB", "monthly": 697.00, "yearly": 6970.00},
    "ar": {"currency": "SAR", "monthly": 33.58, "yearly": 335.78},
    "hi": {"currency": "INR", "monthly": 832.00, "yearly": 8317.00},
    "ja": {"currency": "JPY", "monthly": 1425.00, "yearly": 14254.00},
    "zh": {"currency": "CNY", "monthly": 61.14, "yearly": 611.43},
}

POPULAR_LABELS = {
    "tr": "En Popüler",
    "en": "Most Popular",
    "es": "Más Popular",
    "fr": "Le Plus Populaire",
    "de": "Am Beliebtesten",
    "it": "Più popolare",
    "pt": "Mais Popular",
    "ru": "Самый популярный",
    "ar": "الأكثر شعبية",
    "hi": "सबसे लोकप्रिय",
    "ja": "一番人気",
    "zh": "最受欢迎",
}

NAV_EXTRA = {
    "tr": {"demo": "Demo", "why": "Avantajlar", "faq": "SSS"},
    "en": {"demo": "Demo", "why": "Benefits", "faq": "FAQ"},
    "es": {"demo": "Demo", "why": "Ventajas", "faq": "Preguntas"},
    "fr": {"demo": "Demo", "why": "Avantages", "faq": "Questions"},
    "de": {"demo": "Demo", "why": "Vorteile", "faq": "Fragen"},
    "it": {"demo": "Demo", "why": "Vantaggi", "faq": "Domande"},
    "pt": {"demo": "Demo", "why": "Vantagens", "faq": "Perguntas"},
    "ru": {"demo": "Демо", "why": "Преимущества", "faq": "Вопросы"},
    "ar": {"demo": "عرض", "why": "المزايا", "faq": "الاسئلة"},
    "hi": {"demo": "डेमो", "why": "फायदे", "faq": "सवाल"},
    "ja": {"demo": "デモ", "why": "メリット", "faq": "質問"},
    "zh": {"demo": "演示", "why": "优势", "faq": "常见问题"},
}

MOBILE_MENU_LABELS = {
    "tr": "Menü",
    "en": "Menu",
    "es": "Menú",
    "fr": "Menu",
    "de": "Menü",
    "it": "Menu",
    "pt": "Menu",
    "ru": "Меню",
    "ar": "القائمة",
    "hi": "मेनू",
    "ja": "メニュー",
    "zh": "菜单",
}

APP_STORE_STATUS = {
    "tr": {
        "small": "iPhone ve iPad için yakında",
        "note": "Şu an test aşamasında olduğu için en kısa zamanda indirmeye açılacaktır.",
    },
    "en": {
        "small": "Coming soon for iPhone and iPad",
        "note": "SnapVend is currently in testing and will be available for download soon.",
    },
    "es": {
        "small": "Próximamente para iPhone y iPad",
        "note": "SnapVend está actualmente en fase de pruebas y estará disponible para descarga muy pronto.",
    },
    "fr": {
        "small": "Bientôt pour iPhone et iPad",
        "note": "SnapVend est actuellement en phase de test et sera bientôt disponible au téléchargement.",
    },
    "de": {
        "small": "Bald für iPhone und iPad",
        "note": "SnapVend befindet sich derzeit in der Testphase und wird in Kürze zum Download verfügbar sein.",
    },
    "it": {
        "small": "Presto per iPhone e iPad",
        "note": "SnapVend è attualmente in fase di test e sarà disponibile per il download a breve.",
    },
    "pt": {
        "small": "Em breve para iPhone e iPad",
        "note": "O SnapVend está em fase de testes e estará disponível para download em breve.",
    },
    "ru": {
        "small": "Скоро для iPhone и iPad",
        "note": "SnapVend сейчас находится на этапе тестирования и скоро будет доступен для загрузки.",
    },
    "ar": {
        "small": "قريبا لاجهزة iPhone و iPad",
        "note": "SnapVend حاليا في مرحلة الاختبار وسيكون متاحا للتنزيل قريبا.",
    },
    "hi": {
        "small": "iPhone और iPad के लिए जल्द",
        "note": "SnapVend अभी परीक्षण चरण में है और जल्द ही डाउनलोड के लिए उपलब्ध होगा।",
    },
    "ja": {
        "small": "iPhone / iPad 版は近日公開",
        "note": "SnapVend は現在テスト段階にあり、近日中にダウンロード可能になります。",
    },
    "zh": {
        "small": "iPhone / iPad 版即将开放",
        "note": "SnapVend 目前处于测试阶段，将很快开放下载。",
    },
}

DOWNLOAD_QR_COPY = {
    "tr": {
        "title": "Mobil indirme erişimi",
        "body": "QR kodu telefonunuzla tarayın; SnapVend Gallery cihazınıza uygun indirme kanalını güvenli şekilde açsın.",
        "hint": "Masaüstü ve notebook ziyaretçileri için güvenli mağaza yönlendirmesi",
        "alt": "SnapVend Gallery indirme QR kodu",
    },
    "en": {
        "title": "Mobile download access",
        "body": "Scan the QR code with your phone and let SnapVend Gallery open the right download channel for your device.",
        "hint": "Secure store routing for desktop and notebook visitors",
        "alt": "SnapVend Gallery download QR code",
    },
    "es": {
        "title": "Acceso móvil de descarga",
        "body": "Escanea el código QR con tu teléfono y deja que SnapVend Gallery abra el canal de descarga adecuado para tu dispositivo.",
        "hint": "Enrutamiento seguro a la tienda para visitantes desde escritorio o portátil",
        "alt": "Código QR de descarga de SnapVend Gallery",
    },
    "fr": {
        "title": "Accès mobile au téléchargement",
        "body": "Scannez le QR code avec votre téléphone et laissez SnapVend Gallery ouvrir le bon canal de téléchargement pour votre appareil.",
        "hint": "Orientation sécurisée vers la boutique pour les visiteurs sur ordinateur",
        "alt": "QR code de téléchargement SnapVend Gallery",
    },
    "de": {
        "title": "Mobiler Download-Zugang",
        "body": "Scanne den QR-Code mit deinem Telefon und lasse SnapVend Gallery den passenden Download-Kanal öffnen.",
        "hint": "Sichere Store-Weiterleitung für Desktop- und Notebook-Besucher",
        "alt": "SnapVend Gallery Download-QR-Code",
    },
    "it": {
        "title": "Accesso download mobile",
        "body": "Scansiona il codice QR con il telefono e lascia che SnapVend Gallery apra il canale di download corretto per il dispositivo.",
        "hint": "Instradamento sicuro allo store per visitatori da desktop o notebook",
        "alt": "Codice QR per scaricare SnapVend Gallery",
    },
    "pt": {
        "title": "Acesso móvel ao download",
        "body": "Leia o QR code com o telefone e deixe o SnapVend Gallery abrir o canal de download correto para o seu dispositivo.",
        "hint": "Roteamento seguro para a loja para visitantes de desktop ou notebook",
        "alt": "QR code de download do SnapVend Gallery",
    },
    "ru": {
        "title": "Мобильный доступ к загрузке",
        "body": "Отсканируйте QR-код телефоном, и SnapVend Gallery откроет подходящий канал загрузки для вашего устройства.",
        "hint": "Безопасный переход в магазин для пользователей компьютеров и ноутбуков",
        "alt": "QR-код для загрузки SnapVend Gallery",
    },
    "ar": {
        "title": "وصول تنزيل عبر الهاتف",
        "body": "امسح رمز QR بهاتفك ودع SnapVend Gallery يفتح قناة التنزيل المناسبة لجهازك.",
        "hint": "توجيه آمن إلى المتجر لزوار الكمبيوتر والكمبيوتر المحمول",
        "alt": "رمز QR لتنزيل SnapVend Gallery",
    },
    "hi": {
        "title": "मोबाइल डाउनलोड एक्सेस",
        "body": "अपने फोन से QR कोड स्कैन करें और SnapVend Gallery को आपके डिवाइस के लिए सही डाउनलोड चैनल खोलने दें।",
        "hint": "डेस्कटॉप और लैपटॉप विजिटर्स के लिए सुरक्षित स्टोर रूटिंग",
        "alt": "SnapVend Gallery डाउनलोड QR कोड",
    },
    "ja": {
        "title": "モバイルダウンロードアクセス",
        "body": "スマートフォンで QR コードを読み取り、SnapVend Gallery が端末に合ったダウンロード先を開きます。",
        "hint": "デスクトップやノートPC利用者向けの安全なストア案内",
        "alt": "SnapVend Gallery ダウンロード QR コード",
    },
    "zh": {
        "title": "移动端下载入口",
        "body": "使用手机扫描二维码，让 SnapVend Gallery 为你的设备打开合适的下载渠道。",
        "hint": "为桌面电脑和笔记本访客提供安全的商店跳转",
        "alt": "SnapVend Gallery 下载 QR 码",
    },
}

DEMO_SECTION = {
    "tr": {
        "eyebrow": "Canlı Demo",
        "title": "WiFi / erişim noktası bağlantısından oturum galerisine kadar akışı göster.",
        "lead": "SnapVend müşteriyi önce WiFi veya erişim noktası QR bağlantısıyla aynı ağa alır, sonra doğru oturum galerisine yönlendirir ve teslime kadar akışı tek deneyimde toplar.",
        "screen_label": "Canlı ürün demosu",
        "screen_tag": "Saha deneyimi",
        "screen_note": "Demo video Android sürümü üzerinden hazırlanmıştır. SnapVend’in temel galeri, QR erişim, seçim ve teslim akışı iPhone ve iPad tarafında da aynı ürün deneyimiyle sunulur.",
        "cta": "Demodan sonra indir",
        "steps": [
            {"title": "Fotoğrafları içe al", "body": "Yerel galeriden seç ya da FTP destekli profesyonel fotoğraf makinesinden doğrudan uygulamaya aktar."},
            {"title": "WiFi / erişim noktası QR bağlantısını aç", "body": "Müşteriyi uygulama indirtmeden aynı ağ ya da erişim noktası üstünde saniyeler içinde bağla."},
            {"title": "Oturum QR ile galeriye al", "body": "Müşteri kendi oturum QR kodunu okutup yalnızca kendisine ait galeriye girsin."},
            {"title": "Ödeme, PAC ve teslim", "body": "Seçimleri doğrula, ödeme ve PAC kontrolünü yap, sonra onaylanan dosyaları ZIP olarak teslim et."},
        ],
    },
    "en": {
        "eyebrow": "Live Demo",
        "title": "Show the flow from WiFi / hotspot access to the session gallery.",
        "lead": "SnapVend first brings the client onto the same network through a WiFi or hotspot QR connection, then moves them into the right session gallery and through delivery in one product journey.",
        "screen_label": "Live product demo",
        "screen_tag": "Field experience",
        "screen_note": "This demo video was prepared from the Android version. SnapVend’s core gallery, QR access, selection and delivery flow is also presented with the same product experience on iPhone and iPad.",
        "cta": "Download after demo",
        "steps": [
            {"title": "Bring photos in", "body": "Select them from local media or transfer them directly into the app from an FTP-capable professional camera."},
            {"title": "Open WiFi / hotspot QR access", "body": "Bring the client onto the same network in seconds without asking them to install the app."},
            {"title": "Open the session gallery with QR", "body": "Let the client scan the session QR code and enter only the gallery created for that shoot."},
            {"title": "Approve and deliver", "body": "Confirm payment, handle PAC approval and finish delivery as ZIP from the same device."},
        ],
    },
    "es": {
        "eyebrow": "Demo",
        "title": "Muestre QR, sesiones y entrega en una sola pantalla.",
        "lead": "SnapVend reúne la transferencia FTP desde cámara profesional, la gestión por sesión, el acceso por QR y la entrega final en una experiencia clara y profesional.",
        "screen_label": "Demo del producto",
        "screen_tag": "Experiencia en campo",
        "screen_note": "Este video de demostración fue preparado con la versión Android. El flujo principal de galería, acceso por QR, selección y entrega de SnapVend también se ofrece con la misma experiencia en iPhone y iPad.",
        "cta": "Descargar después del demo",
        "steps": [
            {"title": "Importe las fotos", "body": "Use la galería local o transfiéralas directamente a la aplicación desde una cámara profesional con FTP."},
            {"title": "Abra una sesión", "body": "Cree una sesión separada para cada cliente, toma o evento y mantenga el flujo ordenado."},
            {"title": "Abra la galería con QR", "body": "El cliente entra a su galería de sesión en segundos al escanear el QR en la misma red."},
            {"title": "Aprobación y entrega", "body": "Confirme el pago, valide PAC y entregue los archivos aprobados en ZIP."},
        ],
    },
    "fr": {
        "eyebrow": "Démo",
        "title": "Montrez QR, sessions et livraison sur un seul écran.",
        "lead": "SnapVend réunit le transfert FTP depuis un appareil photo pro, la gestion par session, l'accès QR et la livraison finale dans une expérience claire et professionnelle.",
        "screen_label": "Démo produit",
        "screen_tag": "Expérience terrain",
        "screen_note": "Cette vidéo de démonstration a été préparée à partir de la version Android. Le flux principal de galerie, d'accès QR, de sélection et de livraison de SnapVend est également proposé avec la même expérience sur iPhone et iPad.",
        "cta": "Télécharger après la démo",
        "steps": [
            {"title": "Importer les photos", "body": "Prenez-les depuis la galerie locale ou transférez-les directement dans l'application depuis un appareil photo pro compatible FTP."},
            {"title": "Ouvrir une session", "body": "Créez une session séparée pour chaque client, prise de vue ou événement afin de garder un flux propre."},
            {"title": "Ouvrir la galerie par QR", "body": "Le client entre dans sa galerie de session en quelques secondes via le QR sur le même réseau."},
            {"title": "Valider et livrer", "body": "Confirmez le paiement, validez le PAC et livrez les fichiers approuvés en ZIP."},
        ],
    },
    "de": {
        "eyebrow": "Demo",
        "title": "Zeigen Sie QR, Sessions und Auslieferung auf einem klaren Bildschirm.",
        "lead": "SnapVend verbindet FTP-Transfer aus professionellen Kameras, Session-Verwaltung, QR-Zugang und Auslieferung in einem professionellen Ablauf.",
        "screen_label": "Live Produktdemo",
        "screen_tag": "Praxisablauf",
        "screen_note": "Dieses Demo-Video wurde mit der Android-Version erstellt. Der zentrale Galerie-, QR-Zugangs-, Auswahl- und Auslieferungsablauf von SnapVend wird auch auf iPhone und iPad mit derselben Produkterfahrung angeboten.",
        "cta": "Nach der Demo herunterladen",
        "steps": [
            {"title": "Fotos importieren", "body": "Waehlen Sie sie aus lokaler Galerie oder uebertragen Sie sie direkt aus einer FTP-faehigen Profikamera in die App."},
            {"title": "Session starten", "body": "Erstellen Sie fuer jeden Kunden, jedes Shooting oder Event eine eigene Session und halten Sie den Ablauf sauber getrennt."},
            {"title": "Galerie per QR oeffnen", "body": "Der Kunde oeffnet seine Session-Galerie in Sekunden per QR im gleichen Netzwerk."},
            {"title": "Freigeben und liefern", "body": "Zahlung bestaetigen, PAC pruefen und freigegebene Dateien als ZIP ausliefern."},
        ],
    },
    "it": {
        "eyebrow": "Demo",
        "title": "Mostra QR, sessioni e consegna in un flusso chiaro.",
        "lead": "SnapVend unisce il trasferimento FTP da fotocamere professionali, la gestione per sessione, l'accesso con QR e la consegna finale in un'esperienza professionale e ordinata.",
        "screen_label": "Demo del prodotto",
        "screen_tag": "Esperienza sul campo",
        "screen_note": "Questo video dimostrativo è stato realizzato con la versione Android. Il flusso principale di galleria, accesso QR, selezione e consegna di SnapVend è disponibile con la stessa esperienza di prodotto anche su iPhone e iPad.",
        "cta": "Scarica dopo la demo",
        "steps": [
            {"title": "Importa le foto", "body": "Selezionale dalla galleria locale oppure trasferiscile direttamente nell'applicazione da una fotocamera professionale con supporto FTP."},
            {"title": "Apri una sessione", "body": "Crea una sessione separata per ogni cliente, servizio o evento e mantieni il flusso ordinato."},
            {"title": "Apri la galleria con QR", "body": "Il cliente entra nella propria galleria di sessione in pochi secondi scansionando il QR sulla stessa rete."},
            {"title": "Conferma e consegna", "body": "Conferma il pagamento, completa la verifica PAC e consegna i file approvati in ZIP."},
        ],
    },
    "pt": {
        "eyebrow": "Demo",
        "title": "Mostre QR, sessoes e entrega em uma unica tela.",
        "lead": "SnapVend une transferencia FTP de camera profissional, gestao por sessao, acesso por QR e entrega final em um fluxo claro e profissional.",
        "screen_label": "Demo do produto",
        "screen_tag": "Experiencia em campo",
        "screen_note": "Este vídeo de demonstração foi preparado com a versão Android. O fluxo principal de galeria, acesso por QR, seleção e entrega do SnapVend também é oferecido com a mesma experiência no iPhone e no iPad.",
        "cta": "Baixar depois do demo",
        "steps": [
            {"title": "Importe as fotos", "body": "Use a galeria local ou transfira direto para o aplicativo a partir de uma camera profissional com FTP."},
            {"title": "Abra uma sessao", "body": "Crie uma sessao separada para cada cliente, ensaio ou evento e mantenha o fluxo organizado."},
            {"title": "Abra a galeria por QR", "body": "O cliente entra na propria galeria da sessao em segundos ao escanear o QR na mesma rede."},
            {"title": "Aprove e entregue", "body": "Confirme o pagamento, valide o PAC e entregue os arquivos aprovados em ZIP."},
        ],
    },
    "ru": {
        "eyebrow": "Демо",
        "title": "Покажите QR, сессии и выдачу на одном экране.",
        "lead": "SnapVend объединяет FTP-передачу с профессиональной камеры, управление сессиями, QR-доступ и финальную выдачу в одном понятном сценарии.",
        "screen_label": "Живое демо",
        "screen_tag": "Полевой сценарий",
        "screen_note": "Это демонстрационное видео подготовлено на Android-версии. Основной сценарий галереи, QR-доступа, выбора и выдачи в SnapVend также доступен на iPhone и iPad с тем же продуктовым опытом.",
        "cta": "Скачать после демо",
        "steps": [
            {"title": "Импорт фото", "body": "Загрузите из локальной галереи или передайте прямо в приложение с профессиональной камеры по FTP."},
            {"title": "Откройте сессию", "body": "Создайте отдельную сессию для каждого клиента, съемки или события, чтобы не смешивать потоки."},
            {"title": "Вход по QR", "body": "Клиент за секунды открывает свою галерею сессии по QR в той же сети."},
            {"title": "Подтверждение и выдача", "body": "Подтвердите оплату, проверьте PAC и выдайте одобренные файлы в ZIP."},
        ],
    },
    "ar": {
        "eyebrow": "عرض حي",
        "title": "اعرض QR والجلسات والتسليم على شاشة واحدة واضحة.",
        "lead": "يجمع SnapVend بين النقل عبر FTP من الكاميرات الاحترافية وادارة الجلسات ودخول QR والتسليم النهائي في تجربة احترافية واحدة.",
        "screen_label": "عرض المنتج",
        "screen_tag": "تجربة ميدانية",
        "screen_note": "تم إعداد فيديو العرض هذا باستخدام إصدار Android. كما يتم تقديم تجربة SnapVend الأساسية للمعرض والوصول عبر QR والاختيار والتسليم بنفس منطق المنتج على iPhone و iPad.",
        "cta": "نزّل بعد العرض",
        "steps": [
            {"title": "استيراد الصور", "body": "اخترها من المعرض المحلي او انقلها مباشرة الى التطبيق من كاميرا احترافية تدعم FTP."},
            {"title": "افتح جلسة مستقلة", "body": "ابدأ جلسة مستقلة لكل عميل او جلسة تصوير او فعالية حتى يبقى التدفق منظما."},
            {"title": "فتح المعرض عبر QR", "body": "يدخل العميل الى معرض الجلسة الخاص به خلال ثوان عبر QR على نفس الشبكة."},
            {"title": "اعتماد وتسليم", "body": "اكد الدفع وراجع PAC ثم سلم الملفات المعتمدة بصيغة ZIP."},
        ],
    },
    "hi": {
        "eyebrow": "लाइव डेमो",
        "title": "QR, सेशन और डिलीवरी फ्लो को एक साफ स्क्रीन पर दिखाएँ।",
        "lead": "SnapVend प्रोफेशनल कैमरे से FTP ट्रांसफर, सेशन प्रबंधन, QR एक्सेस और डिलीवरी को एक ही पेशेवर अनुभव में जोड़ता है।",
        "screen_label": "लाइव प्रोडक्ट डेमो",
        "screen_tag": "फील्ड अनुभव",
        "screen_note": "यह डेमो वीडियो Android संस्करण पर तैयार किया गया है। SnapVend का मुख्य गैलरी, QR एक्सेस, चयन और डिलीवरी अनुभव iPhone और iPad पर भी उसी प्रोडक्ट अनुभव के साथ उपलब्ध है।",
        "cta": "डेमो के बाद डाउनलोड करें",
        "steps": [
            {"title": "फोटो इम्पोर्ट करें", "body": "लोकल गैलरी से चुनें या FTP-सक्षम प्रोफेशनल कैमरे से सीधे ऐप में ट्रांसफर करें।"},
            {"title": "अलग सेशन शुरू करें", "body": "हर ग्राहक, शूट या इवेंट के लिए अलग सेशन खोलें, ताकि फ्लो आपस में न मिले।"},
            {"title": "QR से गैलरी खोलें", "body": "ग्राहक उसी नेटवर्क पर QR स्कैन करके अपनी सेशन गैलरी तुरंत खोल सकता है।"},
            {"title": "मंजूरी और डिलीवरी", "body": "भुगतान की पुष्टि करें, PAC जांचें और मंजूर फाइलों को ZIP में डिलीवर करें।"},
        ],
    },
    "ja": {
        "eyebrow": "ライブデモ",
        "title": "QR、セッション、納品の流れを1画面で見せる。",
        "lead": "SnapVend はプロ向けカメラからの FTP 転送、セッション管理、QR アクセス、納品までをひとつの分かりやすい体験にまとめます。",
        "screen_label": "ライブデモ",
        "screen_tag": "現場フロー",
        "screen_note": "このデモ動画は Android 版をもとに作成されています。SnapVend の基本となるギャラリー、QR アクセス、選択、納品の流れは iPhone と iPad でも同じ製品体験として提供されます。",
        "cta": "デモのあとにダウンロード",
        "steps": [
            {"title": "写真を取り込む", "body": "ローカルメディアから選ぶか、FTP 対応のプロ向けカメラからアプリへ直接取り込みます。"},
            {"title": "セッションを開始する", "body": "顧客、撮影、イベントごとに個別のセッションを作り、流れを整理します。"},
            {"title": "QR でギャラリー共有", "body": "同じネットワーク上でクライアントが QR を読み取り、自分のセッションギャラリーをすぐ開けます。"},
            {"title": "承認して納品", "body": "支払いを確認し、PAC を確認して、承認済みファイルを ZIP で納品します。"},
        ],
    },
    "zh": {
        "eyebrow": "实时演示",
        "title": "把二维码、会话与交付流程清晰地展示在同一界面。",
        "lead": "SnapVend 将专业相机 FTP 传输、会话管理、二维码进入和最终交付整合成一套更专业的体验。",
        "screen_label": "产品演示",
        "screen_tag": "现场流程",
        "screen_note": "该演示视频基于 Android 版本制作。SnapVend 的核心画廊、二维码进入、选择与交付流程在 iPhone 和 iPad 上也以相同的产品体验提供。",
        "cta": "看完演示后下载",
        "steps": [
            {"title": "导入照片", "body": "可从本地相册选择，也可通过支持 FTP 的专业相机直接传入应用。"},
            {"title": "创建会话", "body": "为每位客户、每次拍摄或每场活动建立独立会话，避免流程混淆。"},
            {"title": "通过二维码打开画廊", "body": "客户在同一网络下扫描二维码，几秒内进入自己的会话画廊。"},
            {"title": "确认并交付", "body": "确认付款，完成 PAC 检查，并以 ZIP 方式交付已批准文件。"},
        ],
    },
}

FAQ_SECTION = {
    "tr": {
        "eyebrow": "SSS",
        "title": "Karar vermeden önce en çok sorulanlar",
        "lead": "Müşterilerin ve saha ekiplerinin en sık sorduğu temel soruları burada topladık.",
        "items": [
            {"q": "SnapVend internetsiz çalışır mı?", "a": "Evet. Ana akış yerel ağ veya hotspot üzerinde çalışabilir. Bulut zorunlu değildir."},
            {"q": "Müşteri fotoğrafları nasıl görür?", "a": "Müşteri aynı ağda QR kodu okutarak tarayıcıdan galeriye girer ve seçim yapar."},
            {"q": "Kendi işletme adımı ve logomu kullanabilir miyim?", "a": "Evet. Pro planlarda özel işletme adı, logo ve teslim markalaması açılır."},
            {"q": "Müşteriye ülkeye göre ödeme yöntemi gösterebilir miyim?", "a": "Evet. İşletme ülkesi seçildiğinde kurulumu tamamlanan yerel yöntemler ödeme popup ekranında görünür. Türkiye, İspanya, Hindistan, Çin ve Japonya için hazır yöntem setleri vardır."},
            {"q": "Teslim limiti hangi planda kalkıyor?", "a": "Aylık ve yıllık Pro planlar günlük teslim limitini kaldırır."},
        ],
    },
    "en": {
        "eyebrow": "FAQ",
        "title": "The most common questions before teams start",
        "lead": "These are the core questions photographers and event teams usually ask first.",
        "items": [
            {"q": "Does SnapVend work without internet?", "a": "Yes. The main workflow can run over local network or hotspot. Cloud access is not required."},
            {"q": "How do clients view the photos?", "a": "Clients scan a QR code on the same network, open the browser gallery and make their selections there."},
            {"q": "Can I use my own business name and logo?", "a": "Yes. Pro plans unlock custom business branding, logo usage and branded delivery."},
            {"q": "Can I show country-specific payment methods to clients?", "a": "Yes. Once the business country is selected, completed local methods appear in the payment popup. Ready local method sets are available for Turkey, Spain, India, China and Japan."},
            {"q": "Which plan removes delivery limits?", "a": "Both monthly and yearly Pro plans remove the daily delivery limit."},
        ],
    },
    "es": {
        "eyebrow": "Preguntas",
        "title": "Las preguntas mas comunes antes de empezar",
        "lead": "Aqui reunimos las dudas clave de fotografos y equipos de eventos.",
        "items": [
            {"q": "¿SnapVend funciona sin internet?", "a": "Si. El flujo principal puede funcionar con red local o hotspot sin depender de la nube."},
            {"q": "¿Como ve el cliente las fotos?", "a": "El cliente escanea un QR en la misma red y abre la galeria en el navegador."},
            {"q": "¿Puedo usar mi propio logo y nombre?", "a": "Si. Los planes Pro desbloquean nombre comercial, logo y entrega con marca propia."},
            {"q": "¿Puedo mostrar metodos de pago segun el pais?", "a": "Si. Al elegir el pais del negocio, los metodos locales configurados aparecen en el popup de pago. Hay metodos listos para Turquia, Espana, India, China y Japon."},
            {"q": "¿Que plan elimina el limite de entrega?", "a": "Los planes Pro mensual y anual eliminan el limite diario."},
        ],
    },
    "fr": {
        "eyebrow": "Questions",
        "title": "Les questions les plus frequentes avant de commencer",
        "lead": "Voici les points que les photographes et equipes terrain demandent le plus souvent.",
        "items": [
            {"q": "SnapVend fonctionne t il sans internet ?", "a": "Oui. Le flux principal peut tourner sur reseau local ou hotspot sans cloud obligatoire."},
            {"q": "Comment le client voit il les photos ?", "a": "Le client scanne un QR sur le meme reseau et ouvre la galerie dans le navigateur."},
            {"q": "Puis je utiliser mon propre logo ?", "a": "Oui. Les plans Pro ouvrent le nom d entreprise, le logo et la livraison personnalisee."},
            {"q": "Puis je afficher des methodes de paiement selon le pays ?", "a": "Oui. Une fois le pays de l entreprise choisi, les methodes locales configurees apparaissent dans la fenetre de paiement. Des ensembles prets existent pour la Turquie, l Espagne, l Inde, la Chine et le Japon."},
            {"q": "Quel plan retire la limite de livraison ?", "a": "Les plans Pro mensuel et annuel retirent la limite quotidienne."},
        ],
    },
    "de": {
        "eyebrow": "Fragen",
        "title": "Die wichtigsten Fragen vor dem Start",
        "lead": "Hier stehen die Fragen, die Fotografen und Einsatzteams am haufigsten stellen.",
        "items": [
            {"q": "Funktioniert SnapVend ohne Internet?", "a": "Ja. Der Hauptablauf kann uber lokales Netzwerk oder Hotspot ohne Cloud laufen."},
            {"q": "Wie sehen Kunden die Fotos?", "a": "Kunden scannen im gleichen Netzwerk den QR Code und offnen die Galerie im Browser."},
            {"q": "Kann ich eigenes Branding nutzen?", "a": "Ja. Pro schaltet Firmenname, Logo und gebrandete Auslieferung frei."},
            {"q": "Kann ich landerspezifische Zahlungsarten zeigen?", "a": "Ja. Sobald das Geschaeftsland gewahlt ist, erscheinen fertig eingerichtete lokale Methoden im Zahlungsfenster. Vorbereitete Sets gibt es fur die Turkei, Spanien, Indien, China und Japan."},
            {"q": "Welcher Plan entfernt das Lieferlimit?", "a": "Sowohl der monatliche als auch der jahrliche Pro Plan entfernen das Tageslimit."},
        ],
    },
    "it": {
        "eyebrow": "Domande",
        "title": "Le domande più comuni prima di iniziare",
        "lead": "Qui trovi le domande principali che fotografi e team sul campo fanno più spesso.",
        "items": [
            {"q": "SnapVend funziona senza internet?", "a": "Sì. Il flusso principale può funzionare su rete locale o hotspot senza dipendere dal cloud."},
            {"q": "Come vedono le foto i clienti?", "a": "Il cliente scansiona un QR sulla stessa rete e apre la galleria nel browser."},
            {"q": "Posso usare il mio nome e il mio logo?", "a": "Sì. I piani Pro sbloccano nome attività, logo e consegna brandizzata."},
            {"q": "Posso mostrare metodi di pagamento in base al paese?", "a": "Sì. Quando selezioni il paese dell'attività, i metodi locali configurati compaiono nel popup di pagamento. Esistono set pronti per Turchia, Spagna, India, Cina e Giappone."},
            {"q": "Quale piano rimuove il limite di consegna?", "a": "Sia il piano Pro mensile sia quello annuale rimuovono il limite giornaliero."},
        ],
    },
    "pt": {
        "eyebrow": "Perguntas",
        "title": "Perguntas mais comuns antes de comecar",
        "lead": "Aqui estao as duvidas que equipes fotograficas fazem com mais frequencia.",
        "items": [
            {"q": "O SnapVend funciona sem internet?", "a": "Sim. O fluxo principal pode rodar em rede local ou hotspot sem depender da nuvem."},
            {"q": "Como o cliente ve as fotos?", "a": "O cliente escaneia um QR na mesma rede e abre a galeria no navegador."},
            {"q": "Posso usar meu proprio nome e logo?", "a": "Sim. Os planos Pro liberam branding, logo e entrega personalizada."},
            {"q": "Posso mostrar metodos de pagamento por pais?", "a": "Sim. Ao escolher o pais do negocio, os metodos locais configurados aparecem no popup de pagamento. Ha conjuntos prontos para Turquia, Espanha, India, China e Japao."},
            {"q": "Qual plano remove o limite de entrega?", "a": "Os planos Pro mensal e anual removem o limite diario."},
        ],
    },
    "ru": {
        "eyebrow": "Вопросы",
        "title": "Частые вопросы перед стартом",
        "lead": "Здесь собраны основные вопросы, которые чаще всего задают фотографы и выездные команды.",
        "items": [
            {"q": "Работает ли SnapVend без интернета?", "a": "Да. Основной сценарий может работать через локальную сеть или точку доступа без облака."},
            {"q": "Как клиент смотрит фотографии?", "a": "Клиент сканирует QR код в той же сети и открывает галерею в браузере."},
            {"q": "Можно ли использовать свой логотип и бренд?", "a": "Да. Pro открывает фирменное имя, логотип и брендированную выдачу."},
            {"q": "Можно ли показать клиенту способы оплаты по стране?", "a": "Да. После выбора страны бизнеса настроенные локальные методы появляются во всплывающем окне оплаты. Готовые наборы есть для Турции, Испании, Индии, Китая и Японии."},
            {"q": "Какой тариф снимает лимит выдачи?", "a": "И месячный, и годовой Pro снимают ежедневный лимит выдачи."},
        ],
    },
    "ar": {
        "eyebrow": "الاسئلة الشائعة",
        "title": "اكثر الاسئلة شيوعا قبل البدء",
        "lead": "جمعنا هنا الاسئلة الاساسية التي يطرحها المصورون وفرق العمل الميدانية.",
        "items": [
            {"q": "هل يعمل SnapVend بدون انترنت؟", "a": "نعم. يمكن تشغيل التدفق الرئيسي عبر شبكة محلية او hotspot بدون اعتماد على السحابة."},
            {"q": "كيف يشاهد العميل الصور؟", "a": "يقوم العميل بمسح QR على نفس الشبكة ويفتح المعرض من المتصفح."},
            {"q": "هل يمكنني استخدام اسمي التجاري وشعاري؟", "a": "نعم. خطط Pro تفتح اسم النشاط والشعار والتسليم بعلامتك الخاصة."},
            {"q": "هل يمكنني عرض طرق دفع حسب البلد للعميل؟", "a": "نعم. عند اختيار بلد النشاط تظهر الطرق المحلية المكتملة في نافذة الدفع. توجد مجموعات جاهزة لتركيا واسبانيا والهند والصين واليابان."},
            {"q": "اي خطة تزيل حد التسليم اليومي؟", "a": "كل من الخطة الشهرية والسنوية Pro يزيلان حد التسليم اليومي."},
        ],
    },
    "hi": {
        "eyebrow": "सवाल",
        "title": "शुरू करने से पहले सबसे आम सवाल",
        "lead": "फोटोग्राफर और ऑन-साइट टीमें आम तौर पर सबसे पहले यही सवाल पूछती हैं।",
        "items": [
            {"q": "क्या SnapVend बिना इंटरनेट के काम करता है?", "a": "हाँ। मुख्य फ्लो लोकल नेटवर्क या हॉटस्पॉट पर चल सकता है, क्लाउड जरूरी नहीं है।"},
            {"q": "ग्राहक फोटो कैसे देखता है?", "a": "ग्राहक उसी नेटवर्क पर QR स्कैन करके ब्राउज़र गैलरी खोलता है।"},
            {"q": "क्या मैं अपना नाम और लोगो इस्तेमाल कर सकता हूँ?", "a": "हाँ। Pro प्लान कस्टम ब्रांडिंग, लोगो और ब्रांडेड डिलीवरी खोलते हैं।"},
            {"q": "क्या मैं ग्राहक को देश के हिसाब से भुगतान तरीके दिखा सकता हूँ?", "a": "हाँ। बिज़नेस देश चुनने के बाद कॉन्फ़िगर किए गए लोकल तरीके भुगतान विंडो में दिखते हैं। Turkey, Spain, India, China और Japan के लिए तैयार method sets मौजूद हैं।"},
            {"q": "कौन सा प्लान डिलीवरी सीमा हटाता है?", "a": "मासिक और वार्षिक दोनों Pro प्लान दैनिक डिलीवरी सीमा हटा देते हैं।"},
        ],
    },
    "ja": {
        "eyebrow": "質問",
        "title": "導入前によくある質問",
        "lead": "フォトグラファーや現場チームからよく聞かれる質問をまとめました。",
        "items": [
            {"q": "SnapVend はインターネットなしで使えますか？", "a": "はい。主なフローはローカルネットワークや hotspot 上で動作でき、クラウドは必須ではありません。"},
            {"q": "クライアントはどうやって写真を見ますか？", "a": "同じネットワーク上で QR を読み取り、ブラウザギャラリーを開いて確認します。"},
            {"q": "自分のブランド名やロゴを使えますか？", "a": "はい。Pro プランで独自ブランド名、ロゴ、ブランド納品が使えます。"},
            {"q": "国ごとの決済方法をクライアントに表示できますか？", "a": "はい。事業国を選ぶと、設定済みのローカル決済方法が支払いポップアップに表示されます。トルコ、スペイン、インド、中国、日本向けの方法セットが用意されています。"},
            {"q": "どのプランで納品制限がなくなりますか？", "a": "月額 Pro と年額 Pro の両方で日次納品制限が解除されます。"},
        ],
    },
    "zh": {
        "eyebrow": "常见问题",
        "title": "开始前最常见的问题",
        "lead": "这里整理了摄影团队和现场团队最常问的核心问题。",
        "items": [
            {"q": "SnapVend 可以在没有互联网时使用吗？", "a": "可以。主要流程可在本地网络或 hotspot 上运行，不依赖云端。"},
            {"q": "客户如何查看照片？", "a": "客户在同一网络中扫描 QR 后，就能在浏览器里打开画廊。"},
            {"q": "我可以使用自己的品牌名和 logo 吗？", "a": "可以。Pro 计划会开放自定义品牌名、logo 和品牌化交付。"},
            {"q": "可以向客户显示按国家配置的支付方式吗？", "a": "可以。选择商家所在国家后，已完成设置的本地支付方式会显示在支付弹窗中。目前已为土耳其、西班牙、印度、中国和日本准备了现成方式。"},
            {"q": "哪个计划会移除交付限制？", "a": "月度 Pro 和年度 Pro 都会移除每日交付限制。"},
        ],
    },
}


PROOF_SECTION = {
    "tr": {
        "eyebrow": "Kullanım Senaryoları",
        "title": "SnapVend'in öne çıktığı saha akışları",
        "lead": "Doğrulanmış müşteri logosu ve yorumları eklendiğinde bu alan kolayca genişletilebilir. Şimdilik ürünün en iyi oturduğu kullanım senaryolarını ve ekip profillerini burada özetliyoruz.",
        "use_label": "Kullanım Senaryoları",
        "reference_label": "Referans Profilleri",
        "use_cases": [
            {"title": "Düğün ve davet seçimi", "body": "Çekim devam ederken ya da hemen sonrasında misafire QR ile galeri açın, seçimleri toplayın ve aynı cihazdan teslim edin."},
            {"title": "Stüdyo seçim masası", "body": "Portre veya aile çekimlerinde müşteriyle yan yana durup kareleri birlikte eleyin, onaylayın ve tek ekrandan ilerleyin."},
            {"title": "Okul ve spor oturumları", "body": "Birden fazla seansı karıştırmadan sınıf, takım veya kulüp bazlı seçim ve teslim akışlarını ayrı tutun."},
            {"title": "Sokak ve turistik alan portre satışı", "body": "Sahada hızlı çekim yapın, seçilen kareleri anında gösterin ve tekli ya da paket satış akışını aynı cihaz üzerinden yönetin."},
            {"title": "Kurumsal etkinlik standı", "body": "Etkinlik alanında anlık çekim, QR girişi ve ZIP teslimi ile markalı bir deneyim sunun."},
        ],
        "references": [
            {"title": "Hızlı teslim ekipleri", "body": "Sahada çekim alıp aynı gün seçim ve teslim sürecini kapatmak isteyen ekipler için uygundur."},
            {"title": "Markalı deneyim arayan stüdyolar", "body": "Özel logo, işletme adı ve kontrollü müşteri akışı isteyen profesyonel stüdyolar için güçlü bir yapı sunar."},
            {"title": "Yerel ağ ile çalışan operasyonlar", "body": "İnternet bağlantısına güvenmeden erişim noktası veya yerel ağ üzerinden işleyen ekipler için doğrudan uyumludur."},
            {"title": "Çoklu oturum yöneten ekipler", "body": "Farklı müşteri veya organizasyonları ayrı akışlarda tutmak isteyen yoğun saha operasyonları için tasarlanmıştır."},
        ],
    },
    "en": {
        "eyebrow": "Use Cases",
        "title": "Show the field workflows where SnapVend fits best",
        "lead": "Until verified customer logos and named testimonials are added, this section highlights the strongest operating scenarios and team profiles for the product.",
        "use_label": "Use Cases",
        "reference_label": "Reference Profiles",
        "use_cases": [
            {"title": "Wedding and guest selection flow", "body": "Open a QR gallery during or right after the shoot, collect selections and complete delivery from the same device."},
            {"title": "Studio review desk", "body": "Stand next to the client in portrait sessions, narrow the set together and move to approval from one screen."},
            {"title": "School and sports sessions", "body": "Keep classes, teams and session groups separate while managing many deliveries in one day."},
            {"title": "Street and tourist-spot portrait sales", "body": "Shoot on location, show the selected frames instantly and manage single-image or package sales from the same device."},
            {"title": "Corporate event booth", "body": "Run quick captures, QR access and ZIP delivery on location with a more branded handoff."},
        ],
        "references": [
            {"title": "Fast delivery teams", "body": "Strong for crews that want to shoot, review and close delivery on the same day."},
            {"title": "Brand-focused studios", "body": "A solid fit for studios that want custom branding, cleaner approval flow and controlled presentation."},
            {"title": "Local-network operations", "body": "Designed for teams that prefer hotspot or local network workflows instead of depending on internet."},
            {"title": "Multi-session field crews", "body": "Built for teams that manage separate clients or event groups without mixing deliveries."},
        ],
    },
    "es": {
        "eyebrow": "Casos De Uso",
        "title": "Muestre los flujos de campo donde SnapVend encaja mejor",
        "lead": "Hasta agregar logos o testimonios verificados, esta seccion resume los escenarios y perfiles de equipo donde el producto destaca.",
        "use_label": "Casos De Uso",
        "reference_label": "Perfiles De Referencia",
        "use_cases": [
            {"title": "Bodas y seleccion de invitados", "body": "Abra la galeria QR durante o despues del trabajo, recoja selecciones y entregue desde el mismo dispositivo."},
            {"title": "Mesa de revision en estudio", "body": "Revise retratos con el cliente al lado, descarte fotos y avance a la aprobacion desde una sola pantalla."},
            {"title": "Sesiones de escuela y deporte", "body": "Separe clases, equipos o grupos mientras gestiona muchas entregas en una sola jornada."},
            {"title": "Ventas de retrato en calle y zonas turisticas", "body": "Fotografie en el lugar, muestre al instante las imagenes elegidas y gestione ventas unitarias o en paquete desde el mismo dispositivo."},
            {"title": "Stand en eventos corporativos", "body": "Maneje captura rapida, acceso por QR y entrega ZIP con una experiencia mas cuidada."},
        ],
        "references": [
            {"title": "Equipos de entrega rapida", "body": "Ideal para equipos que quieren fotografiar, revisar y cerrar la entrega el mismo dia."},
            {"title": "Estudios con enfoque de marca", "body": "Muy util para estudios que necesitan branding propio y una presentacion mas controlada."},
            {"title": "Operaciones por red local", "body": "Pensado para equipos que trabajan con punto de acceso o red local sin depender de internet."},
            {"title": "Equipos con muchas sesiones", "body": "Ayuda a manejar varios clientes o grupos sin mezclar entregas."},
        ],
    },
    "fr": {
        "eyebrow": "Cas D Usage",
        "title": "Montrez les flux terrain ou SnapVend est le plus pertinent",
        "lead": "En attendant de vrais logos clients ou temoignages verifies, cette section resume les scenarios et profils d equipe les plus adaptes.",
        "use_label": "Cas D Usage",
        "reference_label": "Profils De Reference",
        "use_cases": [
            {"title": "Mariage et selection des invites", "body": "Ouvrez la galerie QR pendant ou juste apres la prise de vue, recupererez les choix puis livrez depuis le meme appareil."},
            {"title": "Table de selection en studio", "body": "Travaillez avec le client a cote de vous, triez les portraits et passez a la validation sur un seul ecran."},
            {"title": "Ecole et sport", "body": "Gardez classes, equipes et groupes bien separes meme quand le volume de livraison augmente."},
            {"title": "Vente de portraits en rue et zones touristiques", "body": "Photographiez sur place, montrez aussitot les images retenues et gerez la vente a l'unite ou en pack depuis le meme appareil."},
            {"title": "Stand evenementiel d'entreprise", "body": "Associez prise de vue rapide, acces QR et livraison ZIP dans une experience plus professionnelle."},
        ],
        "references": [
            {"title": "Equipes de livraison rapide", "body": "Adapte aux equipes qui veulent photographier, faire choisir et livrer le meme jour."},
            {"title": "Studios centres sur la marque", "body": "Bon choix pour les studios qui veulent une image de marque plus forte et un parcours client maitrise."},
            {"title": "Operations en reseau local", "body": "Concu pour les equipes qui preferent point d'acces ou reseau local au lieu d'une dependance internet."},
            {"title": "Equipes multi sessions", "body": "Permet de gerer plusieurs clients ou groupes sans melanger les livraisons."},
        ],
    },
    "de": {
        "eyebrow": "Einsatzszenarien",
        "title": "Zeigen Sie die Einsatzablaufe, in denen SnapVend am starksten ist",
        "lead": "Bis verifizierte Kundenlogos oder Testimonials vorliegen, fasst dieser Bereich die passendsten Szenarien und Teamprofile zusammen.",
        "use_label": "Einsatzszenarien",
        "reference_label": "Referenzprofile",
        "use_cases": [
            {"title": "Hochzeit und Gasteauswahl", "body": "Offnen Sie die QR Galerie wahrend oder direkt nach dem Shooting, sammeln Sie Auswahlen und liefern Sie vom selben Gerat."},
            {"title": "Studio Auswahlplatz", "body": "Sichten Sie Portratfotos gemeinsam mit dem Kunden und gehen Sie direkt zur Freigabe uber."},
            {"title": "Schule und Sport", "body": "Halten Sie Klassen, Teams und Gruppen sauber getrennt, auch bei vielen Sessions pro Tag."},
            {"title": "Portraitverkauf auf Strassen und Touristenorten", "body": "Fotografieren Sie vor Ort, zeigen Sie ausgewaehlte Bilder sofort und steuern Sie Einzel- oder Paketverkaeufe vom selben Geraet."},
            {"title": "Eventstand fur Unternehmen", "body": "Verbinden Sie schnelle Aufnahme, QR Zugang und ZIP Auslieferung in einem professionellen Vor Ort Ablauf."},
        ],
        "references": [
            {"title": "Schnelle Lieferteams", "body": "Passend fur Crews, die Aufnahme, Auswahl und Auslieferung am selben Tag abschliessen wollen."},
            {"title": "Markenorientierte Studios", "body": "Gut fur Studios mit Bedarf an eigenem Branding und kontrollierter Kundenprasentation."},
            {"title": "Lokale Netzwerk Teams", "body": "Entwickelt fur Teams, die lieber per mobiler Zugangspunkt oder lokalem Netzwerk als uber Internet arbeiten."},
            {"title": "Teams mit mehreren Sessions", "body": "Hilft beim getrennten Verwalten vieler Kunden oder Gruppen ohne Lieferchaos."},
        ],
    },
    "it": {
        "eyebrow": "Casi D'Uso",
        "title": "Mostra i flussi sul campo in cui SnapVend rende al meglio",
        "lead": "Finché non aggiungerai loghi clienti verificati o testimonianze reali, questa sezione riassume gli scenari e i profili di team più adatti al prodotto.",
        "use_label": "Casi D'Uso",
        "reference_label": "Profili Di Riferimento",
        "use_cases": [
            {"title": "Matrimoni e scelta degli invitati", "body": "Apri la galleria QR durante o subito dopo il servizio, raccogli le selezioni e completa la consegna dallo stesso dispositivo."},
            {"title": "Postazione di selezione in studio", "body": "Rivedi i ritratti accanto al cliente, filtra le foto e passa all'approvazione da un'unica schermata."},
            {"title": "Scuola e sport", "body": "Tieni separati classi, squadre e gruppi anche quando aumentano sessioni e consegne nello stesso giorno."},
            {"title": "Vendita di ritratti in strada e aree turistiche", "body": "Scatta sul posto, mostra subito le immagini selezionate e gestisci la vendita singola o in pacchetto dallo stesso dispositivo."},
            {"title": "Stand per eventi aziendali", "body": "Unisci cattura rapida, accesso QR e consegna ZIP in un'esperienza più professionale sul posto."},
        ],
        "references": [
            {"title": "Team di consegna rapida", "body": "Adatto ai team che vogliono fotografare, far scegliere e consegnare tutto nello stesso giorno."},
            {"title": "Studi orientati al brand", "body": "Utile per studi che vogliono nome, logo e una presentazione cliente più controllata."},
            {"title": "Operazioni su rete locale", "body": "Pensato per team che preferiscono punto di accesso o rete locale invece di dipendere da internet."},
            {"title": "Team con più sessioni", "body": "Aiuta a gestire più clienti o gruppi senza mescolare le consegne."},
        ],
    },
    "pt": {
        "eyebrow": "Casos De Uso",
        "title": "Mostre os fluxos de campo onde o SnapVend funciona melhor",
        "lead": "Enquanto logos ou depoimentos reais nao sao adicionados, esta area resume os cenarios e perfis de equipe mais adequados ao produto.",
        "use_label": "Casos De Uso",
        "reference_label": "Perfis De Referencia",
        "use_cases": [
            {"title": "Casamentos e selecao de convidados", "body": "Abra a galeria QR durante ou apos a sessao, receba as escolhas e conclua a entrega no mesmo dispositivo."},
            {"title": "Mesa de selecao no estudio", "body": "Revise retratos ao lado do cliente, filtre as fotos e avance para aprovacao em uma unica tela."},
            {"title": "Escola e esporte", "body": "Separe turmas, times e grupos mesmo quando o volume de sessoes e entregas aumenta."},
            {"title": "Venda de retratos na rua e em areas turisticas", "body": "Fotografe no local, mostre as imagens escolhidas na hora e gerencie vendas avulsas ou em pacote a partir do mesmo dispositivo."},
            {"title": "Stand em evento corporativo", "body": "Combine captura rapida, acesso por QR e entrega ZIP em uma experiencia mais profissional."},
        ],
        "references": [
            {"title": "Equipes de entrega rapida", "body": "Bom encaixe para equipes que querem fotografar, revisar e entregar no mesmo dia."},
            {"title": "Estudios com foco em marca", "body": "Ideal para estudios que querem branding proprio e um fluxo de aprovacao mais organizado."},
            {"title": "Operacoes em rede local", "body": "Pensado para equipes que preferem ponto de acesso ou rede local sem depender da internet."},
            {"title": "Equipes com muitas sessoes", "body": "Ajuda a manter clientes e grupos separados sem misturar entregas."},
        ],
    },
    "ru": {
        "eyebrow": "Сценарии",
        "title": "Покажите полевые сценарии, где SnapVend особенно силен",
        "lead": "Пока на сайте нет подтвержденных логотипов клиентов и именных отзывов, этот блок показывает самые подходящие сценарии и профили команд.",
        "use_label": "Сценарии Использования",
        "reference_label": "Профили Команд",
        "use_cases": [
            {"title": "Свадьбы и выбор гостей", "body": "Откройте QR галерею во время или сразу после съемки, соберите выбор и завершите выдачу с того же устройства."},
            {"title": "Студийный стол отбора", "body": "Просматривайте портреты вместе с клиентом, быстро отбирайте кадры и переходите к подтверждению на одном экране."},
            {"title": "Школа и спорт", "body": "Держите классы, команды и группы отдельно даже при большом количестве сессий и выдач."},
            {"title": "Продажа портретов на улице и в туристических зонах", "body": "Снимайте на месте, сразу показывайте выбранные кадры и управляйте продажей по одной фотографии или пакетами с того же устройства."},
            {"title": "Корпоративная стойка", "body": "Запускайте съемку, вход по QR и ZIP выдачу прямо на площадке в более профессиональном формате."},
        ],
        "references": [
            {"title": "Команды быстрой выдачи", "body": "Подходит для команд, которым нужно снять, показать и выдать в тот же день."},
            {"title": "Студии с акцентом на бренд", "body": "Удобно для студий, которым важны собственный логотип, имя и более управляемый клиентский путь."},
            {"title": "Локальные сетевые операции", "body": "Создано для работы через точку доступа или локальную сеть без зависимости от интернета."},
            {"title": "Полевые команды с многими сессиями", "body": "Помогает вести несколько клиентов и групп без смешивания выдач."},
        ],
    },
    "ar": {
        "eyebrow": "سيناريوهات الاستخدام",
        "title": "اعرض مسارات العمل الميدانية التي يتفوق فيها SnapVend",
        "lead": "الى حين اضافة شعارات عملاء حقيقية او شهادات موثقة، يوضح هذا القسم اهم السيناريوهات وملفات الفرق المناسبة للمنتج.",
        "use_label": "سيناريوهات الاستخدام",
        "reference_label": "ملفات الفرق",
        "use_cases": [
            {"title": "حفلات الزفاف واختيار الضيوف", "body": "افتح معرض QR اثناء التصوير او بعده مباشرة، اجمع الاختيارات واكمل التسليم من نفس الجهاز."},
            {"title": "طاولة الاختيار في الاستوديو", "body": "راجع الصور مع العميل وجها لوجه، استبعد اللقطات وانتقل الى الاعتماد من شاشة واحدة."},
            {"title": "المدارس والرياضة", "body": "افصل الصفوف والفرق والمجموعات حتى مع عدد كبير من الجلسات وعمليات التسليم."},
            {"title": "بيع البورتريه في الشارع والمناطق السياحية", "body": "التقط الصور في الموقع واعرض اللقطات المختارة مباشرة وادِر بيع الصور بشكل فردي او ضمن باقات من نفس الجهاز."},
            {"title": "جناح الفعاليات", "body": "ادمج التصوير السريع ودخول QR وتسليم ZIP في تجربة ميدانية اكثر احترافية."},
        ],
        "references": [
            {"title": "فرق التسليم السريع", "body": "مناسب للفرق التي تريد التصوير والمراجعة والتسليم في اليوم نفسه."},
            {"title": "استوديوهات تهتم بالعلامة", "body": "ملائم للاستوديوهات التي تريد شعارها واسمها وتجربة عميل اكثر تنظيما."},
            {"title": "عمليات تعمل عبر الشبكة المحلية", "body": "مصمم للفرق التي تعتمد على نقطة الاتصال او الشبكة المحلية بدون الاعتماد على الانترنت."},
            {"title": "فرق تدير جلسات متعددة", "body": "يساعد على ادارة عدة عملاء او مجموعات بدون خلط عمليات التسليم."},
        ],
    },
    "hi": {
        "eyebrow": "उपयोग परिदृश्य",
        "title": "वे कार्यप्रवाह देखें जहाँ SnapVend सबसे बेहतर बैठता है",
        "lead": "जब तक सत्यापित ग्राहक लोगो या नाम सहित प्रशंसापत्र नहीं जुड़ते, यह हिस्सा उन सबसे मजबूत उपयोग परिदृश्यों और टीम प्रोफ़ाइल को दिखाता है जहाँ SnapVend अच्छी तरह फिट बैठता है।",
        "use_label": "उपयोग परिदृश्य",
        "reference_label": "टीम प्रोफ़ाइल",
        "use_cases": [
            {"title": "शादी और मेहमान चयन", "body": "शूट के दौरान या उसके तुरंत बाद QR गैलरी खोलें, चयन लें और उसी डिवाइस से डिलीवरी पूरी करें।"},
            {"title": "स्टूडियो समीक्षा डेस्क", "body": "ग्राहक के साथ पोर्ट्रेट शॉट देखें, शॉर्टलिस्ट करें और एक ही स्क्रीन से मंजूरी तक जाएँ।"},
            {"title": "स्कूल और स्पोर्ट्स सेशन", "body": "कई कक्षाओं, टीमों और समूहों को अलग रखते हुए डिलीवरी फ्लो संभालें।"},
            {"title": "सड़क और पर्यटन क्षेत्र पोर्ट्रेट बिक्री", "body": "मौके पर शूट करें, चुनी हुई तस्वीरें तुरंत दिखाएँ और एकल या पैकेज बिक्री उसी डिवाइस से संभालें।"},
            {"title": "कॉर्पोरेट इवेंट बूथ", "body": "ऑन-साइट कैप्चर, QR एक्सेस और ZIP डिलीवरी को एक पेशेवर फ्लो में चलाएँ।"},
        ],
        "references": [
            {"title": "तेज़ डिलीवरी टीमें", "body": "उन टीमों के लिए सही जो उसी दिन शूट, समीक्षा और डिलीवरी पूरा करना चाहती हैं।"},
            {"title": "ब्रांड-केंद्रित स्टूडियो", "body": "उन स्टूडियो के लिए उपयोगी जिन्हें अपना लोगो, व्यवसाय नाम और साफ मंजूरी फ्लो चाहिए।"},
            {"title": "लोकल नेटवर्क टीमें", "body": "मोबाइल हॉटस्पॉट या लोकल नेटवर्क पर काम करने वाली टीमों के लिए बनाया गया है।"},
            {"title": "मल्टी-सेशन टीमें", "body": "कई ग्राहकों या समूहों को अलग रखते हुए डिलीवरी संभालने में मदद करता है।"},
        ],
    },
    "ja": {
        "eyebrow": "利用シナリオ",
        "title": "SnapVend が特に力を発揮する現場フローを紹介します",
        "lead": "実在する顧客ロゴや確認済みレビューを追加するまで、このセクションでは製品に合う代表的なシナリオとチーム像を示します。",
        "use_label": "利用シナリオ",
        "reference_label": "チームプロファイル",
        "use_cases": [
            {"title": "結婚式とゲスト選定", "body": "撮影中または直後に QR ギャラリーを開き、選択を集めて同じ端末から納品まで進めます。"},
            {"title": "スタジオ確認デスク", "body": "クライアントの横でポートレートを見ながら絞り込み、そのまま承認へ進めます。"},
            {"title": "学校とスポーツ撮影", "body": "クラスやチームを分けたまま、多くのセッションと納品を整理できます。"},
            {"title": "ストリートと観光地でのポートレート販売", "body": "現地で撮影し、選ばれた写真をすぐ見せて、単品販売やパッケージ販売を同じ端末で進められます。"},
            {"title": "企業イベントブース", "body": "会場での撮影、QR アクセス、ZIP 納品を一つの流れで提供できます。"},
        ],
        "references": [
            {"title": "即日納品チーム", "body": "撮影から確認、納品までを同日に終えたいチームに向いています。"},
            {"title": "ブランド重視のスタジオ", "body": "独自ロゴや屋号、より整理された承認フローを求めるスタジオに適しています。"},
            {"title": "ローカルネット運用", "body": "インターネット依存ではなくホットスポットやローカルネットで動かしたい現場向けです。"},
            {"title": "複数セッション運営チーム", "body": "複数の顧客やグループを混ぜずに納品管理したいチームに合います。"},
        ],
    },
    "zh": {
        "eyebrow": "使用场景",
        "title": "展示 SnapVend 最适合的现场工作流程",
        "lead": "在加入已验证客户标志和真实评价之前，这个部分会先展示最适合产品的典型场景和团队类型。",
        "use_label": "使用场景",
        "reference_label": "团队画像",
        "use_cases": [
            {"title": "婚礼与宾客选片", "body": "在拍摄中或拍摄后立刻打开 QR 画廊，收集选择并在同一设备上完成交付。"},
            {"title": "影楼选片台", "body": "与客户并排查看人像照片，快速筛选并直接进入确认流程。"},
            {"title": "学校与体育拍摄", "body": "即使有很多班级、队伍和场次，也能保持交付流程清晰分离。"},
            {"title": "街拍与旅游区域人像销售", "body": "在现场快速拍摄、即时展示所选照片，并通过同一设备完成单张或套餐销售流程。"},
            {"title": "企业活动展位", "body": "把现场拍摄、QR 进入和 ZIP 交付整合成更专业的活动流程。"},
        ],
        "references": [
            {"title": "快速交付团队", "body": "适合希望在同一天内完成拍摄、选片和交付的团队。"},
            {"title": "重视品牌的影楼", "body": "适合需要自定义品牌名、标识和更整洁客户流程的团队。"},
            {"title": "本地网络运营团队", "body": "为希望通过热点或本地网络工作而不是依赖互联网的团队设计。"},
            {"title": "多场次执行团队", "body": "帮助团队在不混淆客户或群组的情况下管理多场次交付。"},
        ],
    },
}


LANGUAGE_SUPPORT_SECTION = {
    "tr": {
        "eyebrow": "Dil Desteği",
        "title": "Çok dilli müşteri deneyimi ile daha anlaşılır akış",
        "lead": "SnapVend, farklı ülkelerden gelen müşteriler için web sitesi, müşteri galerisi ve desteklenen akışlarda daha anlaşılır bir dil deneyimi sunar.",
        "cards": [
            {"title": "Web sitesi ve ilk yönlendirme", "body": "Ziyaretçi desteklenen dillerden biriyle geldiğinde içeriği daha rahat takip edebilir ve doğru sayfaya daha hızlı ulaşır."},
            {"title": "Galeri ve müşteri seçimi", "body": "Müşteri tarafındaki galeri deneyimi ve seçim süreci, dil bariyerini azaltacak şekilde daha anlaşılır ilerler."},
            {"title": "Onay ve teslim akışı", "body": "Ödeme, onay ve teslim adımları desteklenen dillerde daha net anlatılarak sahadaki iletişimi kolaylaştırır."},
        ],
        "supported_label": "Desteklenen Diller",
    },
    "en": {
        "eyebrow": "Language Support",
        "title": "A clearer client flow with multilingual support",
        "lead": "SnapVend gives international clients a clearer experience across the website, customer gallery and supported delivery flow screens.",
        "cards": [
            {"title": "Website and first touchpoint", "body": "Visitors can follow the website more comfortably and land on the right page faster when their language is supported."},
            {"title": "Gallery and client selection", "body": "The browser gallery and selection flow become easier to understand for clients coming from different countries."},
            {"title": "Approval and delivery flow", "body": "Payment, approval and delivery steps stay easier to explain when supported languages are available inside the flow."},
        ],
        "supported_label": "Supported Languages",
    },
    "es": {
        "eyebrow": "Idiomas",
        "title": "Un flujo de cliente mas claro con soporte multilingue",
        "lead": "SnapVend ofrece una experiencia mas comprensible para clientes internacionales en el sitio web, la galeria del cliente y los flujos compatibles.",
        "cards": [
            {"title": "Sitio web y primer acceso", "body": "Cuando el idioma esta soportado, el visitante entiende mejor el sitio y llega antes a la pagina correcta."},
            {"title": "Galeria y seleccion del cliente", "body": "La experiencia de galeria y el proceso de seleccion resultan mas claros para clientes de distintos paises."},
            {"title": "Aprobacion y entrega", "body": "Los pasos de pago, aprobacion y entrega se explican de forma mas clara cuando el flujo incluye idiomas compatibles."},
        ],
        "supported_label": "Idiomas Compatibles",
    },
    "fr": {
        "eyebrow": "Langues",
        "title": "Un parcours client plus clair grace au support multilingue",
        "lead": "SnapVend propose une experience plus facile a comprendre pour les clients internationaux sur le site, la galerie client et les flux compatibles.",
        "cards": [
            {"title": "Site web et premiere entree", "body": "Quand la langue est prise en charge, le visiteur comprend plus vite le site et atteint plus facilement la bonne page."},
            {"title": "Galerie et selection client", "body": "La galerie navigateur et le processus de selection deviennent plus simples a suivre pour des clients de differents pays."},
            {"title": "Validation et livraison", "body": "Les etapes de paiement, validation et livraison sont plus claires quand le flux est disponible dans des langues prises en charge."},
        ],
        "supported_label": "Langues Prises En Charge",
    },
    "de": {
        "eyebrow": "Sprachen",
        "title": "Ein klarerer Kundenablauf mit mehrsprachiger Unterstuetzung",
        "lead": "SnapVend bietet internationalen Kunden ein verstaendlicheres Erlebnis ueber Website, Kundengalerie und unterstuetzte Ablaufschritte hinweg.",
        "cards": [
            {"title": "Website und erster Einstieg", "body": "Wenn die Sprache unterstuetzt wird, finden Besucher sich schneller zurecht und kommen einfacher auf die richtige Seite."},
            {"title": "Galerie und Kundenauswahl", "body": "Browser-Galerie und Auswahlablauf werden fuer Kunden aus unterschiedlichen Laendern leichter verstaendlich."},
            {"title": "Freigabe und Lieferung", "body": "Zahlung, Freigabe und Lieferung lassen sich klarer erklaeren, wenn diese Schritte in unterstuetzten Sprachen verfuegbar sind."},
        ],
        "supported_label": "Unterstuetzte Sprachen",
    },
    "it": {
        "eyebrow": "Lingue",
        "title": "Un flusso cliente piu chiaro grazie al supporto multilingue",
        "lead": "SnapVend offre ai clienti internazionali un'esperienza piu comprensibile tra sito web, galleria cliente e schermate dei flussi supportati.",
        "cards": [
            {"title": "Sito web e primo accesso", "body": "Quando la lingua e supportata, il visitatore segue il sito con piu facilita e arriva piu velocemente alla pagina corretta."},
            {"title": "Galleria e selezione del cliente", "body": "La galleria nel browser e il processo di selezione risultano piu chiari per clienti che arrivano da paesi diversi."},
            {"title": "Conferma e consegna", "body": "Pagamento, conferma e consegna sono piu facili da spiegare quando i passaggi supportati sono disponibili in piu lingue."},
        ],
        "supported_label": "Lingue Supportate",
    },
    "pt": {
        "eyebrow": "Idiomas",
        "title": "Um fluxo mais claro para o cliente com suporte multilíngue",
        "lead": "SnapVend oferece uma experiencia mais facil de entender para clientes internacionais no site, na galeria do cliente e nos fluxos compativeis.",
        "cards": [
            {"title": "Site e primeiro acesso", "body": "Quando o idioma e suportado, o visitante entende melhor o site e chega mais rapido a pagina certa."},
            {"title": "Galeria e selecao do cliente", "body": "A galeria no navegador e o processo de selecao ficam mais claros para clientes de diferentes paises."},
            {"title": "Aprovacao e entrega", "body": "Pagamento, aprovacao e entrega ficam mais faceis de explicar quando o fluxo esta disponivel em idiomas suportados."},
        ],
        "supported_label": "Idiomas Suportados",
    },
    "ru": {
        "eyebrow": "Языки",
        "title": "Более понятный клиентский путь благодаря поддержке языков",
        "lead": "SnapVend делает сайт, клиентскую галерею и поддерживаемые шаги выдачи более понятными для международных клиентов.",
        "cards": [
            {"title": "Сайт и первый вход", "body": "Если язык поддерживается, посетителю проще понять сайт и быстрее попасть на нужную страницу."},
            {"title": "Галерея и выбор клиента", "body": "Галерея в браузере и процесс выбора становятся понятнее для клиентов из разных стран."},
            {"title": "Подтверждение и выдача", "body": "Шаги оплаты, подтверждения и выдачи легче объяснять, когда поддерживаемые экраны доступны на нужном языке."},
        ],
        "supported_label": "Поддерживаемые Языки",
    },
    "ar": {
        "eyebrow": "دعم اللغة",
        "title": "تجربة عميل اوضح مع دعم متعدد اللغات",
        "lead": "يوفر SnapVend تجربة اكثر وضوحا للعملاء الدوليين عبر الموقع ومعرض العميل وشاشات التدفق المدعومة.",
        "cards": [
            {"title": "الموقع ونقطة الدخول الاولى", "body": "عندما تكون اللغة مدعومة يصبح تتبع الموقع اسهل ويصل الزائر الى الصفحة الصحيحة بشكل اسرع."},
            {"title": "المعرض واختيار العميل", "body": "تصبح تجربة المعرض في المتصفح وخطوات الاختيار اوضح للعملاء القادمين من بلدان مختلفة."},
            {"title": "الاعتماد والتسليم", "body": "تصبح خطوات الدفع والاعتماد والتسليم اسهل شرحا عندما تكون الشاشات المدعومة متاحة باكثر من لغة."},
        ],
        "supported_label": "اللغات المدعومة",
    },
    "hi": {
        "eyebrow": "भाषा समर्थन",
        "title": "बहुभाषी समर्थन के साथ ज्यादा स्पष्ट ग्राहक अनुभव",
        "lead": "SnapVend अंतरराष्ट्रीय ग्राहकों के लिए वेबसाइट, ग्राहक गैलरी और समर्थित फ्लो स्क्रीन पर ज्यादा समझने योग्य अनुभव देता है।",
        "cards": [
            {"title": "वेबसाइट और पहला प्रवेश", "body": "जब भाषा समर्थित होती है, विज़िटर साइट को बेहतर समझता है और सही पेज तक जल्दी पहुँचता है।"},
            {"title": "गैलरी और ग्राहक चयन", "body": "ब्राउज़र गैलरी और चयन फ्लो अलग-अलग देशों के ग्राहकों के लिए ज्यादा स्पष्ट हो जाता है।"},
            {"title": "अनुमोदन और डिलीवरी", "body": "जब समर्थित स्क्रीन उनकी भाषा में उपलब्ध हों, तो भुगतान, मंजूरी और डिलीवरी के चरण समझाना आसान हो जाता है।"},
        ],
        "supported_label": "समर्थित भाषाएँ",
    },
    "ja": {
        "eyebrow": "言語サポート",
        "title": "多言語対応でより分かりやすい顧客フロー",
        "lead": "SnapVend は、Web サイト、顧客ギャラリー、対応フロー画面を通して、海外顧客にも分かりやすい体験を提供します。",
        "cards": [
            {"title": "Web サイトと最初の導線", "body": "対応言語で表示されることで、訪問者はサイトを理解しやすくなり、目的のページへ素早く進めます。"},
            {"title": "ギャラリーと顧客の選択", "body": "ブラウザギャラリーと選択フローが、異なる国の顧客にもより分かりやすくなります。"},
            {"title": "承認と納品", "body": "対応言語で表示されることで、支払い、承認、納品の流れを現場でより説明しやすくなります。"},
        ],
        "supported_label": "対応言語",
    },
    "zh": {
        "eyebrow": "语言支持",
        "title": "通过多语言支持带来更清晰的客户流程",
        "lead": "SnapVend 让国际客户在网站、客户画廊和支持的流程界面中获得更容易理解的体验。",
        "cards": [
            {"title": "网站与首次进入", "body": "当语言受支持时，访问者能更容易理解网站，并更快到达正确页面。"},
            {"title": "画廊与客户选片", "body": "浏览器画廊和选片流程会对来自不同国家的客户更加清晰。"},
            {"title": "确认与交付", "body": "当支持的界面提供多语言时，支付、确认和交付步骤会更容易解释。"},
        ],
        "supported_label": "支持的语言",
    },
}

LANGUAGE_SUPPORT_FAQ = {
    "tr": {"q": "Hangi dilleri destekliyor?", "a_intro": "Web sitesi, müşteri galerisi ve desteklenen akışlarda şu diller sunulabilir:"},
    "en": {"q": "Which languages are supported?", "a_intro": "The website, customer gallery and supported flow screens can be presented in these languages:"},
    "es": {"q": "¿Qué idiomas son compatibles?", "a_intro": "El sitio web, la galeria del cliente y los flujos compatibles pueden mostrarse en estos idiomas:"},
    "fr": {"q": "Quelles langues sont prises en charge ?", "a_intro": "Le site web, la galerie client et les flux compatibles peuvent etre proposes dans ces langues :"},
    "de": {"q": "Welche Sprachen werden unterstuetzt?", "a_intro": "Website, Kundengalerie und unterstuetzte Ablaufschritte koennen in diesen Sprachen bereitgestellt werden:"},
    "it": {"q": "Quali lingue sono supportate?", "a_intro": "Il sito web, la galleria cliente e i flussi supportati possono essere presentati in queste lingue:"},
    "pt": {"q": "Quais idiomas sao suportados?", "a_intro": "O site, a galeria do cliente e os fluxos compativeis podem ser apresentados nestes idiomas:"},
    "ru": {"q": "Какие языки поддерживаются?", "a_intro": "Сайт, клиентская галерея и поддерживаемые шаги потока могут быть доступны на этих языках:"},
    "ar": {"q": "ما اللغات المدعومة؟", "a_intro": "يمكن تقديم الموقع ومعرض العميل وشاشات التدفق المدعومة بهذه اللغات:"},
    "hi": {"q": "कौन-कौन सी भाषाएँ समर्थित हैं?", "a_intro": "वेबसाइट, ग्राहक गैलरी और समर्थित फ्लो स्क्रीन इन भाषाओं में दिखाई जा सकती हैं:"},
    "ja": {"q": "どの言語に対応していますか？", "a_intro": "Web サイト、顧客ギャラリー、対応フロー画面では次の言語を利用できます:"},
    "zh": {"q": "支持哪些语言？", "a_intro": "网站、客户画廊和支持的流程界面可提供以下语言:"},
}

LOCALIZED_LANGUAGE_NAMES = {
    "tr": {"tr": "Türkçe", "en": "İngilizce", "es": "İspanyolca", "fr": "Fransızca", "de": "Almanca", "it": "İtalyanca", "pt": "Portekizce", "ru": "Rusça", "ar": "Arapça", "hi": "Hintçe", "ja": "Japonca", "zh": "Çince"},
    "en": {"tr": "Turkish", "en": "English", "es": "Spanish", "fr": "French", "de": "German", "it": "Italian", "pt": "Portuguese", "ru": "Russian", "ar": "Arabic", "hi": "Hindi", "ja": "Japanese", "zh": "Chinese"},
    "es": {"tr": "Turco", "en": "Ingles", "es": "Espanol", "fr": "Frances", "de": "Aleman", "it": "Italiano", "pt": "Portugues", "ru": "Ruso", "ar": "Arabe", "hi": "Hindi", "ja": "Japones", "zh": "Chino"},
    "fr": {"tr": "Turc", "en": "Anglais", "es": "Espagnol", "fr": "Francais", "de": "Allemand", "it": "Italien", "pt": "Portugais", "ru": "Russe", "ar": "Arabe", "hi": "Hindi", "ja": "Japonais", "zh": "Chinois"},
    "de": {"tr": "Türkisch", "en": "Englisch", "es": "Spanisch", "fr": "Französisch", "de": "Deutsch", "it": "Italienisch", "pt": "Portugiesisch", "ru": "Russisch", "ar": "Arabisch", "hi": "Hindi", "ja": "Japanisch", "zh": "Chinesisch"},
    "it": {"tr": "Turco", "en": "Inglese", "es": "Spagnolo", "fr": "Francese", "de": "Tedesco", "it": "Italiano", "pt": "Portoghese", "ru": "Russo", "ar": "Arabo", "hi": "Hindi", "ja": "Giapponese", "zh": "Cinese"},
    "pt": {"tr": "Turco", "en": "Ingles", "es": "Espanhol", "fr": "Frances", "de": "Alemao", "it": "Italiano", "pt": "Portugues", "ru": "Russo", "ar": "Arabe", "hi": "Hindi", "ja": "Japones", "zh": "Chines"},
    "ru": {"tr": "Турецкий", "en": "Английский", "es": "Испанский", "fr": "Французский", "de": "Немецкий", "it": "Итальянский", "pt": "Португальский", "ru": "Русский", "ar": "Арабский", "hi": "Хинди", "ja": "Японский", "zh": "Китайский"},
    "ar": {"tr": "التركية", "en": "الإنجليزية", "es": "الإسبانية", "fr": "الفرنسية", "de": "الألمانية", "it": "الإيطالية", "pt": "البرتغالية", "ru": "الروسية", "ar": "العربية", "hi": "الهندية", "ja": "اليابانية", "zh": "الصينية"},
    "hi": {"tr": "तुर्की", "en": "अंग्रेज़ी", "es": "स्पैनिश", "fr": "फ़्रेंच", "de": "जर्मन", "it": "इतालवी", "pt": "पुर्तगाली", "ru": "रूसी", "ar": "अरबी", "hi": "हिन्दी", "ja": "जापानी", "zh": "चीनी"},
    "ja": {"tr": "トルコ語", "en": "英語", "es": "スペイン語", "fr": "フランス語", "de": "ドイツ語", "it": "イタリア語", "pt": "ポルトガル語", "ru": "ロシア語", "ar": "アラビア語", "hi": "ヒンディー語", "ja": "日本語", "zh": "中国語"},
    "zh": {"tr": "土耳其语", "en": "英语", "es": "西班牙语", "fr": "法语", "de": "德语", "it": "意大利语", "pt": "葡萄牙语", "ru": "俄语", "ar": "阿拉伯语", "hi": "印地语", "ja": "日语", "zh": "中文"},
}


SEO_KEYWORD_SEEDS_BY_LOCALE = {
    "tr": ["SnapVend Gallery uygulaması", "fotoğrafçılar için QR galeri uygulaması", "fotoğraf teslim uygulaması"],
    "en": ["SnapVend Gallery app", "QR photo gallery app", "photographer delivery app"],
    "es": ["aplicación SnapVend Gallery", "aplicación de galería QR para fotógrafos", "aplicación de entrega fotográfica"],
    "fr": ["application SnapVend Gallery", "application de galerie QR pour photographes", "application de livraison photo"],
    "de": ["SnapVend Gallery App", "QR-Galerie-App für Fotografen", "Fotoauslieferungs-App"],
    "it": ["app SnapVend Gallery", "app galleria QR per fotografi", "app per consegna foto"],
    "pt": ["app SnapVend Gallery", "app de galeria QR para fotografos", "app de entrega de fotos"],
    "ru": ["приложение SnapVend Gallery", "QR-галерея для фотографов", "приложение для выдачи фотографий"],
    "ar": ["تطبيق SnapVend Gallery", "تطبيق معرض QR للمصورين", "تطبيق تسليم الصور"],
    "hi": ["SnapVend Gallery ऐप", "फोटोग्राफरों के लिए QR गैलरी ऐप", "फोटो डिलीवरी ऐप"],
    "ja": ["SnapVend Gallery アプリ", "フォトグラファー向け QR ギャラリーアプリ", "写真納品アプリ"],
    "zh": ["SnapVend Gallery 应用", "摄影师二维码画廊应用", "照片交付应用"],
}

SCHEMA_DISAMBIGUATION_BY_LOCALE = {
    "tr": {
        "organization": "SnapVend Gallery, snapvendgallery.com üzerinde yayınlanan fotoğrafçılar için QR galeri ve yerel fotoğraf teslim uygulamasıdır.",
        "software": "SnapVend Gallery, fotoğrafçılar için mobil QR galeri, FTP kamera aktarımı ve yerel ZIP teslim uygulamasıdır.",
    },
    "en": {
        "organization": "SnapVend Gallery is the photographer QR gallery and local photo delivery app published at snapvendgallery.com.",
        "software": "SnapVend Gallery is a mobile QR gallery, FTP camera transfer and local ZIP delivery app for photographers.",
    },
    "es": {
        "organization": "SnapVend Gallery es la aplicación de galería QR y entrega local para fotógrafos publicada en snapvendgallery.com.",
        "software": "SnapVend Gallery es una aplicación móvil de galería QR, transferencia FTP desde cámara y entrega ZIP local para fotógrafos.",
    },
    "fr": {
        "organization": "SnapVend Gallery est l'application de galerie QR et de livraison photo locale pour photographes publiée sur snapvendgallery.com.",
        "software": "SnapVend Gallery est une application mobile de galerie QR, transfert FTP depuis l'appareil photo et livraison ZIP locale pour photographes.",
    },
    "de": {
        "organization": "SnapVend Gallery ist die auf snapvendgallery.com veröffentlichte QR-Galerie- und lokale Fotoauslieferungs-App für Fotografen.",
        "software": "SnapVend Gallery ist eine mobile QR-Galerie-App mit FTP-Kameraimport und lokaler ZIP-Auslieferung für Fotografen.",
    },
    "it": {
        "organization": "SnapVend Gallery è l'app di galleria QR e consegna fotografica locale per fotografi pubblicata su snapvendgallery.com.",
        "software": "SnapVend Gallery è un'app mobile per fotografi con galleria QR, trasferimento FTP dalla fotocamera e consegna ZIP locale.",
    },
    "pt": {
        "organization": "SnapVend Gallery é o app de galeria QR e entrega local de fotos para fotografos publicado em snapvendgallery.com.",
        "software": "SnapVend Gallery é um app movel para fotografos com galeria QR, transferencia FTP da camera e entrega ZIP local.",
    },
    "ru": {
        "organization": "SnapVend Gallery — опубликованное на snapvendgallery.com приложение QR-галереи и локальной выдачи фотографий для фотографов.",
        "software": "SnapVend Gallery — мобильное приложение для фотографов с QR-галереей, FTP-передачей с камеры и локальной ZIP-выдачей.",
    },
    "ar": {
        "organization": "SnapVend Gallery هو تطبيق معرض QR وتسليم صور محلي للمصورين منشور على snapvendgallery.com.",
        "software": "SnapVend Gallery هو تطبيق جوال للمصورين يجمع معرض QR ونقل FTP من الكاميرا وتسليم ZIP المحلي.",
    },
    "hi": {
        "organization": "SnapVend Gallery, snapvendgallery.com पर प्रकाशित फोटोग्राफरों के लिए QR गैलरी और स्थानीय फोटो डिलीवरी ऐप है।",
        "software": "SnapVend Gallery फोटोग्राफरों के लिए मोबाइल QR गैलरी, FTP कैमरा ट्रांसफर और स्थानीय ZIP डिलीवरी ऐप है।",
    },
    "ja": {
        "organization": "SnapVend Gallery は、snapvendgallery.com で公開されているフォトグラファー向け QR ギャラリーおよびローカル写真納品アプリです。",
        "software": "SnapVend Gallery は、フォトグラファー向けのモバイル QR ギャラリー、FTP カメラ転送、ローカル ZIP 納品アプリです。",
    },
    "zh": {
        "organization": "SnapVend Gallery 是发布在 snapvendgallery.com 的摄影师二维码画廊与本地照片交付应用。",
        "software": "SnapVend Gallery 是面向摄影师的移动二维码画廊、FTP 相机传输和本地 ZIP 交付应用。",
    },
}


FIELD_OPERATIONS_SECTION = {
    "tr": {
        "eyebrow": "Yeni Saha Gücü",
        "title": "Satış, baskı ve lisans aynı profesyonel akışta",
        "lead": "SnapVend artık yalnızca QR galeri paylaşımı değil; canlı sunum, çalışan onayı, gerçek baskı hazırlığı ve cihaz bazlı Premium lisans yönetimini aynı saha operasyonunda toplar.",
        "cards": [
            {"title": "Canlı satış sunumu", "body": "Fotoğrafları notebook, tablet veya TV tarayıcısında premium bir vitrin gibi gösterin; müşteri QR ile kendi galerisine geçsin."},
            {"title": "Çalışan onayı ve PAC kontrolü", "body": "Müşteri seçimi satış talebine dönüşür. Ekip onaylar, reddeder veya PAC kodu ile teslimi güvenli şekilde doğrular."},
            {"title": "Düğün baskı hazırlığı", "body": "Seçilen kareleri baskı sipariş listesine alın; iOS tarafında 10x15 cm PDF hazırlayıp AirPrint akışına gönderin."},
            {"title": "Rapor ve dışa aktarma", "body": "Galeri satışı, canlı sunum ve baskı gelirlerini ayrı izleyin; etkinlik sonunda PDF ve Excel çıktısı alın."},
        ],
        "license_label": "Premium lisans",
        "license_title": "1 telefon + 1 tablet ile kontrollü Premium kullanım",
        "license_body": "Premium plan; teslim, canlı sunum ve baskı sipariş listesi limitlerini kaldırır. Doğrulanmış lisans, tanımlı offline pencerede sahada çalışmaya devam eder.",
        "license_points": [
            "Google Play ve App Store abonelik altyapısına hazır",
            "Cihaz aktivasyonu ve cihaz değiştirme akışı",
            "Özel işletme adı, logo ve ZIP dosya adı",
        ],
    },
    "en": {
        "eyebrow": "New Field Power",
        "title": "Sales, printing and licensing in one professional flow",
        "lead": "SnapVend is no longer only a QR gallery handoff; it brings live presentation, staff approval, real print preparation and device-based Premium licensing into the same field operation.",
        "cards": [
            {"title": "Live sales presentation", "body": "Show photos on a notebook, tablet or TV browser like a premium viewing wall; clients enter their own gallery through QR."},
            {"title": "Staff approval and PAC control", "body": "Client selections become sales requests. Your team can approve, reject or validate delivery securely with a PAC code."},
            {"title": "Wedding print preparation", "body": "Move selected frames into the print order list; on iOS, prepare 10x15 cm PDFs and send them into the AirPrint flow."},
            {"title": "Reports and export", "body": "Track gallery sales, live presentation sales and print revenue separately; export PDF and Excel summaries after the event."},
        ],
        "license_label": "Premium license",
        "license_title": "Controlled Premium use with 1 phone + 1 tablet",
        "license_body": "Premium removes delivery, live presentation and print order list limits. A verified license can keep field work running through the defined offline access window.",
        "license_points": [
            "Ready for Google Play and App Store subscriptions",
            "Device activation and device replacement flow",
            "Custom business name, logo and ZIP filename",
        ],
    },
    "es": {
        "eyebrow": "Nueva Potencia En Campo",
        "title": "Venta, impresion y licencia en un flujo profesional",
        "lead": "SnapVend ya no es solo una galeria QR; reune presentacion en vivo, aprobacion del equipo, preparacion real de impresion y licencia Premium por dispositivo en una misma operacion.",
        "cards": [
            {"title": "Presentacion de venta en vivo", "body": "Muestre fotos en navegador de notebook, tablet o TV como una vitrina premium; el cliente entra a su galeria con QR."},
            {"title": "Aprobacion del equipo y control PAC", "body": "La seleccion del cliente se convierte en solicitud de venta. El equipo aprueba, rechaza o valida la entrega con codigo PAC."},
            {"title": "Preparacion de impresion para bodas", "body": "Pase las fotos elegidas a la lista de pedidos de impresion; en iOS genere PDF 10x15 cm y envie al flujo AirPrint."},
            {"title": "Reportes y exportacion", "body": "Separe ventas de galeria, presentacion en vivo e ingresos de impresion; exporte resumen PDF y Excel al terminar el evento."},
        ],
        "license_label": "Licencia Premium",
        "license_title": "Uso Premium controlado con 1 telefono + 1 tablet",
        "license_body": "Premium elimina limites de entrega, presentacion en vivo y lista de pedidos de impresion. La licencia verificada puede seguir funcionando durante la ventana offline definida.",
        "license_points": [
            "Preparado para suscripciones de Google Play y App Store",
            "Activacion de dispositivo y flujo de reemplazo",
            "Nombre comercial, logo y nombre ZIP personalizados",
        ],
    },
    "fr": {
        "eyebrow": "Nouvelle Puissance Terrain",
        "title": "Vente, impression et licence dans un flux professionnel",
        "lead": "SnapVend n'est plus seulement un partage de galerie QR; il regroupe presentation en direct, validation equipe, preparation d'impression et licence Premium par appareil dans une meme operation.",
        "cards": [
            {"title": "Presentation de vente en direct", "body": "Affichez les photos sur notebook, tablette ou TV comme une vitrine premium; le client accede a sa galerie via QR."},
            {"title": "Validation equipe et controle PAC", "body": "La selection client devient une demande de vente. L'equipe approuve, refuse ou valide la livraison avec un code PAC."},
            {"title": "Preparation d'impression mariage", "body": "Ajoutez les images choisies a la liste de commandes d'impression; sur iOS, preparez des PDF 10x15 cm et envoyez vers AirPrint."},
            {"title": "Rapports et export", "body": "Suivez separement ventes galerie, presentation en direct et revenus d'impression; exportez PDF et Excel apres l'evenement."},
        ],
        "license_label": "Licence Premium",
        "license_title": "Usage Premium controle avec 1 telephone + 1 tablette",
        "license_body": "Premium supprime les limites de livraison, presentation en direct et liste de commandes d'impression. Une licence verifiee continue de fonctionner pendant la fenetre offline definie.",
        "license_points": [
            "Pret pour les abonnements Google Play et App Store",
            "Activation d'appareil et parcours de remplacement",
            "Nom d'entreprise, logo et nom de fichier ZIP personnalises",
        ],
    },
    "de": {
        "eyebrow": "Neue Einsatzkraft",
        "title": "Verkauf, Druck und Lizenz in einem professionellen Ablauf",
        "lead": "SnapVend ist nicht mehr nur eine QR Galerie; Live-Prasentation, Teamfreigabe, echte Druckvorbereitung und geratebasierte Premium-Lizenz laufen in einer Vor-Ort-Operation zusammen.",
        "cards": [
            {"title": "Live Verkaufsprasentation", "body": "Zeigen Sie Fotos im Notebook-, Tablet- oder TV-Browser wie eine Premium-Auslage; Kunden wechseln per QR in ihre eigene Galerie."},
            {"title": "Teamfreigabe und PAC Kontrolle", "body": "Kundenauswahlen werden zu Verkaufsanfragen. Das Team kann freigeben, ablehnen oder die Lieferung per PAC-Code absichern."},
            {"title": "Druckvorbereitung fur Hochzeiten", "body": "Legen Sie ausgewahlte Bilder in die Druckbestellliste; auf iOS werden 10x15 cm PDFs vorbereitet und an AirPrint ubergeben."},
            {"title": "Reports und Export", "body": "Verfolgen Sie Galerieverkauf, Live-Prasentation und Druckumsatz getrennt; exportieren Sie PDF- und Excel-Zusammenfassungen nach dem Event."},
        ],
        "license_label": "Premium Lizenz",
        "license_title": "Kontrollierte Premium Nutzung mit 1 Telefon + 1 Tablet",
        "license_body": "Premium entfernt Limits fur Lieferung, Live-Prasentation und Druckbestellliste. Eine verifizierte Lizenz kann innerhalb des definierten Offline-Fensters weiterarbeiten.",
        "license_points": [
            "Bereit fur Google Play und App Store Abonnements",
            "Gerateaktivierung und Geratewechsel-Ablauf",
            "Eigener Firmenname, Logo und ZIP-Dateiname",
        ],
    },
    "it": {
        "eyebrow": "Nuova Forza Sul Campo",
        "title": "Vendita, stampa e licenza in un flusso professionale",
        "lead": "SnapVend non e piu solo una galleria QR; unisce presentazione live, approvazione dello staff, preparazione reale alla stampa e licenza Premium per dispositivo nella stessa operazione.",
        "cards": [
            {"title": "Presentazione vendita live", "body": "Mostra le foto su notebook, tablet o TV come una vetrina premium; il cliente entra nella propria galleria tramite QR."},
            {"title": "Approvazione staff e controllo PAC", "body": "La selezione del cliente diventa una richiesta di vendita. Il team approva, rifiuta o valida la consegna con codice PAC."},
            {"title": "Preparazione stampa matrimonio", "body": "Porta gli scatti scelti nella lista ordini di stampa; su iOS prepara PDF 10x15 cm e inviali al flusso AirPrint."},
            {"title": "Report ed esportazione", "body": "Monitora vendite galleria, presentazione live e ricavi stampa separatamente; esporta riepiloghi PDF ed Excel dopo l'evento."},
        ],
        "license_label": "Licenza Premium",
        "license_title": "Uso Premium controllato con 1 telefono + 1 tablet",
        "license_body": "Premium rimuove i limiti di consegna, presentazione live e lista ordini di stampa. Una licenza verificata continua a lavorare nella finestra offline definita.",
        "license_points": [
            "Pronta per abbonamenti Google Play e App Store",
            "Attivazione dispositivo e flusso di sostituzione",
            "Nome azienda, logo e nome file ZIP personalizzati",
        ],
    },
    "pt": {
        "eyebrow": "Nova Forca Em Campo",
        "title": "Venda, impressao e licenca em um fluxo profissional",
        "lead": "SnapVend nao e apenas uma galeria QR; ele reune apresentacao ao vivo, aprovacao da equipe, preparacao real de impressao e licenca Premium por dispositivo na mesma operacao.",
        "cards": [
            {"title": "Apresentacao de venda ao vivo", "body": "Mostre fotos no navegador de notebook, tablet ou TV como uma vitrine premium; o cliente entra na propria galeria por QR."},
            {"title": "Aprovacao da equipe e controle PAC", "body": "A selecao do cliente vira uma solicitacao de venda. A equipe aprova, rejeita ou valida a entrega com codigo PAC."},
            {"title": "Preparacao de impressao para casamentos", "body": "Envie as fotos escolhidas para a lista de pedidos de impressao; no iOS gere PDFs 10x15 cm e envie ao fluxo AirPrint."},
            {"title": "Relatorios e exportacao", "body": "Acompanhe vendas de galeria, apresentacao ao vivo e receita de impressao separadamente; exporte PDF e Excel apos o evento."},
        ],
        "license_label": "Licenca Premium",
        "license_title": "Uso Premium controlado com 1 telefone + 1 tablet",
        "license_body": "Premium remove limites de entrega, apresentacao ao vivo e lista de pedidos de impressao. Uma licenca verificada continua funcionando durante a janela offline definida.",
        "license_points": [
            "Pronto para assinaturas Google Play e App Store",
            "Ativacao de dispositivo e fluxo de substituicao",
            "Nome comercial, logo e nome ZIP personalizados",
        ],
    },
    "ru": {
        "eyebrow": "Новая Сила В Поле",
        "title": "Продажи, печать и лицензия в одном профессиональном потоке",
        "lead": "SnapVend теперь не просто QR галерея: живая презентация, подтверждение сотрудником, подготовка печати и Premium лицензия по устройствам объединены в одной полевой операции.",
        "cards": [
            {"title": "Живая презентация продаж", "body": "Показывайте фото в браузере ноутбука, планшета или TV как премиальную витрину; клиент переходит в свою галерею по QR."},
            {"title": "Подтверждение команды и PAC", "body": "Выбор клиента становится заявкой на продажу. Команда подтверждает, отклоняет или проверяет выдачу через PAC код."},
            {"title": "Подготовка свадебной печати", "body": "Добавляйте выбранные кадры в список заказов печати; на iOS готовьте PDF 10x15 см и отправляйте в AirPrint."},
            {"title": "Отчеты и экспорт", "body": "Отдельно отслеживайте продажи галереи, живой презентации и печати; после события экспортируйте PDF и Excel."},
        ],
        "license_label": "Premium лицензия",
        "license_title": "Контролируемое Premium использование: 1 телефон + 1 планшет",
        "license_body": "Premium снимает лимиты выдачи, живой презентации и списка заказов печати. Проверенная лицензия продолжает работу в заданном offline окне.",
        "license_points": [
            "Готово к подпискам Google Play и App Store",
            "Активация устройства и сценарий замены",
            "Свой бренд, логотип и имя ZIP файла",
        ],
    },
    "ar": {
        "eyebrow": "قوة ميدانية جديدة",
        "title": "المبيعات والطباعة والترخيص في مسار احترافي واحد",
        "lead": "لم يعد SnapVend مجرد معرض QR؛ بل يجمع العرض المباشر واعتماد الفريق وتجهيز الطباعة الحقيقي وترخيص Premium حسب الجهاز داخل عملية ميدانية واحدة.",
        "cards": [
            {"title": "عرض مبيعات مباشر", "body": "اعرض الصور على متصفح حاسوب او جهاز لوحي او شاشة TV كواجهة عرض احترافية، ثم يدخل العميل الى معرضه عبر QR."},
            {"title": "اعتماد الفريق وتحكم PAC", "body": "تتحول اختيارات العميل الى طلب بيع. يمكن للفريق الاعتماد او الرفض او تأكيد التسليم بأمان عبر رمز PAC."},
            {"title": "تجهيز طباعة حفلات الزفاف", "body": "انقل الصور المختارة الى قائمة طلبات الطباعة؛ وعلى iOS يتم تجهيز PDF بقياس 10x15 سم وارساله الى AirPrint."},
            {"title": "تقارير وتصدير", "body": "تابع مبيعات المعرض والعرض المباشر ودخل الطباعة بشكل منفصل، ثم صدّر ملخصات PDF و Excel بعد الحدث."},
        ],
        "license_label": "ترخيص Premium",
        "license_title": "استخدام Premium مضبوط عبر هاتف واحد + جهاز لوحي واحد",
        "license_body": "يزيل Premium حدود التسليم والعرض المباشر وقائمة طلبات الطباعة. ويمكن للترخيص الموثق متابعة العمل خلال نافذة offline المحددة.",
        "license_points": [
            "جاهز لاشتراكات Google Play و App Store",
            "تفعيل الجهاز ومسار استبدال الجهاز",
            "اسم تجاري وشعار واسم ملف ZIP مخصص",
        ],
    },
    "hi": {
        "eyebrow": "नई मैदानी क्षमता",
        "title": "बिक्री, प्रिंट और लाइसेंस एक पेशेवर प्रवाह में",
        "lead": "SnapVend अब केवल QR गैलरी साझा करने तक सीमित नहीं है; यह लाइव प्रस्तुति, टीम अनुमोदन, वास्तविक प्रिंट तैयारी और डिवाइस आधारित प्रीमियम लाइसेंस प्रबंधन को एक ही मैदानी संचालन में जोड़ता है।",
        "cards": [
            {"title": "लाइव बिक्री प्रस्तुति", "body": "तस्वीरों को लैपटॉप, टैबलेट या टीवी ब्राउज़र पर प्रीमियम प्रदर्शन की तरह दिखाएँ; ग्राहक QR से अपनी गैलरी में प्रवेश करे।"},
            {"title": "टीम अनुमोदन और PAC नियंत्रण", "body": "ग्राहक का चयन बिक्री अनुरोध में बदलता है। टीम उसे स्वीकृत, अस्वीकृत या PAC कोड से सुरक्षित रूप से सत्यापित कर सकती है।"},
            {"title": "शादी प्रिंट तैयारी", "body": "चुनी हुई तस्वीरों को प्रिंट ऑर्डर सूची में भेजें; iOS पर 10x15 cm PDF तैयार करके AirPrint प्रवाह में भेजें।"},
            {"title": "रिपोर्ट और निर्यात", "body": "गैलरी बिक्री, लाइव प्रस्तुति और प्रिंट आय को अलग-अलग देखें; कार्यक्रम के बाद PDF और Excel सारांश निर्यात करें।"},
        ],
        "license_label": "प्रीमियम लाइसेंस",
        "license_title": "1 फोन + 1 टैबलेट के साथ नियंत्रित प्रीमियम उपयोग",
        "license_body": "प्रीमियम योजना डिलीवरी, लाइव प्रस्तुति और प्रिंट ऑर्डर सूची की सीमाएँ हटाती है। सत्यापित लाइसेंस निर्धारित ऑफलाइन अवधि में भी मैदानी काम जारी रख सकता है।",
        "license_points": [
            "Google Play और App Store सदस्यताओं के लिए तैयार",
            "डिवाइस सक्रियण और डिवाइस बदलने का प्रवाह",
            "कस्टम व्यवसाय नाम, लोगो और ZIP फ़ाइल नाम",
        ],
    },
    "ja": {
        "eyebrow": "新しい現場力",
        "title": "販売、プリント、ライセンスを一つのプロ向けフローに",
        "lead": "SnapVend は QR ギャラリー共有だけでなく、ライブ表示、スタッフ承認、実プリント準備、デバイス単位の Premium ライセンス管理を同じ現場オペレーションに統合します。",
        "cards": [
            {"title": "ライブ販売プレゼンテーション", "body": "ノートPC、タブレット、TV ブラウザで写真をプレミアムな展示のように表示し、顧客は QR から自分のギャラリーへ入れます。"},
            {"title": "スタッフ承認と PAC 管理", "body": "顧客の選択は販売リクエストになります。チームは承認、却下、または PAC コードで納品を安全に確認できます。"},
            {"title": "ウェディングプリント準備", "body": "選択された写真をプリント注文リストへ送り、iOS では 10x15 cm PDF を作成して AirPrint フローへ渡せます。"},
            {"title": "レポートとエクスポート", "body": "ギャラリー販売、ライブ表示、プリント売上を分けて追跡し、イベント後に PDF と Excel で出力できます。"},
        ],
        "license_label": "Premium ライセンス",
        "license_title": "1 台のスマートフォン + 1 台のタブレットで管理された Premium 利用",
        "license_body": "Premium は納品、ライブ表示、プリント注文リストの制限を解除します。確認済みライセンスは定義されたオフライン期間でも現場作業を継続できます。",
        "license_points": [
            "Google Play と App Store のサブスクリプションに対応準備",
            "デバイス有効化とデバイス交換フロー",
            "独自の事業名、ロゴ、ZIP ファイル名",
        ],
    },
    "zh": {
        "eyebrow": "全新现场能力",
        "title": "销售、打印与授权进入同一个专业流程",
        "lead": "SnapVend 不再只是 QR 画廊分享；它把现场展示、员工确认、真实打印准备和基于设备的 Premium 授权管理放进同一个现场工作流。",
        "cards": [
            {"title": "现场销售展示", "body": "在笔记本、平板或 TV 浏览器中以高级展示墙方式播放照片；客户通过 QR 进入自己的画廊。"},
            {"title": "员工确认与 PAC 控制", "body": "客户选片会变成销售请求。团队可以批准、拒绝，或通过 PAC 代码安全确认交付。"},
            {"title": "婚礼打印准备", "body": "将选中的照片加入打印订单列表；在 iOS 上生成 10x15 cm PDF，并发送到 AirPrint 流程。"},
            {"title": "报表与导出", "body": "分别追踪画廊销售、现场展示销售和打印收入；活动结束后导出 PDF 与 Excel 汇总。"},
        ],
        "license_label": "Premium 授权",
        "license_title": "1 部手机 + 1 台平板的受控 Premium 使用",
        "license_body": "Premium 会解除交付、现场展示和打印订单列表限制。已验证授权可在定义的离线窗口内继续支持现场工作。",
        "license_points": [
            "已准备支持 Google Play 与 App Store 订阅",
            "设备激活与设备更换流程",
            "自定义商家名称、logo 和 ZIP 文件名",
        ],
    },
}


WHY_SNAPVEND_SECTION = {
    "tr": {
        "eyebrow": "Neden SnapVend?",
        "title": "Klasik galeri paylaşımından daha kontrollü saha akışı",
        "lead": "SnapVend yalnızca fotoğraf göstermek için değil; seçim, ödeme, baskı listesi ve teslimi aynı operasyon içinde toplamak için tasarlandı.",
        "cards": [
            {"title": "Müşteriye uygulama indirtmez", "body": "Müşteri aynı ağda QR ile tarayıcı galerisine girer; ekstra kurulum istemeden akış daha hızlı başlar."},
            {"title": "Oturum bazlı düzen kurar", "body": "Her müşteri, çekim veya grup ayrı kalır; seçim, ödeme ve teslim kayıtları birbirine karışmaz."},
            {"title": "Satış ve teslim tek cihazda kalır", "body": "Yerel ödeme yöntemleri, PAC onayı ve ZIP teslim aynı cihaz üzerinde tamamlanır."},
            {"title": "Canlı çekim için operasyonel kontrol", "body": "FTP kamera aktarımı, baskı listesi, raporlar ve marka ayarları yoğun saha işlerinde daha temiz bir süreç sunar."},
        ],
        "panel_label": "SnapVend farkı",
        "panel_title": "Fotoğrafçının gününü sadeleştirir",
        "panel_points": [
            "QR erişim, oturum, ödeme ve teslim tek akışta ilerler.",
            "Düğün, etkinlik, stüdyo ve mobil portre satışına uyum sağlar.",
            "Yerel ağ mantığı sayesinde hızlı, kontrollü ve internete daha az bağımlı çalışır.",
        ],
    },
    "en": {
        "eyebrow": "Why SnapVend",
        "title": "A more controlled field workflow than a classic gallery handoff",
        "lead": "SnapVend is built not only to show photos, but to combine selection, payment, print prep and delivery in one operational flow.",
        "cards": [
            {"title": "No extra app for the client", "body": "Clients enter the browser gallery through QR on the same network, so the flow starts faster without another app install."},
            {"title": "Session-based structure", "body": "Each client, shoot or group stays separate, so selection, payment and delivery records do not get mixed."},
            {"title": "Sales and delivery stay on one device", "body": "Local payment methods, PAC approval and ZIP delivery are completed on the same device."},
            {"title": "Operational control for live shoots", "body": "FTP camera intake, print list, reports and branding controls keep busy field work more organized."},
        ],
        "panel_label": "The SnapVend difference",
        "panel_title": "It simplifies the photographer's day",
        "panel_points": [
            "QR access, sessions, payment and delivery move through one connected flow.",
            "It fits weddings, events, studio reviews and mobile portrait sales.",
            "The local-network model stays fast, controlled and less dependent on internet coverage.",
        ],
    },
    "es": {
        "eyebrow": "Por que SnapVend",
        "title": "Un flujo en campo mas controlado que una entrega clasica por galeria",
        "lead": "SnapVend no esta pensado solo para mostrar fotos, sino para reunir seleccion, cobro, lista de impresion y entrega en un mismo flujo operativo.",
        "cards": [
            {"title": "No obliga al cliente a instalar otra aplicacion", "body": "El cliente entra a la galeria del navegador con QR en la misma red y el flujo empieza mas rapido sin otra instalacion."},
            {"title": "Orden por sesiones separadas", "body": "Cada cliente, sesion o grupo queda separado, para que seleccion, pago y entrega no se mezclen."},
            {"title": "Venta y entrega en un solo dispositivo", "body": "Los metodos de pago locales, la aprobacion PAC y la entrega ZIP se completan desde el mismo dispositivo."},
            {"title": "Control operativo para trabajo en vivo", "body": "La entrada FTP desde camara, la lista de impresion, los reportes y la marca ayudan a ordenar jornadas intensas."},
        ],
        "panel_label": "Diferencia SnapVend",
        "panel_title": "Simplifica el dia del fotografo",
        "panel_points": [
            "QR, sesiones, pago y entrega avanzan en un mismo flujo conectado.",
            "Funciona bien para bodas, eventos, estudio y ventas de retrato en movilidad.",
            "El modelo de red local mantiene el trabajo rapido, controlado y menos dependiente de internet.",
        ],
    },
    "fr": {
        "eyebrow": "Pourquoi SnapVend",
        "title": "Un flux terrain plus maitrise qu'un simple partage de galerie",
        "lead": "SnapVend n'est pas concu uniquement pour montrer des photos, mais pour reunir selection, paiement, liste d'impression et livraison dans un seul flux operationnel.",
        "cards": [
            {"title": "Aucune application supplementaire pour le client", "body": "Le client entre dans la galerie navigateur via QR sur le meme reseau, sans installation supplementaire."},
            {"title": "Une organisation par session", "body": "Chaque client, prise de vue ou groupe reste separe afin que selection, paiement et livraison ne se melangent pas."},
            {"title": "Vente et livraison depuis un seul appareil", "body": "Paiement local, validation PAC et livraison ZIP se terminent sur le meme appareil."},
            {"title": "Plus de controle pendant les prises en direct", "body": "Le transfert FTP depuis l'appareil photo, la liste d'impression, les rapports et le branding gardent le terrain mieux organise."},
        ],
        "panel_label": "L'avantage SnapVend",
        "panel_title": "Il simplifie la journee du photographe",
        "panel_points": [
            "Acces QR, sessions, paiement et livraison avancent dans un seul flux relie.",
            "Adapte aux mariages, evenements, studios et ventes de portraits mobiles.",
            "Le modele reseau local reste rapide, maitrise et moins dependant d'une connexion internet stable.",
        ],
    },
    "de": {
        "eyebrow": "Warum SnapVend",
        "title": "Ein kontrollierterer Vor-Ort-Ablauf als eine klassische Galerie-Freigabe",
        "lead": "SnapVend wurde nicht nur zum Zeigen von Fotos entwickelt, sondern um Auswahl, Zahlung, Druckliste und Lieferung in einem Ablauf zu vereinen.",
        "cards": [
            {"title": "Keine zusaetzliche App fuer den Kunden", "body": "Kunden oeffnen die Browser-Galerie per QR im selben Netzwerk, sodass der Ablauf ohne weitere Installation schneller startet."},
            {"title": "Klare Ordnung durch Sessions", "body": "Jeder Kunde, jedes Shooting und jede Gruppe bleibt getrennt, damit Auswahl, Zahlung und Lieferung nicht vermischt werden."},
            {"title": "Verkauf und Lieferung auf einem Geraet", "body": "Lokale Zahlungsmethoden, PAC-Freigabe und ZIP-Lieferung werden auf demselben Geraet abgeschlossen."},
            {"title": "Mehr operative Kontrolle bei Live-Shootings", "body": "FTP-Kameraimport, Druckliste, Reports und Branding halten intensive Einsaetze besser organisiert."},
        ],
        "panel_label": "Der SnapVend Unterschied",
        "panel_title": "Es vereinfacht den Tag des Fotografen",
        "panel_points": [
            "QR-Zugang, Sessions, Zahlung und Lieferung laufen in einem verbundenen Ablauf.",
            "Geeignet fuer Hochzeiten, Events, Studios und mobilen Portraitverkauf.",
            "Das lokale Netzwerkmodell bleibt schnell, kontrolliert und weniger von Internetabdeckung abhaengig.",
        ],
    },
    "it": {
        "eyebrow": "Perche SnapVend",
        "title": "Un flusso sul campo piu controllato di una classica consegna via galleria",
        "lead": "SnapVend non e pensato solo per mostrare foto, ma per unire selezione, pagamento, lista di stampa e consegna in un unico flusso operativo.",
        "cards": [
            {"title": "Nessuna app extra per il cliente", "body": "Il cliente entra nella galleria browser via QR sulla stessa rete, cosi il flusso parte piu velocemente senza un'altra installazione."},
            {"title": "Ordine basato su sessioni", "body": "Ogni cliente, servizio o gruppo resta separato, quindi selezione, pagamento e consegna non si confondono."},
            {"title": "Vendita e consegna su un solo dispositivo", "body": "Metodi di pagamento locali, approvazione PAC e consegna ZIP si completano sullo stesso dispositivo."},
            {"title": "Controllo operativo per servizi live", "body": "Ingresso FTP dalla fotocamera, lista di stampa, report e branding aiutano a gestire giornate intense in modo piu pulito."},
        ],
        "panel_label": "Differenza SnapVend",
        "panel_title": "Semplifica la giornata del fotografo",
        "panel_points": [
            "Accesso QR, sessioni, pagamento e consegna avanzano in un unico flusso collegato.",
            "Si adatta a matrimoni, eventi, studi fotografici e vendite ritratto in mobilita.",
            "Il modello in rete locale resta rapido, controllato e meno dipendente da internet.",
        ],
    },
    "pt": {
        "eyebrow": "Por que SnapVend",
        "title": "Um fluxo em campo mais controlado do que uma entrega classica por galeria",
        "lead": "O SnapVend nao foi criado apenas para mostrar fotos, mas para reunir selecao, pagamento, lista de impressao e entrega em um unico fluxo operacional.",
        "cards": [
            {"title": "Sem exigir outro aplicativo do cliente", "body": "O cliente entra na galeria do navegador via QR na mesma rede, entao o fluxo comeca mais rapido sem outra instalacao."},
            {"title": "Organizacao por sessoes", "body": "Cada cliente, ensaio ou grupo fica separado para que selecao, pagamento e entrega nao se misturem."},
            {"title": "Venda e entrega em um unico dispositivo", "body": "Metodos de pagamento locais, aprovacao PAC e entrega ZIP sao concluídos no mesmo dispositivo."},
            {"title": "Controle operacional para captacao ao vivo", "body": "Entrada FTP da camera, lista de impressao, relatorios e branding deixam rotinas intensas mais organizadas."},
        ],
        "panel_label": "Diferenca SnapVend",
        "panel_title": "Ele simplifica o dia do fotografo",
        "panel_points": [
            "Acesso por QR, sessoes, pagamento e entrega avancam em um unico fluxo conectado.",
            "Combina com casamentos, eventos, estudio e vendas de retrato em mobilidade.",
            "O modelo de rede local continua rapido, controlado e menos dependente de internet.",
        ],
    },
    "ru": {
        "eyebrow": "Почему SnapVend",
        "title": "Более управляемый выездной процесс, чем обычная передача галереи",
        "lead": "SnapVend создан не только для показа фотографий, но и для того, чтобы объединить выбор, оплату, список на печать и выдачу в одном рабочем процессе.",
        "cards": [
            {"title": "Клиенту не нужно отдельное приложение", "body": "Клиент открывает браузерную галерею по QR в той же сети, поэтому работа начинается быстрее без дополнительной установки."},
            {"title": "Порядок через отдельные сессии", "body": "Каждый клиент, съемка или группа остаются отдельно, поэтому выбор, оплата и выдача не смешиваются."},
            {"title": "Продажа и выдача на одном устройстве", "body": "Локальные способы оплаты, подтверждение PAC и ZIP-выдача завершаются на одном и том же устройстве."},
            {"title": "Операционный контроль на живой съемке", "body": "FTP-импорт с камеры, список печати, отчеты и брендирование помогают лучше держать загруженную площадку под контролем."},
        ],
        "panel_label": "Преимущество SnapVend",
        "panel_title": "Он упрощает день фотографа",
        "panel_points": [
            "QR-доступ, сессии, оплата и выдача идут в одном связанном потоке.",
            "Подходит для свадеб, мероприятий, студий и мобильных портретных продаж.",
            "Локальная сетевая модель остается быстрой, контролируемой и менее зависимой от интернета.",
        ],
    },
    "ar": {
        "eyebrow": "لماذا SnapVend",
        "title": "تدفق ميداني اكثر تحكما من مشاركة معرض تقليدية",
        "lead": "لم يتم تصميم SnapVend فقط لعرض الصور، بل لجمع الاختيار والدفع وقائمة الطباعة والتسليم داخل تدفق تشغيلي واحد.",
        "cards": [
            {"title": "لا يطلب من العميل تثبيت تطبيق اضافي", "body": "يدخل العميل الى معرض المتصفح عبر QR على نفس الشبكة، لذلك يبدأ التدفق بسرعة اكبر من دون تثبيت اخر."},
            {"title": "تنظيم قائم على الجلسات", "body": "يبقى كل عميل او جلسة او مجموعة منفصلة، لذلك لا تختلط الاختيارات والمدفوعات وعمليات التسليم."},
            {"title": "البيع والتسليم من نفس الجهاز", "body": "تكتمل وسائل الدفع المحلية وموافقة PAC وتسليم ZIP على نفس الجهاز."},
            {"title": "تحكم تشغيلي للتصوير الحي", "body": "استيراد FTP من الكاميرا وقائمة الطباعة والتقارير والعلامة التجارية تجعل العمل الميداني المكثف اكثر تنظيما."},
        ],
        "panel_label": "فرق SnapVend",
        "panel_title": "يبسط يوم المصور",
        "panel_points": [
            "الوصول عبر QR والجلسات والدفع والتسليم تتحرك داخل تدفق واحد مترابط.",
            "مناسب لحفلات الزفاف والفعاليات والاستوديو وبيع البورتريه المتنقل.",
            "يعتمد على شبكة محلية سريعة ومضبوطة واقل اعتمادا على تغطية الانترنت.",
        ],
    },
    "hi": {
        "eyebrow": "क्यों SnapVend",
        "title": "सामान्य गैलरी शेयरिंग से ज्यादा नियंत्रित फील्ड फ्लो",
        "lead": "SnapVend सिर्फ फोटो दिखाने के लिए नहीं, बल्कि चयन, भुगतान, प्रिंट सूची और डिलीवरी को एक ही संचालन प्रवाह में जोड़ने के लिए बनाया गया है।",
        "cards": [
            {"title": "ग्राहक को अलग ऐप नहीं चाहिए", "body": "ग्राहक उसी नेटवर्क पर QR से ब्राउज़र गैलरी में जाता है, इसलिए बिना किसी अतिरिक्त इंस्टॉल के फ्लो जल्दी शुरू हो जाता है।"},
            {"title": "सेशन आधारित व्यवस्थित ढांचा", "body": "हर ग्राहक, शूट या समूह अलग रहता है, इसलिए चयन, भुगतान और डिलीवरी रिकॉर्ड आपस में नहीं मिलते।"},
            {"title": "बिक्री और डिलीवरी एक ही डिवाइस पर", "body": "स्थानीय भुगतान तरीके, PAC अनुमोदन और ZIP डिलीवरी एक ही डिवाइस पर पूरी हो जाती है।"},
            {"title": "लाइव शूट के लिए बेहतर संचालन नियंत्रण", "body": "FTP कैमरा इंपोर्ट, प्रिंट सूची, रिपोर्ट और ब्रांडिंग नियंत्रण व्यस्त फील्ड कार्य को ज्यादा व्यवस्थित बनाते हैं।"},
        ],
        "panel_label": "SnapVend का फर्क",
        "panel_title": "यह फोटोग्राफर का दिन आसान बनाता है",
        "panel_points": [
            "QR एक्सेस, सेशन, भुगतान और डिलीवरी एक जुड़े हुए फ्लो में चलते हैं।",
            "यह शादी, इवेंट, स्टूडियो और मोबाइल पोर्ट्रेट बिक्री के लिए अच्छी तरह काम करता है।",
            "लोकल नेटवर्क मॉडल तेज, नियंत्रित और इंटरनेट पर कम निर्भर रहता है।",
        ],
    },
    "ja": {
        "eyebrow": "なぜ SnapVend",
        "title": "従来のギャラリー共有よりも管理しやすい現場フロー",
        "lead": "SnapVend は写真を見せるだけでなく、選択、支払い、プリント準備、納品までを一つの運用フローにまとめるために作られています。",
        "cards": [
            {"title": "顧客に別アプリを入れさせない", "body": "顧客は同じネットワーク上で QR からブラウザギャラリーへ入れるため、追加インストールなしで流れが始まります。"},
            {"title": "セッション単位で整理できる", "body": "顧客、撮影、グループごとに分けて管理できるので、選択、支払い、納品が混ざりません。"},
            {"title": "販売と納品を一台で完了", "body": "ローカル決済、PAC 承認、ZIP 納品までを同じ端末で完了できます。"},
            {"title": "ライブ撮影向けの運用コントロール", "body": "FTP カメラ取り込み、プリントリスト、レポート、ブランド設定が忙しい現場をより整理しやすくします。"},
        ],
        "panel_label": "SnapVend の違い",
        "panel_title": "フォトグラファーの一日をシンプルにする",
        "panel_points": [
            "QR アクセス、セッション、支払い、納品が一つの流れでつながります。",
            "結婚式、イベント、スタジオ、モバイルポートレート販売に合います。",
            "ローカルネットワーク中心なので、速く、管理しやすく、インターネット依存も抑えられます。",
        ],
    },
    "zh": {
        "eyebrow": "为什么选择 SnapVend",
        "title": "比传统画廊分享更可控的现场流程",
        "lead": "SnapVend 不只是用来展示照片，而是为了把选片、收款、打印准备和交付整合进同一套工作流程。",
        "cards": [
            {"title": "不要求客户额外安装应用", "body": "客户在同一网络内通过二维码进入浏览器画廊，无需额外安装，流程启动更快。"},
            {"title": "基于会话的清晰管理", "body": "每位客户、每场拍摄或每个群组都能保持独立，因此选片、付款和交付不会混在一起。"},
            {"title": "销售与交付留在同一设备", "body": "本地支付方式、PAC 确认和 ZIP 交付都可以在同一设备上完成。"},
            {"title": "适合现场拍摄的运营控制", "body": "FTP 相机导入、打印列表、报表和品牌设置，让高强度现场工作更有秩序。"},
        ],
        "panel_label": "SnapVend 的不同点",
        "panel_title": "让摄影师的一天更简单",
        "panel_points": [
            "二维码进入、会话、支付和交付连接在同一个流程里。",
            "适合婚礼、活动、影楼和移动人像销售场景。",
            "本地网络模式更快、更可控，也更少依赖互联网覆盖。",
        ],
    },
}


CONTACT_SECTION = {
    "tr": {
        "eyebrow": "İletişim",
        "title": "İstek, talep ve iş birliği mesajlarını doğrudan bize gönderin",
        "lead": "Formu gönderdiğinizde varsayılan e-posta uygulamanız açılır ve mesaj snapvendinfo@gmail.com adresine hazır şekilde gider.",
        "panel_title": "Bize Yazın",
        "panel_note": "Demo talebi, fiyat sorusu, iş ortaklığı veya özel akış ihtiyacınız için formu kullanın.",
        "highlights": ["Demo talebi", "Fiyat ve lisans soruları", "Özel akış ve iş ortaklığı"],
        "type_label": "Konu",
        "topics": ["Genel Bilgi", "Demo Talebi", "Fiyatlandırma", "İş Ortaklığı", "Özel Talep"],
        "name_label": "Ad Soyad",
        "company_label": "İşletme / Marka",
        "email_label": "E-posta",
        "message_label": "Mesaj",
        "message_placeholder": "İhtiyacınızı, etkinlik tipinizi veya iletmek istediğiniz talebi kısaca yazın.",
        "submit": "Gönder",
        "direct_email": "Doğrudan E-posta Gönder",
        "disclaimer": "Gönder butonu mail uygulamanızı açar; mesajı oradan onaylayabilirsiniz.",
        "subject_prefix": "SnapVend web talebi",
    },
    "en": {
        "eyebrow": "Contact",
        "title": "Send your request, inquiry or partnership message directly to us",
        "lead": "When you submit the form, your default mail app opens and prepares the message for snapvendinfo@gmail.com.",
        "panel_title": "Write To Us",
        "panel_note": "Use this form for demo requests, pricing questions, partnerships or custom workflow needs.",
        "highlights": ["Demo request", "Pricing and licensing", "Custom workflow or partnership"],
        "type_label": "Topic",
        "topics": ["General Inquiry", "Demo Request", "Pricing", "Partnership", "Custom Request"],
        "name_label": "Full Name",
        "company_label": "Business / Brand",
        "email_label": "Email",
        "message_label": "Message",
        "message_placeholder": "Briefly describe your need, event type or request.",
        "submit": "Send",
        "direct_email": "Send Email Directly",
        "disclaimer": "The send button opens your mail app so you can review and confirm the message.",
        "subject_prefix": "SnapVend website inquiry",
    },
    "es": {
        "eyebrow": "Contacto",
        "title": "Envíe su consulta, solicitud o mensaje comercial directamente",
        "lead": "Al enviar el formulario se abre su aplicacion de correo y el mensaje queda listo para snapvendinfo@gmail.com.",
        "panel_title": "Escribanos",
        "panel_note": "Use este formulario para demos, precios, alianzas o necesidades especiales.",
        "highlights": ["Solicitud de demo", "Precios y licencias", "Alianza o flujo especial"],
        "type_label": "Tema",
        "topics": ["Consulta General", "Solicitud De Demo", "Precios", "Alianza", "Solicitud Especial"],
        "name_label": "Nombre",
        "company_label": "Empresa / Marca",
        "email_label": "Correo",
        "message_label": "Mensaje",
        "message_placeholder": "Describa brevemente su necesidad o tipo de evento.",
        "submit": "Enviar",
        "direct_email": "Enviar Correo Directo",
        "disclaimer": "El boton abre su correo para revisar y confirmar el mensaje.",
        "subject_prefix": "Consulta web de SnapVend",
    },
    "fr": {
        "eyebrow": "Contact",
        "title": "Envoyez nous directement votre demande ou message commercial",
        "lead": "Quand vous envoyez le formulaire, votre application mail s'ouvre et prepare le message pour snapvendinfo@gmail.com.",
        "panel_title": "Ecrivez Nous",
        "panel_note": "Utilisez ce formulaire pour une demo, des tarifs, un partenariat ou un besoin specifique.",
        "highlights": ["Demande de demo", "Tarifs et licences", "Partenariat ou besoin special"],
        "type_label": "Sujet",
        "topics": ["Question Generale", "Demande De Demo", "Tarifs", "Partenariat", "Demande Speciale"],
        "name_label": "Nom Complet",
        "company_label": "Entreprise / Marque",
        "email_label": "Email",
        "message_label": "Message",
        "message_placeholder": "Decrivez brievement votre besoin ou type d'evenement.",
        "submit": "Envoyer",
        "direct_email": "Envoyer Un Courriel",
        "disclaimer": "Le bouton ouvre votre application mail pour verifier et confirmer le message.",
        "subject_prefix": "Demande web SnapVend",
    },
    "de": {
        "eyebrow": "Kontakt",
        "title": "Senden Sie Anfrage, Wunsch oder Partnerschaft direkt an uns",
        "lead": "Beim Absenden offnet sich Ihr Mail Programm und bereitet die Nachricht fur snapvendinfo@gmail.com vor.",
        "panel_title": "Schreiben Sie Uns",
        "panel_note": "Nutzen Sie das Formular fur Demoanfragen, Preise, Partnerschaften oder spezielle Ablaufe.",
        "highlights": ["Demo Anfrage", "Preise und Lizenzen", "Partnerschaft oder Sonderwunsch"],
        "type_label": "Thema",
        "topics": ["Allgemeine Anfrage", "Demo Anfrage", "Preise", "Partnerschaft", "Sonderwunsch"],
        "name_label": "Vollstandiger Name",
        "company_label": "Firma / Marke",
        "email_label": "E-Mail",
        "message_label": "Nachricht",
        "message_placeholder": "Beschreiben Sie kurz Ihren Bedarf oder den Einsatztyp.",
        "submit": "Senden",
        "direct_email": "Direkt Per E-Mail",
        "disclaimer": "Der Senden Button offnet Ihr Mail Programm zur Bestatigung.",
        "subject_prefix": "SnapVend Website Anfrage",
    },
    "it": {
        "eyebrow": "Contatto",
        "title": "Invia direttamente richieste, domande o proposte di collaborazione",
        "lead": "Quando invii il modulo, si apre l'applicazione email predefinita e il messaggio viene preparato per snapvendinfo@gmail.com.",
        "panel_title": "Scrivici",
        "panel_note": "Usa questo modulo per demo, prezzi, partnership o esigenze di flussi personalizzati.",
        "highlights": ["Richiesta demo", "Prezzi e licenze", "Partnership o flusso personalizzato"],
        "type_label": "Argomento",
        "topics": ["Richiesta Generale", "Richiesta Demo", "Prezzi", "Partnership", "Richiesta Personalizzata"],
        "name_label": "Nome e Cognome",
        "company_label": "Azienda / Brand",
        "email_label": "E-mail",
        "message_label": "Messaggio",
        "message_placeholder": "Descrivi brevemente la tua esigenza, il tipo di evento o la richiesta.",
        "submit": "Invia",
        "direct_email": "Invia E-mail Direttamente",
        "disclaimer": "Il pulsante apre la tua applicazione email cosi puoi controllare e confermare il messaggio.",
        "subject_prefix": "Richiesta dal sito SnapVend",
    },
    "pt": {
        "eyebrow": "Contato",
        "title": "Envie sua solicitacao, duvida ou proposta diretamente para nos",
        "lead": "Ao enviar o formulario, seu aplicativo de e-mail abre e prepara a mensagem para snapvendinfo@gmail.com.",
        "panel_title": "Fale Conosco",
        "panel_note": "Use o formulario para demos, precos, parcerias ou necessidades especiais de fluxo.",
        "highlights": ["Pedido de demo", "Precos e licencas", "Parceria ou fluxo especial"],
        "type_label": "Assunto",
        "topics": ["Contato Geral", "Pedido De Demo", "Precos", "Parceria", "Solicitacao Especial"],
        "name_label": "Nome Completo",
        "company_label": "Empresa / Marca",
        "email_label": "E-mail",
        "message_label": "Mensagem",
        "message_placeholder": "Descreva rapidamente sua necessidade ou tipo de evento.",
        "submit": "Enviar",
        "direct_email": "Enviar E-mail Direto",
        "disclaimer": "O botao abrira seu aplicativo de e-mail para revisar e confirmar a mensagem.",
        "subject_prefix": "Contato web SnapVend",
    },
    "ru": {
        "eyebrow": "Контакт",
        "title": "Отправьте запрос, пожелание или предложение напрямую",
        "lead": "После отправки формы откроется ваша почтовая программа и подготовит письмо для snapvendinfo@gmail.com.",
        "panel_title": "Напишите Нам",
        "panel_note": "Форма подходит для запроса демо, цен, партнерства или особого сценария.",
        "highlights": ["Запрос демо", "Цены и лицензии", "Партнерство или особый сценарий"],
        "type_label": "Тема",
        "topics": ["Общий Вопрос", "Запрос Демо", "Цены", "Партнерство", "Особый Запрос"],
        "name_label": "Имя",
        "company_label": "Компания / Бренд",
        "email_label": "Почта",
        "message_label": "Сообщение",
        "message_placeholder": "Кратко опишите задачу, тип мероприятия или запрос.",
        "submit": "Отправить",
        "direct_email": "Написать На Почту",
        "disclaimer": "Кнопка откроет почтовое приложение, где письмо можно проверить и отправить.",
        "subject_prefix": "Запрос с сайта SnapVend",
    },
    "ar": {
        "eyebrow": "تواصل",
        "title": "ارسل طلبك او استفسارك او رسالة الشراكة مباشرة الينا",
        "lead": "عند ارسال النموذج سيفتح تطبيق البريد الافتراضي لديك ويجهز الرسالة الى snapvendinfo@gmail.com.",
        "panel_title": "اكتب لنا",
        "panel_note": "استخدم النموذج لطلب عرض تجريبي او سؤال عن الاسعار او شراكة او احتياج خاص.",
        "highlights": ["طلب عرض تجريبي", "اسعار وتراخيص", "شراكة او طلب خاص"],
        "type_label": "الموضوع",
        "topics": ["استفسار عام", "طلب عرض", "الاسعار", "شراكة", "طلب خاص"],
        "name_label": "الاسم",
        "company_label": "الجهة / العلامة",
        "email_label": "البريد",
        "message_label": "الرسالة",
        "message_placeholder": "اكتب باختصار احتياجك او نوع الحدث او الطلب.",
        "submit": "ارسال",
        "direct_email": "ارسال بريد مباشر",
        "disclaimer": "زر الارسال يفتح تطبيق البريد لتراجع الرسالة وتؤكدها.",
        "subject_prefix": "طلب من موقع SnapVend",
    },
    "hi": {
        "eyebrow": "संपर्क",
        "title": "अपनी पूछताछ, अनुरोध या साझेदारी संदेश सीधे हमें भेजें",
        "lead": "फॉर्म सबमिट करते ही आपका डिफ़ॉल्ट मेल ऐप खुलेगा और संदेश snapvendinfo@gmail.com के लिए तैयार हो जाएगा।",
        "panel_title": "हमें लिखें",
        "panel_note": "डेमो अनुरोध, कीमत, साझेदारी या कस्टम कार्यप्रवाह की जरूरत के लिए यह फॉर्म इस्तेमाल करें।",
        "highlights": ["डेमो अनुरोध", "कीमत और लाइसेंस", "कस्टम कार्यप्रवाह या साझेदारी"],
        "type_label": "विषय",
        "topics": ["सामान्य पूछताछ", "डेमो अनुरोध", "मूल्य जानकारी", "साझेदारी", "कस्टम अनुरोध"],
        "name_label": "पूरा नाम",
        "company_label": "व्यवसाय / ब्रांड",
        "email_label": "ईमेल",
        "message_label": "संदेश",
        "message_placeholder": "अपनी जरूरत या इवेंट प्रकार संक्षेप में लिखें।",
        "submit": "भेजें",
        "direct_email": "सीधा ईमेल भेजें",
        "disclaimer": "भेजें बटन आपका मेल ऐप खोलेगा ताकि आप संदेश देखकर भेज सकें।",
        "subject_prefix": "SnapVend वेबसाइट पूछताछ",
    },
    "ja": {
        "eyebrow": "お問い合わせ",
        "title": "ご要望やご相談、提携メッセージを直接お送りください",
        "lead": "フォーム送信時に既定のメールアプリが開き、snapvendinfo@gmail.com 宛ての内容が準備されます。",
        "panel_title": "ご連絡ください",
        "panel_note": "デモ依頼、料金確認、提携相談、特別な運用相談にこのフォームを使えます。",
        "highlights": ["デモ依頼", "料金とライセンス", "提携または特別相談"],
        "type_label": "件名",
        "topics": ["一般的な問い合わせ", "デモ依頼", "料金", "提携", "特別な依頼"],
        "name_label": "お名前",
        "company_label": "会社 / ブランド",
        "email_label": "メール",
        "message_label": "メッセージ",
        "message_placeholder": "用途やイベント内容、相談したい内容を簡単に記入してください。",
        "submit": "送信",
        "direct_email": "メールを直接送る",
        "disclaimer": "送信ボタンを押すとメールアプリが開き、内容を確認して送れます。",
        "subject_prefix": "SnapVend サイト問い合わせ",
    },
    "zh": {
        "eyebrow": "联系",
        "title": "把需求、咨询或合作消息直接发给我们",
        "lead": "提交表单后，系统会打开你的默认邮件应用，并自动准备发往 snapvendinfo@gmail.com 的内容。",
        "panel_title": "给我们留言",
        "panel_note": "这个表单可用于演示申请、价格咨询、合作沟通或特殊流程需求。",
        "highlights": ["演示申请", "价格与授权", "合作或特殊需求"],
        "type_label": "主题",
        "topics": ["一般咨询", "演示申请", "价格咨询", "合作", "特殊需求"],
        "name_label": "姓名",
        "company_label": "公司 / 品牌",
        "email_label": "邮箱",
        "message_label": "留言",
        "message_placeholder": "请简要说明你的需求、活动类型或想咨询的问题。",
        "submit": "发送",
        "direct_email": "直接发邮件",
        "disclaimer": "点击发送后会打开邮件应用，你可以检查后再发送。",
        "subject_prefix": "SnapVend 网站咨询",
    },
}


COPY = {
    "tr": {
        "meta_title": "SnapVend | Fotoğrafçılar İçin QR Galeri ve Yerel Teslim",
        "meta_description": "SnapVend, fotoğrafçıların aynı telefon veya tablette QR galeri paylaşımı, FTP kamera aktarımı ve ZIP teslim akışını yönetmesine yardımcı olur.",
        "nav_how": "Nasıl Çalışır",
        "nav_audience": "Kimler İçin",
        "nav_pricing": "Fiyatlandırma",
        "nav_download": "İndir",
        "language_label": "Dil",
        "hero_eyebrow": "QR galeri, FTP aktarım, yerel teslim",
        "hero_title": "Çekimden teslimata tek cihazda akış.",
        "hero_lead": "Fotoğrafları kameradan ya da galeriden alın, müşteriyi QR ile içeri alın, PAC onayını verin ve onaylanan dosyaları aynı cihazdan ZIP olarak teslim edin.",
        "google_small": "Android için indir",
        "apple_small": "iPhone ve iPad için indir",
        "setup_note": "Aylık ve yıllık fiyatlarla doğrudan App Store bağlantısını site-config.js dosyasından güncelleyebilirsin. Apple mağaza ID'si eklenene kadar iOS logosu bölgesel App Store arama sonucunu açar.",
        "metrics": [
            {"value": "1 cihaz", "label": "Al, göster, teslim et"},
            {"value": "6 yöntem", "label": "Hazır yerel ödeme akışı"},
            {"value": "0 bulut", "label": "Yerel çalışma, takip yok"},
        ],
        "workflow_eyebrow": "Akış",
        "workflow_title": "Sahada hızlı, kontrollü ve anlaşılır kullanım",
        "workflow_lead": "SnapVend çekim sırasında fotoğraf almayı, müşteriye göstermeyi ve teslimi tek bir operasyon haline getirir.",
        "workflow_cards": [
            {"title": "Fotoğrafları içe aktar", "body": "Yerel galeriden seçin ya da FTP destekli kameradan SnapVend akışına gönderin."},
            {"title": "Galeriyi QR ile paylaş", "body": "Müşteri aynı ağdayken QR kodu okutur ve tarayıcıdan galeriye girer."},
            {"title": "Yerel ödeme yöntemini göster", "body": "İşletme ülkenize göre FAST / EFT, Bizum, UPI, Alipay, WeChat Pay veya PayPay gibi hazır yöntemleri ödeme popup ekranında gösterin."},
            {"title": "Seçim ve PAC onayı", "body": "Müşteri kareleri seçer, siz ödeme ve PAC doğrulamasını kontrol edersiniz."},
            {"title": "ZIP teslim ve raporlama", "body": "Onaylanan dosyalar ZIP olarak iner; teslim ve gelir akışı uygulama içinde izlenir."},
        ],
        "audience_eyebrow": "Kimler İçin",
        "audience_title": "Profesyonel saha ekipleri için tasarlandı",
        "audience_lead": "Müşteriye hızlı önizleme ve kontrollü teslim sunmak isteyen fotoğraf ekipleri için doğru merkez.",
        "audience_cards": [
            {"title": "Düğün ve etkinlik fotoğrafçıları", "body": "Canlı çekimde müşteriye hızlı seçim ve teslim sunmak isteyen ekipler."},
            {"title": "Stüdyo ve portre çekimleri", "body": "Müşteriyle birlikte seçim yapıp daha düzenli ilerlemek isteyen stüdyolar."},
            {"title": "Okul, spor ve kurumsal işler", "body": "Oturumları karıştırmadan toplu çekimleri yönetmek isteyen ekipler."},
            {"title": "Sokak, turistik alan ve mobil portre çekimleri", "body": "Sahada hızlı çekim yapıp, seçilen kareleri anında göstererek tekli veya paket teslim satışı yapmak isteyen fotoğrafçılar için güçlü bir akış sunar."},
            {"title": "Mobil teslim ekipleri", "body": "İnternete bağlı kalmadan yerel ağ ve hotspot ile çalışan operasyonlar."},
        ],
        "pricing_eyebrow": "Planlar",
        "pricing_title": "Ücretsiz başlayın, Pro ile büyütün",
        "pricing_lead": "Ücretsiz plan akışı öğrenmek için hazırdır. Pro planlar teslim limitini kaldırır ve işletme markalamasını açar.",
        "config_warning": "Bu repoda kesin aylık/yıllık fiyat yok. Fiyatlar ve doğrudan App Store linki site-config.js dosyasından güncellenir.",
        "free_badge": "Ücretsiz",
        "free_title": "Akışı öğrenmek için ideal",
        "free_period": "başlangıç",
        "free_features": [
            "Günlük 10 fotoğraf teslim limiti",
            "SnapVend markası görünür kalır",
            "Özel işletme adı ve logo kapalıdır",
            "Canlı kullanım öncesi sistemi denemek için uygundur",
        ],
        "free_cta": "Ücretsiz başla",
        "monthly_badge": "Pro Aylık",
        "monthly_title": "Esnek aylık kullanım",
        "monthly_placeholder": "Fiyatı güncelle",
        "monthly_period": "/ ay",
        "monthly_features": [
            "Sınırsız günlük teslim",
            "Özel işletme adı ve logo",
            "Özel ZIP dosya adı",
            "Sınırsız düğün baskı listesi",
        ],
        "monthly_cta": "Uygulamayı indir",
        "yearly_badge": "Pro Yıllık",
        "yearly_title": "Düzenli kullanım için avantajlı",
        "yearly_placeholder": "Fiyatı güncelle",
        "yearly_period": "/ yıl",
        "yearly_features": [
            "Daha düşük yıllık maliyet hedefi",
            "Sınırsız günlük teslim",
            "Tam marka kontrolü",
            "Yoğun saha kullanımı için kalıcı çözüm",
        ],
        "yearly_cta": "Uygulamayı indir",
        "cta_eyebrow": "Hazır mısın?",
        "cta_title": "SnapVend ile sahada daha hızlı göster, seçtir ve teslim et.",
        "cta_lead": "QR erişimi, FTP aktarımı, yerel paylaşım ve raporlama tek deneyimde buluşur.",
        "footer_note": "SnapVend medyayı cihaz üzerinde işler. Paylaşım yalnızca sizin başlattığınız yerel ağ akışında açılır.",
    },
    "en": {
        "meta_title": "SnapVend | QR Gallery and Local Photo Delivery for Photographers",
        "meta_description": "SnapVend helps photographers import, present and deliver photos from one phone or tablet with QR gallery sharing, FTP camera transfer and ZIP delivery.",
        "nav_how": "How It Works",
        "nav_audience": "Users",
        "nav_pricing": "Pricing",
        "nav_download": "Download",
        "language_label": "Language",
        "hero_eyebrow": "QR gallery, FTP transfer, local delivery",
        "hero_title": "One device from capture to delivery.",
        "hero_lead": "Bring photos in from your camera or gallery, let clients enter through a QR link, confirm PAC and deliver approved files as ZIP from the same device.",
        "google_small": "Download for Android",
        "apple_small": "Download for iPhone and iPad",
        "setup_note": "You can update the monthly and yearly prices plus the direct App Store link from site-config.js. Until the Apple app ID is added, the iOS logo opens the regional App Store search result.",
        "metrics": [
            {"value": "1 device", "label": "Receive, show and deliver"},
            {"value": "6 methods", "label": "Ready local payment flow"},
            {"value": "0 cloud", "label": "Local workflow, no tracking"},
        ],
        "workflow_eyebrow": "Workflow",
        "workflow_title": "Fast, controlled and field-ready",
        "workflow_lead": "SnapVend turns photo intake, client preview and delivery into one clean operation during live shoots.",
        "workflow_cards": [
            {"title": "Import the photos", "body": "Pick them from local media or send them into SnapVend from an FTP-capable camera."},
            {"title": "Share the gallery with QR", "body": "The client scans the code on the same network and opens the browser gallery instantly."},
            {"title": "Show local payment methods", "body": "Display ready methods such as FAST / EFT, Bizum, UPI, Alipay, WeChat Pay or PayPay in the payment popup based on your business country."},
            {"title": "Selection and PAC approval", "body": "The client selects the shots and you confirm payment plus PAC validation."},
            {"title": "ZIP delivery and reports", "body": "Approved files download as ZIP while delivery and revenue stay visible inside the app."},
        ],
        "audience_eyebrow": "Who Uses It",
        "audience_title": "Built for professional on-site teams",
        "audience_lead": "A strong center for photographers who need quick preview, controlled selection and immediate delivery.",
        "audience_cards": [
            {"title": "Wedding and event photographers", "body": "Teams that need a fast selection and delivery flow during live shoots."},
            {"title": "Studio and portrait sessions", "body": "Studios that want to review, select and deliver with the client in one place."},
            {"title": "School, sports and corporate jobs", "body": "Crews that manage many sessions without mixing customers or deliveries."},
            {"title": "Street, tourist-area and mobile portrait shoots", "body": "A strong fit for photographers who want to shoot on location, show selected frames instantly and sell single images or bundled packages."},
            {"title": "Mobile delivery teams", "body": "Operations that work over local network or hotspot without internet dependency."},
        ],
        "pricing_eyebrow": "Plans",
        "pricing_title": "Start free and grow with Pro",
        "pricing_lead": "The free plan is ready for learning the flow. Pro removes delivery limits and unlocks business branding.",
        "config_warning": "This repository does not include final monthly or yearly prices. Pricing and the direct App Store URL are controlled from site-config.js.",
        "free_badge": "Free",
        "free_title": "Ideal for learning the flow",
        "free_period": "to start",
        "free_features": [
            "Daily limit of 10 delivered photos",
            "SnapVend branding stays visible",
            "Custom business name and logo stay locked",
            "Good for testing before live use",
        ],
        "free_cta": "Start Free",
        "monthly_badge": "Pro Monthly",
        "monthly_title": "Flexible monthly use",
        "monthly_placeholder": "Update price",
        "monthly_period": "/ month",
        "monthly_features": [
            "Unlimited daily deliveries",
            "Custom business name and logo",
            "Custom ZIP file name",
            "Unlimited wedding print list",
        ],
        "monthly_cta": "Download the app",
        "yearly_badge": "Pro Yearly",
        "yearly_title": "Better for regular use",
        "yearly_placeholder": "Update price",
        "yearly_period": "/ year",
        "yearly_features": [
            "Lower effective annual cost target",
            "Unlimited daily deliveries",
            "Full branding control",
            "Built for heavier field usage",
        ],
        "yearly_cta": "Download the app",
        "cta_eyebrow": "Ready?",
        "cta_title": "Show, select and deliver faster on location with SnapVend.",
        "cta_lead": "QR access, FTP transfer, local sharing and reporting come together in one workflow.",
        "footer_note": "SnapVend processes media on the device. Sharing is exposed only when you explicitly start a local delivery flow.",
    },
    "es": {
        "meta_title": "SnapVend | Galería QR y entrega local para fotógrafos",
        "meta_description": "SnapVend ayuda a fotógrafos a importar, mostrar y entregar fotos desde un solo teléfono o tablet con galería QR, FTP y entrega ZIP.",
        "nav_how": "Cómo Funciona",
        "nav_audience": "Para Quién",
        "nav_pricing": "Precios",
        "nav_download": "Descargar",
        "language_label": "Idioma",
        "hero_eyebrow": "Galería QR, transferencia FTP, entrega local",
        "hero_title": "Un solo dispositivo desde la captura hasta la entrega.",
        "hero_lead": "Importe fotos desde la cámara o la galería, deje que el cliente entre por QR, confirme el PAC y entregue los archivos aprobados en ZIP desde el mismo dispositivo.",
        "google_small": "Descargar para Android",
        "apple_small": "Descargar para iPhone y iPad",
        "setup_note": "Puede actualizar los precios mensual y anual y el enlace directo de App Store desde site-config.js. Hasta agregar el ID de Apple, el logo de iOS abre la búsqueda regional en App Store.",
        "metrics": [
            {"value": "1 equipo", "label": "Recibir, mostrar y entregar"},
            {"value": "6 métodos", "label": "Pago local listo"},
            {"value": "0 nube", "label": "Flujo local, sin rastreo"},
        ],
        "workflow_eyebrow": "Flujo",
        "workflow_title": "Rápido, controlado y listo para campo",
        "workflow_lead": "SnapVend convierte la recepción de fotos, la vista del cliente y la entrega en una sola operación clara.",
        "workflow_cards": [
            {"title": "Importe las fotos", "body": "Tómelas desde la galería local o envíelas a SnapVend desde una cámara con FTP."},
            {"title": "Comparta la galería con QR", "body": "El cliente escanea el código en la misma red y abre la galería web al instante."},
            {"title": "Mostrar pago local", "body": "Según el país del negocio, muestre en el popup métodos listos como FAST / EFT, Bizum, UPI, Alipay, WeChat Pay o PayPay."},
            {"title": "Selección y validación PAC", "body": "El cliente elige las fotos y usted confirma el pago y la validación PAC."},
            {"title": "Entrega ZIP y reportes", "body": "Los archivos aprobados bajan en ZIP y la entrega o ingresos quedan visibles en la app."},
        ],
        "audience_eyebrow": "Para Quién",
        "audience_title": "Diseñado para equipos profesionales en sitio",
        "audience_lead": "Un centro claro para fotógrafos que necesitan vista rápida, selección controlada y entrega inmediata.",
        "audience_cards": [
            {"title": "Fotógrafos de bodas y eventos", "body": "Equipos que necesitan selección y entrega rápidas durante un trabajo en vivo."},
            {"title": "Estudio y retrato", "body": "Estudios que quieren revisar, seleccionar y entregar junto al cliente."},
            {"title": "Escuela, deporte y corporativo", "body": "Equipos que gestionan muchas sesiones sin mezclar clientes ni entregas."},
            {"title": "Fotografía callejera, turística y retrato móvil", "body": "Un flujo fuerte para fotógrafos que quieren tomar fotos en campo, mostrar las imágenes elegidas al instante y vender entregas individuales o en paquete."},
            {"title": "Equipos móviles de entrega", "body": "Operaciones que trabajan por red local o punto de acceso sin depender de internet."},
        ],
        "pricing_eyebrow": "Planes",
        "pricing_title": "Empiece gratis y escale con el plan profesional",
        "pricing_lead": "El plan gratuito sirve para aprender el flujo. El plan profesional elimina límites y abre la marca del negocio.",
        "config_warning": "Este repositorio no incluye precios finales. Los precios y el enlace directo de App Store se actualizan desde site-config.js.",
        "free_badge": "Gratis",
        "free_title": "Ideal para aprender el flujo",
        "free_period": "para empezar",
        "free_features": [
            "Límite diario de 10 fotos entregadas",
            "La marca SnapVend sigue visible",
            "Nombre y logo del negocio bloqueados",
            "Útil para probar antes del uso real",
        ],
        "free_cta": "Empezar Gratis",
        "monthly_badge": "Profesional mensual",
        "monthly_title": "Uso mensual flexible",
        "monthly_placeholder": "Actualizar precio",
        "monthly_period": "/ mes",
        "monthly_features": [
            "Entregas diarias ilimitadas",
            "Nombre y logo personalizados",
            "Nombre ZIP personalizado",
            "Lista de impresion de bodas ilimitada",
        ],
        "monthly_cta": "Descargar la app",
        "yearly_badge": "Profesional anual",
        "yearly_title": "Mejor para uso frecuente",
        "yearly_placeholder": "Actualizar precio",
        "yearly_period": "/ año",
        "yearly_features": [
            "Objetivo de menor costo anual",
            "Entregas diarias ilimitadas",
            "Control total de marca",
            "Preparado para uso intensivo en campo",
        ],
        "yearly_cta": "Descargar la app",
        "cta_eyebrow": "¿Listo?",
        "cta_title": "Muestre, deje elegir y entregue más rápido con SnapVend.",
        "cta_lead": "Acceso por QR, transferencia FTP, uso local y reportes dentro del mismo flujo.",
        "footer_note": "SnapVend procesa el contenido en el dispositivo. La entrega solo se abre cuando usted inicia el flujo local.",
    },
    "fr": {
        "meta_title": "SnapVend | Galerie QR et livraison locale pour photographes",
        "meta_description": "SnapVend aide les photographes a importer, presenter et livrer des photos depuis un seul telephone ou tablette avec galerie QR, FTP et livraison ZIP.",
        "nav_how": "Fonctionnement",
        "nav_audience": "Pour Qui",
        "nav_pricing": "Tarifs",
        "nav_download": "Telecharger",
        "language_label": "Langue",
        "hero_eyebrow": "Galerie QR, transfert FTP, livraison locale",
        "hero_title": "Un seul appareil de la prise de vue a la livraison.",
        "hero_lead": "Importez les photos depuis l'appareil photo ou la galerie, faites entrer le client par QR, validez le PAC et livrez les fichiers approuves en ZIP depuis le meme appareil.",
        "google_small": "Telecharger pour Android",
        "apple_small": "Telecharger pour iPhone et iPad",
        "setup_note": "Vous pouvez mettre a jour les prix mensuel et annuel ainsi que le lien direct App Store depuis site-config.js. Tant que l'ID Apple n'est pas ajoute, le logo iOS ouvre la recherche regionale App Store.",
        "metrics": [
            {"value": "1 appareil", "label": "Recevoir, montrer, livrer"},
            {"value": "6 methodes", "label": "Paiement local pret"},
            {"value": "0 cloud", "label": "Flux local, sans suivi"},
        ],
        "workflow_eyebrow": "Flux",
        "workflow_title": "Rapide, controle et pret pour le terrain",
        "workflow_lead": "SnapVend transforme l'import, l'aperçu client et la livraison en une seule operation claire.",
        "workflow_cards": [
            {"title": "Importez les photos", "body": "Prenez-les depuis la galerie locale ou envoyez-les dans SnapVend depuis un appareil photo compatible FTP."},
            {"title": "Partagez la galerie par QR", "body": "Le client scanne le code sur le meme reseau et ouvre aussitot la galerie web."},
            {"title": "Afficher le paiement local", "body": "Selon le pays de l entreprise, affichez dans la fenetre de paiement des methodes pretes comme FAST / EFT, Bizum, UPI, Alipay, WeChat Pay ou PayPay."},
            {"title": "Selection et validation PAC", "body": "Le client choisit les images et vous confirmez le paiement puis la validation PAC."},
            {"title": "Livraison ZIP et rapports", "body": "Les fichiers approuves sont telecharges en ZIP et les livraisons restent visibles dans l'application."},
        ],
        "audience_eyebrow": "Pour Qui",
        "audience_title": "Concu pour les equipes photo sur le terrain",
        "audience_lead": "Un centre clair pour les photographes qui veulent un aperçu rapide, une selection controlee et une livraison immediate.",
        "audience_cards": [
            {"title": "Mariage et evenementiel", "body": "Des equipes qui ont besoin d'une selection et d'une livraison rapides pendant la prise de vue."},
            {"title": "Studio et portrait", "body": "Des studios qui veulent choisir et livrer avec le client dans un seul espace."},
            {"title": "Ecole, sport et entreprise", "body": "Des equipes qui gerent plusieurs sessions sans melanger clients et livraisons."},
            {"title": "Photo de rue, zones touristiques et portrait mobile", "body": "Un flux adapte aux photographes qui veulent shooter sur place, montrer immediatement les images choisies et vendre a l'unite ou en pack."},
            {"title": "Equipes mobiles", "body": "Des operations qui travaillent en reseau local ou point d'acces sans dependance internet."},
        ],
        "pricing_eyebrow": "Forfaits",
        "pricing_title": "Commencez gratuitement puis passez au plan professionnel",
        "pricing_lead": "Le plan gratuit sert a apprendre le flux. Le plan professionnel supprime les limites et debloque l'image de marque.",
        "config_warning": "Ce depot ne contient pas les prix definitifs. Les prix et le lien App Store direct se reglent dans site-config.js.",
        "free_badge": "Gratuit",
        "free_title": "Ideal pour apprendre le flux",
        "free_period": "pour commencer",
        "free_features": [
            "Limite quotidienne de 10 photos livrees",
            "La marque SnapVend reste visible",
            "Nom et logo de l'entreprise verrouilles",
            "Pratique pour tester avant un usage reel",
        ],
        "free_cta": "Commencer Gratuitement",
        "monthly_badge": "Professionnel mensuel",
        "monthly_title": "Usage mensuel flexible",
        "monthly_placeholder": "Mettre a jour le prix",
        "monthly_period": "/ mois",
        "monthly_features": [
            "Livraisons quotidiennes illimitees",
            "Nom et logo personnalises",
            "Nom de fichier ZIP personnalise",
            "Liste d'impression mariage illimitee",
        ],
        "monthly_cta": "Telecharger l'application",
        "yearly_badge": "Professionnel annuel",
        "yearly_title": "Mieux pour un usage regulier",
        "yearly_placeholder": "Mettre a jour le prix",
        "yearly_period": "/ an",
        "yearly_features": [
            "Objectif de cout annuel plus bas",
            "Livraisons quotidiennes illimitees",
            "Controle complet de la marque",
            "Concu pour un usage terrain intensif",
        ],
        "yearly_cta": "Telecharger l'application",
        "cta_eyebrow": "Pret ?",
        "cta_title": "Montrez, faites choisir et livrez plus vite avec SnapVend.",
        "cta_lead": "Acces QR, transfert FTP, partage local et rapports dans un seul flux.",
        "footer_note": "SnapVend traite les medias sur l'appareil. Le partage n'est ouvert que lorsque vous lancez la livraison locale.",
    },
    "de": {
        "meta_title": "SnapVend | QR-Galerie und lokale Auslieferung fur Fotografen",
        "meta_description": "SnapVend hilft Fotografen, Fotos von einem Telefon oder Tablet aus mit QR-Galerie, FTP-Kameraimport und ZIP-Auslieferung zu importieren, zu zeigen und zu liefern.",
        "nav_how": "Ablauf",
        "nav_audience": "Fur Wen",
        "nav_pricing": "Preise",
        "nav_download": "Download",
        "language_label": "Sprache",
        "hero_eyebrow": "QR-Galerie, FTP-Transfer, lokale Lieferung",
        "hero_title": "Ein Geraet von Aufnahme bis Auslieferung.",
        "hero_lead": "Importieren Sie Fotos aus Kamera oder Galerie, lassen Sie Kunden per QR eintreten, bestaetigen Sie PAC und liefern Sie freigegebene Dateien als ZIP vom selben Geraet.",
        "google_small": "Fur Android laden",
        "apple_small": "Fur iPhone und iPad laden",
        "setup_note": "Monats- und Jahrespreise sowie der direkte App-Store-Link lassen sich in site-config.js aktualisieren. Bis die Apple-ID vorliegt, oeffnet das iOS-Logo die regionale App-Store-Suche.",
        "metrics": [
            {"value": "1 Geraet", "label": "Empfangen, zeigen, liefern"},
            {"value": "6 Methoden", "label": "Lokaler Zahlungsfluss"},
            {"value": "0 Cloud", "label": "Lokal, ohne Tracking"},
        ],
        "workflow_eyebrow": "Ablauf",
        "workflow_title": "Schnell, kontrolliert und einsatzbereit",
        "workflow_lead": "SnapVend macht Import, Kundenvorschau und Auslieferung zu einem klaren Ablauf vor Ort.",
        "workflow_cards": [
            {"title": "Fotos importieren", "body": "Waehlen Sie sie aus lokaler Galerie oder senden Sie sie per FTP-faehiger Kamera direkt in SnapVend."},
            {"title": "Galerie per QR teilen", "body": "Der Kunde scannt den Code im selben Netzwerk und oeffnet sofort die Web-Galerie."},
            {"title": "Lokale Zahlarten zeigen", "body": "Je nach Geschaeftsland zeigen Sie im Zahlungsfenster vorbereitete Methoden wie FAST / EFT, Bizum, UPI, Alipay, WeChat Pay oder PayPay."},
            {"title": "Auswahl und PAC-Freigabe", "body": "Der Kunde waehlt Bilder aus und Sie bestaetigen Zahlung und PAC-Pruefung."},
            {"title": "ZIP-Lieferung und Berichte", "body": "Freigegebene Dateien werden als ZIP geladen, waehrend Lieferung und Umsatz sichtbar bleiben."},
        ],
        "audience_eyebrow": "Fur Wen",
        "audience_title": "Fur professionelle Teams im Einsatz gebaut",
        "audience_lead": "Ein starker Mittelpunkt fuer Fotografen, die schnelle Vorschau, kontrollierte Auswahl und sofortige Lieferung brauchen.",
        "audience_cards": [
            {"title": "Hochzeit und Event", "body": "Teams, die waehrend des Shootings schnell zeigen, auswaehlen und liefern muessen."},
            {"title": "Studio und Portrait", "body": "Studios, die Auswahl und Lieferung gemeinsam mit dem Kunden erledigen moechten."},
            {"title": "Schule, Sport und Unternehmen", "body": "Teams, die viele Sessions ohne Vermischung von Kunden und Lieferungen verwalten."},
            {"title": "Strasse, Touristenorte und mobile Portraits", "body": "Ein starker Ablauf fuer Fotografen, die vor Ort schnell fotografieren, ausgewaehlte Bilder direkt zeigen und einzeln oder im Paket verkaufen wollen."},
            {"title": "Mobile Lieferteams", "body": "Ablaufe, die per lokalem Netzwerk oder mobilem Zugangspunkt ohne Internetabhaengigkeit arbeiten."},
        ],
        "pricing_eyebrow": "Plaene",
        "pricing_title": "Kostenlos starten und mit dem Profi-Plan wachsen",
        "pricing_lead": "Der Gratisplan hilft beim Einstieg. Der Profi-Plan entfernt Limits und oeffnet den Markenauftritt des Unternehmens.",
        "config_warning": "Dieses Repository enthaelt keine finalen Preise. Preise und direkter App-Store-Link werden ueber site-config.js gepflegt.",
        "free_badge": "Kostenlos",
        "free_title": "Ideal zum Kennenlernen",
        "free_period": "zum Start",
        "free_features": [
            "Taegliches Limit von 10 gelieferten Fotos",
            "SnapVend-Branding bleibt sichtbar",
            "Eigener Firmenname und Logo bleiben gesperrt",
            "Gut zum Testen vor dem Live-Einsatz",
        ],
        "free_cta": "Kostenlos Starten",
        "monthly_badge": "Profi Monatlich",
        "monthly_title": "Flexible Monatsnutzung",
        "monthly_placeholder": "Preis aktualisieren",
        "monthly_period": "/ Monat",
        "monthly_features": [
            "Unbegrenzte taegliche Lieferungen",
            "Eigener Firmenname und Logo",
            "Eigener ZIP-Dateiname",
            "Unbegrenzte Hochzeitsdruckliste",
        ],
        "monthly_cta": "App herunterladen",
        "yearly_badge": "Profi Jaehrlich",
        "yearly_title": "Besser fuer regelmaessige Nutzung",
        "yearly_placeholder": "Preis aktualisieren",
        "yearly_period": "/ Jahr",
        "yearly_features": [
            "Ziel fuer geringere Jahreskosten",
            "Unbegrenzte taegliche Lieferungen",
            "Volle Branding-Kontrolle",
            "Fuer intensiven Feldeinsatz gebaut",
        ],
        "yearly_cta": "App herunterladen",
        "cta_eyebrow": "Bereit?",
        "cta_title": "Mit SnapVend vor Ort schneller zeigen, auswaehlen und liefern.",
        "cta_lead": "QR-Zugang, FTP-Transfer, lokales Teilen und Berichte in einem Ablauf.",
        "footer_note": "SnapVend verarbeitet Medien auf dem Geraet. Teilen wird nur aktiviert, wenn Sie den lokalen Lieferablauf starten.",
    },
    "it": {
        "meta_title": "SnapVend | Galleria QR e consegna locale per fotografi",
        "meta_description": "SnapVend aiuta i fotografi a importare, mostrare e consegnare foto da un solo telefono o tablet con galleria QR, trasferimento FTP e consegna ZIP.",
        "nav_how": "Come Funziona",
        "nav_audience": "Per Chi È",
        "nav_pricing": "Prezzi",
        "nav_download": "Scarica",
        "language_label": "Lingua",
        "hero_eyebrow": "Galleria QR, trasferimento FTP, consegna locale",
        "hero_title": "Un solo dispositivo dalla ripresa alla consegna.",
        "hero_lead": "Importa le foto dalla fotocamera o dalla galleria, fai entrare il cliente tramite QR, conferma il PAC e consegna i file approvati in ZIP dallo stesso dispositivo.",
        "google_small": "Scarica per Android",
        "apple_small": "Scarica per iPhone e iPad",
        "setup_note": "Puoi aggiornare prezzo mensile, prezzo annuale e link diretto App Store da site-config.js. Finché non aggiungi l'ID Apple, il logo iOS apre il risultato regionale di ricerca su App Store.",
        "metrics": [
            {"value": "1 dispositivo", "label": "Ricevi, mostra e consegna"},
            {"value": "6 metodi", "label": "Pagamento locale pronto"},
            {"value": "0 cloud", "label": "Flusso locale, senza tracciamento"},
        ],
        "workflow_eyebrow": "Flusso",
        "workflow_title": "Veloce, controllato e pronto per il lavoro sul campo",
        "workflow_lead": "SnapVend trasforma importazione foto, anteprima cliente e consegna in un'unica operazione pulita durante il servizio.",
        "workflow_cards": [
            {"title": "Importa le foto", "body": "Selezionale dalla galleria locale oppure inviale a SnapVend da una fotocamera compatibile con FTP."},
            {"title": "Condividi la galleria con QR", "body": "Il cliente scansiona il codice sulla stessa rete e apre subito la galleria web."},
            {"title": "Mostra il pagamento locale", "body": "In base al paese della tua attività, mostra nel popup metodi pronti come FAST / EFT, Bizum, UPI, Alipay, WeChat Pay o PayPay."},
            {"title": "Selezione e conferma PAC", "body": "Il cliente sceglie le foto e tu confermi il pagamento insieme alla validazione PAC."},
            {"title": "Consegna ZIP e report", "body": "I file approvati vengono scaricati come ZIP e consegne o ricavi restano visibili nell'app."},
        ],
        "audience_eyebrow": "Per Chi È",
        "audience_title": "Pensato per team professionali che lavorano sul posto",
        "audience_lead": "Un centro chiaro per fotografi che vogliono anteprima veloce, selezione controllata e consegna immediata.",
        "audience_cards": [
            {"title": "Fotografi di matrimoni ed eventi", "body": "Team che hanno bisogno di selezione e consegna rapide durante servizi dal vivo."},
            {"title": "Studio e ritratto", "body": "Studi che vogliono rivedere, selezionare e consegnare insieme al cliente in un unico posto."},
            {"title": "Scuola, sport e lavori aziendali", "body": "Team che gestiscono molte sessioni senza confondere clienti o consegne."},
            {"title": "Fotografia di strada, aree turistiche e ritratti mobili", "body": "Un flusso solido per fotografi che vogliono scattare sul posto, mostrare subito le immagini selezionate e vendere singole foto o pacchetti."},
            {"title": "Team di consegna mobile", "body": "Operazioni che lavorano su rete locale o punto di accesso senza dipendere da internet."},
        ],
        "pricing_eyebrow": "Piani",
        "pricing_title": "Inizia gratis e cresci con il piano professionale",
        "pricing_lead": "Il piano gratuito è pronto per imparare il flusso. Il piano professionale rimuove i limiti di consegna e sblocca il branding aziendale.",
        "config_warning": "Questo repository non include prezzi mensili o annuali definitivi. Prezzi e link diretto App Store sono gestiti da site-config.js.",
        "free_badge": "Gratis",
        "free_title": "Ideale per imparare il flusso",
        "free_period": "per iniziare",
        "free_features": [
            "Limite giornaliero di 10 foto consegnate",
            "Il brand SnapVend resta visibile",
            "Nome attività e logo personalizzati restano bloccati",
            "Utile per testare prima dell'uso reale",
        ],
        "free_cta": "Inizia Gratis",
        "monthly_badge": "Professionale mensile",
        "monthly_title": "Uso mensile flessibile",
        "monthly_placeholder": "Aggiorna il prezzo",
        "monthly_period": "/ mese",
        "monthly_features": [
            "Consegne giornaliere illimitate",
            "Nome attività e logo personalizzati",
            "Nome file ZIP personalizzato",
            "Lista di stampa matrimoni illimitata",
        ],
        "monthly_cta": "Scarica l'applicazione",
        "yearly_badge": "Professionale annuale",
        "yearly_title": "Più vantaggioso per un uso regolare",
        "yearly_placeholder": "Aggiorna il prezzo",
        "yearly_period": "/ anno",
        "yearly_features": [
            "Costo annuale effettivo più conveniente",
            "Consegne giornaliere illimitate",
            "Controllo completo del brand",
            "Pensato per uso intenso sul campo",
        ],
        "yearly_cta": "Scarica l'applicazione",
        "cta_eyebrow": "Pronto?",
        "cta_title": "Con SnapVend mostri, fai scegliere e consegni più velocemente sul posto.",
        "cta_lead": "Accesso QR, trasferimento FTP, condivisione locale e report in un unico flusso.",
        "footer_note": "SnapVend elabora i media sul dispositivo. La condivisione si apre solo quando avvii tu il flusso di consegna locale.",
    },
    "pt": {
        "meta_title": "SnapVend | Galeria QR e entrega local para fotografos",
        "meta_description": "SnapVend ajuda fotografos a importar, apresentar e entregar fotos de um telefone ou tablet com galeria QR, transferencia FTP e entrega ZIP.",
        "nav_how": "Como Funciona",
        "nav_audience": "Para Quem",
        "nav_pricing": "Precos",
        "nav_download": "Baixar",
        "language_label": "Idioma",
        "hero_eyebrow": "Galeria QR, transferencia FTP, entrega local",
        "hero_title": "Um so dispositivo da captura ate a entrega.",
        "hero_lead": "Importe fotos da camera ou da galeria, deixe o cliente entrar por QR, confirme o PAC e entregue os arquivos aprovados em ZIP no mesmo dispositivo.",
        "google_small": "Baixar para Android",
        "apple_small": "Baixar para iPhone e iPad",
        "setup_note": "Voce pode atualizar os precos mensal e anual e o link direto da App Store em site-config.js. Ate adicionar o ID da Apple, o logo do iOS abre a busca regional na App Store.",
        "metrics": [
            {"value": "1 aparelho", "label": "Receber, mostrar e entregar"},
            {"value": "6 metodos", "label": "Pagamento local pronto"},
            {"value": "0 nuvem", "label": "Fluxo local, sem rastreio"},
        ],
        "workflow_eyebrow": "Fluxo",
        "workflow_title": "Rapido, controlado e pronto para campo",
        "workflow_lead": "SnapVend transforma entrada de fotos, visualizacao do cliente e entrega em uma operacao unica e clara.",
        "workflow_cards": [
            {"title": "Importe as fotos", "body": "Escolha na galeria local ou envie direto para o SnapVend de uma camera com FTP."},
            {"title": "Compartilhe a galeria por QR", "body": "O cliente escaneia o codigo na mesma rede e abre a galeria web na hora."},
            {"title": "Mostrar pagamento local", "body": "Conforme o pais do negocio, mostre no popup de pagamento metodos prontos como FAST / EFT, Bizum, UPI, Alipay, WeChat Pay ou PayPay."},
            {"title": "Selecao e aprovacao PAC", "body": "O cliente escolhe as fotos e voce confirma o pagamento e a validacao do PAC."},
            {"title": "Entrega ZIP e relatorios", "body": "Os arquivos aprovados baixam em ZIP e a entrega ou a receita ficam visiveis no app."},
        ],
        "audience_eyebrow": "Para Quem",
        "audience_title": "Feito para equipes profissionais em campo",
        "audience_lead": "Um centro forte para fotografos que precisam de pre-visualizacao rapida, selecao controlada e entrega imediata.",
        "audience_cards": [
            {"title": "Casamentos e eventos", "body": "Equipes que precisam mostrar, selecionar e entregar rapidamente durante o trabalho."},
            {"title": "Estudio e retrato", "body": "Estudios que querem revisar, escolher e entregar junto com o cliente."},
            {"title": "Escola, esporte e corporativo", "body": "Equipes que gerenciam muitas sessoes sem misturar clientes nem entregas."},
            {"title": "Rua, areas turisticas e retrato movel", "body": "Um fluxo forte para fotografos que querem fotografar no local, mostrar as imagens escolhidas na hora e vender fotos avulsas ou em pacotes."},
            {"title": "Operacoes moveis", "body": "Fluxos que funcionam em rede local ou ponto de acesso sem depender da internet."},
        ],
        "pricing_eyebrow": "Planos",
        "pricing_title": "Comece gratis e cresca com o plano profissional",
        "pricing_lead": "O plano gratuito serve para aprender o fluxo. O plano profissional remove limites e libera a marca do negocio.",
        "config_warning": "Este repositorio nao inclui os precos finais. Os precos e o link direto da App Store sao controlados em site-config.js.",
        "free_badge": "Gratis",
        "free_title": "Ideal para aprender o fluxo",
        "free_period": "para comecar",
        "free_features": [
            "Limite diario de 10 fotos entregues",
            "A marca SnapVend continua visivel",
            "Nome e logo do negocio ficam bloqueados",
            "Bom para testar antes do uso real",
        ],
        "free_cta": "Comecar Gratis",
        "monthly_badge": "Profissional mensal",
        "monthly_title": "Uso mensal flexivel",
        "monthly_placeholder": "Atualizar preco",
        "monthly_period": "/ mes",
        "monthly_features": [
            "Entregas diarias ilimitadas",
            "Nome e logo personalizados",
            "Nome ZIP personalizado",
            "Lista de impressao de casamento ilimitada",
        ],
        "monthly_cta": "Baixar o aplicativo",
        "yearly_badge": "Profissional anual",
        "yearly_title": "Melhor para uso frequente",
        "yearly_placeholder": "Atualizar preco",
        "yearly_period": "/ ano",
        "yearly_features": [
            "Meta de menor custo anual",
            "Entregas diarias ilimitadas",
            "Controle total da marca",
            "Feito para uso intenso em campo",
        ],
        "yearly_cta": "Baixar o aplicativo",
        "cta_eyebrow": "Pronto?",
        "cta_title": "Mostre, selecione e entregue mais rapido com SnapVend.",
        "cta_lead": "Acesso por QR, transferencia FTP, compartilhamento local e relatorios no mesmo fluxo.",
        "footer_note": "O SnapVend processa a midia no dispositivo. O compartilhamento so e aberto quando voce inicia o fluxo local.",
    },
    "ru": {
        "meta_title": "SnapVend | QR-галерея и локальная выдача для фотографов",
        "meta_description": "SnapVend помогает фотографам импортировать, показывать и выдавать фото с одного телефона или планшета через QR-галерею, FTP и ZIP-доставку.",
        "nav_how": "Как Работает",
        "nav_audience": "Для Кого",
        "nav_pricing": "Тарифы",
        "nav_download": "Скачать",
        "language_label": "Язык",
        "hero_eyebrow": "QR-галерея, FTP-передача, локальная выдача",
        "hero_title": "Одно устройство от съемки до выдачи.",
        "hero_lead": "Загрузите фото из камеры или галереи, впустите клиента по QR, подтвердите PAC и выдайте одобренные файлы ZIP с того же устройства.",
        "google_small": "Скачать для Android",
        "apple_small": "Скачать для iPhone и iPad",
        "setup_note": "Месячную и годовую цену, а также прямую ссылку App Store можно обновить в site-config.js. Пока не добавлен Apple ID приложения, логотип iOS открывает региональный поиск App Store.",
        "metrics": [
            {"value": "1 устройство", "label": "Получить, показать, выдать"},
            {"value": "6 методов", "label": "Готовые локальные платежи"},
            {"value": "0 облака", "label": "Локальная работа, без трекинга"},
        ],
        "workflow_eyebrow": "Поток",
        "workflow_title": "Быстро, под контролем и готово к полю",
        "workflow_lead": "SnapVend объединяет прием фото, показ клиенту и выдачу в одну понятную операцию на съемке.",
        "workflow_cards": [
            {"title": "Импортируйте фото", "body": "Берите их из локальной галереи или отправляйте в SnapVend с FTP-камеры."},
            {"title": "Поделитесь галереей по QR", "body": "Клиент сканирует код в той же сети и сразу открывает веб-галерею."},
            {"title": "Показать локальную оплату", "body": "В зависимости от страны бизнеса показывайте во всплывающем окне оплаты готовые методы: FAST / EFT, Bizum, UPI, Alipay, WeChat Pay или PayPay."},
            {"title": "Выбор и подтверждение PAC", "body": "Клиент выбирает кадры, а вы подтверждаете оплату и проверку PAC."},
            {"title": "ZIP-выдача и отчеты", "body": "Одобренные файлы скачиваются ZIP, а выдача и выручка видны внутри приложения."},
        ],
        "audience_eyebrow": "Для Кого",
        "audience_title": "Создано для профессиональных команд на площадке",
        "audience_lead": "Надежный центр для фотографов, которым нужен быстрый просмотр, контролируемый выбор и мгновенная выдача.",
        "audience_cards": [
            {"title": "Свадьбы и мероприятия", "body": "Команды, которым нужен быстрый выбор и выдача прямо во время съемки."},
            {"title": "Студия и портрет", "body": "Студии, которые хотят выбирать и отдавать фотографии вместе с клиентом."},
            {"title": "Школа, спорт и корпоратив", "body": "Команды, которые ведут много сессий и не смешивают клиентов и выдачу."},
            {"title": "Улица, туристические зоны и мобильный портрет", "body": "Подходит фотографам, которые снимают на месте, сразу показывают выбранные кадры и продают фотографии по одной или пакетами."},
            {"title": "Мобильные команды", "body": "Операции на локальной сети или через точку доступа без зависимости от интернета."},
        ],
        "pricing_eyebrow": "Планы",
        "pricing_title": "Начните бесплатно и переходите на профессиональный план",
        "pricing_lead": "Бесплатный план подходит для знакомства с процессом. Профессиональный план снимает лимиты и открывает брендинг.",
        "config_warning": "В этом репозитории нет финальных цен. Цены и прямая ссылка App Store настраиваются через site-config.js.",
        "free_badge": "Бесплатно",
        "free_title": "Подходит для знакомства с потоком",
        "free_period": "для старта",
        "free_features": [
            "Ежедневный лимит: 10 выданных фото",
            "Брендинг SnapVend остается видимым",
            "Свой бренд и логотип заблокированы",
            "Удобно для теста перед реальной работой",
        ],
        "free_cta": "Начать Бесплатно",
        "monthly_badge": "Профи ежемесячно",
        "monthly_title": "Гибкое помесячное использование",
        "monthly_placeholder": "Обновить цену",
        "monthly_period": "/ месяц",
        "monthly_features": [
            "Неограниченная ежедневная выдача",
            "Свой бренд и логотип",
            "Собственное ZIP-имя",
            "Неограниченный список свадебной печати",
        ],
        "monthly_cta": "Скачать приложение",
        "yearly_badge": "Профи годовой",
        "yearly_title": "Лучше для постоянной работы",
        "yearly_placeholder": "Обновить цену",
        "yearly_period": "/ год",
        "yearly_features": [
            "Цель более низкой годовой стоимости",
            "Неограниченная ежедневная выдача",
            "Полный контроль бренда",
            "Решение для интенсивной полевой работы",
        ],
        "yearly_cta": "Скачать приложение",
        "cta_eyebrow": "Готовы?",
        "cta_title": "Показывайте, отбирайте и выдавайте быстрее с SnapVend.",
        "cta_lead": "QR-доступ, FTP-передача, локальный обмен и отчеты в одном процессе.",
        "footer_note": "SnapVend обрабатывает медиа на устройстве. Публикация включается только когда вы запускаете локальную выдачу.",
    },
    "ar": {
        "meta_title": "SnapVend | معرض QR وتسليم محلي للمصورين",
        "meta_description": "يساعد SnapVend المصورين على استيراد الصور وعرضها وتسليمها من هاتف او جهاز لوحي واحد عبر معرض QR ونقل FTP وتسليم ZIP.",
        "nav_how": "كيف يعمل",
        "nav_audience": "لمن",
        "nav_pricing": "الاسعار",
        "nav_download": "تنزيل",
        "language_label": "اللغة",
        "hero_eyebrow": "معرض QR، نقل FTP، تسليم محلي",
        "hero_title": "جهاز واحد من الالتقاط حتى التسليم.",
        "hero_lead": "استورد الصور من الكاميرا او المعرض، دع العميل يدخل عبر QR، اكد PAC ثم سلم الملفات المعتمدة كملف ZIP من الجهاز نفسه.",
        "google_small": "تنزيل لاندرويد",
        "apple_small": "تنزيل لايفون وايباد",
        "setup_note": "يمكنك تحديث السعر الشهري والسنوي والرابط المباشر لـ App Store من site-config.js. وحتى اضافة معرف Apple يفتح شعار iOS نتيجة البحث الاقليمية في App Store.",
        "metrics": [
            {"value": "جهاز واحد", "label": "استلم، اعرض، سلم"},
            {"value": "6 طرق", "label": "دفع محلي جاهز"},
            {"value": "0 سحابة", "label": "عمل محلي بدون تتبع"},
        ],
        "workflow_eyebrow": "سير العمل",
        "workflow_title": "سريع، منظم وجاهز للميدان",
        "workflow_lead": "يجمع SnapVend استقبال الصور ومعاينة العميل والتسليم في عملية واحدة واضحة اثناء التصوير.",
        "workflow_cards": [
            {"title": "استيراد الصور", "body": "اخترها من المعرض المحلي او ارسلها الى SnapVend من كاميرا تدعم FTP."},
            {"title": "شارك المعرض عبر QR", "body": "يمسح العميل الرمز على الشبكة نفسها ويفتح معرض الويب مباشرة."},
            {"title": "اعرض الدفع المحلي", "body": "بحسب بلد النشاط اعرض في نافذة الدفع طرقا جاهزة مثل FAST / EFT و Bizum و UPI و Alipay و WeChat Pay و PayPay."},
            {"title": "الاختيار وتأكيد PAC", "body": "يختار العميل الصور وتؤكد انت الدفع والتحقق من PAC."},
            {"title": "تسليم ZIP والتقارير", "body": "تنزل الملفات المعتمدة كملف ZIP وتبقى عمليات التسليم والايراد ظاهرة داخل التطبيق."},
        ],
        "audience_eyebrow": "لمن",
        "audience_title": "مصمم لفرق التصوير الاحترافية في الموقع",
        "audience_lead": "مركز واضح للمصورين الذين يحتاجون الى معاينة سريعة واختيار منظم وتسليم فوري.",
        "audience_cards": [
            {"title": "تصوير الاعراس والفعاليات", "body": "فرق تحتاج الى اختيار وتسليم سريع اثناء العمل المباشر."},
            {"title": "الاستوديو والبورتريه", "body": "استوديوهات تريد مراجعة الصور واختيارها وتسليمها مع العميل."},
            {"title": "المدارس والرياضة والشركات", "body": "فرق تدير جلسات كثيرة بدون خلط العملاء او التسليمات."},
            {"title": "تصوير الشارع والمناطق السياحية والبورتريه المتنقل", "body": "مناسب للمصورين الذين يريدون التصوير في الموقع وعرض الصور المختارة مباشرة وبيعها بشكل فردي او ضمن باقات."},
            {"title": "فرق التسليم المتنقلة", "body": "عمليات تعمل عبر الشبكة المحلية او نقطة الاتصال بدون اعتماد على الانترنت."},
        ],
        "pricing_eyebrow": "الخطط",
        "pricing_title": "ابدأ مجانا ثم توسع مع الخطة الاحترافية",
        "pricing_lead": "الخطة المجانية مناسبة لتعلم التدفق. الخطة الاحترافية تزيل الحدود وتفتح التحكم بالهوية التجارية.",
        "config_warning": "هذا المستودع لا يحتوي على الاسعار النهائية. يتم تحديث الاسعار والرابط المباشر لـ App Store من خلال site-config.js.",
        "free_badge": "مجاني",
        "free_title": "مثالي لتعلم التدفق",
        "free_period": "للبداية",
        "free_features": [
            "حد يومي 10 صور مسلمة",
            "تبقى علامة SnapVend ظاهرة",
            "اسم وشعار النشاط موقوفان",
            "مناسب للتجربة قبل الاستخدام الفعلي",
        ],
        "free_cta": "ابدأ مجانا",
        "monthly_badge": "احترافية شهرية",
        "monthly_title": "استخدام شهري مرن",
        "monthly_placeholder": "حدث السعر",
        "monthly_period": "/ شهر",
        "monthly_features": [
            "تسليم يومي غير محدود",
            "اسم وشعار مخصصان",
            "اسم ZIP مخصص",
            "قائمة طباعة الاعراس بدون حدود",
        ],
        "monthly_cta": "نزّل التطبيق",
        "yearly_badge": "احترافية سنوية",
        "yearly_title": "افضل للاستخدام المنتظم",
        "yearly_placeholder": "حدث السعر",
        "yearly_period": "/ سنة",
        "yearly_features": [
            "استهداف تكلفة سنوية اقل",
            "تسليم يومي غير محدود",
            "تحكم كامل بالهوية",
            "حل مناسب للاستخدام المكثف",
        ],
        "yearly_cta": "نزّل التطبيق",
        "cta_eyebrow": "جاهز؟",
        "cta_title": "اعرض واختر وسلم بشكل اسرع مع SnapVend.",
        "cta_lead": "دخول QR ونقل FTP ومشاركة محلية وتقارير ضمن تجربة واحدة.",
        "footer_note": "يعالج SnapVend الوسائط على الجهاز نفسه. لا يتم فتح المشاركة الا عندما تبدأ انت تدفق التسليم المحلي.",
    },
    "hi": {
        "meta_title": "SnapVend | फोटोग्राफरों के लिए QR गैलरी और लोकल डिलीवरी",
        "meta_description": "SnapVend फोटोग्राफरों को एक ही फोन या टैबलेट से फोटो इम्पोर्ट करने, दिखाने और ZIP में डिलीवर करने में मदद करता है, QR गैलरी और FTP ट्रांसफर के साथ।",
        "nav_how": "प्रक्रिया",
        "nav_audience": "किसके लिए",
        "nav_pricing": "मूल्य",
        "nav_download": "डाउनलोड",
        "language_label": "भाषा",
        "hero_eyebrow": "QR गैलरी, FTP ट्रांसफर, लोकल डिलीवरी",
        "hero_title": "कैप्चर से डिलीवरी तक एक ही डिवाइस।",
        "hero_lead": "कैमरा या गैलरी से फोटो लें, ग्राहक को QR से अंदर लाएँ, PAC की पुष्टि करें और मंजूर फाइलें उसी डिवाइस से ZIP में दें।",
        "google_small": "Android के लिए डाउनलोड",
        "apple_small": "iPhone और iPad के लिए डाउनलोड",
        "setup_note": "मासिक और वार्षिक कीमतें तथा सीधा App Store लिंक site-config.js में अपडेट किए जा सकते हैं। जब तक Apple app ID नहीं जुड़ती, iOS लोगो क्षेत्रीय App Store खोज परिणाम खोलता है।",
        "metrics": [
            {"value": "1 डिवाइस", "label": "लाओ, दिखाओ, डिलीवर करो"},
            {"value": "6 तरीके", "label": "तैयार लोकल भुगतान"},
            {"value": "0 क्लाउड", "label": "लोकल फ्लो, बिना ट्रैकिंग"},
        ],
        "workflow_eyebrow": "वर्कफ़्लो",
        "workflow_title": "तेज, नियंत्रित और फील्ड के लिए तैयार",
        "workflow_lead": "SnapVend फोटो इम्पोर्ट, ग्राहक प्रीव्यू और डिलीवरी को एक साफ ऑपरेशन में बदल देता है।",
        "workflow_cards": [
            {"title": "फोटो इम्पोर्ट करें", "body": "लोकल गैलरी से चुनें या FTP कैमरे से सीधे SnapVend में भेजें।"},
            {"title": "QR से गैलरी साझा करें", "body": "ग्राहक उसी नेटवर्क पर QR स्कैन करके तुरंत वेब गैलरी खोलता है।"},
            {"title": "लोकल भुगतान दिखाएँ", "body": "बिज़नेस देश के हिसाब से भुगतान पॉपअप में FAST / EFT, Bizum, UPI, Alipay, WeChat Pay या PayPay जैसे तैयार तरीके दिखाएँ।"},
            {"title": "चयन और PAC पुष्टि", "body": "ग्राहक फोटो चुनता है और आप भुगतान व PAC सत्यापन की पुष्टि करते हैं।"},
            {"title": "ZIP डिलीवरी और रिपोर्ट", "body": "मंजूर फाइलें ZIP में डाउनलोड होती हैं और डिलीवरी व आय ऐप में दिखती रहती है।"},
        ],
        "audience_eyebrow": "किसके लिए",
        "audience_title": "पेशेवर ऑन-साइट टीमों के लिए बनाया गया",
        "audience_lead": "उन फोटोग्राफरों के लिए एक मजबूत केंद्र जिन्हें तेज प्रीव्यू, नियंत्रित चयन और तुरंत डिलीवरी चाहिए।",
        "audience_cards": [
            {"title": "शादी और इवेंट फोटोग्राफर", "body": "टीमें जिन्हें लाइव शूट के दौरान तेज चयन और डिलीवरी चाहिए।"},
            {"title": "स्टूडियो और पोर्ट्रेट", "body": "स्टूडियो जो ग्राहक के साथ एक ही जगह पर समीक्षा, चयन और डिलीवरी करना चाहते हैं।"},
            {"title": "स्कूल, स्पोर्ट्स और कॉर्पोरेट", "body": "टीमें जो कई सेशन संभालती हैं और ग्राहकों या डिलीवरी को मिक्स नहीं करना चाहतीं।"},
            {"title": "सड़क, पर्यटन क्षेत्र और मोबाइल पोर्ट्रेट शूट", "body": "ऐसे फोटोग्राफरों के लिए मजबूत फ्लो जो मौके पर शूट करें, चुनी हुई तस्वीरें तुरंत दिखाएँ और एकल या पैकेज बिक्री करना चाहें।"},
            {"title": "मोबाइल डिलीवरी टीमें", "body": "ऐसे ऑपरेशन जो लोकल नेटवर्क या हॉटस्पॉट पर इंटरनेट के बिना चलते हैं।"},
        ],
        "pricing_eyebrow": "प्लान",
        "pricing_title": "मुफ़्त से शुरू करें और प्रो के साथ बढ़ें",
        "pricing_lead": "मुफ़्त प्लान फ्लो सीखने के लिए तैयार है। प्रो सीमा हटाता है और बिज़नेस ब्रांडिंग खोलता है।",
        "config_warning": "इस रिपॉजिटरी में अंतिम कीमतें नहीं हैं। कीमतें और सीधा App Store लिंक site-config.js से नियंत्रित होते हैं।",
        "free_badge": "मुफ़्त",
        "free_title": "फ्लो सीखने के लिए सही",
        "free_period": "शुरुआत के लिए",
        "free_features": [
            "प्रति दिन 10 फोटो डिलीवरी सीमा",
            "SnapVend ब्रांडिंग दिखाई देती रहती है",
            "कस्टम बिज़नेस नाम और लोगो लॉक रहते हैं",
            "लाइव उपयोग से पहले टेस्ट करने के लिए अच्छा",
        ],
        "free_cta": "मुफ़्त शुरू करें",
        "monthly_badge": "प्रो मासिक",
        "monthly_title": "लचीला मासिक उपयोग",
        "monthly_placeholder": "कीमत अपडेट करें",
        "monthly_period": "/ महीना",
        "monthly_features": [
            "असीमित दैनिक डिलीवरी",
            "कस्टम बिज़नेस नाम और लोगो",
            "कस्टम ZIP नाम",
            "असीमित वेडिंग प्रिंट सूची",
        ],
        "monthly_cta": "ऐप डाउनलोड करें",
        "yearly_badge": "प्रो वार्षिक",
        "yearly_title": "नियमित उपयोग के लिए बेहतर",
        "yearly_placeholder": "कीमत अपडेट करें",
        "yearly_period": "/ वर्ष",
        "yearly_features": [
            "कम वार्षिक लागत का लक्ष्य",
            "असीमित दैनिक डिलीवरी",
            "पूरा ब्रांड नियंत्रण",
            "भारी फील्ड उपयोग के लिए उपयुक्त",
        ],
        "yearly_cta": "ऐप डाउनलोड करें",
        "cta_eyebrow": "तैयार?",
        "cta_title": "SnapVend के साथ ऑन-साइट तेज़ी से दिखाएँ, चुनवाएँ और डिलीवर करें।",
        "cta_lead": "QR एक्सेस, FTP ट्रांसफर, लोकल शेयरिंग और रिपोर्ट एक ही फ्लो में मिलते हैं।",
        "footer_note": "SnapVend मीडिया को डिवाइस पर प्रोसेस करता है। शेयरिंग केवल तब खुलती है जब आप लोकल डिलीवरी फ्लो शुरू करते हैं।",
    },
    "ja": {
        "meta_title": "SnapVend | 写真家向けQRギャラリーとローカル納品",
        "meta_description": "SnapVend は QR ギャラリー共有、FTP 転送、ZIP 納品を使って、1台のスマホやタブレットで写真の受け取りから納品までを支援します。",
        "nav_how": "使い方",
        "nav_audience": "対象",
        "nav_pricing": "料金",
        "nav_download": "ダウンロード",
        "language_label": "言語",
        "hero_eyebrow": "QR ギャラリー、FTP 転送、ローカル納品",
        "hero_title": "撮影から納品までを1台で。",
        "hero_lead": "カメラやギャラリーから写真を取り込み、QR で顧客を案内し、PAC 承認後に同じ端末から ZIP 納品できます。",
        "google_small": "Android 版を入手",
        "apple_small": "iPhone / iPad 版を入手",
        "setup_note": "月額・年額の価格と App Store の直接リンクは site-config.js で更新できます。Apple のアプリ ID が入るまでは、iOS ロゴは地域別 App Store 検索結果を開きます。",
        "metrics": [
            {"value": "1台", "label": "受け取り・提示・納品"},
            {"value": "6方式", "label": "ローカル決済対応"},
            {"value": "0クラウド", "label": "ローカル運用、追跡なし"},
        ],
        "workflow_eyebrow": "ワークフロー",
        "workflow_title": "現場向けに速く、明確で、管理しやすい",
        "workflow_lead": "SnapVend は写真の受け取り、顧客プレビュー、納品をひとつの分かりやすい流れにまとめます。",
        "workflow_cards": [
            {"title": "写真を取り込む", "body": "端末のギャラリーから選ぶか、FTP 対応カメラから SnapVend に直接送れます。"},
            {"title": "QR でギャラリー共有", "body": "同じネットワーク上で顧客が QR を読み取り、Web ギャラリーをすぐ開けます。"},
            {"title": "現地向け決済を表示", "body": "事業国に応じて、支払いポップアップに FAST / EFT、Bizum、UPI、Alipay、WeChat Pay、PayPay などの方法を表示できます。"},
            {"title": "選択と PAC 承認", "body": "顧客が写真を選び、支払いと PAC 確認はあなたが管理します。"},
            {"title": "ZIP 納品とレポート", "body": "承認済みファイルは ZIP で渡され、納品や売上の流れもアプリ内で確認できます。"},
        ],
        "audience_eyebrow": "対象ユーザー",
        "audience_title": "現場で動くプロの撮影チーム向け",
        "audience_lead": "素早いプレビュー、管理しやすい選択、即時納品を求める写真チームのための中核です。",
        "audience_cards": [
            {"title": "ウェディング・イベント撮影", "body": "ライブ撮影中にすぐ見せて、選ばせて、納品したいチーム向け。"},
            {"title": "スタジオ・ポートレート", "body": "顧客と一緒に確認しながら選定と納品を進めたいスタジオ向け。"},
            {"title": "学校・スポーツ・法人撮影", "body": "多数のセッションを混線させずに整理したいチーム向け。"},
            {"title": "ストリート、観光地、モバイルポートレート撮影", "body": "現地で撮影し、選ばれた写真をすぐ見せて、単品またはパッケージで販売したいフォトグラファーに向いています。"},
            {"title": "モバイル納品チーム", "body": "インターネット不要でローカルネットワークやホットスポットを使う運用向け。"},
        ],
        "pricing_eyebrow": "プラン",
        "pricing_title": "無料で始めて、プロで拡張",
        "pricing_lead": "無料プランで流れを学べます。プロは納品制限を外し、業務用ブランディングを解放します。",
        "config_warning": "このリポジトリには最終価格が入っていません。価格と App Store 直リンクは site-config.js から更新できます。",
        "free_badge": "無料",
        "free_title": "まず流れを学ぶために最適",
        "free_period": "開始用",
        "free_features": [
            "1日の納品上限は10枚",
            "SnapVend ブランド表示は残る",
            "独自の店名とロゴはロック",
            "本番前のテストに向いている",
        ],
        "free_cta": "無料で始める",
        "monthly_badge": "プロ 月額",
        "monthly_title": "柔軟な月額利用",
        "monthly_placeholder": "価格を更新",
        "monthly_period": "/ 月",
        "monthly_features": [
            "1日の納品数が無制限",
            "独自の店名とロゴ",
            "独自 ZIP 名",
            "ウェディングプリントリスト無制限",
        ],
        "monthly_cta": "アプリを入手",
        "yearly_badge": "プロ 年額",
        "yearly_title": "継続利用に最適",
        "yearly_placeholder": "価格を更新",
        "yearly_period": "/ 年",
        "yearly_features": [
            "より低い年間コストを想定",
            "1日の納品数が無制限",
            "ブランド設定を完全開放",
            "現場での高頻度運用向け",
        ],
        "yearly_cta": "アプリを入手",
        "cta_eyebrow": "準備はできましたか？",
        "cta_title": "SnapVend なら現場でより速く見せて、選ばせて、納品できます。",
        "cta_lead": "QR アクセス、FTP 転送、ローカル共有、レポートをひとつの流れで扱えます。",
        "footer_note": "SnapVend はメディアを端末上で処理します。共有はローカル納品フローを開始したときだけ開かれます。",
    },
    "zh": {
        "meta_title": "SnapVend | 面向摄影团队的 QR 画廊与本地交付",
        "meta_description": "SnapVend 通过 QR 画廊、FTP 传输和 ZIP 交付，帮助摄影团队在一台手机或平板上完成照片接收、展示与交付。",
        "nav_how": "工作方式",
        "nav_audience": "适用对象",
        "nav_pricing": "价格",
        "nav_download": "下载",
        "language_label": "语言",
        "hero_eyebrow": "QR 画廊、FTP 传输、本地交付",
        "hero_title": "一台设备完成拍摄到交付。",
        "hero_lead": "从相机或画廊导入照片，让客户通过 QR 进入，完成 PAC 确认后，再从同一设备交付 ZIP 文件。",
        "google_small": "下载 Android 版",
        "apple_small": "下载 iPhone / iPad 版",
        "setup_note": "月度和年度价格以及 App Store 直链都可以在 site-config.js 中更新。在 Apple 应用 ID 添加前，iOS 图标会先打开对应地区的 App Store 搜索结果。",
        "metrics": [
            {"value": "1 台设备", "label": "接收、展示、交付"},
            {"value": "6 种", "label": "本地支付流程"},
            {"value": "0 云依赖", "label": "本地流程，无追踪"},
        ],
        "workflow_eyebrow": "流程",
        "workflow_title": "更快、更可控、更适合现场",
        "workflow_lead": "SnapVend 把照片接收、客户预览和交付整合为一个清晰的现场流程。",
        "workflow_cards": [
            {"title": "导入照片", "body": "可从本地画廊选择，也可通过支持 FTP 的相机直接进入 SnapVend。"},
            {"title": "通过 QR 分享画廊", "body": "客户在同一网络下扫描二维码，即可立即打开网页画廊。"},
            {"title": "显示本地支付方式", "body": "可根据商家所在国家，在支付弹窗中显示 FAST / EFT、Bizum、UPI、Alipay、WeChat Pay、PayPay 等现成方式。"},
            {"title": "选择与 PAC 确认", "body": "客户选择照片，由你确认付款和 PAC 验证。"},
            {"title": "ZIP 交付与报表", "body": "已批准的文件以 ZIP 下载，交付和收入状态在应用内可追踪。"},
        ],
        "audience_eyebrow": "适用对象",
        "audience_title": "为现场工作的专业团队而设计",
        "audience_lead": "适合需要快速预览、可控选择和即时交付的摄影团队。",
        "audience_cards": [
            {"title": "婚礼与活动摄影", "body": "适合需要在拍摄现场快速展示、选择和交付的团队。"},
            {"title": "影棚与人像拍摄", "body": "适合希望与客户一起完成选片和交付的工作室。"},
            {"title": "学校、体育与企业拍摄", "body": "适合管理多个会话而不混淆客户与交付的团队。"},
            {"title": "街拍、旅游区域与移动人像拍摄", "body": "适合希望在现场快速拍摄、即时展示所选照片，并按单张或套餐完成销售的摄影师。"},
            {"title": "移动交付团队", "body": "适合通过本地网络或热点运行且不依赖互联网的团队。"},
        ],
        "pricing_eyebrow": "方案",
        "pricing_title": "先免费开始，再用专业版扩展",
        "pricing_lead": "免费方案适合先熟悉流程。专业版会移除交付限制，并开放品牌自定义能力。",
        "config_warning": "此仓库中没有最终订阅价格。价格和 App Store 直链可在 site-config.js 中更新。",
        "free_badge": "免费",
        "free_title": "适合先熟悉流程",
        "free_period": "开始使用",
        "free_features": [
            "每日最多交付 10 张照片",
            "SnapVend 品牌保持可见",
            "自定义店名和标识处于锁定状态",
            "适合正式上线前测试",
        ],
        "free_cta": "免费开始",
        "monthly_badge": "专业版（月）",
        "monthly_title": "灵活的月度使用",
        "monthly_placeholder": "更新价格",
        "monthly_period": "/ 月",
        "monthly_features": [
            "无限每日交付",
            "自定义店名和标识",
            "自定义 ZIP 文件名",
            "无限婚礼打印列表",
        ],
        "monthly_cta": "下载应用",
        "yearly_badge": "专业版（年）",
        "yearly_title": "更适合长期使用",
        "yearly_placeholder": "更新价格",
        "yearly_period": "/ 年",
        "yearly_features": [
            "目标更低的年化成本",
            "无限每日交付",
            "完整品牌控制",
            "适合高频现场工作",
        ],
        "yearly_cta": "下载应用",
        "cta_eyebrow": "准备好了吗？",
        "cta_title": "用 SnapVend 更快地展示、选片并完成交付。",
        "cta_lead": "QR 访问、FTP 传输、本地分享与报表在同一套流程中完成。",
        "footer_note": "SnapVend 在设备本地处理媒体。只有当你主动启动本地交付流程时，分享才会开放。",
    },
}

COPY_FLOW_OVERRIDES = {
    "tr": {
        "hero_lead": "Fotoğrafları yerel galeriden ya da FTP destekli profesyonel fotoğraf makinesinden doğrudan uygulamaya alın, WiFi veya erişim noktası QR bağlantısını açın, her çekim için ayrı oturum yönetin, müşteriyi QR galeriye alın ve onaylanan dosyaları aynı cihazdan ZIP olarak teslim edin.",
        "metrics": [
            {"value": "1 cihaz", "label": "Çek, göster, teslim et"},
            {"value": "QR erişim", "label": "WiFi ya da erişim noktası ile bağlan"},
            {"value": "Çoklu oturum", "label": "Her çekimi ayrı yönet"},
        ],
        "workflow_title": "QR, oturum ve teslim tek akışta",
        "workflow_lead": "SnapVend profesyonel fotoğraf makinesinden doğrudan FTP aktarımını, WiFi veya erişim noktası üzerinden QR bağlantısını, oturum bazlı müşteri akışını ve teslim sonrası raporlamayı tek operasyon haline getirir.",
        "workflow_cards": [
            {"title": "Fotoğrafları profesyonel kameradan al", "body": "Yerel galeriden seçin ya da FTP destekli profesyonel fotoğraf makinesinden kareleri doğrudan SnapVend akışına aktarın."},
            {"title": "WiFi / erişim noktası QR bağlantısını başlat", "body": "Aynı ortamda müşteriyi uygulama kurdurmadan ağa alın; bağlantı QR ekranı ağ adı, şifre ve erişim bilgisini net şekilde paylaşsın."},
            {"title": "Oturum galerisini QR ile aç", "body": "Her müşteri veya etkinlik için ayrı açılan oturum galerisi, tarayıcıdan QR ile saniyeler içinde açılsın ve seçimler karışmadan ilerlesin."},
            {"title": "Yerel ödeme ve PAC onayı", "body": "İşletme ülkenize göre hazır ödeme yöntemlerini gösterin, seçimi kontrol edin ve PAC doğrulamasını tamamlayın."},
            {"title": "ZIP teslim ve satış raporu", "body": "Onaylanan dosyaları ZIP olarak teslim edin; indirme, satış, dönüşüm ve gelir akışını uygulama içindeki rapor ekranında oturum mantığını bozmadan izleyin."},
        ],
    },
    "en": {
        "hero_lead": "Bring photos in from local media or transfer them directly into the app from an FTP-capable professional camera, open WiFi or hotspot QR access, keep every shoot in its own session, let clients enter the QR gallery and deliver approved files as ZIP from the same device.",
        "metrics": [
            {"value": "1 device", "label": "Capture, show and deliver"},
            {"value": "QR access", "label": "Connect over WiFi or hotspot"},
            {"value": "Multi-session", "label": "Keep every shoot separate"},
        ],
        "workflow_title": "QR, sessions and delivery in one flow",
        "workflow_lead": "SnapVend turns direct FTP intake from professional cameras, WiFi or hotspot QR access, session-based client flow and post-delivery reporting into one field-ready operation.",
        "workflow_cards": [
            {"title": "Import from a pro camera", "body": "Pick photos from local media or transfer frames directly into SnapVend from an FTP-capable professional camera."},
            {"title": "Start WiFi / hotspot QR access", "body": "Bring clients onto the same network without asking them to install the app; the QR connection screen presents the network name, password and access details clearly."},
            {"title": "Open the session gallery with QR", "body": "Each client or event can have its own session gallery, opened in seconds from the browser through a dedicated QR code."},
            {"title": "Show local payment and confirm PAC", "body": "Display ready local payment methods for your business country, review the selection and complete PAC validation."},
            {"title": "Deliver ZIP and review reports", "body": "Deliver approved files as ZIP, then track downloads, sales, conversion and revenue from the in-app reports view without losing the session structure."},
        ],
    },
    "es": {
        "hero_lead": "Importe fotos desde la galería local o transfiéralas directamente a la aplicación desde una cámara profesional con FTP, abra una sesión separada para cada trabajo, deje que el cliente entre por QR y entregue los archivos aprobados en ZIP desde el mismo dispositivo.",
        "metrics": [
            {"value": "1 equipo", "label": "Capturar, mostrar y entregar"},
            {"value": "Acceso QR", "label": "El cliente entra en segundos"},
            {"value": "Sesiones múltiples", "label": "Cada toma queda separada"},
        ],
        "workflow_title": "QR, sesiones y entrega en un solo flujo",
        "workflow_lead": "SnapVend convierte la transferencia directa por FTP desde cámaras profesionales, la gestión por sesión, el acceso por QR y la entrega en una sola operación de campo.",
        "workflow_cards": [
            {"title": "Importe desde cámara profesional", "body": "Use la galería local o transfiera imágenes directamente a SnapVend desde una cámara profesional compatible con FTP."},
            {"title": "Abra una sesión separada", "body": "Cree una sesión distinta para cada cliente, toma o evento para que archivos, elecciones y entregas no se mezclen."},
            {"title": "Abra la galería por QR", "body": "El cliente escanea el QR en la misma red y entra a su propia galería de sesión en segundos."},
            {"title": "Muestre pago local y confirme PAC", "body": "Enseñe métodos de pago locales según el país del negocio, revise la selección y complete la validación PAC."},
            {"title": "Entregue ZIP y siga la sesión", "body": "Entregue los archivos aprobados en ZIP y mantenga visible en la aplicación el seguimiento por sesión y por ingresos."},
        ],
    },
    "fr": {
        "hero_lead": "Importez les photos depuis la galerie locale ou transférez-les directement dans l'application depuis un appareil photo pro compatible FTP, ouvrez une session distincte pour chaque prise de vue, faites entrer le client par QR et livrez les fichiers approuvés en ZIP depuis le même appareil.",
        "metrics": [
            {"value": "1 appareil", "label": "Capturer, montrer, livrer"},
            {"value": "Accès QR", "label": "Le client entre en quelques secondes"},
            {"value": "Sessions multiples", "label": "Chaque prise reste séparée"},
        ],
        "workflow_title": "QR, sessions et livraison dans un seul flux",
        "workflow_lead": "SnapVend transforme le transfert FTP direct depuis des appareils photo pros, la gestion par session, l'accès QR et la livraison en une seule opération terrain.",
        "workflow_cards": [
            {"title": "Importer depuis un appareil photo pro", "body": "Prenez les photos depuis la galerie locale ou transférez-les directement dans SnapVend depuis un appareil photo pro compatible FTP."},
            {"title": "Ouvrir une session distincte", "body": "Créez une session pour chaque client, prise de vue ou événement afin d'éviter tout mélange de fichiers, choix et livraisons."},
            {"title": "Ouvrir la galerie par QR", "body": "Le client scanne le QR sur le même réseau et entre dans sa galerie de session en quelques secondes."},
            {"title": "Afficher le paiement local et valider le PAC", "body": "Affichez les méthodes de paiement locales selon le pays de l'entreprise, vérifiez la sélection puis terminez la validation PAC."},
            {"title": "Livrer le ZIP et suivre la session", "body": "Livrez les fichiers approuvés en ZIP et gardez le suivi de la session ainsi que des revenus visible dans l'application."},
        ],
    },
    "de": {
        "hero_lead": "Importieren Sie Fotos aus lokaler Galerie oder uebertragen Sie sie direkt aus einer FTP-faehigen Profikamera in SnapVend, starten Sie fuer jedes Shooting eine eigene Session, lassen Sie Kunden per QR eintreten und liefern Sie freigegebene Dateien als ZIP vom selben Geraet.",
        "metrics": [
            {"value": "1 Geraet", "label": "Aufnehmen, zeigen, liefern"},
            {"value": "QR-Zugang", "label": "Kunden sind in Sekunden drin"},
            {"value": "Mehrere Sessions", "label": "Jedes Shooting bleibt getrennt"},
        ],
        "workflow_title": "QR, Sessions und Lieferung in einem Ablauf",
        "workflow_lead": "SnapVend verbindet direkten FTP-Import aus Profikameras, Session-Verwaltung, QR-Zugang und Auslieferung zu einer einzigen Feldoperation.",
        "workflow_cards": [
            {"title": "Aus Profikamera importieren", "body": "Waehlen Sie Fotos aus lokaler Galerie oder uebertragen Sie Bilder direkt aus einer FTP-faehigen Profikamera in SnapVend."},
            {"title": "Getrennte Session starten", "body": "Legen Sie fuer jeden Kunden, jedes Shooting oder Event eine eigene Session an, damit Dateien, Auswahl und Lieferung getrennt bleiben."},
            {"title": "Session-Galerie per QR oeffnen", "body": "Der Kunde scannt im selben Netzwerk den QR-Code und oeffnet seine Session-Galerie in Sekunden."},
            {"title": "Lokale Zahlung und PAC bestaetigen", "body": "Zeigen Sie lokale Zahlungsarten fuer Ihr Geschaeftsland, pruefen Sie die Auswahl und schliessen Sie die PAC-Bestaetigung ab."},
            {"title": "ZIP liefern und Session verfolgen", "body": "Liefern Sie freigegebene Dateien als ZIP und behalten Sie Session-basierte Lieferung sowie Umsatz im Blick."},
        ],
    },
    "it": {
        "hero_lead": "Importa le foto dalla galleria locale oppure trasferiscile direttamente nell'applicazione da una fotocamera professionale con FTP, apri una sessione separata per ogni servizio, fai entrare il cliente tramite QR e consegna i file approvati in ZIP dallo stesso dispositivo.",
        "metrics": [
            {"value": "1 dispositivo", "label": "Scatta, mostra, consegna"},
            {"value": "Accesso QR", "label": "Il cliente entra in pochi secondi"},
            {"value": "Sessioni multiple", "label": "Ogni servizio resta separato"},
        ],
        "workflow_title": "QR, sessioni e consegna in un unico flusso",
        "workflow_lead": "SnapVend unisce import diretto via FTP da fotocamere professionali, gestione per sessione, accesso QR e consegna in un'unica operazione sul campo.",
        "workflow_cards": [
            {"title": "Importa dalla fotocamera professionale", "body": "Scegli le foto dalla galleria locale oppure trasferiscile direttamente in SnapVend da una fotocamera professionale compatibile con FTP."},
            {"title": "Avvia una sessione dedicata", "body": "Crea una sessione per ogni cliente, servizio o evento così file, selezioni e consegne restano ben separati."},
            {"title": "Apri la galleria sessione con QR", "body": "Il cliente scansiona il QR sulla stessa rete e apre in pochi secondi la propria galleria di sessione."},
            {"title": "Mostra il pagamento locale e conferma il PAC", "body": "Mostra i metodi di pagamento locali in base al paese della tua attività, controlla la selezione e completa la validazione PAC."},
            {"title": "Consegna ZIP e monitora i report", "body": "Consegna i file approvati in ZIP e tieni sotto controllo consegne e ricavi per sessione direttamente nell'applicazione."},
        ],
    },
    "pt": {
        "hero_lead": "Importe fotos da galeria local ou transfira direto para o aplicativo a partir de uma camera profissional com FTP, abra uma sessao separada para cada trabalho, deixe o cliente entrar por QR e entregue os arquivos aprovados em ZIP no mesmo dispositivo.",
        "metrics": [
            {"value": "1 aparelho", "label": "Capturar, mostrar e entregar"},
            {"value": "Acesso QR", "label": "Cliente entra em segundos"},
            {"value": "Multissessoes", "label": "Cada ensaio fica separado"},
        ],
        "workflow_title": "QR, sessoes e entrega no mesmo fluxo",
        "workflow_lead": "SnapVend transforma transferencia FTP direta de camera profissional, gestao por sessao, acesso por QR e entrega em uma unica operacao de campo.",
        "workflow_cards": [
            {"title": "Importe da camera profissional", "body": "Escolha as fotos na galeria local ou transfira direto para o SnapVend a partir de uma camera profissional com FTP."},
            {"title": "Abra uma sessao separada", "body": "Crie uma sessao para cada cliente, ensaio ou evento para manter arquivos, escolhas e entregas organizados."},
            {"title": "Abra a galeria por QR", "body": "O cliente escaneia o QR na mesma rede e entra na propria galeria da sessao em segundos."},
            {"title": "Mostre pagamento local e confirme PAC", "body": "Exiba metodos locais conforme o pais do negocio, revise a selecao e conclua a validacao do PAC."},
            {"title": "Entregue ZIP e acompanhe a sessao", "body": "Entregue os arquivos aprovados em ZIP e mantenha visiveis no aplicativo o acompanhamento da sessao e da receita."},
        ],
    },
    "ru": {
        "hero_lead": "Загружайте фото из локальной галереи или передавайте их прямо в приложение с профессиональной камеры по FTP, открывайте отдельную сессию для каждой съемки, впускайте клиента по QR и выдавайте одобренные файлы в ZIP с того же устройства.",
        "metrics": [
            {"value": "1 устройство", "label": "Снять, показать, выдать"},
            {"value": "QR-доступ", "label": "Клиент входит за секунды"},
            {"value": "Несколько сессий", "label": "Каждая съемка отдельно"},
        ],
        "workflow_title": "QR, сессии и выдача в одном потоке",
        "workflow_lead": "SnapVend объединяет прямую FTP-передачу с профессиональной камеры, управление сессиями, QR-доступ и выдачу в одну полевую операцию.",
        "workflow_cards": [
            {"title": "Импорт с профкамеры", "body": "Берите фото из локальной галереи или передавайте кадры прямо в SnapVend с профессиональной камеры по FTP."},
            {"title": "Откройте отдельную сессию", "body": "Создавайте отдельную сессию для каждого клиента, съемки или события, чтобы файлы, выбор и выдача не смешивались."},
            {"title": "Откройте галерею по QR", "body": "Клиент сканирует QR в той же сети и за секунды входит в свою галерею сессии."},
            {"title": "Покажите локальную оплату и подтвердите PAC", "body": "Покажите локальные способы оплаты для страны бизнеса, проверьте выбор и завершите подтверждение PAC."},
            {"title": "Выдайте ZIP и отслеживайте сессию", "body": "Выдавайте одобренные файлы в ZIP и держите внутри приложения видимой выдачу и выручку по сессиям."},
        ],
    },
    "ar": {
        "hero_lead": "استورد الصور من المعرض المحلي او انقلها مباشرة الى التطبيق من كاميرا احترافية تدعم FTP، وافتح جلسة مستقلة لكل جلسة تصوير، ثم دع العميل يدخل عبر QR وسلم الملفات المعتمدة بصيغة ZIP من الجهاز نفسه.",
        "metrics": [
            {"value": "جهاز واحد", "label": "التقاط، عرض، تسليم"},
            {"value": "دخول QR", "label": "العميل يدخل خلال ثوان"},
            {"value": "جلسات متعددة", "label": "كل جلسة تبقى منفصلة"},
        ],
        "workflow_title": "QR والجلسات والتسليم في تدفق واحد",
        "workflow_lead": "يجمع SnapVend بين النقل المباشر عبر FTP من الكاميرات الاحترافية وادارة الجلسات ودخول QR والتسليم في عملية ميدانية واحدة.",
        "workflow_cards": [
            {"title": "استيراد من كاميرا احترافية", "body": "اختر الصور من المعرض المحلي او انقل اللقطات مباشرة الى SnapVend من كاميرا احترافية تدعم FTP."},
            {"title": "افتح جلسة مستقلة", "body": "ابدأ جلسة منفصلة لكل عميل او جلسة تصوير او فعالية حتى لا تختلط الملفات والاختيارات وعمليات التسليم."},
            {"title": "افتح المعرض عبر QR", "body": "يمسح العميل QR على الشبكة نفسها ويدخل الى معرض الجلسة الخاص به خلال ثوان."},
            {"title": "اعرض الدفع المحلي واكد PAC", "body": "اعرض طرق الدفع المحلية بحسب بلد النشاط وراجع الاختيار ثم اكمل التحقق من PAC."},
            {"title": "سلم ZIP وتابع الجلسة", "body": "سلم الملفات المعتمدة بصيغة ZIP وابق تتبع الجلسة والايراد ظاهرا داخل التطبيق."},
        ],
    },
    "hi": {
        "hero_lead": "लोकल गैलरी से फोटो लें या FTP-सक्षम प्रोफेशनल कैमरे से सीधे ऐप में ट्रांसफर करें, हर शूट के लिए अलग सेशन खोलें, ग्राहक को QR से अंदर लाएँ और मंजूर फाइलें उसी डिवाइस से ZIP में डिलीवर करें।",
        "metrics": [
            {"value": "1 डिवाइस", "label": "शूट, दिखाओ, डिलीवर करो"},
            {"value": "QR एक्सेस", "label": "ग्राहक सेकंडों में अंदर आए"},
            {"value": "अलग सेशन", "label": "हर शूट अलग रहे"},
        ],
        "workflow_title": "QR, सेशन और डिलीवरी एक ही फ्लो में",
        "workflow_lead": "SnapVend प्रोफेशनल कैमरे से सीधे FTP इम्पोर्ट, सेशन प्रबंधन, QR एक्सेस और डिलीवरी को एक ही फील्ड वर्कफ़्लो में जोड़ता है।",
        "workflow_cards": [
            {"title": "प्रोफेशनल कैमरे से इम्पोर्ट करें", "body": "लोकल गैलरी से चुनें या FTP-सक्षम प्रोफेशनल कैमरे से फ्रेम सीधे SnapVend में भेजें।"},
            {"title": "अलग सेशन शुरू करें", "body": "हर ग्राहक, शूट या इवेंट के लिए अलग सेशन खोलकर फाइलें, चयन और डिलीवरी व्यवस्थित रखें।"},
            {"title": "QR से सेशन गैलरी खोलें", "body": "ग्राहक उसी नेटवर्क पर QR स्कैन करके अपनी सेशन गैलरी सेकंडों में खोलता है।"},
            {"title": "लोकल भुगतान दिखाएँ और PAC की पुष्टि करें", "body": "बिज़नेस देश के हिसाब से लोकल भुगतान तरीके दिखाएँ, चयन की समीक्षा करें और PAC सत्यापन पूरा करें।"},
            {"title": "ZIP डिलीवर करें और सेशन ट्रैक करें", "body": "मंजूर फाइलों को ZIP में डिलीवर करें और ऐप के अंदर सेशन-आधारित डिलीवरी तथा आय देखते रहें।"},
        ],
    },
    "ja": {
        "hero_lead": "ローカルギャラリーから写真を取り込むか、FTP 対応のプロ向けカメラからアプリへ直接転送し、撮影ごとに個別のセッションを作成して、QR で顧客を案内し、承認済みファイルを同じ端末から ZIP 納品します。",
        "metrics": [
            {"value": "1台", "label": "撮る、見せる、納品する"},
            {"value": "QR アクセス", "label": "顧客は数秒で入場"},
            {"value": "複数セッション", "label": "撮影ごとに分けて管理"},
        ],
        "workflow_title": "QR、セッション、納品を一つの流れに",
        "workflow_lead": "SnapVend はプロ向けカメラからの直接 FTP 取り込み、セッション管理、QR アクセス、納品を一つの現場フローにまとめます。",
        "workflow_cards": [
            {"title": "プロ向けカメラから取り込む", "body": "ローカルギャラリーから選ぶか、FTP 対応のプロ向けカメラから SnapVend に直接転送します。"},
            {"title": "個別セッションを開始する", "body": "顧客、撮影、イベントごとに個別のセッションを作成し、ファイル、選択、納品を混ぜずに管理します。"},
            {"title": "QR でセッションギャラリーを開く", "body": "同じネットワーク上で顧客が QR を読み取り、自分のセッションギャラリーを数秒で開きます。"},
            {"title": "ローカル決済を表示して PAC を確認", "body": "事業国に合わせたローカル決済方法を表示し、選択内容を確認して PAC 検証を完了します。"},
            {"title": "ZIP 納品とセッション追跡", "body": "承認済みファイルを ZIP で納品し、セッションごとの納品状況と売上をアプリ内で追跡します。"},
        ],
    },
    "zh": {
        "hero_lead": "可从本地相册导入照片，也可通过支持 FTP 的专业相机直接传入应用；为每次拍摄建立独立会话，让客户通过二维码进入，并从同一设备交付已批准的 ZIP 文件。",
        "metrics": [
            {"value": "1 台设备", "label": "拍摄、展示、交付"},
            {"value": "二维码进入", "label": "客户几秒内进入"},
            {"value": "多会话", "label": "每次拍摄独立管理"},
        ],
        "workflow_title": "二维码、会话与交付在同一流程中",
        "workflow_lead": "SnapVend 将专业相机的直接 FTP 导入、会话管理、二维码进入和交付整合为一个现场工作流程。",
        "workflow_cards": [
            {"title": "从专业相机导入", "body": "可从本地相册选择，也可通过支持 FTP 的专业相机把照片直接传入 SnapVend。"},
            {"title": "创建独立会话", "body": "为每位客户、每次拍摄或每场活动建立独立会话，让文件、选片和交付互不混淆。"},
            {"title": "通过二维码打开会话画廊", "body": "客户在同一网络下扫描二维码，几秒内进入自己的会话画廊。"},
            {"title": "显示本地支付并确认 PAC", "body": "根据商家所在国家显示本地支付方式，检查所选照片并完成 PAC 验证。"},
            {"title": "交付 ZIP 并追踪会话", "body": "以 ZIP 方式交付已批准文件，并在应用内追踪按会话区分的交付与收入。"},
        ],
    },
}

FAQ_FLOW_OVERRIDES = {
    "tr": [
        {"q": "SnapVend internetsiz çalışır mı?", "a": "Evet. Ana akış yerel ağ veya erişim noktası üzerinde çalışabilir. Bulut zorunlu değildir."},
        {"q": "Profesyonel fotoğraf makinesinden doğrudan aktarım yapabilir miyim?", "a": "Evet. FTP destekli profesyonel fotoğraf makinelerinden fotoğrafları aynı ağ veya erişim noktası üzerinden doğrudan SnapVend uygulamasına aktarabilirsiniz."},
        {"q": "Müşteri fotoğrafları nasıl görür?", "a": "Müşteri önce WiFi ya da erişim noktası QR bağlantısıyla aynı ağa alınır, ardından oturum QR kodunu okutup yalnızca kendisine ait galeriyi tarayıcıdan açar."},
        {"q": "Oturum yapısı ne işe yarar?", "a": "Her müşteri, çekim veya etkinlik ayrı bir oturum olarak tutulur. Böylece fotoğraflar, seçimler, ödeme akışı ve teslim kayıtları karışmaz; ayrıca her oturumun sonucu daha kontrollü izlenir."},
        {"q": "Raporlar bölümünde neyi takip edebilirim?", "a": "Rapor ekranı üzerinden satış adedi, gelir, indirme hareketleri, dönüşüm ve ortalama sepet gibi temel performans göstergelerini sahadaki operasyonu kapatmadan izleyebilirsiniz."},
        {"q": "Kendi işletme adımı ve logomu kullanabilir miyim?", "a": "Evet. Pro planlarda özel işletme adı, logo ve teslim markalaması açılır."},
        {"q": "Müşteriye ülkeye göre ödeme yöntemi gösterebilir miyim?", "a": "Evet. İşletme ülkesi seçildiğinde kurulumu tamamlanan yerel yöntemler ödeme popup ekranında görünür. Türkiye, İspanya, Hindistan, Çin ve Japonya için hazır yöntem setleri vardır."},
        {"q": "Teslim limiti hangi planda kalkıyor?", "a": "Aylık ve yıllık Pro planlar günlük teslim limitini kaldırır."},
    ],
    "en": [
        {"q": "Does SnapVend work without internet?", "a": "Yes. The main workflow can run over local network or hotspot. Cloud access is not required."},
        {"q": "Can I transfer directly from a professional camera?", "a": "Yes. Photos can move directly into SnapVend from an FTP-capable professional camera over the same network or hotspot."},
        {"q": "How do clients view the photos?", "a": "Clients first join through a WiFi or hotspot QR connection, then scan the session QR code to open only the gallery created for them in the browser."},
        {"q": "What does the session structure do?", "a": "Each client, shoot or event can stay in its own session so files, selections, payment flow and delivery records never get mixed, while each outcome stays easier to track."},
        {"q": "What can I track in the reports section?", "a": "The reports view helps you monitor sales count, revenue, download activity, conversion and average basket without breaking the live field workflow."},
        {"q": "Can I use my own business name and logo?", "a": "Yes. Pro plans unlock custom business branding, logo usage and branded delivery."},
        {"q": "Can I show country-specific payment methods to clients?", "a": "Yes. Once the business country is selected, completed local methods appear in the payment popup. Ready local method sets are available for Turkey, Spain, India, China and Japan."},
        {"q": "Which plan removes delivery limits?", "a": "Both monthly and yearly Pro plans remove the daily delivery limit."},
    ],
    "es": [
        {"q": "¿SnapVend funciona sin internet?", "a": "Si. El flujo principal puede funcionar con red local o punto de acceso sin depender de la nube."},
        {"q": "¿Puedo transferir directo desde una camara profesional?", "a": "Si. Puede enviar fotos directamente a SnapVend desde una camara profesional con FTP usando la misma red o punto de acceso."},
        {"q": "¿Como ve el cliente las fotos?", "a": "El cliente escanea un QR en la misma red, entra a su galeria de sesion en el navegador y hace alli la seleccion."},
        {"q": "¿Para que sirve la estructura de sesion?", "a": "Cada cliente, toma o evento puede mantenerse en su propia sesion para que archivos, selecciones, pago y entrega no se mezclen."},
        {"q": "¿Puedo usar mi propio logo y nombre?", "a": "Si. Los planes profesionales desbloquean nombre comercial, logo y entrega con marca propia."},
        {"q": "¿Puedo mostrar metodos de pago segun el pais?", "a": "Si. Al elegir el pais del negocio, los metodos locales configurados aparecen en el popup de pago. Hay metodos listos para Turquia, Espana, India, China y Japon."},
        {"q": "¿Que plan elimina el limite de entrega?", "a": "Los planes profesional mensual y profesional anual eliminan el limite diario."},
    ],
    "fr": [
        {"q": "SnapVend fonctionne t il sans internet ?", "a": "Oui. Le flux principal peut tourner sur reseau local ou point d'acces sans cloud obligatoire."},
        {"q": "Puis je transferer directement depuis un appareil photo pro ?", "a": "Oui. Vous pouvez envoyer les photos directement dans SnapVend depuis un appareil photo pro compatible FTP sur le meme reseau ou point d'acces."},
        {"q": "Comment le client voit il les photos ?", "a": "Le client scanne un QR sur le meme reseau, ouvre sa galerie de session dans le navigateur et fait ses choix."},
        {"q": "A quoi sert la structure de session ?", "a": "Chaque client, prise de vue ou evenement peut rester dans sa propre session pour que fichiers, choix, paiement et livraison ne se melangent pas."},
        {"q": "Puis je utiliser mon propre logo ?", "a": "Oui. Les plans professionnels ouvrent le nom d entreprise, le logo et la livraison personnalisee."},
        {"q": "Puis je afficher des methodes de paiement selon le pays ?", "a": "Oui. Une fois le pays de l entreprise choisi, les methodes locales configurees apparaissent dans la fenetre de paiement. Des ensembles prets existent pour la Turquie, l Espagne, l Inde, la Chine et le Japon."},
        {"q": "Quel plan retire la limite de livraison ?", "a": "Les plans professionnel mensuel et professionnel annuel retirent la limite quotidienne."},
    ],
    "de": [
        {"q": "Funktioniert SnapVend ohne Internet?", "a": "Ja. Der Hauptablauf kann uber lokales Netzwerk oder einen mobilen Zugangspunkt ohne Cloud laufen."},
        {"q": "Kann ich direkt aus einer Profikamera uebertragen?", "a": "Ja. Fotos koennen ueber dieselbe Netzwerkverbindung oder einen mobilen Zugangspunkt direkt aus einer FTP-faehigen Profikamera in SnapVend gehen."},
        {"q": "Wie sehen Kunden die Fotos?", "a": "Kunden scannen im gleichen Netzwerk den QR Code, oeffnen ihre Session-Galerie im Browser und treffen dort die Auswahl."},
        {"q": "Wozu dient die Session-Struktur?", "a": "Jeder Kunde, jedes Shooting oder Event bleibt in einer eigenen Session, damit Dateien, Auswahl, Zahlung und Lieferung nicht vermischt werden."},
        {"q": "Kann ich eigenes Branding nutzen?", "a": "Ja. Der Profi-Plan schaltet Firmenname, Logo und gebrandete Auslieferung frei."},
        {"q": "Kann ich landerspezifische Zahlungsarten zeigen?", "a": "Ja. Sobald das Geschaeftsland gewahlt ist, erscheinen fertig eingerichtete lokale Methoden im Zahlungsfenster. Vorbereitete Sets gibt es fur die Turkei, Spanien, Indien, China und Japan."},
        {"q": "Welcher Plan entfernt das Lieferlimit?", "a": "Sowohl der monatliche als auch der jahrliche Profi-Plan entfernen das Tageslimit."},
    ],
    "it": [
        {"q": "SnapVend funziona senza internet?", "a": "Sì. Il flusso principale può funzionare su rete locale o punto di accesso senza dipendere dal cloud."},
        {"q": "Posso trasferire direttamente da una fotocamera professionale?", "a": "Sì. Le foto possono entrare direttamente in SnapVend da una fotocamera professionale compatibile con FTP sulla stessa rete o punto di accesso."},
        {"q": "Come vedono le foto i clienti?", "a": "Il cliente scansiona un QR sulla stessa rete, apre la propria galleria di sessione nel browser e seleziona le foto lì."},
        {"q": "A cosa serve la struttura a sessioni?", "a": "Ogni cliente, servizio o evento può restare in una sessione separata, così file, selezioni, pagamenti e consegne non si mescolano."},
        {"q": "Posso usare il mio nome e il mio logo?", "a": "Sì. I piani professionali sbloccano branding personalizzato, logo e consegna brandizzata."},
        {"q": "Posso mostrare metodi di pagamento in base al paese?", "a": "Sì. Dopo aver scelto il paese dell'attività, i metodi locali configurati compaiono nel popup di pagamento. Esistono set pronti per Turchia, Spagna, India, Cina e Giappone."},
        {"q": "Quale piano rimuove il limite di consegna?", "a": "Sia il piano professionale mensile sia quello annuale rimuovono il limite giornaliero."},
    ],
    "pt": [
        {"q": "O SnapVend funciona sem internet?", "a": "Sim. O fluxo principal pode rodar em rede local ou ponto de acesso sem depender da nuvem."},
        {"q": "Posso transferir direto de uma camera profissional?", "a": "Sim. As fotos podem entrar direto no SnapVend a partir de uma camera profissional com FTP usando a mesma rede ou ponto de acesso."},
        {"q": "Como o cliente ve as fotos?", "a": "O cliente escaneia um QR na mesma rede, abre sua galeria de sessao no navegador e faz a selecao ali."},
        {"q": "Para que serve a estrutura de sessao?", "a": "Cada cliente, ensaio ou evento pode ficar em sua propria sessao para que arquivos, escolhas, pagamento e entrega nao se misturem."},
        {"q": "Posso usar meu proprio nome e logo?", "a": "Sim. Os planos profissionais liberam branding, logo e entrega personalizada."},
        {"q": "Posso mostrar metodos de pagamento por pais?", "a": "Sim. Ao escolher o pais do negocio, os metodos locais configurados aparecem no popup de pagamento. Ha conjuntos prontos para Turquia, Espanha, India, China e Japao."},
        {"q": "Qual plano remove o limite de entrega?", "a": "Os planos profissional mensal e profissional anual removem o limite diario."},
    ],
    "ru": [
        {"q": "Работает ли SnapVend без интернета?", "a": "Да. Основной сценарий может работать через локальную сеть или точку доступа без облака."},
        {"q": "Можно ли передавать напрямую с профессиональной камеры?", "a": "Да. Фото можно отправлять прямо в SnapVend с профессиональной камеры по FTP через ту же сеть или точку доступа."},
        {"q": "Как клиент смотрит фотографии?", "a": "Клиент сканирует QR-код в той же сети, открывает свою галерею сессии в браузере и выбирает фотографии там."},
        {"q": "Для чего нужна структура сессий?", "a": "Каждый клиент, съемка или событие могут идти в отдельной сессии, чтобы файлы, выбор, оплата и выдача не смешивались."},
        {"q": "Можно ли использовать свой логотип и бренд?", "a": "Да. Профессиональный план открывает фирменное имя, логотип и брендированную выдачу."},
        {"q": "Можно ли показать клиенту способы оплаты по стране?", "a": "Да. После выбора страны бизнеса настроенные локальные методы появляются во всплывающем окне оплаты. Готовые наборы есть для Турции, Испании, Индии, Китая и Японии."},
        {"q": "Какой тариф снимает лимит выдачи?", "a": "И месячный, и годовой профессиональный план снимают ежедневный лимит выдачи."},
    ],
    "ar": [
        {"q": "هل يعمل SnapVend بدون انترنت؟", "a": "نعم. يمكن تشغيل التدفق الرئيسي عبر شبكة محلية او نقطة اتصال بدون اعتماد على السحابة."},
        {"q": "هل يمكن النقل مباشرة من كاميرا احترافية؟", "a": "نعم. يمكن نقل الصور مباشرة الى SnapVend من كاميرا احترافية تدعم FTP عبر الشبكة نفسها او نقطة الاتصال."},
        {"q": "كيف يشاهد العميل الصور؟", "a": "يمسح العميل QR على نفس الشبكة ويدخل الى معرض الجلسة الخاص به من المتصفح ويختار الصور هناك."},
        {"q": "ما فائدة بنية الجلسات؟", "a": "يمكن حفظ كل عميل او جلسة تصوير او فعالية داخل جلسة مستقلة حتى لا تختلط الملفات والاختيارات والدفع والتسليم."},
        {"q": "هل يمكنني استخدام اسمي التجاري وشعاري؟", "a": "نعم. الخطط الاحترافية تفتح اسم النشاط والشعار والتسليم بعلامتك الخاصة."},
        {"q": "هل يمكنني عرض طرق دفع حسب البلد للعميل؟", "a": "نعم. عند اختيار بلد النشاط تظهر الطرق المحلية المكتملة في نافذة الدفع. توجد مجموعات جاهزة لتركيا واسبانيا والهند والصين واليابان."},
        {"q": "اي خطة تزيل حد التسليم اليومي؟", "a": "كل من الخطة الشهرية والسنوية الاحترافية يزيلان حد التسليم اليومي."},
    ],
    "hi": [
        {"q": "क्या SnapVend बिना इंटरनेट के काम करता है?", "a": "हाँ। मुख्य फ्लो लोकल नेटवर्क या हॉटस्पॉट पर चल सकता है, क्लाउड जरूरी नहीं है।"},
        {"q": "क्या मैं प्रोफेशनल कैमरे से सीधा ट्रांसफर कर सकता हूँ?", "a": "हाँ। FTP-सक्षम प्रोफेशनल कैमरे से फोटो उसी नेटवर्क या हॉटस्पॉट पर सीधे SnapVend में लाई जा सकती हैं।"},
        {"q": "ग्राहक फोटो कैसे देखता है?", "a": "ग्राहक उसी नेटवर्क पर QR स्कैन करके ब्राउज़र में अपनी सेशन गैलरी खोलता है और वहीं चयन करता है।"},
        {"q": "सेशन संरचना किस काम आती है?", "a": "हर ग्राहक, शूट या इवेंट को अलग सेशन में रखा जा सकता है ताकि फाइलें, चयन, भुगतान और डिलीवरी आपस में न मिलें।"},
        {"q": "क्या मैं अपना नाम और लोगो इस्तेमाल कर सकता हूँ?", "a": "हाँ। प्रो प्लान कस्टम ब्रांडिंग, लोगो और ब्रांडेड डिलीवरी खोलते हैं।"},
        {"q": "क्या मैं ग्राहक को देश के हिसाब से भुगतान तरीके दिखा सकता हूँ?", "a": "हाँ। बिज़नेस देश चुनने के बाद कॉन्फ़िगर किए गए लोकल तरीके भुगतान विंडो में दिखते हैं। तुर्की, स्पेन, भारत, चीन और जापान के लिए तैयार भुगतान सेट मौजूद हैं।"},
        {"q": "कौन सा प्लान डिलीवरी सीमा हटाता है?", "a": "मासिक और वार्षिक दोनों प्रो प्लान दैनिक डिलीवरी सीमा हटा देते हैं।"},
    ],
    "ja": [
        {"q": "SnapVend はインターネットなしで使えますか？", "a": "はい。主なフローはローカルネットワークやホットスポット上で動作でき、クラウドは必須ではありません。"},
        {"q": "プロ向けカメラから直接取り込めますか？", "a": "はい。FTP 対応のプロ向けカメラから、同じネットワークやホットスポットを通じて SnapVend へ直接取り込めます。"},
        {"q": "クライアントはどうやって写真を見ますか？", "a": "同じネットワーク上で QR を読み取り、自分のセッションギャラリーをブラウザで開いて選択します。"},
        {"q": "セッション構造は何のためにありますか？", "a": "顧客、撮影、イベントごとに個別のセッションで管理できるため、ファイル、選択、支払い、納品が混ざりません。"},
        {"q": "自分のブランド名やロゴを使えますか？", "a": "はい。プロプランで独自ブランド名、ロゴ、ブランド納品が使えます。"},
        {"q": "国ごとの決済方法をクライアントに表示できますか？", "a": "はい。事業国を選ぶと、設定済みのローカル決済方法が支払いポップアップに表示されます。トルコ、スペイン、インド、中国、日本向けの方法セットが用意されています。"},
        {"q": "どのプランで納品制限がなくなりますか？", "a": "月額プロと年額プロの両方で日次納品制限が解除されます。"},
    ],
    "zh": [
        {"q": "SnapVend 可以在没有互联网时使用吗？", "a": "可以。主要流程可在本地网络或热点上运行，不依赖云端。"},
        {"q": "可以直接从专业相机传入吗？", "a": "可以。支持 FTP 的专业相机可通过同一网络或热点直接把照片传入 SnapVend。"},
        {"q": "客户如何查看照片？", "a": "客户在同一网络中扫描二维码后，就能在浏览器里打开自己的会话画廊并完成选片。"},
        {"q": "会话结构有什么作用？", "a": "每位客户、每次拍摄或每场活动都可以放在独立会话中，这样文件、选片、付款和交付记录不会混在一起。"},
        {"q": "我可以使用自己的品牌名和标识吗？", "a": "可以。专业版计划会开放自定义品牌名、标识和品牌化交付。"},
        {"q": "可以向客户显示按国家配置的支付方式吗？", "a": "可以。选择商家所在国家后，已完成设置的本地支付方式会显示在支付弹窗中。目前已为土耳其、西班牙、印度、中国和日本准备了现成方式。"},
        {"q": "哪个计划会移除交付限制？", "a": "月度专业版和年度专业版都会移除每日交付限制。"},
    ],
}

PRINT_QUEUE_OVERRIDES = {
    "tr": {
        "audience_body": "Canlı çekimde hızlı seçim, anında teslim ve baskı listesini aynı akışta yönetmek isteyen düğün ekipleri için güçlü bir yapı sunar.",
        "use_case": {
            "title": "Düğün baskı listesi",
            "body": "Çift, aile ve misafir seçimlerini toplarken baskıya gidecek kareleri ayrı bir baskı listesinde toplayın; sahadaki baskı akışı dijital teslimden kopmadan ilerlesin.",
        },
        "reference": {
            "title": "Düğün baskı ve teslim ekipleri",
            "body": "Hem dijital teslimi hem de baskı hazırlığını aynı operasyon içinde yönetmek isteyen düğün fotoğrafçıları için tasarlanmıştır.",
        },
        "faq": {
            "q": "Baskı listesi ne işe yarar?",
            "a": "Baskı listesi, seçilen kareleri teslim akışından koparmadan baskı için ayrı tutar. Özellikle düğün fotoğrafçılarında hangi fotoğrafın basılacağı ve baskı hazırlığının nasıl ilerlediği daha kontrollü yönetilir.",
        },
    },
    "en": {
        "audience_body": "A strong fit for wedding teams that want to manage fast selection, immediate delivery and a live print list in the same workflow.",
        "use_case": {
            "title": "Wedding print list",
            "body": "Collect couple, family and guest selections while keeping print-ready frames in a separate print list, so on-site printing can move forward without breaking digital delivery.",
        },
        "reference": {
            "title": "Wedding print and delivery teams",
            "body": "Built for wedding photographers who want to manage digital delivery and print preparation inside the same operation.",
        },
        "faq": {
            "q": "What does the print list do?",
            "a": "The print list keeps selected frames ready for printing without breaking the delivery flow. It gives wedding teams a more controlled way to track which photos should be printed and how print preparation should move forward.",
        },
    },
    "es": {
        "audience_body": "Un flujo fuerte para equipos de boda que quieren gestionar seleccion rapida, entrega inmediata y lista de impresion dentro del mismo proceso.",
        "use_case": {
            "title": "Lista de impresion para bodas",
            "body": "Recoja selecciones de pareja, familia e invitados y mantenga las fotos listas dentro de una lista de impresion separada sin romper la entrega digital.",
        },
        "reference": {
            "title": "Equipos de impresion y entrega en bodas",
            "body": "Pensado para fotografos de boda que quieren llevar entrega digital y preparacion de impresion dentro de la misma operacion.",
        },
        "faq": {
            "q": "¿Para que sirve la lista de impresion?",
            "a": "La lista de impresion mantiene las fotos seleccionadas listas para imprimir sin cortar el flujo de entrega. Ayuda a los equipos de boda a controlar mejor que imagen se imprimira y como avanzara la preparacion de impresion.",
        },
    },
    "fr": {
        "audience_body": "Un flux solide pour les equipes mariage qui veulent gerer selection rapide, livraison immediate et liste d'impression dans la meme operation.",
        "use_case": {
            "title": "Liste d'impression mariage",
            "body": "Recuperez les choix du couple, de la famille et des invites puis gardez les images a imprimer dans une liste separee sans casser la livraison numerique.",
        },
        "reference": {
            "title": "Equipes mariage impression et livraison",
            "body": "Concu pour les photographes de mariage qui veulent gerer livraison numerique et preparation des impressions dans le meme flux.",
        },
        "faq": {
            "q": "A quoi sert la liste d'impression ?",
            "a": "La liste d'impression garde les images selectionnees pretes a imprimer sans interrompre la livraison. Elle aide les equipes mariage a mieux suivre quelles photos doivent etre imprimees et comment la preparation impression avance.",
        },
    },
    "de": {
        "audience_body": "Ein starker Ablauf fuer Hochzeitsteams, die schnelle Auswahl, sofortige Lieferung und Druckliste im selben Prozess steuern wollen.",
        "use_case": {
            "title": "Hochzeits-Druckliste",
            "body": "Sammeln Sie Auswahl von Paar, Familie und Gaesten und halten Sie druckbereite Bilder in einer eigenen Druckliste, ohne die digitale Lieferung zu unterbrechen.",
        },
        "reference": {
            "title": "Hochzeits-Teams fur Druck und Lieferung",
            "body": "Gedacht fuer Hochzeitsfotografen, die digitale Lieferung und Druckvorbereitung in derselben Operation verwalten wollen.",
        },
        "faq": {
            "q": "Wofuer ist die Druckliste gedacht?",
            "a": "Die Druckliste haelt ausgewaehlte Bilder druckbereit, ohne den Lieferablauf zu stoppen. So koennen Hochzeitsteams besser verfolgen, welche Fotos gedruckt werden sollen und wie die Druckvorbereitung weitergeht.",
        },
    },
    "it": {
        "audience_body": "Un flusso molto forte per team wedding che vogliono gestire selezione rapida, consegna immediata e lista di stampa nella stessa operazione.",
        "use_case": {
            "title": "Lista di stampa per matrimoni",
            "body": "Raccogli le selezioni di sposi, famiglia e invitati e tieni le foto destinate alla stampa in una lista separata, senza interrompere la consegna digitale.",
        },
        "reference": {
            "title": "Team matrimoni per stampa e consegna",
            "body": "Pensato per fotografi di matrimonio che vogliono gestire consegna digitale e preparazione della stampa nella stessa operazione.",
        },
        "faq": {
            "q": "A cosa serve la lista di stampa?",
            "a": "La lista di stampa mantiene le foto selezionate pronte per la stampa senza interrompere il flusso di consegna. Aiuta i team wedding a controllare meglio quali immagini stampare e come far avanzare la preparazione.",
        },
    },
    "pt": {
        "audience_body": "Um fluxo forte para equipes de casamento que querem gerenciar selecao rapida, entrega imediata e lista de impressao dentro da mesma operacao.",
        "use_case": {
            "title": "Lista de impressao para casamento",
            "body": "Recolha as escolhas de noivos, familia e convidados e mantenha as fotos prontas em uma lista de impressao separada sem quebrar a entrega digital.",
        },
        "reference": {
            "title": "Equipes de impressao e entrega em casamento",
            "body": "Feito para fotografos de casamento que querem controlar entrega digital e preparacao de impressao na mesma operacao.",
        },
        "faq": {
            "q": "Para que serve a lista de impressao?",
            "a": "A lista de impressao mantem as fotos selecionadas prontas para imprimir sem interromper a entrega. Isso ajuda equipes de casamento a controlar melhor quais fotos vao para impressao e como a preparacao deve seguir.",
        },
    },
    "ru": {
        "audience_body": "Сильный сценарий для свадебных команд, которым нужно вести быстрый отбор, мгновенную выдачу и список на печать в одном процессе.",
        "use_case": {
            "title": "Свадебный список на печать",
            "body": "Собирайте выбор пары, семьи и гостей и держите кадры для печати в отдельном списке, не прерывая цифровую выдачу.",
        },
        "reference": {
            "title": "Свадебные команды печати и выдачи",
            "body": "Подходит свадебным фотографам, которые хотят вести цифровую выдачу и подготовку печати внутри одной операции.",
        },
        "faq": {
            "q": "Для чего нужен список на печать?",
            "a": "Список на печать держит выбранные кадры готовыми к печати без разрыва основного потока выдачи. Это помогает свадебным командам лучше контролировать, какие фото печатать и как должна идти подготовка печати.",
        },
    },
    "ar": {
        "audience_body": "مسار قوي لفرق تصوير الاعراس التي تريد ادارة الاختيار السريع والتسليم الفوري وقائمة الطباعة داخل العملية نفسها.",
        "use_case": {
            "title": "قائمة طباعة الاعراس",
            "body": "اجمع اختيارات العروسين والعائلة والضيوف ثم احتفظ بالصور الجاهزة في قائمة طباعة منفصلة بدون قطع مسار التسليم الرقمي.",
        },
        "reference": {
            "title": "فرق طباعة وتسليم الاعراس",
            "body": "مصمم لمصوري الاعراس الذين يريدون ادارة التسليم الرقمي وتجهيز الطباعة ضمن العملية نفسها.",
        },
        "faq": {
            "q": "ما فائدة قائمة الطباعة؟",
            "a": "تحافظ قائمة الطباعة على الصور المختارة جاهزة للطباعة من دون ايقاف مسار التسليم. وتساعد فرق الاعراس على متابعة الصور التي يجب طباعتها وكيف يتقدم تجهيز الطباعة بشكل اوضح.",
        },
    },
    "hi": {
        "audience_body": "यह वेडिंग टीमों के लिए खास तौर पर मजबूत फ्लो है, जहाँ तेज चयन, तुरंत डिलीवरी और प्रिंट सूची एक ही ऑपरेशन में संभाली जाती है।",
        "use_case": {
            "title": "वेडिंग प्रिंट सूची",
            "body": "दूल्हा-दुल्हन, परिवार और मेहमानों की पसंद लेते हुए प्रिंट-तैयार तस्वीरों को अलग प्रिंट सूची में रखें, ताकि डिजिटल डिलीवरी रुके बिना ऑन-साइट प्रिंटिंग चलती रहे।",
        },
        "reference": {
            "title": "वेडिंग प्रिंट और डिलीवरी टीमें",
            "body": "उन वेडिंग फोटोग्राफरों के लिए बनाया गया है जो डिजिटल डिलीवरी और प्रिंट तैयारी को एक ही ऑपरेशन में चलाना चाहते हैं।",
        },
        "faq": {
            "q": "प्रिंट सूची क्या करती है?",
            "a": "प्रिंट सूची चुनी हुई तस्वीरों को डिलीवरी फ्लो रोके बिना प्रिंट के लिए तैयार रखती है। इससे वेडिंग टीमों को यह समझना आसान होता है कि कौन-सी तस्वीरें प्रिंट होंगी और प्रिंट तैयारी कैसे आगे बढ़ेगी।",
        },
    },
    "ja": {
        "audience_body": "素早い選定、即時納品、プリントリストを同じ流れで管理したいウェディングチームに特に向いています。",
        "use_case": {
            "title": "ウェディング向けプリントリスト",
            "body": "新郎新婦、家族、ゲストの選定を集めながら、印刷対象の写真を別のプリントリストで管理し、デジタル納品を止めずに現場印刷を進められます。",
        },
        "reference": {
            "title": "ウェディングの印刷・納品チーム",
            "body": "デジタル納品と印刷準備を同じ運用の中で進めたいウェディングフォトグラファー向けです。",
        },
        "faq": {
            "q": "プリントリストは何のためですか？",
            "a": "プリントリストは、納品フローを止めずに選択済み写真を印刷用に整理します。どの写真を印刷するか、そして印刷準備をどう進めるかを、ウェディングチームがより管理しやすくなります。",
        },
    },
    "zh": {
        "audience_body": "非常适合需要在同一流程中管理快速选片、即时交付和打印列表的婚礼摄影团队。",
        "use_case": {
            "title": "婚礼打印列表",
            "body": "在收集新人、家人和宾客选片的同时，把需要打印的照片放进独立列表，让现场打印不打断数字交付流程。",
        },
        "reference": {
            "title": "婚礼打印与交付团队",
            "body": "适合希望在同一套运营中同时管理数字交付和打印准备的婚礼摄影师。",
        },
        "faq": {
            "q": "打印列表有什么作用？",
            "a": "打印列表会在不打断交付流程的情况下，把已选照片保持为待打印状态，帮助婚礼团队更清楚地管理哪些照片要打印，以及打印准备该如何推进。",
        },
    },
}

for locale_code, overrides in COPY_FLOW_OVERRIDES.items():
    COPY[locale_code].update(overrides)

for locale_code, items in FAQ_FLOW_OVERRIDES.items():
    FAQ_SECTION[locale_code]["items"] = items

BRAND_SEARCH_SIGNAL_BY_LOCALE = {
    "tr": {
        "meta_title": "SnapVend Gallery | Fotoğrafçılar İçin QR Galeri ve Yerel Teslim",
        "meta_description": "SnapVend Gallery, fotoğrafçıların QR galeri paylaşımı, FTP kamera aktarımı, müşteri seçimi ve ZIP teslim akışını tek telefon veya tablette yönetmesine yardımcı olur.",
        "faq": {
            "q": "SnapVend Gallery nedir?",
            "a": "SnapVend Gallery, fotoğrafçılar için geliştirilen QR galeri, FTP kamera aktarımı, müşteri seçimi, yerel ödeme onayı ve ZIP teslim akışını tek cihazda birleştiren mobil uygulamadır.",
        },
    },
    "en": {
        "meta_title": "SnapVend Gallery | QR Gallery and Local Photo Delivery for Photographers",
        "meta_description": "SnapVend Gallery helps photographers manage QR gallery sharing, FTP camera transfer, client selection and ZIP delivery from one phone or tablet.",
        "faq": {
            "q": "What is SnapVend Gallery?",
            "a": "SnapVend Gallery is a mobile app for photographers that combines QR galleries, FTP camera transfer, client selection, local payment approval and ZIP delivery on one device.",
        },
    },
    "es": {
        "meta_title": "SnapVend Gallery | Galería QR y entrega local para fotógrafos",
        "meta_description": "SnapVend Gallery ayuda a fotógrafos a gestionar galería QR, transferencia FTP desde cámara, selección del cliente y entrega ZIP desde un solo teléfono o tablet.",
        "faq": {
            "q": "¿Qué es SnapVend Gallery?",
            "a": "SnapVend Gallery es una aplicación móvil para fotógrafos que une galería QR, transferencia FTP desde cámara, selección del cliente, aprobación de pago local y entrega ZIP en un solo dispositivo.",
        },
    },
    "fr": {
        "meta_title": "SnapVend Gallery | Galerie QR et livraison locale pour photographes",
        "meta_description": "SnapVend Gallery aide les photographes a gerer galerie QR, transfert FTP depuis l appareil photo, selection client et livraison ZIP depuis un seul telephone ou tablette.",
        "faq": {
            "q": "Qu'est-ce que SnapVend Gallery ?",
            "a": "SnapVend Gallery est une application mobile pour photographes qui regroupe galerie QR, transfert FTP depuis l appareil photo, selection client, validation de paiement local et livraison ZIP sur un seul appareil.",
        },
    },
    "de": {
        "meta_title": "SnapVend Gallery | QR-Galerie und lokale Fotoauslieferung",
        "meta_description": "SnapVend Gallery hilft Fotografen, QR-Galerie, FTP-Kameraimport, Kundenauswahl und ZIP-Auslieferung auf einem Telefon oder Tablet zu verwalten.",
        "faq": {
            "q": "Was ist SnapVend Gallery?",
            "a": "SnapVend Gallery ist eine mobile App fuer Fotografen, die QR-Galerien, FTP-Kameraimport, Kundenauswahl, lokale Zahlungsfreigabe und ZIP-Auslieferung auf einem Geraet verbindet.",
        },
    },
    "it": {
        "meta_title": "SnapVend Gallery | Galleria QR e consegna locale per fotografi",
        "meta_description": "SnapVend Gallery aiuta i fotografi a gestire galleria QR, trasferimento FTP dalla fotocamera, selezione cliente e consegna ZIP da un solo telefono o tablet.",
        "faq": {
            "q": "Che cos'è SnapVend Gallery?",
            "a": "SnapVend Gallery è un'app mobile per fotografi che unisce gallerie QR, trasferimento FTP dalla fotocamera, selezione cliente, approvazione pagamento locale e consegna ZIP su un solo dispositivo.",
        },
    },
    "pt": {
        "meta_title": "SnapVend Gallery | Galeria QR e entrega local para fotografos",
        "meta_description": "SnapVend Gallery ajuda fotografos a gerenciar galeria QR, transferencia FTP da camera, selecao do cliente e entrega ZIP em um unico telefone ou tablet.",
        "faq": {
            "q": "O que é o SnapVend Gallery?",
            "a": "SnapVend Gallery é um app movel para fotografos que combina galerias QR, transferencia FTP da camera, selecao do cliente, aprovacao de pagamento local e entrega ZIP em um unico dispositivo.",
        },
    },
    "ru": {
        "meta_title": "SnapVend Gallery | QR-галерея и локальная выдача для фотографов",
        "meta_description": "SnapVend Gallery помогает фотографам управлять QR-галереей, FTP-передачей с камеры, выбором клиента и ZIP-выдачей с одного телефона или планшета.",
        "faq": {
            "q": "Что такое SnapVend Gallery?",
            "a": "SnapVend Gallery — мобильное приложение для фотографов, которое объединяет QR-галереи, FTP-передачу с камеры, выбор клиента, локальное подтверждение оплаты и ZIP-выдачу на одном устройстве.",
        },
    },
    "ar": {
        "meta_title": "SnapVend Gallery | معرض QR وتسليم محلي للمصورين",
        "meta_description": "يساعد SnapVend Gallery المصورين على ادارة معرض QR ونقل FTP من الكاميرا واختيار العميل وتسليم ZIP من هاتف او جهاز لوحي واحد.",
        "faq": {
            "q": "ما هو SnapVend Gallery؟",
            "a": "SnapVend Gallery هو تطبيق جوال للمصورين يجمع معرض QR ونقل FTP من الكاميرا واختيار العميل واعتماد الدفع المحلي وتسليم ZIP على جهاز واحد.",
        },
    },
    "hi": {
        "meta_title": "SnapVend Gallery | फोटोग्राफरों के लिए QR गैलरी और लोकल डिलीवरी",
        "meta_description": "SnapVend Gallery फोटोग्राफरों को एक ही फोन या टैबलेट से QR गैलरी, FTP कैमरा ट्रांसफर, ग्राहक चयन और ZIP डिलीवरी प्रबंधित करने में मदद करता है।",
        "faq": {
            "q": "SnapVend Gallery क्या है?",
            "a": "SnapVend Gallery फोटोग्राफरों के लिए मोबाइल ऐप है, जो QR गैलरी, FTP कैमरा ट्रांसफर, ग्राहक चयन, लोकल भुगतान स्वीकृति और ZIP डिलीवरी को एक ही डिवाइस में जोड़ता है।",
        },
    },
    "ja": {
        "meta_title": "SnapVend Gallery | 写真家向けQRギャラリーとローカル納品",
        "meta_description": "SnapVend Gallery は、QR ギャラリー、FTP カメラ転送、顧客の選択、ZIP 納品を1台のスマホやタブレットで管理できる写真家向けアプリです。",
        "faq": {
            "q": "SnapVend Gallery とは何ですか？",
            "a": "SnapVend Gallery は、QR ギャラリー、FTP カメラ転送、顧客選択、ローカル決済確認、ZIP 納品を1台の端末でまとめる写真家向けモバイルアプリです。",
        },
    },
    "zh": {
        "meta_title": "SnapVend Gallery | 面向摄影团队的 QR 画廊与本地交付",
        "meta_description": "SnapVend Gallery 帮助摄影团队在一台手机或平板上管理 QR 画廊、相机 FTP 传输、客户选片与 ZIP 交付。",
        "faq": {
            "q": "SnapVend Gallery 是什么？",
            "a": "SnapVend Gallery 是一款面向摄影师的移动应用，把 QR 画廊、相机 FTP 传输、客户选片、本地支付确认和 ZIP 交付整合到一台设备中。",
        },
    },
}

for locale_code, values in BRAND_SEARCH_SIGNAL_BY_LOCALE.items():
    COPY[locale_code]["meta_title"] = values["meta_title"]
    COPY[locale_code]["meta_description"] = values["meta_description"]
    FAQ_SECTION[locale_code]["items"].insert(0, values["faq"])

for locale_code, overrides in PRINT_QUEUE_OVERRIDES.items():
    COPY[locale_code]["audience_cards"][0]["body"] = overrides["audience_body"]
    PROOF_SECTION[locale_code]["use_cases"].insert(1, overrides["use_case"])
    PROOF_SECTION[locale_code]["references"].insert(0, overrides["reference"])
    FAQ_SECTION[locale_code]["items"].insert(-1, overrides["faq"])

YEARLY_PROMO_FEATURE_BY_LOCALE = {
    "tr": "Yıllık Pro plan, 12 aylık kullanımda toplam maliyeti daha verimli yönetmenizi sağlar.",
    "en": "Annual Pro plan helps you optimize total cost across a full 12-month operating cycle.",
    "es": "El plan Pro anual te permite optimizar el costo total durante un ciclo operativo completo de 12 meses.",
    "fr": "Le plan Pro annuel vous permet d'optimiser le coût total sur un cycle opérationnel complet de 12 mois.",
    "de": "Der jährliche Pro-Plan hilft dabei, die Gesamtkosten über einen vollständigen 12-Monats-Betriebszyklus zu optimieren.",
    "it": "Il piano Pro annuale consente di ottimizzare il costo totale lungo un ciclo operativo completo di 12 mesi.",
    "pt": "O plano Pro anual ajuda a otimizar o custo total em um ciclo operacional completo de 12 meses.",
    "ru": "Годовой тариф Pro помогает оптимизировать совокупные затраты на полном 12-месячном операционном цикле.",
    "ar": "تساعدك باقة Pro السنوية على تحسين التكلفة الإجمالية عبر دورة تشغيل كاملة لمدة 12 شهرا.",
    "hi": "वार्षिक Pro प्लान 12 महीने के पूर्ण संचालन चक्र में कुल लागत को अधिक कुशल तरीके से प्रबंधित करने में मदद करता है।",
    "ja": "年間Proプランは、12か月の運用サイクル全体で総コストの最適化を支援します。",
    "zh": "年度 Pro 方案可帮助你在完整 12 个月运营周期内优化总体成本。",
}

for locale_code, promo_text in YEARLY_PROMO_FEATURE_BY_LOCALE.items():
    COPY[locale_code]["yearly_features"].insert(0, promo_text)

def localized_language_name(display_locale: str, language_code: str) -> str:
    locale_names = LOCALIZED_LANGUAGE_NAMES.get(display_locale, {})
    return locale_names.get(language_code, LOCALE_META[language_code]["native"])


def localized_supported_language_names(display_locale: str) -> str:
    return ", ".join(localized_language_name(display_locale, code) for code in LOCALE_ORDER)

for locale_code, values in LANGUAGE_SUPPORT_FAQ.items():
    FAQ_SECTION[locale_code]["items"].insert(
        -1,
        {
            "q": values["q"],
            "a": f'{values["a_intro"]} {localized_supported_language_names(locale_code)}',
        },
    )

LICENSE_CONTENT_OVERRIDES = {
    "tr": {
        "pricing_note": "Lisanslar plan ve dönem bazlıdır. Pro özellikleri aboneliğiniz aktif kaldığı sürece çalışır; ek cihaz veya ekip lisansı için bizimle iletişime geçebilirsiniz.",
        "why_card": {
            "title": "Lisans görünürlüğü saha akışını korur",
            "body": "Plan seviyesi ve erişim hakları uygulama içinde net görünür. Böylece çekim sırasında hangi özelliklerin açık olduğu ekip tarafından karışmadan yönetilir.",
        },
        "faq": {
            "q": "Lisans yapısı nasıl çalışır?",
            "a": "SnapVend lisansları plan bazlıdır. Ücretsiz plan temel akışı sunar; Pro planlar abonelik süresi boyunca gelişmiş teslim, marka ve operasyon özelliklerini açar. Ek cihaz veya ekip lisansı için bize yazabilirsiniz.",
        },
    },
    "en": {
        "pricing_note": "Licensing is plan and term based. Pro capabilities stay active while your subscription is active; contact us for additional device or team licensing.",
        "why_card": {
            "title": "Visible licensing keeps field work predictable",
            "body": "Your plan tier and access rights stay clear inside the app, so teams can see exactly which features are active during live shoots.",
        },
        "faq": {
            "q": "How does licensing work?",
            "a": "SnapVend licensing is plan based. The free plan covers the core workflow, while Pro plans unlock advanced delivery, branding and operational controls during the active subscription period. Contact us for extra device or team licensing.",
        },
    },
    "es": {
        "pricing_note": "La licencia se gestiona por plan y periodo. Las funciones Pro permanecen activas mientras la suscripcion este activa; para mas dispositivos o licencias de equipo, contactenos.",
        "why_card": {
            "title": "La licencia visible evita sorpresas en campo",
            "body": "El nivel del plan y los permisos se ven claramente dentro de la aplicacion, para que el equipo sepa que funciones estan activas durante la sesion.",
        },
        "faq": {
            "q": "¿Como funciona la licencia?",
            "a": "La licencia de SnapVend es por plan. El plan gratuito cubre el flujo basico y los planes profesionales abren entrega avanzada, marca y controles operativos durante la suscripcion activa. Escribanos para licencias de equipo o dispositivos adicionales.",
        },
    },
    "fr": {
        "pricing_note": "La licence est geree par plan et par periode. Les fonctions Pro restent actives tant que l abonnement est actif. Contactez nous pour des licences equipe ou appareils supplementaires.",
        "why_card": {
            "title": "Une licence visible evite les surprises terrain",
            "body": "Le niveau de plan et les droits d acces restent visibles dans l application pour que l equipe sache clairement quelles fonctions sont actives pendant la prestation.",
        },
        "faq": {
            "q": "Comment fonctionne la licence ?",
            "a": "La licence SnapVend fonctionne par plan. Le plan gratuit couvre le flux principal, et les plans professionnels ouvrent les fonctions avancees de livraison, branding et pilotage pendant la periode d abonnement active. Contactez nous pour des licences equipe ou appareils supplementaires.",
        },
    },
    "de": {
        "pricing_note": "Die Lizenzierung ist plan- und laufzeitbasiert. Pro-Funktionen bleiben aktiv, solange das Abonnement aktiv ist. Fuer zusaetzliche Geraete- oder Teamlizenzen kontaktieren Sie uns.",
        "why_card": {
            "title": "Sichtbare Lizenzen halten den Einsatz planbar",
            "body": "Planstufe und Zugriffsrechte sind in der App klar sichtbar, sodass Teams bei Live-Shootings sofort sehen, welche Funktionen aktiv sind.",
        },
        "faq": {
            "q": "Wie funktioniert die Lizenzierung?",
            "a": "Die SnapVend-Lizenzierung ist planbasiert. Der Gratisplan deckt den Kernablauf ab, und die Profi-Plaene schalten erweiterte Lieferung, Branding und operative Steuerung fuer die aktive Abolaufzeit frei. Fuer Team- oder Zusatzgeraete-Lizenzen koennen Sie uns direkt schreiben.",
        },
    },
    "it": {
        "pricing_note": "La licenza e basata su piano e periodo. Le funzioni professionali restano attive finche l'abbonamento e attivo; per licenze team o dispositivi aggiuntivi contattaci.",
        "why_card": {
            "title": "Licenza visibile, flusso sul campo piu chiaro",
            "body": "Livello del piano e diritti di accesso restano visibili nell'app, cosi il team sa sempre quali funzioni sono attive durante il servizio.",
        },
        "faq": {
            "q": "Come funziona la licenza?",
            "a": "La licenza SnapVend e basata sul piano. Il piano gratuito copre il flusso principale, mentre i piani professionali sbloccano consegna avanzata, branding e controlli operativi per tutta la durata dell'abbonamento attivo. Scrivici per licenze team o dispositivi aggiuntivi.",
        },
    },
    "pt": {
        "pricing_note": "O licenciamento e baseado em plano e periodo. Os recursos profissionais ficam ativos enquanto a assinatura estiver ativa; para licencas de equipe ou dispositivos extras, fale conosco.",
        "why_card": {
            "title": "Licenca visivel traz previsibilidade no campo",
            "body": "O nivel do plano e as permissoes aparecem com clareza no app, para que a equipe saiba quais recursos estao ativos durante o trabalho ao vivo.",
        },
        "faq": {
            "q": "Como funciona o licenciamento?",
            "a": "O licenciamento do SnapVend e baseado em plano. O plano gratuito cobre o fluxo principal e os planos profissionais liberam entrega avancada, branding e controles operacionais durante a assinatura ativa. Fale conosco para licencas de equipe ou dispositivos extras.",
        },
    },
    "ru": {
        "pricing_note": "Лицензирование зависит от плана и периода. Функции Pro активны, пока активна подписка. Для дополнительных устройств или командной лицензии свяжитесь с нами.",
        "why_card": {
            "title": "Видимая лицензия делает работу предсказуемой",
            "body": "Уровень плана и права доступа остаются понятными внутри приложения, поэтому команда видит, какие функции активны прямо во время съемки.",
        },
        "faq": {
            "q": "Как работает лицензирование?",
            "a": "Лицензирование SnapVend построено по планам. Бесплатный план покрывает базовый процесс, а профессиональные планы открывают расширенную выдачу, брендинг и операционные инструменты на время активной подписки. Для дополнительных устройств или командной лицензии напишите нам.",
        },
    },
    "ar": {
        "pricing_note": "الترخيص مبني على الخطة والفترة. تبقى ميزات Pro فعالة ما دامت الاشتراك نشطا. للتراخيص الاضافية للاجهزة او للفرق تواصل معنا.",
        "why_card": {
            "title": "وضوح الترخيص يحافظ على استقرار العمل الميداني",
            "body": "مستوى الخطة وصلاحيات الوصول تبقى واضحة داخل التطبيق، لذلك يعرف الفريق الميزات الفعالة اثناء التصوير المباشر.",
        },
        "faq": {
            "q": "كيف يعمل الترخيص؟",
            "a": "ترخيص SnapVend يعتمد على الخطة. الخطة المجانية تغطي التدفق الاساسي، والخطط الاحترافية تفتح التسليم المتقدم والهوية التجارية والتحكم التشغيلي طوال فترة الاشتراك النشط. ولتراخيص الفريق او الاجهزة الاضافية يمكنكم مراسلتنا.",
        },
    },
    "hi": {
        "pricing_note": "लाइसेंस प्लान और अवधि के आधार पर काम करता है। प्रो सुविधाएं आपकी सदस्यता सक्रिय रहने तक उपलब्ध रहती हैं; अतिरिक्त डिवाइस या टीम लाइसेंस के लिए हमसे संपर्क करें।",
        "why_card": {
            "title": "लाइसेंस की स्पष्टता मैदानी प्रवाह को स्थिर रखती है",
            "body": "योजना स्तर और प्रवेश अधिकार ऐप के अंदर साफ दिखाई देते हैं, ताकि लाइव शूट के दौरान टीम तुरंत समझ सके कि कौन-सी सुविधाएं सक्रिय हैं।",
        },
        "faq": {
            "q": "लाइसेंसिंग कैसे काम करती है?",
            "a": "SnapVend लाइसेंसिंग योजना आधारित है। मुफ्त योजना मुख्य कार्यप्रवाह देती है, जबकि प्रो योजना सक्रिय सदस्यता अवधि में उन्नत डिलीवरी, ब्रांडिंग और संचालन नियंत्रण खोलती है। अतिरिक्त डिवाइस या टीम लाइसेंस के लिए हमें लिखें।",
        },
    },
    "ja": {
        "pricing_note": "ライセンスはプランと期間に基づいて管理されます。Pro 機能はサブスクリプションが有効な間は利用できます。追加端末やチームライセンスはお問い合わせください。",
        "why_card": {
            "title": "ライセンス可視化で現場運用が安定",
            "body": "プランレベルと権限がアプリ内で明確に見えるため、ライブ撮影中でもチームが有効機能を把握しやすくなります。",
        },
        "faq": {
            "q": "ライセンスはどのように機能しますか？",
            "a": "SnapVend のライセンスはプランベースです。無料プランは基本フローを提供し、Pro プランは契約期間中に高度な納品・ブランディング・運用機能を開放します。追加端末やチームライセンスはお問い合わせください。",
        },
    },
    "zh": {
        "pricing_note": "授权按方案与周期管理。专业版功能会在订阅有效期内保持可用；如需额外设备或团队授权，请联系我们。",
        "why_card": {
            "title": "授权状态可见，现场流程更稳",
            "body": "方案等级与访问权限在应用内清晰可见，团队在拍摄现场也能快速确认当前可用功能。",
        },
        "faq": {
            "q": "授权机制如何工作？",
            "a": "SnapVend 采用按方案授权。免费方案覆盖核心流程，专业版方案会在订阅有效期内开启高级交付、品牌与运营能力。若需额外设备或团队授权，可直接联系我们。",
        },
    },
}

for locale_code, values in LICENSE_CONTENT_OVERRIDES.items():
    COPY[locale_code]["pricing_license_note"] = values["pricing_note"]
    WHY_SNAPVEND_SECTION[locale_code]["cards"].append(values["why_card"])
    FAQ_SECTION[locale_code]["items"].insert(-1, values["faq"])

BRAND_MOTTO_BY_LOCALE = {
    "tr": "Çek - Göster - Sat",
    "en": "Shoot - Show - Sell",
    "es": "Captura - Muestra - Vende",
    "fr": "Capture - Montre - Vends",
    "de": "Aufnehmen - Zeigen - Verkaufen",
    "it": "Scatta - Mostra - Vendi",
    "pt": "Capture - Mostre - Venda",
    "ru": "Сними - Покажи - Продай",
    "ar": "التقط - اعرض - بع",
    "hi": "शूट - दिखाओ - बेचो",
    "ja": "撮る - 見せる - 売る",
    "zh": "拍摄 - 展示 - 销售",
}

BRAND_KICKER_BY_LOCALE = {
    "tr": "Profesyonel Fotoğraf Teslimi",
    "es": "Entrega fotografica profesional",
    "fr": "Livraison photo professionnelle",
    "de": "Professionelle Fotoauslieferung",
    "it": "Consegna fotografica professionale",
    "pt": "Entrega fotografica profissional",
    "ru": "Профессиональная доставка фото",
    "ar": "تسليم صور احترافي",
    "hi": "प्रोफेशनल फोटो डिलीवरी",
    "ja": "プロフェッショナル写真納品",
    "zh": "专业照片交付",
}

APPLICATION_SUBCATEGORY_BY_LOCALE = {
    "tr": "Fotoğraf akışı, baskı yönetimi ve teslim",
    "es": "Flujo fotografico, gestion de impresion y entrega",
    "fr": "Flux photo, gestion des impressions et livraison",
    "de": "Fotoablauf, Druckverwaltung und Auslieferung",
    "it": "Flusso fotografico, gestione della stampa e consegna",
    "pt": "Fluxo fotografico, gestao de impressao e entrega",
    "ru": "Фотопоток, управление печатью и выдача",
    "ar": "تدفق الصور وادارة الطباعة والتسليم",
    "hi": "फोटो वर्कफ़्लो, प्रिंट प्रबंधन और डिलीवरी",
    "ja": "写真ワークフロー、プリント管理、納品",
    "zh": "照片流程、打印管理与交付",
}

LOCALIZED_FLOW_COVERAGE_LABEL_BY_LOCALE = {
    "tr": "Yerellestirilmis musteri akisi kapsami",
    "es": "Cobertura de flujo localizada para clientes",
    "fr": "Couverture du flux client localise",
    "de": "Lokalisierte Kundenfluss-Abdeckung",
    "it": "Copertura del flusso cliente localizzato",
    "pt": "Cobertura de fluxo localizado para clientes",
    "ru": "Локализованное покрытие клиентского потока",
    "ar": "تغطية تدفق العميل المترجم",
    "hi": "स्थानीयकृत ग्राहक फ्लो कवरेज",
    "ja": "ローカライズされた顧客フロー対応",
    "zh": "本地化客户流程覆盖",
}

IMAGE_ALT_BY_LOCALE = {
    "default": {
        "hero_main": "SnapVend home dashboard with live gallery and session overview",
        "hero_secondary": "SnapVend WiFi and hotspot QR connection screen",
        "workflow_ftp": "SnapVend FTP server settings for professional cameras",
        "workflow_dashboard": "SnapVend gallery home dashboard",
        "workflow_qr": "SnapVend QR codes and session access screen",
        "workflow_http_gallery": "SnapVend HTTP gallery with selected photos",
        "workflow_payment": "SnapVend payment approval and delivery options screen",
    },
    "tr": {
        "hero_main": "SnapVend ana ekranı, canlı galeri ve oturum özeti",
        "hero_secondary": "SnapVend WiFi ve erişim noktası QR bağlantı ekranı",
        "workflow_ftp": "SnapVend profesyonel fotoğraf makineleri için FTP sunucu ayarları",
        "workflow_dashboard": "SnapVend galeri ana ekranı",
        "workflow_qr": "SnapVend QR kodları ve oturum erişim ekranı",
        "workflow_http_gallery": "SnapVend seçilmiş fotoğrafların müşteri galerisi",
        "workflow_payment": "SnapVend ödeme onayı ve teslim seçenekleri ekranı",
    },
    "es": {
        "hero_main": "Panel principal de SnapVend con galeria activa y resumen de sesiones",
        "hero_secondary": "Pantalla de conexion QR por WiFi y punto de acceso de SnapVend",
        "workflow_ftp": "Configuracion del servidor FTP de SnapVend para camaras profesionales",
        "workflow_dashboard": "Pantalla principal de galeria en SnapVend",
        "workflow_qr": "Pantalla de codigos QR y acceso por sesion en SnapVend",
        "workflow_http_gallery": "Galeria web de SnapVend con fotos seleccionadas",
        "workflow_payment": "Pantalla de aprobacion de pago y opciones de entrega en SnapVend",
    },
    "fr": {
        "hero_main": "Tableau de bord SnapVend avec galerie active et vue des sessions",
        "hero_secondary": "Ecran de connexion QR WiFi et point d'acces de SnapVend",
        "workflow_ftp": "Parametres du serveur FTP SnapVend pour appareils photo professionnels",
        "workflow_dashboard": "Ecran principal de galerie SnapVend",
        "workflow_qr": "Ecran des QR codes et de l'acces session dans SnapVend",
        "workflow_http_gallery": "Galerie web SnapVend avec photos selectionnees",
        "workflow_payment": "Ecran de validation du paiement et des options de livraison SnapVend",
    },
    "de": {
        "hero_main": "SnapVend Startansicht mit aktiver Galerie und Session-Ubersicht",
        "hero_secondary": "SnapVend Bildschirm fur QR-Verbindung per WiFi und mobilem Zugangspunkt",
        "workflow_ftp": "SnapVend FTP-Servereinstellungen fur Profikameras",
        "workflow_dashboard": "SnapVend Galerie-Startansicht",
        "workflow_qr": "SnapVend Bildschirm fur QR-Codes und Session-Zugang",
        "workflow_http_gallery": "SnapVend Browser-Galerie mit ausgewaehlten Fotos",
        "workflow_payment": "SnapVend Bildschirm fur Zahlungsfreigabe und Lieferoptionen",
    },
    "it": {
        "hero_main": "Dashboard principale di SnapVend con galleria attiva e riepilogo sessioni",
        "hero_secondary": "Schermata di connessione QR WiFi e punto di accesso di SnapVend",
        "workflow_ftp": "Impostazioni del server FTP di SnapVend per fotocamere professionali",
        "workflow_dashboard": "Schermata principale della galleria SnapVend",
        "workflow_qr": "Schermata dei codici QR e dell'accesso sessione in SnapVend",
        "workflow_http_gallery": "Galleria web SnapVend con foto selezionate",
        "workflow_payment": "Schermata SnapVend con conferma pagamento e opzioni di consegna",
    },
    "pt": {
        "hero_main": "Painel principal do SnapVend com galeria ativa e resumo de sessoes",
        "hero_secondary": "Tela de conexao QR por WiFi e ponto de acesso do SnapVend",
        "workflow_ftp": "Configuracoes do servidor FTP do SnapVend para cameras profissionais",
        "workflow_dashboard": "Tela principal da galeria do SnapVend",
        "workflow_qr": "Tela de codigos QR e acesso por sessao no SnapVend",
        "workflow_http_gallery": "Galeria web do SnapVend com fotos selecionadas",
        "workflow_payment": "Tela do SnapVend com aprovacao de pagamento e opcoes de entrega",
    },
    "ru": {
        "hero_main": "Главный экран SnapVend с активной галереей и обзором сессий",
        "hero_secondary": "Экран QR-подключения SnapVend по WiFi и через точку доступа",
        "workflow_ftp": "Настройки FTP-сервера SnapVend для профессиональных камер",
        "workflow_dashboard": "Главный экран галереи SnapVend",
        "workflow_qr": "Экран QR-кодов и доступа к сессии в SnapVend",
        "workflow_http_gallery": "Веб-галерея SnapVend с выбранными фотографиями",
        "workflow_payment": "Экран подтверждения оплаты и вариантов выдачи в SnapVend",
    },
    "ar": {
        "hero_main": "لوحة SnapVend الرئيسية مع المعرض الحي ونظرة عامة على الجلسات",
        "hero_secondary": "شاشة اتصال QR عبر WiFi ونقطة الاتصال في SnapVend",
        "workflow_ftp": "اعدادات خادم FTP في SnapVend للكاميرات الاحترافية",
        "workflow_dashboard": "الشاشة الرئيسية للمعرض في SnapVend",
        "workflow_qr": "شاشة رموز QR والوصول الى الجلسة في SnapVend",
        "workflow_http_gallery": "معرض SnapVend على الويب مع الصور المختارة",
        "workflow_payment": "شاشة تأكيد الدفع وخيارات التسليم في SnapVend",
    },
    "hi": {
        "hero_main": "लाइव गैलरी और सेशन सारांश के साथ SnapVend मुख्य डैशबोर्ड",
        "hero_secondary": "SnapVend का WiFi और हॉटस्पॉट QR कनेक्शन स्क्रीन",
        "workflow_ftp": "प्रोफेशनल कैमरों के लिए SnapVend FTP सर्वर सेटिंग्स",
        "workflow_dashboard": "SnapVend गैलरी होम स्क्रीन",
        "workflow_qr": "SnapVend का QR कोड और सेशन एक्सेस स्क्रीन",
        "workflow_http_gallery": "चुनी हुई तस्वीरों के साथ SnapVend वेब गैलरी",
        "workflow_payment": "SnapVend भुगतान अनुमोदन और डिलीवरी विकल्प स्क्रीन",
    },
    "ja": {
        "hero_main": "ライブギャラリーとセッション概要を備えた SnapVend のホームダッシュボード",
        "hero_secondary": "SnapVend の WiFi / ホットスポット QR 接続画面",
        "workflow_ftp": "プロ向けカメラ用 SnapVend FTP サーバー設定",
        "workflow_dashboard": "SnapVend のギャラリーホーム画面",
        "workflow_qr": "SnapVend の QR コードとセッションアクセス画面",
        "workflow_http_gallery": "選択済み写真を表示する SnapVend の Web ギャラリー",
        "workflow_payment": "SnapVend の支払い承認と納品オプション画面",
    },
    "zh": {
        "hero_main": "SnapVend 首页仪表盘与会话总览",
        "hero_secondary": "SnapVend WiFi 与热点二维码连接界面",
        "workflow_ftp": "SnapVend 专业相机 FTP 服务器设置",
        "workflow_dashboard": "SnapVend 应用画廊首页",
        "workflow_qr": "SnapVend 二维码与会话访问界面",
        "workflow_http_gallery": "SnapVend 客户已选照片画廊",
        "workflow_payment": "SnapVend 支付确认与交付选项界面",
    },
}

MARKETING_ASSETS = {
    "hero_main": "assets/marketing/google_play/web/01_gallery_dashboard_hero.jpg",
    "hero_secondary": "assets/marketing/google_play/web/02_session_qr_access_hero.png",
    "workflow_ftp": "assets/marketing/google_play/web/05_ftp_server_settings_web.png",
    "workflow_dashboard": "assets/marketing/google_play/web/01_gallery_dashboard_web.png",
    "workflow_qr": "assets/marketing/google_play/web/03_browser_gallery_selection_web.png",
    "workflow_http_gallery": "assets/marketing/google_play/web/06_customer_gallery_selection_en_web.png",
    "workflow_payment": "assets/marketing/google_play/web/04_payment_approval_flow_web.png",
    "schema_report": "assets/marketing/google_play/web/07_reports_dashboard_web.png",
}

LOCALE_MARKETING_ASSET_OVERRIDES = {
    "tr": {
        "workflow_http_gallery": "assets/marketing/google_play/web/06_customer_gallery_selection_tr_web.png",
    },
}

for locale_code in LOCALE_ORDER:
    COPY[locale_code]["brand_motto"] = BRAND_MOTTO_BY_LOCALE[locale_code]


def e(value: str) -> str:
    return html.escape(value, quote=True)


def marketing_asset(slot: str, locale_code: str | None = None) -> str:
    if locale_code is not None:
        locale_overrides = LOCALE_MARKETING_ASSET_OVERRIDES.get(locale_code, {})
        if slot in locale_overrides:
            return locale_overrides[slot]
    return MARKETING_ASSETS[slot]


def image_alt(locale_code: str, slot: str) -> str:
    locale_map = IMAGE_ALT_BY_LOCALE.get(locale_code, {})
    return locale_map.get(slot, IMAGE_ALT_BY_LOCALE["default"][slot])


def page_path(locale_code: str) -> str:
    locale = LOCALE_META[locale_code]
    return "/" if locale["path"] == "" else f"/{locale['path']}/"


def canonical_url(locale_code: str) -> str:
    return f"{SITE_URL}{page_path(locale_code)}"


def asset_prefix(locale_code: str) -> str:
    return "." if LOCALE_META[locale_code]["path"] == "" else ".."


def relative_page_href(current_code: str, target_code: str) -> str:
    current_path = LOCALE_META[current_code]["path"]
    target_path = LOCALE_META[target_code]["path"]

    if current_code == target_code:
        return "./index.html"

    if current_path == "":
        return "./index.html" if target_path == "" else f"./{target_path}/index.html"

    if target_path == "":
        return "../index.html"

    return f"../{target_path}/index.html"


def flag_asset(country_code: str, prefix: str) -> str:
    if len(country_code) != 2:
        return ""
    return f'{prefix}/assets/flags/{country_code.lower()}.svg'


def flag_markup(country_code: str, prefix: str, class_name: str = "language-flag") -> str:
    src = flag_asset(country_code, prefix)
    if not src:
        return ""
    return f'<span class="{class_name}" aria-hidden="true"><img src="{src}" alt="" loading="lazy" decoding="async"></span>'


def build_alternates(current_code: str) -> str:
    links = [
        f'    <link rel="alternate" hreflang="x-default" href="{SITE_URL}/">\n'
    ]
    for locale_code in LOCALE_ORDER:
        target_url = canonical_url(locale_code)
        for hreflang in LOCALE_META[locale_code]["hreflang"]:
            links.append(
                f'    <link rel="alternate" hreflang="{hreflang}" href="{target_url}">\n'
            )
    return "".join(links)


def build_language_menu(current_code: str) -> str:
    items = []
    prefix = asset_prefix(current_code)
    for locale_code in LOCALE_ORDER:
        meta = LOCALE_META[locale_code]
        active = " language-option-active" if locale_code == current_code else ""
        flag = flag_markup(meta["app_store_country"], prefix)
        display_name = localized_language_name(current_code, locale_code)
        items.append(
            f'              <a class="language-option{active}" href="{relative_page_href(current_code, locale_code)}" lang="{locale_code}" hreflang="{meta["hreflang"][0]}">{flag}<span class="language-name">{e(display_name)}</span></a>'
        )
    return "\n".join(items)


def build_metric_cards(copy: dict) -> str:
    cards = []
    for metric in copy["metrics"]:
        cards.append(
            f"""            <article class="metric-card reveal">
              <span class="metric-value">{e(metric["value"])}</span>
              <span class="metric-label">{e(metric["label"])}</span>
            </article>"""
        )
    return "\n".join(cards)


def build_workflow_cards(copy: dict) -> str:
    cards = []
    for index, card in enumerate(copy["workflow_cards"], start=1):
        cards.append(
            f"""              <li class="workflow-card reveal">
                <span class="step-index">{index:02d}</span>
                <h3>{e(card["title"])}</h3>
                <p>{e(card["body"])}</p>
              </li>"""
        )
    return "\n".join(cards)


def build_audience_cards(copy: dict) -> str:
    cards = []
    for card in copy["audience_cards"]:
        cards.append(
            f"""            <article class="audience-card reveal">
              <h3>{e(card["title"])}</h3>
              <p>{e(card["body"])}</p>
            </article>"""
        )
    return "\n".join(cards)


def build_language_support_cards(section: dict) -> str:
    icons = [
        """<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.75a9.25 9.25 0 1 0 0 18.5 9.25 9.25 0 0 0 0-18.5Zm5.87 7.75h-3.04a15.3 15.3 0 0 0-1.08-4.2 7.79 7.79 0 0 1 4.12 4.2ZM12 4.21c.73.96 1.37 2.45 1.73 4.29h-3.46C10.63 6.66 11.27 5.17 12 4.21Zm-1.48.09A15.3 15.3 0 0 0 9.43 8.5H6.39a7.79 7.79 0 0 1 4.13-4.2ZM5.92 12c0-.52.06-1.02.17-1.5h3.13c-.07.49-.11.99-.11 1.5 0 .51.04 1.01.11 1.5H6.09A7.9 7.9 0 0 1 5.92 12Zm.47 3.5h3.04c.22 1.5.61 2.88 1.09 4.2a7.79 7.79 0 0 1-4.13-4.2Zm5.61 4.29c-.73-.96-1.37-2.45-1.73-4.29h3.46c-.36 1.84-1 3.33-1.73 4.29Zm2.21-.09c.48-1.32.87-2.7 1.09-4.2h3.04a7.79 7.79 0 0 1-4.13 4.2Zm1.39-6.2c.07-.49.11-.99.11-1.5 0-.51-.04-1.01-.11-1.5h3.13c.11.48.17.98.17 1.5 0 .52-.06 1.02-.17 1.5H15.6Z" fill="currentColor"/></svg>""",
        """<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.75 4.75A2.75 2.75 0 0 0 4 7.5v9A2.75 2.75 0 0 0 6.75 19.25h10.5A2.75 2.75 0 0 0 20 16.5v-9a2.75 2.75 0 0 0-2.75-2.75H6.75Zm0 1.5h10.5c.69 0 1.25.56 1.25 1.25v5.32l-2.43-2.43a1.75 1.75 0 0 0-2.48 0l-1.22 1.22-2.02-2.02a1.75 1.75 0 0 0-2.48 0L5.5 11.96V7.5c0-.69.56-1.25 1.25-1.25Zm9.75 11.5H6.75c-.69 0-1.25-.56-1.25-1.25v-2.42l3.43-3.43a.25.25 0 0 1 .35 0l2.55 2.55c.29.29.77.29 1.06 0l1.75-1.75a.25.25 0 0 1 .35 0l3.51 3.51v1.54c0 .69-.56 1.25-1.25 1.25ZM8.75 8.5a1.25 1.25 0 1 0 0 2.5 1.25 1.25 0 0 0 0-2.5Z" fill="currentColor"/></svg>""",
        """<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.75c-2.02 1.65-4.62 2.5-7.25 2.5-.41 0-.75.34-.75.75v4.93c0 4.73 2.88 8.99 7.27 10.77.18.07.38.07.56 0C16.22 19.92 19 15.66 19 10.93V6c0-.41-.34-.75-.75-.75-2.63 0-5.23-.85-7.25-2.5Zm-5.5 4c2.03-.12 4-.71 5.5-1.68 1.5.97 3.47 1.56 5.5 1.68v4.18c0 3.98-2.31 7.57-5.5 9.25-3.2-1.68-5.5-5.27-5.5-9.25V6.75Zm8.3 2.96a.75.75 0 0 1 0 1.06l-3.47 3.47a.75.75 0 0 1-1.06 0L9 12.97a.75.75 0 1 1 1.06-1.06l.74.74 2.94-2.94a.75.75 0 0 1 1.06 0Z" fill="currentColor"/></svg>""",
    ]
    cards = []
    for index, card in enumerate(section["cards"]):
        cards.append(
            f"""              <article class="language-support-card reveal">
                <div class="language-support-card-head">
                  <span class="language-support-icon" aria-hidden="true">{icons[index % len(icons)]}</span>
                  <h3>{e(card["title"])}</h3>
                </div>
                <p>{e(card["body"])}</p>
              </article>"""
        )
    return "\n".join(cards)


def build_language_support_badges(display_locale: str) -> str:
    badges = []
    prefix = asset_prefix(display_locale)
    for locale_code in LOCALE_ORDER:
        flag = flag_markup(LOCALE_META[locale_code]["app_store_country"], prefix, "language-support-badge-flag")
        badges.append(
            f'                <span class="language-support-badge">{flag}<span class="language-support-badge-name">{e(localized_language_name(display_locale, locale_code))}</span></span>'
        )
    return "\n".join(badges)


def build_why_snapvend_cards(section: dict) -> str:
    icons = [
        """<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.25a8.75 8.75 0 0 0-8.75 8.75c0 4.83 3.92 8.75 8.75 8.75s8.75-3.92 8.75-8.75S16.83 3.25 12 3.25Zm0 1.5c3.28 0 6 2.4 6.52 5.53h-3.02A17.9 17.9 0 0 0 13 5.01c-.32-.09-.66-.17-1-.26Zm-1.99.48c.35.08.69.16 1.02.27A16.32 16.32 0 0 1 8.54 10.28H5.48a7.27 7.27 0 0 1 4.53-5.05Zm-4.53 6.55h2.75c-.03.4-.05.8-.05 1.22 0 .56.03 1.1.09 1.63H5.63A7.18 7.18 0 0 1 5.48 11.78Zm.76 4.35h2.27c.39 1.45.98 2.77 1.74 3.88a7.28 7.28 0 0 1-4.01-3.88Zm5.76 3.07c-.77-.94-1.41-2.18-1.84-3.57h3.68c-.43 1.39-1.07 2.63-1.84 3.57Zm2.24.81a10.71 10.71 0 0 0 1.74-3.88h2.27a7.28 7.28 0 0 1-4.01 3.88Zm2.11-5.38c.06-.53.09-1.07.09-1.63 0-.42-.02-.82-.05-1.22h2.75a7.18 7.18 0 0 1-.15 3.85h-2.64Z" fill="currentColor"/></svg>""",
        """<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.75 4.75A2.75 2.75 0 0 0 4 7.5v7.25a2.75 2.75 0 0 0 2.75 2.75H9v2.05c0 .66.78 1.02 1.29.59L13.56 17.5h3.69A2.75 2.75 0 0 0 20 14.75V7.5a2.75 2.75 0 0 0-2.75-2.75H6.75Zm0 1.5h10.5c.69 0 1.25.56 1.25 1.25v7.25c0 .69-.56 1.25-1.25 1.25h-3.95a.75.75 0 0 0-.48.17L10.5 18.1v-1.35a.75.75 0 0 0-.75-.75H6.75c-.69 0-1.25-.56-1.25-1.25V7.5c0-.69.56-1.25 1.25-1.25Zm1.5 2.5a.75.75 0 0 0 0 1.5h7.5a.75.75 0 1 0 0-1.5h-7.5Zm0 3a.75.75 0 0 0 0 1.5h4.25a.75.75 0 1 0 0-1.5H8.25Z" fill="currentColor"/></svg>""",
        """<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.25a4.25 4.25 0 0 0-4.25 4.25v1H6.5A2.5 2.5 0 0 0 4 11v6.5A2.5 2.5 0 0 0 6.5 20h11a2.5 2.5 0 0 0 2.5-2.5V11a2.5 2.5 0 0 0-2.5-2.5h-1.25v-1A4.25 4.25 0 0 0 12 3.25Zm-2.75 5.25v-1a2.75 2.75 0 1 1 5.5 0v1h-5.5Zm-2.75 1.5h11c.55 0 1 .45 1 1v6.5c0 .55-.45 1-1 1h-11c-.55 0-1-.45-1-1V11c0-.55.45-1 1-1Zm5.5 1.75A2.25 2.25 0 0 0 9.75 14c0 .84.46 1.57 1.15 1.96v1.04a1.1 1.1 0 1 0 2.2 0v-1.04A2.25 2.25 0 0 0 14.25 14 2.25 2.25 0 0 0 12 11.75Z" fill="currentColor"/></svg>""",
        """<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.75 3.75A2.75 2.75 0 0 0 4 6.5v11A2.75 2.75 0 0 0 6.75 20.25h10.5A2.75 2.75 0 0 0 20 17.5v-11a2.75 2.75 0 0 0-2.75-2.75H6.75Zm0 1.5h10.5c.69 0 1.25.56 1.25 1.25v11c0 .69-.56 1.25-1.25 1.25H6.75c-.69 0-1.25-.56-1.25-1.25v-11c0-.69.56-1.25 1.25-1.25Zm6.73 3.03a.75.75 0 0 0-1.06 0L10 10.69l-.94-.94A.75.75 0 1 0 8 10.81l1.47 1.47a.75.75 0 0 0 1.06 0l2.95-2.94a.75.75 0 0 0 0-1.06Zm-4.73 5.22a.75.75 0 0 0 0 1.5h6.5a.75.75 0 1 0 0-1.5h-6.5Z" fill="currentColor"/></svg>""",
    ]
    cards = []
    for index, card in enumerate(section["cards"]):
        cards.append(
            f"""              <article class="why-snapvend-card reveal">
                <div class="why-snapvend-card-head">
                  <span class="why-snapvend-icon" aria-hidden="true">{icons[index % len(icons)]}</span>
                  <h3>{e(card["title"])}</h3>
                </div>
                <p>{e(card["body"])}</p>
              </article>"""
        )
    return "\n".join(cards)


def build_why_snapvend_points(section: dict) -> str:
    return "\n".join(f"                <li>{e(point)}</li>" for point in section["panel_points"])


def build_proof_cards(items: list[dict]) -> str:
    cards = []
    for card in items:
        cards.append(
            f"""              <article class="proof-card reveal">
                <h3>{e(card["title"])}</h3>
                <p>{e(card["body"])}</p>
              </article>"""
        )
    return "\n".join(cards)


def build_feature_list(features: list[str]) -> str:
    return "\n".join(f"                <li>{e(feature)}</li>" for feature in features)


def build_demo_steps(demo: dict) -> str:
    steps = []
    for index, step in enumerate(demo["steps"], start=1):
        steps.append(
            f"""            <article class="demo-step reveal">
              <span class="demo-step-index">{index:02d}</span>
              <div>
                <h3>{e(step["title"])}</h3>
                <p>{e(step["body"])}</p>
              </div>
            </article>"""
        )
    return "\n".join(steps)


def build_faq_items(faq: dict) -> str:
    items = []
    for index, item in enumerate(faq["items"]):
        open_attr = " open" if index == 0 else ""
        items.append(
            f"""            <details class="faq-item reveal"{open_attr}>
              <summary>{e(item["q"])}</summary>
              <p>{e(item["a"])}</p>
            </details>"""
        )
    return "\n".join(items)


def build_contact_highlights(contact: dict) -> str:
    return "\n".join(
        f"""              <article class="contact-point reveal">
                <span>{e(item)}</span>
              </article>"""
        for item in contact["highlights"]
    )


def build_contact_topics(contact: dict) -> str:
    return "\n".join(f'                    <option value="{e(item)}">{e(item)}</option>' for item in contact["topics"])


def unique_strings(items: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        value = item.strip()
        if value and value not in seen:
            seen.add(value)
            ordered.append(value)
    return ordered


def build_field_operation_cards(section: dict) -> str:
    cards = []
    for index, card in enumerate(section["cards"], start=1):
        cards.append(
            f"""              <article class="field-operation-card reveal">
                <span class="field-operation-index">{index:02d}</span>
                <div>
                  <h3>{e(card["title"])}</h3>
                  <p>{e(card["body"])}</p>
                </div>
              </article>"""
        )
    return "\n".join(cards)


def build_field_operation_points(section: dict) -> str:
    return "\n".join(f"                <li>{e(point)}</li>" for point in section["license_points"])


def build_keyword_string(
    locale_code: str,
    copy: dict,
    proof: dict,
    contact: dict,
    language_support: dict,
    why_snapvend: dict,
    field_operations: dict,
) -> str:
    values = [
        PRODUCT_NAME,
        PRODUCT_SHORT_NAME,
        "snapvendgallery.com",
        *SEO_KEYWORD_SEEDS_BY_LOCALE.get(locale_code, SEO_KEYWORD_SEEDS_BY_LOCALE["en"]),
        copy["brand_motto"],
        copy["hero_eyebrow"],
        copy["workflow_title"],
        why_snapvend["title"],
        copy["audience_title"],
        proof["title"],
        contact["title"],
        language_support["title"],
        field_operations["title"],
        field_operations["license_title"],
        *[card["title"] for card in copy["workflow_cards"]],
        *[card["title"] for card in why_snapvend["cards"]],
        *[card["title"] for card in field_operations["cards"]],
        *[card["title"] for card in copy["audience_cards"]],
        *[card["title"] for card in language_support["cards"]],
        *[card["title"] for card in proof["use_cases"]],
        *[card["title"] for card in proof["references"]],
        *copy["monthly_features"],
        *copy["yearly_features"],
        *why_snapvend["panel_points"],
        *field_operations["license_points"],
        *contact["topics"],
    ]
    return ", ".join(unique_strings(values))


def build_item_list_schema(page_url: str, fragment: str, name: str, items: list[dict]) -> dict:
    return {
        "@type": "ItemList",
        "@id": f"{page_url}#{fragment}",
        "url": f"{page_url}#{fragment}",
        "name": name,
        "numberOfItems": len(items),
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": index,
                "item": {
                    "@type": "Thing",
                    "name": item["title"],
                    "description": item["body"],
                },
            }
            for index, item in enumerate(items, start=1)
        ],
    }


def build_defined_term_set_schema(page_url: str, fragment: str, name: str, terms: list[str]) -> dict:
    return {
        "@type": "DefinedTermSet",
        "@id": f"{page_url}#{fragment}",
        "url": f"{page_url}#{fragment}",
        "name": name,
        "hasDefinedTerm": [{"@type": "DefinedTerm", "name": term} for term in terms],
    }


def store_badges(locale_code: str, copy: dict) -> str:
    app_store_status = APP_STORE_STATUS[locale_code]
    qr_copy = DOWNLOAD_QR_COPY[locale_code]
    prefix = asset_prefix(locale_code)
    localized_download_url = f"{DOWNLOAD_URL}?lang={locale_code}"
    app_store_label = f'{copy["apple_small"]} App Store. {app_store_status["note"]}'
    qr_label = f'{qr_copy["title"]}. {qr_copy["body"]} {qr_copy["hint"]}'
    return f"""
            <div class="download-options">
            <div class="store-badges">
              <a class="store-badge store-badge-play" data-store-link="googlePlay" href="{GOOGLE_PLAY_URL}" target="_blank" rel="noreferrer">
                <span class="store-logo" aria-hidden="true">
                  <svg viewBox="0 0 48 48" role="img">
                    <path fill="#00d26a" d="M8 6.8 29.2 24 8 41.2z"></path>
                    <path fill="#00a3ff" d="m29.2 24 5.6-4.8c2.4 1.7 2.4 7 0 8.7z"></path>
                    <path fill="#ffd400" d="M8 6.8 20.1 18l9.1 6-9.1 6L8 41.2 14.5 24z"></path>
                    <path fill="#ff5a5f" d="M8 6.8 20.1 18l14.7 1.2z"></path>
                  </svg>
                </span>
                <span class="store-copy">
                  <small>{e(copy["google_small"])}</small>
                  <strong>Google Play</strong>
                </span>
              </a>

              <a class="store-badge store-badge-apple" data-store-link="appStore" data-app-store-alert="{e(app_store_status["note"])}" href="#" aria-label="{e(app_store_label)}">
                <span class="store-logo" aria-hidden="true">
                  <svg viewBox="0 0 48 48" role="img">
                    <path fill="currentColor" d="M32.7 24.8c0-5 4.1-7.4 4.3-7.6-2.4-3.3-6-3.8-7.3-3.9-3-.3-5.9 1.7-7.4 1.7-1.6 0-4-1.6-6.5-1.5-3.4.1-6.5 1.9-8.2 4.8-3.6 6-.9 15 2.6 19.9 1.7 2.4 3.7 5.1 6.3 5 2.5-.1 3.5-1.5 6.7-1.5 3.1 0 4 .1 6.6 1.5 2.7.2 4.5-2.3 6.2-4.7 1.9-2.8 2.7-5.5 2.7-5.6-.1 0-5.9-2.3-5.9-8.1Zm-4.8-14.2c1.5-1.8 2.5-4.2 2.2-6.6-2.2.1-4.8 1.5-6.4 3.3-1.4 1.6-2.6 4-2.3 6.3 2.4.2 4.8-1.2 6.5-3Z"></path>
                  </svg>
                </span>
                <span class="store-copy">
                  <small>{e(copy["apple_small"])}</small>
                  <strong>App Store</strong>
                </span>
              </a>
            </div>

              <a class="download-qr-card" href="{localized_download_url}" aria-label="{e(qr_label)}">
                <span class="download-qr-art" aria-hidden="true">
                  <img class="download-qr-code" src="{prefix}{DOWNLOAD_QR_ASSET}" alt="" width="184" height="184" loading="lazy" decoding="async">
                  <span class="download-qr-logo">
                    <img src="{prefix}{BRAND_MARK_ASSET}" alt="" width="52" height="52" loading="lazy" decoding="async">
                  </span>
                </span>
                <span class="download-qr-copy">
                  <strong>{e(qr_copy["title"])}</strong>
                  <span>{e(qr_copy["body"])}</span>
                  <em>{e(qr_copy["hint"])}</em>
                </span>
              </a>
            </div>"""


def build_schema(
    locale_code: str,
    copy: dict,
    faq: dict,
    proof: dict,
    contact: dict,
    language_support: dict,
    why_snapvend: dict,
    field_operations: dict,
    keywords: str,
) -> str:
    pricing = SCHEMA_PRICING[locale_code]
    page_url = canonical_url(locale_code)
    logo_url = f"{SITE_URL}{BRAND_MARK_ASSET}"
    contact_point_id = f"{SITE_URL}/#sales-contact"
    localized_language_names = [localized_language_name(locale_code, code) for code in LOCALE_ORDER]
    disambiguation = SCHEMA_DISAMBIGUATION_BY_LOCALE.get(locale_code, SCHEMA_DISAMBIGUATION_BY_LOCALE["en"])
    screenshot_urls = [
        f"{SITE_URL}/{marketing_asset('hero_main')}",
        f"{SITE_URL}/{marketing_asset('hero_secondary')}",
        f"{SITE_URL}/{marketing_asset('workflow_ftp')}",
        f"{SITE_URL}/{marketing_asset('workflow_dashboard')}",
        f"{SITE_URL}/{marketing_asset('workflow_qr')}",
        f"{SITE_URL}/{marketing_asset('workflow_http_gallery', locale_code)}",
        f"{SITE_URL}/{marketing_asset('workflow_payment')}",
        f"{SITE_URL}/{marketing_asset('schema_report')}",
    ]
    audience_list = build_item_list_schema(page_url, "audience", copy["audience_title"], copy["audience_cards"])
    language_support_list = build_item_list_schema(page_url, "language-support-benefits", language_support["title"], language_support["cards"])
    why_snapvend_list = build_item_list_schema(page_url, "why-snapvend", why_snapvend["title"], why_snapvend["cards"])
    field_operations_list = build_item_list_schema(page_url, "field-operations", field_operations["title"], field_operations["cards"])
    use_case_list = build_item_list_schema(page_url, "use-cases", proof["use_label"], proof["use_cases"])
    reference_profile_list = build_item_list_schema(page_url, "reference-profiles", proof["reference_label"], proof["references"])
    contact_topic_set = build_defined_term_set_schema(page_url, "contact-topics", contact["type_label"], contact["topics"])
    why_snapvend_points = build_defined_term_set_schema(page_url, "why-snapvend-points", why_snapvend["panel_title"], why_snapvend["panel_points"])
    field_license_points = build_defined_term_set_schema(page_url, "field-license-points", field_operations["license_title"], field_operations["license_points"])
    supported_language_set = build_defined_term_set_schema(
        page_url,
        "supported-languages",
        language_support["supported_label"],
        localized_language_names,
    )

    contact_point = {
        "@type": "ContactPoint",
        "@id": contact_point_id,
        "contactType": "sales",
        "email": "snapvendinfo@gmail.com",
        "url": "mailto:snapvendinfo@gmail.com",
        "availableLanguage": localized_language_names,
    }

    organization = {
        "@type": "Organization",
        "@id": f"{SITE_URL}/#organization",
        "name": PRODUCT_NAME,
        "alternateName": [
            PRODUCT_SHORT_NAME,
            "SnapVend QR Gallery",
            "SnapVend Photo Delivery",
        ],
        "description": copy["meta_description"],
        "disambiguatingDescription": disambiguation["organization"],
        "slogan": copy["brand_motto"],
        "url": f"{SITE_URL}/",
        "logo": {
            "@type": "ImageObject",
            "url": logo_url,
        },
        "image": logo_url,
        "sameAs": [
            f"{SITE_URL}/",
            GOOGLE_PLAY_URL,
        ],
        "contactPoint": [{"@id": contact_point_id}],
    }

    website = {
        "@type": "WebSite",
        "@id": f"{SITE_URL}/#website",
        "url": f"{SITE_URL}/",
        "name": PRODUCT_NAME,
        "alternateName": PRODUCT_SHORT_NAME,
        "inLanguage": locale_code,
        "publisher": {"@id": organization["@id"]},
    }

    webpage = {
        "@type": "WebPage",
        "@id": f"{page_url}#webpage",
        "url": page_url,
        "name": copy["meta_title"],
        "description": copy["meta_description"],
        "inLanguage": locale_code,
        "isPartOf": {"@id": website["@id"]},
        "about": {"@id": f"{page_url}#app"},
        "mainEntity": {"@id": f"{page_url}#app"},
        "primaryImageOfPage": {
            "@type": "ImageObject",
            "url": logo_url,
        },
        "keywords": keywords,
        "hasPart": [
            {"@id": audience_list["@id"]},
            {"@id": language_support_list["@id"]},
            {"@id": why_snapvend_list["@id"]},
            {"@id": field_operations_list["@id"]},
            {"@id": use_case_list["@id"]},
            {"@id": reference_profile_list["@id"]},
            {"@id": f"{page_url}#faq"},
            {"@id": f"{page_url}#contact-page"},
            {"@id": contact_topic_set["@id"]},
            {"@id": why_snapvend_points["@id"]},
            {"@id": field_license_points["@id"]},
            {"@id": supported_language_set["@id"]},
        ],
    }

    software = {
        "@type": "SoftwareApplication",
        "@id": f"{page_url}#app",
        "name": PRODUCT_NAME,
        "alternateName": [
            PRODUCT_SHORT_NAME,
            "SnapVend QR Gallery",
            "SnapVend Photographer Gallery",
        ],
        "description": copy["meta_description"],
        "disambiguatingDescription": disambiguation["software"],
        "applicationCategory": "BusinessApplication",
        "applicationSubCategory": APPLICATION_SUBCATEGORY_BY_LOCALE.get(locale_code, "Photo workflow, print management and delivery"),
        "applicationSuite": PRODUCT_NAME,
        "identifier": "com.snapvend.gallery",
        "operatingSystem": "ANDROID, IOS",
        "inLanguage": locale_code,
        "availableLanguage": localized_language_names,
        "url": page_url,
        "mainEntityOfPage": page_url,
        "image": logo_url,
        "screenshot": screenshot_urls,
        "keywords": keywords,
        "brand": {
            "@type": "Brand",
            "name": PRODUCT_NAME,
            "alternateName": PRODUCT_SHORT_NAME,
        },
        "publisher": {"@id": organization["@id"]},
        "isAccessibleForFree": True,
        "featureList": unique_strings(
            [card["title"] for card in copy["workflow_cards"]]
            + [card["title"] for card in why_snapvend["cards"]]
            + [card["title"] for card in field_operations["cards"]]
            + copy["monthly_features"]
            + copy["yearly_features"]
            + [card["title"] for card in language_support["cards"]]
            + [card["title"] for card in proof["use_cases"][:2]]
        ),
        "additionalProperty": [
            {
                "@type": "PropertyValue",
                "name": language_support["supported_label"],
                "value": ", ".join(localized_language_names),
            },
            {
                "@type": "PropertyValue",
                "name": LOCALIZED_FLOW_COVERAGE_LABEL_BY_LOCALE.get(locale_code, "Localized client flow coverage"),
                "value": language_support["title"],
            },
            {
                "@type": "PropertyValue",
                "name": why_snapvend["panel_label"],
                "value": " | ".join(why_snapvend["panel_points"]),
            },
            {
                "@type": "PropertyValue",
                "name": field_operations["license_label"],
                "value": f'{field_operations["license_title"]}: ' + " | ".join(field_operations["license_points"]),
            },
        ],
        "audience": [
            {
                "@type": "Audience",
                "audienceType": item["title"],
                "description": item["body"],
            }
            for item in copy["audience_cards"]
        ],
        "offers": [
            {
                "@type": "Offer",
                "name": copy["monthly_badge"],
                "description": " | ".join(copy["monthly_features"]),
                "price": pricing["monthly"],
                "priceCurrency": pricing["currency"],
                "availability": "https://schema.org/InStock",
                "url": f"{page_url}#pricing",
            },
            {
                "@type": "Offer",
                "name": copy["yearly_badge"],
                "description": " | ".join(copy["yearly_features"]),
                "price": pricing["yearly"],
                "priceCurrency": pricing["currency"],
                "availability": "https://schema.org/InStock",
                "url": f"{page_url}#pricing",
            },
        ],
        "downloadUrl": GOOGLE_PLAY_URL,
        "installUrl": GOOGLE_PLAY_URL,
        "dateModified": BUILD_DATE,
    }

    contact_page = {
        "@type": "ContactPage",
        "@id": f"{page_url}#contact-page",
        "url": f"{page_url}#contact",
        "name": contact["title"],
        "description": contact["panel_note"],
        "inLanguage": locale_code,
        "isPartOf": {"@id": website["@id"]},
        "about": [{"@id": software["@id"]}, {"@id": contact_topic_set["@id"]}],
        "mainEntity": {"@id": contact_point["@id"]},
        "potentialAction": {
            "@type": "CommunicateAction",
            "name": contact["submit"],
            "target": "mailto:snapvendinfo@gmail.com",
            "recipient": {"@id": organization["@id"]},
        },
    }

    faq_page = {
        "@type": "FAQPage",
        "@id": f"{page_url}#faq",
        "mainEntity": [
            {
                "@type": "Question",
                "name": item["q"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": item["a"],
                },
            }
            for item in faq["items"]
        ],
    }

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            organization,
            contact_point,
            website,
            webpage,
            software,
            audience_list,
            language_support_list,
            why_snapvend_list,
            field_operations_list,
            use_case_list,
            reference_profile_list,
            contact_topic_set,
            why_snapvend_points,
            field_license_points,
            supported_language_set,
            contact_page,
            faq_page,
        ],
    }
    return json.dumps(schema, ensure_ascii=False, separators=(",", ":"))


def render_page(locale_code: str) -> str:
    copy = COPY[locale_code]
    meta = LOCALE_META[locale_code]
    prefix = asset_prefix(locale_code)
    og_image = f"{SITE_URL}{APP_ICON_ASSET}"
    alternates = build_alternates(locale_code)
    language_menu = build_language_menu(locale_code)
    extra_nav = NAV_EXTRA[locale_code]
    demo_copy = DEMO_SECTION[locale_code]
    faq_copy = FAQ_SECTION[locale_code]
    proof_copy = PROOF_SECTION[locale_code]
    language_support_copy = LANGUAGE_SUPPORT_SECTION[locale_code]
    why_snapvend_copy = WHY_SNAPVEND_SECTION[locale_code]
    field_operations_copy = FIELD_OPERATIONS_SECTION[locale_code]
    contact_copy = CONTACT_SECTION[locale_code]
    metrics = build_metric_cards(copy)
    demo_steps = build_demo_steps(demo_copy)
    workflow_cards = build_workflow_cards(copy)
    audience_cards = build_audience_cards(copy)
    language_support_cards = build_language_support_cards(language_support_copy)
    language_support_badges = build_language_support_badges(locale_code)
    why_snapvend_cards = build_why_snapvend_cards(why_snapvend_copy)
    why_snapvend_points = build_why_snapvend_points(why_snapvend_copy)
    field_operation_cards = build_field_operation_cards(field_operations_copy)
    field_operation_points = build_field_operation_points(field_operations_copy)
    proof_use_cases = build_proof_cards(proof_copy["use_cases"])
    proof_references = build_proof_cards(proof_copy["references"])
    faq_items = build_faq_items(faq_copy)
    contact_highlights = build_contact_highlights(contact_copy)
    contact_topics = build_contact_topics(contact_copy)
    keyword_string = build_keyword_string(locale_code, copy, proof_copy, contact_copy, language_support_copy, why_snapvend_copy, field_operations_copy)
    schema_json = build_schema(
        locale_code,
        copy,
        faq_copy,
        proof_copy,
        contact_copy,
        language_support_copy,
        why_snapvend_copy,
        field_operations_copy,
        keyword_string,
    )
    active_flag = flag_markup(meta["app_store_country"], prefix)
    active_language_code = locale_code.upper()
    popular_label = POPULAR_LABELS[locale_code]
    mobile_menu_label = MOBILE_MENU_LABELS[locale_code]
    language_count = f"{len(LOCALE_ORDER)}+"
    brand_kicker = BRAND_KICKER_BY_LOCALE.get(locale_code, "Professional Photo Delivery")

    return f"""<!doctype html>
<html lang="{locale_code}" dir="{meta["dir"]}" data-locale="{locale_code}">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{e(copy["meta_title"])}</title>
    <meta name="description" content="{e(copy["meta_description"])}">
    <meta name="keywords" content="{e(keyword_string)}">
    <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
    <meta name="theme-color" content="#071b45">
    <meta http-equiv="content-language" content="{locale_code}">
    <meta name="application-name" content="{PRODUCT_NAME}">
    <meta property="og:site_name" content="{PRODUCT_NAME}">
    <meta property="og:type" content="website">
    <meta property="og:title" content="{e(copy["meta_title"])}">
    <meta property="og:description" content="{e(copy["meta_description"])}">
    <meta property="og:url" content="{canonical_url(locale_code)}">
    <meta property="og:image" content="{og_image}">
    <meta property="og:image:alt" content="{e(copy["meta_title"])}">
    <meta property="og:locale" content="{meta["og_locale"]}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{e(copy["meta_title"])}">
    <meta name="twitter:description" content="{e(copy["meta_description"])}">
    <meta name="twitter:image" content="{og_image}">
    <meta name="twitter:image:alt" content="{e(copy["meta_title"])}">
    <link rel="canonical" href="{canonical_url(locale_code)}">
{alternates}    <link rel="icon" type="image/png" href="{prefix}{BRAND_MARK_ASSET}">
    <link rel="shortcut icon" href="{prefix}{BRAND_MARK_ASSET}">
    <link rel="apple-touch-icon" href="{prefix}{BRAND_MARK_ASSET}">
    <link rel="manifest" href="{prefix}/manifest.webmanifest">
    <link rel="preload" href="{prefix}/assets/fonts/BebasNeue-Regular.ttf" as="font" type="font/ttf" crossorigin>
    <link rel="preload" href="{prefix}/assets/fonts/JosefinSans-Bold.ttf" as="font" type="font/ttf" crossorigin>
    <link rel="stylesheet" href="{prefix}/styles.css?v={BUILD_VERSION}">
    <script type="application/ld+json">{schema_json}</script>
    <script defer src="{prefix}/site-config.js?v={BUILD_VERSION}"></script>
    <script defer src="{prefix}/script.js?v={BUILD_VERSION}"></script>
  </head>
  <body>
    <div class="page-aura page-aura-left" aria-hidden="true"></div>
    <div class="page-aura page-aura-right" aria-hidden="true"></div>

    <header class="topbar">
      <div class="container topbar-inner">
        <a class="brand" href="{relative_page_href(locale_code, locale_code)}">
          <img class="brand-mark" src="{prefix}{BRAND_MARK_SITE_ASSET}" alt="SnapVend" width="64" height="64" decoding="async" fetchpriority="high">
          <span class="brand-copy">
            <span class="brand-kicker">{e(brand_kicker)}</span>
            <strong>SnapVend</strong>
          </span>
        </a>

        <button class="topbar-menu-toggle" type="button" aria-expanded="false" aria-controls="primary-menu" data-menu-toggle>
          <span class="topbar-menu-toggle-lines" aria-hidden="true">
            <span></span>
            <span></span>
            <span></span>
          </span>
          <span>{e(mobile_menu_label)}</span>
        </button>

        <div class="topbar-menu-panel" id="primary-menu" data-menu-panel>
          <nav class="topnav" aria-label="Sections">
            <a href="#demo">{e(extra_nav["demo"])}</a>
            <a href="#how-it-works">{e(copy["nav_how"])}</a>
            <a href="#why-snapvend">{e(extra_nav["why"])}</a>
            <a href="#audience">{e(copy["nav_audience"])}</a>
            <a href="#pricing">{e(copy["nav_pricing"])}</a>
            <a href="#faq">{e(extra_nav["faq"])}</a>
          </nav>

          <div class="topbar-actions">
            <a class="pill-link" href="#download">{e(copy["nav_download"])}</a>
            <details class="language-switcher">
              <summary><span class="language-summary">{active_flag}<span>{active_language_code}</span></span></summary>
              <div class="language-menu">
{language_menu}
              </div>
            </details>
          </div>
        </div>
      </div>
    </header>

    <main>
      <section class="hero section" id="download">
        <div class="container hero-grid">
          <div class="hero-copy reveal">
            <p class="eyebrow">{e(copy["hero_eyebrow"])}</p>
            <h1>{e(copy["hero_title"])}</h1>
            <p class="hero-motto">{e(copy["brand_motto"])}</p>
            <p class="hero-lead">{e(copy["hero_lead"])}</p>
{store_badges(locale_code, copy)}

            <div class="metric-grid">
{metrics}
            </div>
          </div>

          <div class="hero-visual reveal">
            <article class="visual-frame visual-frame-main">
              <img src="{prefix}/{marketing_asset('hero_main', locale_code)}" alt="{e(image_alt(locale_code, 'hero_main'))}" width="288" height="640" loading="eager" decoding="async" fetchpriority="high">
            </article>
            <article class="visual-frame visual-frame-secondary">
              <img src="{prefix}/{marketing_asset('hero_secondary', locale_code)}" alt="{e(image_alt(locale_code, 'hero_secondary'))}" width="189" height="420" loading="eager" decoding="async">
            </article>
            <article class="visual-chip">
              <span>SnapVend</span>
              <p class="visual-chip-motto">{e(copy["brand_motto"])}</p>
            </article>
          </div>
        </div>
      </section>

      <section class="section language-support deferred-section" id="language-support">
        <div class="container">
          <div class="language-support-shell">
            <div class="section-head reveal">
              <p class="eyebrow">{e(language_support_copy["eyebrow"])}</p>
              <h2>{e(language_support_copy["title"])}</h2>
              <p>{e(language_support_copy["lead"])}</p>
            </div>

            <div class="language-support-topline reveal">
              <div class="language-support-count">
                <strong>{language_count}</strong>
                <span>{e(language_support_copy["supported_label"])}</span>
              </div>
            </div>

            <div class="language-support-grid">
{language_support_cards}
            </div>

            <div class="language-support-footer reveal">
              <span class="proof-label">{e(language_support_copy["supported_label"])}</span>
              <div class="language-support-badges">
{language_support_badges}
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="section demo deferred-section" id="demo">
        <div class="container">
          <div class="section-head reveal">
            <p class="eyebrow">{e(demo_copy["eyebrow"])}</p>
            <h2>{e(demo_copy["title"])}</h2>
            <p>{e(demo_copy["lead"])}</p>
          </div>

          <div class="demo-grid">
            <article class="demo-stage reveal">
              <div class="demo-stage-head">
                <span>{e(demo_copy["screen_label"])}</span>
                <strong>{e(demo_copy["screen_tag"])}</strong>
              </div>
              <div class="demo-stage-screen">
                <div class="demo-device-frame" data-demo-frame>
                  <span class="demo-device-notch" aria-hidden="true"></span>
                  <video class="demo-video" data-demo-video playsinline muted loop preload="none" hidden></video>
                  <button class="demo-placeholder" type="button" data-demo-fallback aria-label="{e(demo_copy['screen_label'])}">
                    <span class="demo-placeholder-play" aria-hidden="true"></span>
                    <strong>{e(demo_copy["screen_tag"])}</strong>
                    <p>{e(demo_copy["screen_label"])}</p>
                  </button>
                </div>
              </div>
              <p class="demo-stage-note" data-demo-note>{e(demo_copy["screen_note"])}</p>
            </article>

            <div class="demo-steps">
{demo_steps}
              <a class="action-link reveal" href="#download">{e(demo_copy["cta"])}</a>
            </div>
          </div>
        </div>
      </section>

      <section class="section deferred-section" id="how-it-works">
        <div class="container">
          <div class="section-head reveal">
            <p class="eyebrow">{e(copy["workflow_eyebrow"])}</p>
            <h2>{e(copy["workflow_title"])}</h2>
            <p>{e(copy["workflow_lead"])}</p>
          </div>

          <div class="workflow-grid">
            <ol class="workflow-list">
{workflow_cards}
            </ol>

            <div class="shot-stack reveal">
              <article class="shot-card shot-card-ftp">
                <img src="{prefix}/{marketing_asset('workflow_ftp', locale_code)}" alt="{e(image_alt(locale_code, 'workflow_ftp'))}" width="324" height="720" loading="lazy" decoding="async">
              </article>
              <article class="shot-card shot-card-dashboard">
                <img src="{prefix}/{marketing_asset('workflow_dashboard', locale_code)}" alt="{e(image_alt(locale_code, 'workflow_dashboard'))}" width="324" height="720" loading="lazy" decoding="async">
              </article>
              <article class="shot-card shot-card-qr">
                <img src="{prefix}/{marketing_asset('workflow_qr', locale_code)}" alt="{e(image_alt(locale_code, 'workflow_qr'))}" width="324" height="720" loading="lazy" decoding="async">
              </article>
              <article class="shot-card shot-card-http">
                <img src="{prefix}/{marketing_asset('workflow_http_gallery', locale_code)}" alt="{e(image_alt(locale_code, 'workflow_http_gallery'))}" width="324" height="720" loading="lazy" decoding="async">
              </article>
              <article class="shot-card shot-card-payment">
                <img src="{prefix}/{marketing_asset('workflow_payment', locale_code)}" alt="{e(image_alt(locale_code, 'workflow_payment'))}" width="324" height="720" loading="lazy" decoding="async">
              </article>
            </div>
          </div>
        </div>
      </section>

      <section class="section why-snapvend deferred-section" id="why-snapvend">
        <div class="container">
          <div class="section-head reveal">
            <p class="eyebrow">{e(why_snapvend_copy["eyebrow"])}</p>
            <h2>{e(why_snapvend_copy["title"])}</h2>
            <p>{e(why_snapvend_copy["lead"])}</p>
          </div>

          <div class="why-snapvend-layout">
            <div class="why-snapvend-grid">
{why_snapvend_cards}
            </div>

            <aside class="why-snapvend-panel reveal">
              <span class="proof-label">{e(why_snapvend_copy["panel_label"])}</span>
              <h3>{e(why_snapvend_copy["panel_title"])}</h3>
              <ul class="why-snapvend-points">
{why_snapvend_points}
              </ul>
            </aside>
          </div>
        </div>
      </section>

      <section class="section field-operations deferred-section" id="field-operations">
        <div class="container">
          <div class="section-head reveal">
            <p class="eyebrow">{e(field_operations_copy["eyebrow"])}</p>
            <h2>{e(field_operations_copy["title"])}</h2>
            <p>{e(field_operations_copy["lead"])}</p>
          </div>

          <div class="field-operations-layout">
            <div class="field-operations-grid">
{field_operation_cards}
            </div>

            <aside class="field-license-panel reveal">
              <span class="proof-label">{e(field_operations_copy["license_label"])}</span>
              <h3>{e(field_operations_copy["license_title"])}</h3>
              <p>{e(field_operations_copy["license_body"])}</p>
              <ul class="field-license-points">
{field_operation_points}
              </ul>
            </aside>
          </div>
        </div>
      </section>

      <section class="section deferred-section" id="audience">
        <div class="container">
          <div class="section-head reveal">
            <p class="eyebrow">{e(copy["audience_eyebrow"])}</p>
            <h2>{e(copy["audience_title"])}</h2>
            <p>{e(copy["audience_lead"])}</p>
          </div>

          <div class="audience-grid">
{audience_cards}
          </div>
        </div>
      </section>

      <section class="section proof deferred-section" id="use-cases">
        <div class="container">
          <div class="section-head reveal">
            <p class="eyebrow">{e(proof_copy["eyebrow"])}</p>
            <h2>{e(proof_copy["title"])}</h2>
            <p>{e(proof_copy["lead"])}</p>
          </div>

          <div class="proof-grid">
            <div class="proof-column">
              <div class="proof-column-head reveal">
                <span class="proof-label">{e(proof_copy["use_label"])}</span>
              </div>
              <div class="proof-stack">
{proof_use_cases}
              </div>
            </div>

            <div class="proof-column" id="reference-profiles">
              <div class="proof-column-head reveal">
                <span class="proof-label">{e(proof_copy["reference_label"])}</span>
              </div>
              <div class="proof-stack">
{proof_references}
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="section pricing deferred-section" id="pricing">
        <div class="container">
          <div class="section-head reveal">
            <p class="eyebrow">{e(copy["pricing_eyebrow"])}</p>
            <h2>{e(copy["pricing_title"])}</h2>
            <p>{e(copy["pricing_lead"])}</p>
          </div>

          <div class="pricing-grid">
            <article class="pricing-card reveal">
              <span class="plan-badge">{e(copy["free_badge"])}</span>
              <h3>{e(copy["free_title"])}</h3>
              <div class="price-line">
                <span class="price-value">0</span>
                <span class="price-period">{e(copy["free_period"])}</span>
              </div>
              <ul class="feature-list">
{build_feature_list(copy["free_features"])}
              </ul>
              <a class="action-link action-link-secondary" href="#download">{e(copy["free_cta"])}</a>
            </article>

            <article class="pricing-card reveal">
              <span class="plan-badge">{e(copy["monthly_badge"])}</span>
              <h3>{e(copy["monthly_title"])}</h3>
              <div class="price-line">
                <span class="price-value" data-config-text="monthlyPrice">{e(copy["monthly_placeholder"])}</span>
                <span class="price-period">{e(copy["monthly_period"])}</span>
              </div>
              <ul class="feature-list">
{build_feature_list(copy["monthly_features"])}
              </ul>
              <a class="action-link" href="#download">{e(copy["monthly_cta"])}</a>
            </article>

            <article class="pricing-card pricing-card-highlight reveal">
              <div class="plan-heading">
                <span class="plan-badge plan-badge-highlight">{e(copy["yearly_badge"])}</span>
                <span class="plan-callout">{e(popular_label)}</span>
              </div>
              <h3>{e(copy["yearly_title"])}</h3>
              <div class="price-line">
                <span class="price-value" data-config-text="yearlyPrice">{e(copy["yearly_placeholder"])}</span>
                <span class="price-period">{e(copy["yearly_period"])}</span>
              </div>
              <ul class="feature-list">
{build_feature_list(copy["yearly_features"])}
              </ul>
              <a class="action-link" href="#download">{e(copy["yearly_cta"])}</a>
            </article>
          </div>
          <p class="pricing-license-note reveal">{e(copy["pricing_license_note"])}</p>
        </div>
      </section>

      <section class="section faq deferred-section" id="faq">
        <div class="container">
          <div class="section-head reveal">
            <p class="eyebrow">{e(faq_copy["eyebrow"])}</p>
            <h2>{e(faq_copy["title"])}</h2>
            <p>{e(faq_copy["lead"])}</p>
          </div>

          <div class="faq-grid">
{faq_items}
          </div>
        </div>
      </section>

      <section class="section contact deferred-section" id="contact">
        <div class="container contact-grid">
          <div class="contact-copy reveal">
            <p class="eyebrow">{e(contact_copy["eyebrow"])}</p>
            <h2>{e(contact_copy["title"])}</h2>
            <p class="hero-lead">{e(contact_copy["lead"])}</p>

            <div class="contact-points">
{contact_highlights}
            </div>
          </div>

          <article class="contact-panel reveal">
            <div class="contact-panel-head">
              <h3>{e(contact_copy["panel_title"])}</h3>
              <p>{e(contact_copy["panel_note"])}</p>
            </div>

            <form
              class="contact-form"
              data-contact-form
              data-contact-email="snapvendinfo@gmail.com"
              data-contact-subject-prefix="{e(contact_copy["subject_prefix"])}"
              data-contact-label-type="{e(contact_copy["type_label"])}"
              data-contact-label-name="{e(contact_copy["name_label"])}"
              data-contact-label-company="{e(contact_copy["company_label"])}"
              data-contact-label-email="{e(contact_copy["email_label"])}"
              data-contact-label-message="{e(contact_copy["message_label"])}"
            >
              <label class="contact-field">
                <span class="contact-field-label">{e(contact_copy["type_label"])}</span>
                <select id="contact-topics" name="topic" required>
{contact_topics}
                </select>
              </label>

              <div class="contact-field-grid">
                <label class="contact-field">
                  <span class="contact-field-label">{e(contact_copy["name_label"])}</span>
                  <input type="text" name="fullName" autocomplete="name" required>
                </label>
                <label class="contact-field">
                  <span class="contact-field-label">{e(contact_copy["company_label"])}</span>
                  <input type="text" name="company" autocomplete="organization">
                </label>
              </div>

              <label class="contact-field">
                <span class="contact-field-label">{e(contact_copy["email_label"])}</span>
                <input type="email" name="email" autocomplete="email" required>
              </label>

              <label class="contact-field">
                <span class="contact-field-label">{e(contact_copy["message_label"])}</span>
                <textarea name="message" rows="6" placeholder="{e(contact_copy["message_placeholder"])}" required></textarea>
              </label>

              <div class="contact-actions">
                <button class="action-link contact-submit" type="submit">{e(contact_copy["submit"])}</button>
                <a class="action-link action-link-secondary contact-direct-link" href="mailto:snapvendinfo@gmail.com">{e(contact_copy["direct_email"])}</a>
              </div>

              <p class="contact-disclaimer">{e(contact_copy["disclaimer"])}</p>
            </form>
          </article>
        </div>
      </section>

      <section class="section deferred-section">
        <div class="container cta-panel reveal">
          <div>
            <p class="eyebrow">{e(copy["cta_eyebrow"])}</p>
            <h2>{e(copy["cta_title"])}</h2>
            <p>{e(copy["cta_lead"])}</p>
          </div>
{store_badges(locale_code, copy)}
        </div>
      </section>
    </main>

    <footer class="footer">
      <div class="container footer-inner">
        <p>{e(copy["footer_note"])}</p>
        <p>© 2026 SnapVend</p>
      </div>
    </footer>
  </body>
</html>
"""


def render_download_page() -> str:
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>SnapVend Gallery | Download Redirect</title>
    <meta name="description" content="Automatic SnapVend Gallery download redirect for Android devices and iOS testing notice.">
    <meta name="robots" content="noindex,follow">
    <meta name="theme-color" content="#071b45">
    <link rel="canonical" href="{DOWNLOAD_URL}">
    <link rel="icon" href="../assets/branding/app_icon_store_512.png" sizes="512x512">
    <link rel="apple-touch-icon" href="../assets/branding/app_icon_store_512.png">
    <link rel="preload" href="../assets/fonts/JosefinSans-Bold.ttf" as="font" type="font/ttf" crossorigin>
    <script src="../site-config.js?v={BUILD_VERSION}"></script>
    <script>
      (() => {{
        const routeCopy = {json.dumps(DOWNLOAD_ROUTE_COPY, ensure_ascii=False)};
        const routeBackUrls = {json.dumps({code: ("../" if meta["path"] == "" else f"../{meta['path']}/") for code, meta in LOCALE_META.items()}, ensure_ascii=False)};
        const defaultConfig = {{
          googlePlayUrl: "{GOOGLE_PLAY_URL}",
          appStoreUrl: "",
        }};
        const config = {{
          ...defaultConfig,
          ...(window.snapVendMarketingConfig || {{}}),
        }};
        const localeCandidates = [
          new URLSearchParams(window.location.search).get("lang") || "",
          ...(navigator.languages || []),
          navigator.language || "",
        ];
        const normalizeLocale = (value) => {{
          const code = String(value || "").toLowerCase().split("-")[0];
          return Object.prototype.hasOwnProperty.call(routeCopy, code) ? code : "";
        }};
        const locale = localeCandidates.map(normalizeLocale).find(Boolean) || "en";
        const copy = routeCopy[locale] || routeCopy.en;
        document.documentElement.lang = locale;
        document.documentElement.dir = locale === "ar" ? "rtl" : "ltr";
        if (copy.pageTitle) document.title = copy.pageTitle;
        const userAgent = navigator.userAgent || "";
        const isAndroid = /Android/i.test(userAgent);
        const isIOS = /iPhone|iPad|iPod/i.test(userAgent) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
        const googlePlayUrl = String(config.googlePlayUrl || "").trim();
        const appStoreUrl = String(config.appStoreUrl || "").trim();

        window.snapVendDownloadConfig = {{
          googlePlayUrl,
          appStoreUrl,
          copy,
          backUrl: routeBackUrls[locale] || "../",
          isIOS,
        }};

        if (isAndroid && googlePlayUrl) {{
          window.location.replace(googlePlayUrl);
          return;
        }}

        if (isIOS && appStoreUrl) {{
          window.location.replace(appStoreUrl);
        }}
      }})();
    </script>
    <link rel="stylesheet" href="../styles.css?v={BUILD_VERSION}">
  </head>
  <body class="download-redirect-page">
    <main class="download-redirect-shell">
      <article class="download-redirect-card">
        <a class="download-redirect-brand" href="../" aria-label="SnapVend Gallery">
          <img src="../assets/branding/snapvend_logo_square_web.png" alt="" width="64" height="64">
          <span>
            <small data-download-brand-kicker>Professional Photo Delivery</small>
            <strong>SnapVend Gallery</strong>
          </span>
        </a>
        <p class="eyebrow">SnapVend Gallery</p>
        <h1 data-download-title>Download for your device</h1>
        <p data-download-intro>We detect your device and send you to the correct store.</p>
        <p class="download-redirect-note" data-download-note>If you are on a desktop or notebook, choose the active store below.</p>
        <p class="download-redirect-ios-note" data-ios-pending-note hidden aria-live="polite">
          SnapVend Gallery for iPhone and iPad is currently in testing. The active public download is available on Google Play for Android.
        </p>
        <div class="download-redirect-actions">
          <a class="store-badge store-badge-play" data-download-google href="{GOOGLE_PLAY_URL}" target="_blank" rel="noreferrer">
            <span class="store-logo" aria-hidden="true">
              <svg viewBox="0 0 48 48" role="img">
                <path fill="#00d26a" d="M8 6.8 29.2 24 8 41.2z"></path>
                <path fill="#00a3ff" d="m29.2 24 5.6-4.8c2.4 1.7 2.4 7 0 8.7z"></path>
                <path fill="#ffd400" d="M8 6.8 20.1 18l9.1 6-9.1 6L8 41.2 14.5 24z"></path>
                <path fill="#ff5a5f" d="M8 6.8 20.1 18l14.7 1.2z"></path>
              </svg>
            </span>
            <span class="store-copy">
              <small>Download for Android</small>
              <strong>Google Play</strong>
            </span>
          </a>

          <a class="store-badge store-badge-apple" data-download-app-store href="#ios-test">
            <span class="store-logo" aria-hidden="true">
              <svg viewBox="0 0 48 48" role="img">
                <path fill="currentColor" d="M32.7 24.8c0-5 4.1-7.4 4.3-7.6-2.4-3.3-6-3.8-7.3-3.9-3-.3-5.9 1.7-7.4 1.7-1.6 0-4-1.6-6.5-1.5-3.4.1-6.5 1.9-8.2 4.8-3.6 6-.9 15 2.6 19.9 1.7 2.4 3.7 5.1 6.3 5 2.5-.1 3.5-1.5 6.7-1.5 3.1 0 4 .1 6.6 1.5 2.7.2 4.5-2.3 6.2-4.7 1.9-2.8 2.7-5.5 2.7-5.6-.1 0-5.9-2.3-5.9-8.1Zm-4.8-14.2c1.5-1.8 2.5-4.2 2.2-6.6-2.2.1-4.8 1.5-6.4 3.3-1.4 1.6-2.6 4-2.3 6.3 2.4.2 4.8-1.2 6.5-3Z"></path>
              </svg>
            </span>
            <span class="store-copy">
              <small data-download-apple-small>iOS version in testing</small>
              <strong>App Store</strong>
            </span>
          </a>
        </div>
        <a class="action-link action-link-secondary" data-download-back href="../">Back to website</a>
      </article>
    </main>
    <script>
      (() => {{
        const config = window.snapVendDownloadConfig || {{}};
        const copy = config.copy || {{}};
        const googleLink = document.querySelector("[data-download-google]");
        const appleLink = document.querySelector("[data-download-app-store]");
        const title = document.querySelector("[data-download-title]");
        const intro = document.querySelector("[data-download-intro]");
        const note = document.querySelector("[data-download-note]");
        const brandKicker = document.querySelector("[data-download-brand-kicker]");
        const googleSmall = document.querySelector("[data-download-google] small");
        const appleSmall = document.querySelector("[data-download-apple-small]");
        const backLink = document.querySelector("[data-download-back]");
        const iosPendingNote = document.querySelector("[data-ios-pending-note]");
        const googlePlayUrl = String(config.googlePlayUrl || "{GOOGLE_PLAY_URL}").trim();
        const appStoreUrl = String(config.appStoreUrl || "").trim();
        const backUrl = String(config.backUrl || "../").trim();
        const iosPendingMessage =
          copy.iosPendingNote ||
          "SnapVend Gallery for iPhone and iPad is currently in testing. The active public download is available on Google Play for Android.";

        if (copy.pageTitle) document.title = copy.pageTitle;
        if (brandKicker && copy.brandKicker) brandKicker.textContent = copy.brandKicker;
        if (title && copy.headline) title.textContent = copy.headline;
        if (intro && copy.intro) intro.textContent = copy.intro;
        if (note && copy.desktopNote) note.textContent = copy.desktopNote;
        if (googleSmall && copy.googleSmall) googleSmall.textContent = copy.googleSmall;
        if (appleSmall && copy.appleSmall) appleSmall.textContent = copy.appleSmall;
        if (backLink && copy.backWebsite) backLink.textContent = copy.backWebsite;
        if (backLink && backUrl) backLink.href = backUrl;

        const showIosPending = (shouldScroll = false) => {{
          if (iosPendingNote) {{
            iosPendingNote.textContent = iosPendingMessage;
            iosPendingNote.hidden = false;
            if (shouldScroll) {{
              iosPendingNote.scrollIntoView({{ behavior: "smooth", block: "center" }});
            }}
          }}
        }};

        googleLink.href = googlePlayUrl;
        if (appStoreUrl) {{
          appleLink.href = appStoreUrl;
          appleLink.target = "_blank";
          appleLink.rel = "noreferrer";
        }} else {{
          appleLink.href = "#ios-test";
          appleLink.removeAttribute("target");
          appleLink.removeAttribute("rel");
          appleLink.addEventListener("click", (event) => {{
            event.preventDefault();
            showIosPending(true);
          }});
        }}

        if (config.isIOS && !appStoreUrl) {{
          showIosPending();
        }}
      }})();
    </script>
  </body>
</html>
"""


def write_page(locale_code: str) -> None:
    meta = LOCALE_META[locale_code]
    output_dir = ROOT if meta["path"] == "" else ROOT / meta["path"]
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "index.html").write_text(render_page(locale_code), encoding="utf-8")


def write_download_page() -> None:
    output_dir = ROOT / "download"
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "index.html").write_text(render_download_page(), encoding="utf-8")


def write_manifest() -> None:
    manifest = {
        "name": PRODUCT_NAME,
        "short_name": "SnapVend",
        "lang": "tr",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#071b45",
        "theme_color": "#071b45",
        "icons": [
            {
                "src": APP_ICON_ASSET,
                "sizes": "512x512",
                "type": "image/png",
            },
            {
                "src": BRAND_MARK_ASSET,
                "sizes": "180x180",
                "type": "image/png",
            },
        ],
    }
    (ROOT / "manifest.webmanifest").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def write_robots() -> None:
    robots = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    (ROOT / "robots.txt").write_text(robots, encoding="utf-8")


def write_sitemap() -> None:
    entries = []
    for locale_code in LOCALE_ORDER:
        loc = canonical_url(locale_code)
        priority = "1.0" if locale_code == "tr" else "0.8"
        entries.append(
            f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{BUILD_DATE}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>"""
        )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(entries)
        + "\n</urlset>\n"
    )
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")


def main() -> None:
    for locale_code in LOCALE_ORDER:
        write_page(locale_code)
    write_download_page()
    write_manifest()
    write_robots()
    write_sitemap()


if __name__ == "__main__":
    main()
