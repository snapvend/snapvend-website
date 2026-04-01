from __future__ import annotations

import html
import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SEO_CONFIG = json.loads((ROOT / "seo-config.json").read_text(encoding="utf-8"))
SITE_URL = SEO_CONFIG["siteUrl"].rstrip("/")
BUILD_DATE = date.today().isoformat()
BRAND_MARK_ASSET = "/assets/branding/snapvend_logo_square.png"
BRAND_MARK_SITE_ASSET = "/assets/branding/snapvend_logo_square_web.png"
APP_ICON_ASSET = "/assets/branding/app_icon_store_512.png"


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


LOCALE_ORDER = ["tr", "en", "es", "fr", "de", "pt", "ru", "ar", "hi", "ja", "zh"]

SCHEMA_PRICING = {
    "tr": {"currency": "TRY", "monthly": 399.00, "yearly": 2499.00},
    "en": {"currency": "USD", "monthly": 9.04, "yearly": 56.59},
    "es": {"currency": "EUR", "monthly": 7.93, "yearly": 49.69},
    "fr": {"currency": "EUR", "monthly": 7.93, "yearly": 49.69},
    "de": {"currency": "EUR", "monthly": 7.93, "yearly": 49.69},
    "pt": {"currency": "BRL", "monthly": 47.00, "yearly": 294.37},
    "ru": {"currency": "RUB", "monthly": 751.00, "yearly": 4704.00},
    "ar": {"currency": "SAR", "monthly": 33.88, "yearly": 212.21},
    "hi": {"currency": "INR", "monthly": 835.00, "yearly": 5232.00},
    "ja": {"currency": "JPY", "monthly": 1438.00, "yearly": 9004.00},
    "zh": {"currency": "CNY", "monthly": 61.99, "yearly": 388.26},
}

POPULAR_LABELS = {
    "tr": "En Popüler",
    "en": "Most Popular",
    "es": "Más Popular",
    "fr": "Le Plus Populaire",
    "de": "Am Beliebtesten",
    "pt": "Mais Popular",
    "ru": "Самый популярный",
    "ar": "الأكثر شعبية",
    "hi": "सबसे लोकप्रिय",
    "ja": "一番人気",
    "zh": "最受欢迎",
}

NAV_EXTRA = {
    "tr": {"demo": "Demo", "faq": "SSS"},
    "en": {"demo": "Demo", "faq": "FAQ"},
    "es": {"demo": "Demo", "faq": "FAQ"},
    "fr": {"demo": "Demo", "faq": "FAQ"},
    "de": {"demo": "Demo", "faq": "FAQ"},
    "pt": {"demo": "Demo", "faq": "FAQ"},
    "ru": {"demo": "Демо", "faq": "FAQ"},
    "ar": {"demo": "عرض", "faq": "الاسئلة"},
    "hi": {"demo": "डेमो", "faq": "FAQ"},
    "ja": {"demo": "デモ", "faq": "FAQ"},
    "zh": {"demo": "演示", "faq": "常见问题"},
}

DEMO_SECTION = {
    "tr": {
        "eyebrow": "Canlı Demo",
        "title": "WiFi / hotspot bağlantısından session galerisine kadar akışı göster.",
        "lead": "SnapVend müşteriyi önce WiFi veya hotspot QR bağlantısıyla aynı ağa alır, sonra session galerisine yönlendirir ve teslime kadar akışı tek deneyimde toplar.",
        "screen_label": "Örnek ürün akışı",
        "screen_note": "Video linki eklersen bu alan otomatik olarak canlı ürün demosuna dönüşür.",
        "cta": "Demodan sonra indir",
        "steps": [
            {"title": "Fotoğrafları içe al", "body": "Yerel galeriden seç ya da FTP destekli profesyonel fotoğraf makinesinden doğrudan uygulamaya aktar."},
            {"title": "WiFi / hotspot QR bağlantısını aç", "body": "Müşteriyi uygulama indirtmeden aynı ağ ya da hotspot üstünde saniyeler içinde bağla."},
            {"title": "Session QR ile galeriye al", "body": "Müşteri kendi session QR kodunu okutup yalnızca kendisine ait galeriye girsin."},
            {"title": "Ödeme, PAC ve teslim", "body": "Seçimleri doğrula, ödeme ve PAC kontrolünü yap, sonra onaylanan dosyaları ZIP olarak teslim et."},
        ],
    },
    "en": {
        "eyebrow": "Live Demo",
        "title": "Show the flow from WiFi / hotspot access to the session gallery.",
        "lead": "SnapVend first brings the client onto the same network through a WiFi or hotspot QR connection, then moves them into the right session gallery and through delivery in one product journey.",
        "screen_label": "Sample product flow",
        "screen_note": "If you add a video URL, this area automatically turns into a live product demo.",
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
        "title": "Muestre QR, sessions y entrega en una sola pantalla.",
        "lead": "SnapVend reúne la transferencia FTP desde cámara profesional, la gestión por session, el acceso por QR y la entrega final en una experiencia clara y profesional.",
        "screen_label": "Flujo de producto",
        "screen_note": "Si agrega un enlace de video, esta zona se convierte automáticamente en un demo en vivo.",
        "cta": "Descargar después del demo",
        "steps": [
            {"title": "Importe las fotos", "body": "Use la galería local o transfiéralas directamente a la app desde una cámara profesional con FTP."},
            {"title": "Abra una session", "body": "Cree una session separada para cada cliente, toma o evento y mantenga el flujo ordenado."},
            {"title": "Abra la galería con QR", "body": "El cliente entra a su galería de session en segundos al escanear el QR en la misma red."},
            {"title": "Aprobación y entrega", "body": "Confirme el pago, valide PAC y entregue los archivos aprobados en ZIP."},
        ],
    },
    "fr": {
        "eyebrow": "Démo",
        "title": "Montrez QR, sessions et livraison sur un seul écran.",
        "lead": "SnapVend réunit le transfert FTP depuis un appareil photo pro, la gestion par session, l'accès QR et la livraison finale dans une expérience claire et professionnelle.",
        "screen_label": "Flux produit",
        "screen_note": "Si vous ajoutez une URL vidéo, cette zone devient automatiquement une démo produit.",
        "cta": "Télécharger après la démo",
        "steps": [
            {"title": "Importer les photos", "body": "Prenez-les depuis la galerie locale ou transférez-les directement dans l'app depuis un appareil photo pro compatible FTP."},
            {"title": "Ouvrir une session", "body": "Créez une session séparée pour chaque client, prise de vue ou événement afin de garder un flux propre."},
            {"title": "Ouvrir la galerie par QR", "body": "Le client entre dans sa galerie de session en quelques secondes via le QR sur le même réseau."},
            {"title": "Valider et livrer", "body": "Confirmez le paiement, validez le PAC et livrez les fichiers approuvés en ZIP."},
        ],
    },
    "de": {
        "eyebrow": "Demo",
        "title": "Zeigen Sie QR, Sessions und Auslieferung auf einem klaren Bildschirm.",
        "lead": "SnapVend verbindet FTP-Transfer aus professionellen Kameras, Session-Verwaltung, QR-Zugang und Auslieferung in einem professionellen Ablauf.",
        "screen_label": "Produktablauf",
        "screen_note": "Wenn Sie eine Video URL hinterlegen, wird dieser Bereich automatisch zur Live Demo.",
        "cta": "Nach der Demo herunterladen",
        "steps": [
            {"title": "Fotos importieren", "body": "Waehlen Sie sie aus lokaler Galerie oder uebertragen Sie sie direkt aus einer FTP-faehigen Profikamera in die App."},
            {"title": "Session starten", "body": "Erstellen Sie fuer jeden Kunden, jedes Shooting oder Event eine eigene Session und halten Sie den Ablauf sauber getrennt."},
            {"title": "Galerie per QR oeffnen", "body": "Der Kunde oeffnet seine Session-Galerie in Sekunden per QR im gleichen Netzwerk."},
            {"title": "Freigeben und liefern", "body": "Zahlung bestaetigen, PAC pruefen und freigegebene Dateien als ZIP ausliefern."},
        ],
    },
    "pt": {
        "eyebrow": "Demo",
        "title": "Mostre QR, sessions e entrega em uma unica tela.",
        "lead": "SnapVend une transferencia FTP de camera profissional, gestao por session, acesso por QR e entrega final em um fluxo claro e profissional.",
        "screen_label": "Fluxo do produto",
        "screen_note": "Se voce adicionar um link de video, esta area vira automaticamente um demo ao vivo.",
        "cta": "Baixar depois do demo",
        "steps": [
            {"title": "Importe as fotos", "body": "Use a galeria local ou transfira direto para o app a partir de uma camera profissional com FTP."},
            {"title": "Abra uma session", "body": "Crie uma session separada para cada cliente, ensaio ou evento e mantenha o fluxo organizado."},
            {"title": "Abra a galeria por QR", "body": "O cliente entra na propria galeria da session em segundos ao escanear o QR na mesma rede."},
            {"title": "Aprove e entregue", "body": "Confirme o pagamento, valide o PAC e entregue os arquivos aprovados em ZIP."},
        ],
    },
    "ru": {
        "eyebrow": "Демо",
        "title": "Покажите QR, сессии и выдачу на одном экране.",
        "lead": "SnapVend объединяет FTP-передачу с профессиональной камеры, управление сессиями, QR-доступ и финальную выдачу в одном понятном сценарии.",
        "screen_label": "Сценарий продукта",
        "screen_note": "Если добавить ссылку на видео, этот блок автоматически станет живой демо зоной.",
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
        "title": "اعرض QR و sessions والتسليم على شاشة واحدة واضحة.",
        "lead": "يجمع SnapVend بين النقل عبر FTP من الكاميرات الاحترافية وادارة sessions ودخول QR والتسليم النهائي في تجربة احترافية واحدة.",
        "screen_label": "تدفق المنتج",
        "screen_note": "عند اضافة رابط فيديو سيتحول هذا القسم تلقائيا الى عرض حي للمنتج.",
        "cta": "نزّل بعد العرض",
        "steps": [
            {"title": "استيراد الصور", "body": "اخترها من المعرض المحلي او انقلها مباشرة الى التطبيق من كاميرا احترافية تدعم FTP."},
            {"title": "افتح session", "body": "ابدأ session مستقلة لكل عميل او جلسة تصوير او فعالية حتى يبقى التدفق منظما."},
            {"title": "فتح المعرض عبر QR", "body": "يدخل العميل الى معرض session الخاص به خلال ثوان عبر QR على نفس الشبكة."},
            {"title": "اعتماد وتسليم", "body": "اكد الدفع وراجع PAC ثم سلم الملفات المعتمدة بصيغة ZIP."},
        ],
    },
    "hi": {
        "eyebrow": "लाइव डेमो",
        "title": "QR, session aur delivery flow ko ek saaf screen par dikhayen.",
        "lead": "SnapVend professional camera FTP transfer, session management, QR access aur delivery ko ek professional experience me jodta hai.",
        "screen_label": "प्रोडक्ट फ्लो",
        "screen_note": "अगर आप video URL जोड़ते हैं तो यह हिस्सा अपने आप live demo बन जाएगा।",
        "cta": "डेमो के बाद डाउनलोड करें",
        "steps": [
            {"title": "फोटो इम्पोर्ट करें", "body": "लोकल गैलरी से लें या professional FTP camera se direct app me transfer karein."},
            {"title": "Session shuru karein", "body": "Har client, shoot ya event ke liye alag session kholen taaki flow mix na ho."},
            {"title": "QR se gallery kholen", "body": "Client usi network par QR scan karke apni session gallery turant kholta hai."},
            {"title": "Manzoori aur delivery", "body": "Payment confirm karein, PAC check karein aur approved files ko ZIP me deliver karein."},
        ],
    },
    "ja": {
        "eyebrow": "ライブデモ",
        "title": "QR、セッション、納品の流れを1画面で見せる。",
        "lead": "SnapVend はプロ向けカメラからの FTP 転送、セッション管理、QR アクセス、納品までをひとつの分かりやすい体験にまとめます。",
        "screen_label": "製品フロー",
        "screen_note": "動画 URL を追加すると、この領域は自動で製品デモに変わります。",
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
        "title": "把 QR、session 与交付流程放在一个清晰界面里展示。",
        "lead": "SnapVend 将专业相机 FTP 传输、session 管理、QR 进入和最终交付整合成一个更专业的体验。",
        "screen_label": "产品流程",
        "screen_note": "如果添加视频链接，这个区域会自动切换为产品演示。",
        "cta": "看完演示后下载",
        "steps": [
            {"title": "导入照片", "body": "可从本地相册选择，也可通过支持 FTP 的专业相机直接传入应用。"},
            {"title": "创建 session", "body": "为每位客户、每次拍摄或每场活动建立独立 session，避免流程混淆。"},
            {"title": "通过 QR 打开画廊", "body": "客户在同一网络下扫描 QR，几秒内进入自己的 session 画廊。"},
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
        "eyebrow": "FAQ",
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
        "eyebrow": "FAQ",
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
        "eyebrow": "FAQ",
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
    "pt": {
        "eyebrow": "FAQ",
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
        "eyebrow": "FAQ",
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
        "eyebrow": "FAQ",
        "title": "शुरू करने से पहले सबसे आम सवाल",
        "lead": "फोटोग्राफर और ऑन साइट टीम आम तौर पर सबसे पहले यही सवाल पूछती हैं।",
        "items": [
            {"q": "क्या SnapVend बिना इंटरनेट के काम करता है?", "a": "हाँ। मुख्य workflow लोकल नेटवर्क या hotspot पर चल सकता है, cloud जरूरी नहीं है।"},
            {"q": "क्लाइंट फोटो कैसे देखता है?", "a": "क्लाइंट उसी नेटवर्क पर QR स्कैन करके browser gallery खोलता है।"},
            {"q": "क्या मैं अपना नाम और logo इस्तेमाल कर सकता हूँ?", "a": "हाँ। Pro plans custom branding, logo और branded delivery खोलते हैं।"},
            {"q": "Kya main client ko country-based payment methods dikha sakta hoon?", "a": "Haan. Business country select karne ke baad configured local methods payment popup me dikhte hain. Turkey, Spain, India, China aur Japan ke liye ready method sets maujood hain."},
            {"q": "कौन सा plan delivery limit हटाता है?", "a": "Monthly और yearly दोनों Pro plans daily delivery limit हटाते हैं।"},
        ],
    },
    "ja": {
        "eyebrow": "FAQ",
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
            {"title": "Yerel ağ ile çalışan operasyonlar", "body": "İnternet bağlantısına güvenmeden hotspot veya yerel ağ üzerinden işleyen ekipler için doğrudan uyumludur."},
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
            {"title": "Operaciones por red local", "body": "Pensado para equipos que trabajan con hotspot o red local sin depender de internet."},
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
            {"title": "Stand evenementiel corporate", "body": "Associez prise de vue rapide, acces QR et livraison ZIP dans une experience plus professionnelle."},
        ],
        "references": [
            {"title": "Equipes de livraison rapide", "body": "Adapte aux equipes qui veulent photographier, faire choisir et livrer le meme jour."},
            {"title": "Studios centres sur la marque", "body": "Bon choix pour les studios qui veulent une image de marque plus forte et un parcours client maitrise."},
            {"title": "Operations en reseau local", "body": "Concu pour les equipes qui preferent hotspot ou reseau local au lieu d'une dependance internet."},
            {"title": "Equipes multi sessions", "body": "Permet de gerer plusieurs clients ou groupes sans melanger les livraisons."},
        ],
    },
    "de": {
        "eyebrow": "Einsatzszenarien",
        "title": "Zeigen Sie die Einsatzablaufe, in denen SnapVend am starksten ist",
        "lead": "Bis verifizierte Kundenlogos oder Testimonials vorliegen, fasst dieser Bereich die passendsten Szenarien und Teamprofile zusammen.",
        "use_label": "Use Cases",
        "reference_label": "Referenzprofile",
        "use_cases": [
            {"title": "Hochzeit und Gasteauswahl", "body": "Offnen Sie die QR Galerie wahrend oder direkt nach dem Shooting, sammeln Sie Auswahlen und liefern Sie vom selben Gerat."},
            {"title": "Studio Auswahlplatz", "body": "Sichten Sie Portratfotos gemeinsam mit dem Kunden und gehen Sie direkt zur Freigabe uber."},
            {"title": "Schule und Sport", "body": "Halten Sie Klassen, Teams und Gruppen sauber getrennt, auch bei vielen Sessions pro Tag."},
            {"title": "Portraitverkauf auf Strassen und Touristenorten", "body": "Fotografieren Sie vor Ort, zeigen Sie ausgewaehlte Bilder sofort und steuern Sie Einzel- oder Paketverkaeufe vom selben Geraet."},
            {"title": "Corporate Event Stand", "body": "Verbinden Sie schnelle Aufnahme, QR Zugang und ZIP Auslieferung in einem professionellen Vor Ort Ablauf."},
        ],
        "references": [
            {"title": "Schnelle Lieferteams", "body": "Passend fur Crews, die Aufnahme, Auswahl und Auslieferung am selben Tag abschliessen wollen."},
            {"title": "Markenorientierte Studios", "body": "Gut fur Studios mit Bedarf an eigenem Branding und kontrollierter Kundenprasentation."},
            {"title": "Lokale Netzwerk Teams", "body": "Entwickelt fur Teams, die lieber per Hotspot oder lokalem Netzwerk als uber Internet arbeiten."},
            {"title": "Mehrfach Session Crews", "body": "Hilft beim getrennten Verwalten vieler Kunden oder Gruppen ohne Lieferchaos."},
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
            {"title": "Operacoes em rede local", "body": "Pensado para equipes que preferem hotspot ou rede local sem depender da internet."},
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
            {"title": "Локальные сетевые операции", "body": "Создано для работы через hotspot или локальную сеть без зависимости от интернета."},
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
            {"title": "عمليات تعمل عبر الشبكة المحلية", "body": "مصمم للفرق التي تعتمد على hotspot او الشبكة المحلية بدون الاعتماد على الانترنت."},
            {"title": "فرق تدير جلسات متعددة", "body": "يساعد على ادارة عدة عملاء او مجموعات بدون خلط عمليات التسليم."},
        ],
    },
    "hi": {
        "eyebrow": "उपयोग परिदृश्य",
        "title": "वे ऑन-site workflow दिखाएं जहां SnapVend सबसे बेहतर फिट बैठता है",
        "lead": "जब तक verified customer logos या named testimonials नहीं जोड़े जाते, यह section product के लिए सबसे मजबूत scenarios और team profiles दिखाता है।",
        "use_label": "Use Cases",
        "reference_label": "Reference Profiles",
        "use_cases": [
            {"title": "शादी और guest selection", "body": "शूट के दौरान या तुरंत बाद QR gallery खोलें, selections लें और उसी device से delivery पूरी करें।"},
            {"title": "studio review desk", "body": "क्लाइंट के साथ portrait shots देखें, shortlist करें और एक ही screen से approval पर जाएं।"},
            {"title": "school और sports sessions", "body": "कई classes, teams और groups को अलग रखते हुए delivery flow संभालें।"},
            {"title": "street aur tourist portrait sales", "body": "मौके पर shoot करें, चुनी हुई photos तुरंत दिखाएं और single या package sale को उसी device से manage करें।"},
            {"title": "corporate event booth", "body": "on-site capture, QR access और ZIP delivery को एक professional flow में चलाएं।"},
        ],
        "references": [
            {"title": "fast delivery teams", "body": "उन teams के लिए सही जो same-day shoot, review और delivery चाहते हैं।"},
            {"title": "brand-focused studios", "body": "उन studios के लिए उपयोगी जिन्हें अपना logo, business name और clean approval flow चाहिए।"},
            {"title": "local network operations", "body": "hotspot या local network पर काम करने वाली teams के लिए बनाया गया है।"},
            {"title": "multi-session crews", "body": "कई clients या groups को अलग रखते हुए delivery manage करने में मदद करता है।"},
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
            {"title": "ローカルネット運用", "body": "インターネット依存ではなく hotspot やローカルネットで動かしたい現場向けです。"},
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
            {"title": "重视品牌的影楼", "body": "适合需要自定义品牌名、logo 和更整洁客户流程的团队。"},
            {"title": "本地网络运营团队", "body": "为希望通过 hotspot 或本地网络工作而不是依赖互联网的团队设计。"},
            {"title": "多场次执行团队", "body": "帮助团队在不混淆客户或群组的情况下管理多场次交付。"},
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
        "lead": "Al enviar el formulario se abre su app de correo y el mensaje queda listo para snapvendinfo@gmail.com.",
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
        "direct_email": "Envoyer Un Email",
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
    "pt": {
        "eyebrow": "Contato",
        "title": "Envie sua solicitacao, duvida ou proposta diretamente para nos",
        "lead": "Ao enviar o formulario, seu app de e-mail abre e prepara a mensagem para snapvendinfo@gmail.com.",
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
        "disclaimer": "O botao abrirá seu app de e-mail para revisar e confirmar a mensagem.",
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
        "email_label": "Email",
        "message_label": "Сообщение",
        "message_placeholder": "Кратко опишите задачу, тип мероприятия или запрос.",
        "submit": "Отправить",
        "direct_email": "Написать На Email",
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
        "title": "अपनी request, inquiry या partnership message सीधे हमें भेजें",
        "lead": "Form submit करते ही आपका default mail app खुलेगा और message snapvendinfo@gmail.com के लिए तैयार हो जाएगा।",
        "panel_title": "हमें लिखें",
        "panel_note": "Demo request, pricing, partnership या custom workflow जरूरत के लिए यह form उपयोग करें।",
        "highlights": ["Demo request", "Pricing और license", "Custom workflow या partnership"],
        "type_label": "विषय",
        "topics": ["General Inquiry", "Demo Request", "Pricing", "Partnership", "Custom Request"],
        "name_label": "पूरा नाम",
        "company_label": "Business / Brand",
        "email_label": "Email",
        "message_label": "Message",
        "message_placeholder": "अपनी जरूरत या event type संक्षेप में लिखें।",
        "submit": "Send",
        "direct_email": "Direct Email भेजें",
        "disclaimer": "Send बटन आपका mail app खोलेगा ताकि आप message review करके भेज सकें।",
        "subject_prefix": "SnapVend website inquiry",
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
        "language_label": "Diller",
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
        "nav_audience": "Who Uses It",
        "nav_pricing": "Pricing",
        "nav_download": "Download",
        "language_label": "Languages",
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
        "language_label": "Idiomas",
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
            {"title": "Equipos móviles de entrega", "body": "Operaciones que trabajan por red local u hotspot sin depender de internet."},
        ],
        "pricing_eyebrow": "Planes",
        "pricing_title": "Empiece gratis y escale con Pro",
        "pricing_lead": "El plan gratuito sirve para aprender el flujo. Pro elimina límites y abre la marca del negocio.",
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
        "monthly_badge": "Pro Mensual",
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
        "yearly_badge": "Pro Anual",
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
        "language_label": "Langues",
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
            {"title": "Mariage et evenementiel", "body": "Des equipes qui ont besoin d'une selection et d'une livraison rapides pendant le shooting."},
            {"title": "Studio et portrait", "body": "Des studios qui veulent choisir et livrer avec le client dans un seul espace."},
            {"title": "Ecole, sport et corporate", "body": "Des equipes qui gerent plusieurs sessions sans melanger clients et livraisons."},
            {"title": "Photo de rue, zones touristiques et portrait mobile", "body": "Un flux adapte aux photographes qui veulent shooter sur place, montrer immediatement les images choisies et vendre a l'unite ou en pack."},
            {"title": "Equipes mobiles", "body": "Des operations qui travaillent en reseau local ou hotspot sans dependance internet."},
        ],
        "pricing_eyebrow": "Forfaits",
        "pricing_title": "Commencez gratuitement puis passez a Pro",
        "pricing_lead": "Le plan gratuit sert a apprendre le flux. Pro supprime les limites et debloque l'image de marque.",
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
        "monthly_badge": "Pro Mensuel",
        "monthly_title": "Usage mensuel flexible",
        "monthly_placeholder": "Mettre a jour le prix",
        "monthly_period": "/ mois",
        "monthly_features": [
            "Livraisons quotidiennes illimitees",
            "Nom et logo personnalises",
            "Nom de fichier ZIP personnalise",
            "Liste d'impression mariage illimitee",
        ],
        "monthly_cta": "Telecharger l'app",
        "yearly_badge": "Pro Annuel",
        "yearly_title": "Mieux pour un usage regulier",
        "yearly_placeholder": "Mettre a jour le prix",
        "yearly_period": "/ an",
        "yearly_features": [
            "Objectif de cout annuel plus bas",
            "Livraisons quotidiennes illimitees",
            "Controle complet de la marque",
            "Concu pour un usage terrain intensif",
        ],
        "yearly_cta": "Telecharger l'app",
        "cta_eyebrow": "Pret ?",
        "cta_title": "Montrez, faites choisir et livrez plus vite avec SnapVend.",
        "cta_lead": "Acces QR, transfert FTP, partage local et rapports dans un seul flux.",
        "footer_note": "SnapVend traite les medias sur l'appareil. Le partage n'est ouvert que lorsque vous lancez la livraison locale.",
    },
    "de": {
        "meta_title": "SnapVend | QR-Galerie und lokale Auslieferung fur Fotografen",
        "meta_description": "SnapVend hilft Fotografen, Fotos von einem Telefon oder Tablet aus mit QR-Galerie, FTP-Kameraimport und ZIP-Auslieferung zu importieren, zu zeigen und zu liefern.",
        "nav_how": "So Funktioniert's",
        "nav_audience": "Fur Wen",
        "nav_pricing": "Preise",
        "nav_download": "Download",
        "language_label": "Sprachen",
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
            {"title": "Schule, Sport und Corporate", "body": "Teams, die viele Sessions ohne Vermischung von Kunden und Lieferungen verwalten."},
            {"title": "Strasse, Touristenorte und mobile Portraits", "body": "Ein starker Ablauf fuer Fotografen, die vor Ort schnell fotografieren, ausgewaehlte Bilder direkt zeigen und einzeln oder im Paket verkaufen wollen."},
            {"title": "Mobile Lieferteams", "body": "Ablaufe, die per lokalem Netzwerk oder Hotspot ohne Internetabhaengigkeit arbeiten."},
        ],
        "pricing_eyebrow": "Plaene",
        "pricing_title": "Kostenlos starten und mit Pro wachsen",
        "pricing_lead": "Der Gratisplan hilft beim Einstieg. Pro entfernt Limits und oeffnet das Business-Branding.",
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
        "monthly_badge": "Pro Monatlich",
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
        "yearly_badge": "Pro Jaehrlich",
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
    "pt": {
        "meta_title": "SnapVend | Galeria QR e entrega local para fotografos",
        "meta_description": "SnapVend ajuda fotografos a importar, apresentar e entregar fotos de um telefone ou tablet com galeria QR, transferencia FTP e entrega ZIP.",
        "nav_how": "Como Funciona",
        "nav_audience": "Para Quem",
        "nav_pricing": "Precos",
        "nav_download": "Baixar",
        "language_label": "Idiomas",
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
            {"title": "Operacoes moveis", "body": "Fluxos que funcionam em rede local ou hotspot sem depender da internet."},
        ],
        "pricing_eyebrow": "Planos",
        "pricing_title": "Comece gratis e cresca com o Pro",
        "pricing_lead": "O plano gratuito serve para aprender o fluxo. O Pro remove limites e libera a marca do negocio.",
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
        "monthly_badge": "Pro Mensal",
        "monthly_title": "Uso mensal flexivel",
        "monthly_placeholder": "Atualizar preco",
        "monthly_period": "/ mes",
        "monthly_features": [
            "Entregas diarias ilimitadas",
            "Nome e logo personalizados",
            "Nome ZIP personalizado",
            "Lista de impressao de casamento ilimitada",
        ],
        "monthly_cta": "Baixar o app",
        "yearly_badge": "Pro Anual",
        "yearly_title": "Melhor para uso frequente",
        "yearly_placeholder": "Atualizar preco",
        "yearly_period": "/ ano",
        "yearly_features": [
            "Meta de menor custo anual",
            "Entregas diarias ilimitadas",
            "Controle total da marca",
            "Feito para uso intenso em campo",
        ],
        "yearly_cta": "Baixar o app",
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
        "language_label": "Языки",
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
            {"title": "Мобильные команды", "body": "Операции на локальной сети или hotspot без зависимости от интернета."},
        ],
        "pricing_eyebrow": "Планы",
        "pricing_title": "Начните бесплатно и растите с Pro",
        "pricing_lead": "Бесплатный план подходит для знакомства с процессом. Pro снимает лимиты и открывает брендинг.",
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
        "monthly_badge": "Pro Ежемесячно",
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
        "yearly_badge": "Pro Год",
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
        "language_label": "اللغات",
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
        "pricing_title": "ابدأ مجانا ثم توسع مع Pro",
        "pricing_lead": "الخطة المجانية مناسبة لتعلم التدفق. Pro يزيل الحدود ويفتح التحكم بالهوية التجارية.",
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
        "monthly_badge": "برو شهري",
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
        "yearly_badge": "برو سنوي",
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
        "meta_description": "SnapVend फोटोग्राफरों को एक ही फोन या टैबलेट से फोटो इम्पोर्ट, दिखाने और ZIP में डिलीवर करने में मदद करता है, QR गैलरी और FTP ट्रांसफर के साथ.",
        "nav_how": "यह कैसे काम करता है",
        "nav_audience": "किसके लिए",
        "nav_pricing": "प्राइसिंग",
        "nav_download": "डाउनलोड",
        "language_label": "भाषाएं",
        "hero_eyebrow": "QR गैलरी, FTP ट्रांसफर, लोकल डिलीवरी",
        "hero_title": "कैप्चर से डिलीवरी तक एक ही डिवाइस.",
        "hero_lead": "कैमरा या गैलरी से फोटो लें, ग्राहक को QR से अंदर लाएं, PAC कन्फर्म करें और मंजूर फाइलें उसी डिवाइस से ZIP में दें.",
        "google_small": "Android के लिए डाउनलोड",
        "apple_small": "iPhone और iPad के लिए डाउनलोड",
        "setup_note": "मासिक और वार्षिक कीमतें तथा सीधा App Store लिंक site-config.js में अपडेट किए जा सकते हैं. जब तक Apple app ID नहीं जुड़ती, iOS लोगो क्षेत्रीय App Store search result खोलता है.",
        "metrics": [
            {"value": "1 डिवाइस", "label": "लो, दिखाओ, डिलीवर करो"},
            {"value": "6 methods", "label": "Ready local payment"},
            {"value": "0 क्लाउड", "label": "लोकल फ्लो, बिना ट्रैकिंग"},
        ],
        "workflow_eyebrow": "वर्कफ़्लो",
        "workflow_title": "तेज, नियंत्रित और फील्ड के लिए तैयार",
        "workflow_lead": "SnapVend फोटो इनटेक, ग्राहक प्रीव्यू और डिलीवरी को एक साफ ऑपरेशन में बदल देता है.",
        "workflow_cards": [
            {"title": "फोटो इम्पोर्ट करें", "body": "लोकल गैलरी से चुनें या FTP कैमरा से सीधे SnapVend में भेजें."},
            {"title": "QR से गैलरी शेयर करें", "body": "ग्राहक उसी नेटवर्क पर QR स्कैन करके तुरंत वेब गैलरी खोलता है."},
            {"title": "Local payment dikhayein", "body": "Business country ke hisab se payment popup me FAST / EFT, Bizum, UPI, Alipay, WeChat Pay ya PayPay jaise ready methods dikhayein."},
            {"title": "चयन और PAC पुष्टि", "body": "ग्राहक फोटो चुनता है और आप भुगतान व PAC सत्यापन की पुष्टि करते हैं."},
            {"title": "ZIP डिलीवरी और रिपोर्ट", "body": "मंजूर फाइलें ZIP में डाउनलोड होती हैं और डिलीवरी व आय ऐप में दिखती रहती है."},
        ],
        "audience_eyebrow": "किसके लिए",
        "audience_title": "प्रोफेशनल ऑन-साइट टीमों के लिए बनाया गया",
        "audience_lead": "उन फोटोग्राफरों के लिए एक मजबूत केंद्र जिन्हें तेज प्रीव्यू, कंट्रोल्ड सिलेक्शन और तुरंत डिलीवरी चाहिए.",
        "audience_cards": [
            {"title": "शादी और इवेंट फोटोग्राफर", "body": "टीमें जिन्हें लाइव शूट के दौरान तेज चयन और डिलीवरी चाहिए."},
            {"title": "स्टूडियो और पोर्ट्रेट", "body": "स्टूडियो जो ग्राहक के साथ एक ही जगह पर समीक्षा, चयन और डिलीवरी करना चाहते हैं."},
            {"title": "स्कूल, स्पोर्ट्स और कॉर्पोरेट", "body": "टीमें जो कई सेशन संभालती हैं और ग्राहकों या डिलीवरी को मिक्स नहीं करना चाहतीं."},
            {"title": "street, tourist area और mobile portrait shoots", "body": "ऐसे photographers के लिए मजबूत flow जो मौके पर shoot करें, चुनी हुई photos तुरंत दिखाएं और single या package sale करना चाहें।"},
            {"title": "मोबाइल डिलीवरी टीमें", "body": "ऐसे ऑपरेशन जो लोकल नेटवर्क या hotspot पर इंटरनेट के बिना चलते हैं."},
        ],
        "pricing_eyebrow": "प्लान",
        "pricing_title": "फ्री से शुरू करें और Pro के साथ बढ़ें",
        "pricing_lead": "फ्री प्लान फ्लो सीखने के लिए तैयार है. Pro लिमिट हटाता है और बिज़नेस ब्रांडिंग खोलता है.",
        "config_warning": "इस रिपॉजिटरी में अंतिम कीमतें नहीं हैं. कीमतें और सीधा App Store लिंक site-config.js से कंट्रोल होते हैं.",
        "free_badge": "फ्री",
        "free_title": "फ्लो सीखने के लिए सही",
        "free_period": "शुरुआत के लिए",
        "free_features": [
            "प्रति दिन 10 फोटो डिलीवरी सीमा",
            "SnapVend ब्रांडिंग दिखाई देती रहती है",
            "कस्टम बिज़नेस नाम और लोगो लॉक रहते हैं",
            "लाइव उपयोग से पहले टेस्ट करने के लिए अच्छा",
        ],
        "free_cta": "फ्री शुरू करें",
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
            "पूरी ब्रांडिंग कंट्रोल",
            "भारी फील्ड उपयोग के लिए उपयुक्त",
        ],
        "yearly_cta": "ऐप डाउनलोड करें",
        "cta_eyebrow": "तैयार?",
        "cta_title": "SnapVend के साथ ऑन-साइट तेज़ी से दिखाएं, चुनवाएं और डिलीवर करें.",
        "cta_lead": "QR एक्सेस, FTP ट्रांसफर, लोकल शेयरिंग और रिपोर्ट एक ही फ्लो में.",
        "footer_note": "SnapVend मीडिया को डिवाइस पर प्रोसेस करता है. शेयरिंग केवल तब खुलती है जब आप लोकल डिलीवरी फ्लो शुरू करते हैं.",
    },
    "ja": {
        "meta_title": "SnapVend | 写真家向けQRギャラリーとローカル納品",
        "meta_description": "SnapVend は QR ギャラリー共有、FTP 転送、ZIP 納品を使って、1台のスマホやタブレットで写真の受け取りから納品までを支援します。",
        "nav_how": "使い方",
        "nav_audience": "対象ユーザー",
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
            {"title": "モバイル納品チーム", "body": "インターネット不要でローカルネットワークや hotspot を使う運用向け。"},
        ],
        "pricing_eyebrow": "プラン",
        "pricing_title": "無料で始めて、Pro で拡張",
        "pricing_lead": "無料プランで流れを学べます。Pro は納品制限を外し、業務用ブランディングを解放します。",
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
        "monthly_badge": "Pro 月額",
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
        "yearly_badge": "Pro 年額",
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
            {"title": "移动交付团队", "body": "适合通过本地网络或热点运行且不依赖互联网的流程。"},
        ],
        "pricing_eyebrow": "方案",
        "pricing_title": "先免费开始，再用 Pro 扩展",
        "pricing_lead": "免费方案适合熟悉流程。Pro 去掉交付限制并开放品牌自定义能力。",
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
        "hero_lead": "Fotoğrafları yerel galeriden ya da FTP destekli profesyonel fotoğraf makinesinden doğrudan uygulamaya alın, WiFi veya hotspot QR bağlantısını açın, her çekim için ayrı session yönetin, müşteriyi QR galeriye alın ve onaylanan dosyaları aynı cihazdan ZIP olarak teslim edin.",
        "metrics": [
            {"value": "1 cihaz", "label": "Çek, göster, teslim et"},
            {"value": "QR erişim", "label": "WiFi ya da hotspot ile bağlan"},
            {"value": "Çoklu session", "label": "Her çekimi ayrı yönet"},
        ],
        "workflow_title": "QR, session ve teslim tek akışta",
        "workflow_lead": "SnapVend profesyonel fotoğraf makinesinden doğrudan FTP aktarımını, WiFi veya hotspot üzerinden QR bağlantısını, session bazlı müşteri akışını ve teslim sonrası raporlamayı tek operasyon haline getirir.",
        "workflow_cards": [
            {"title": "Fotoğrafları profesyonel kameradan al", "body": "Yerel galeriden seçin ya da FTP destekli profesyonel fotoğraf makinesinden kareleri doğrudan SnapVend akışına aktarın."},
            {"title": "WiFi / hotspot QR bağlantısını başlat", "body": "Aynı ortamda müşteriyi uygulama kurdurmadan ağa alın; bağlantı QR ekranı ağ adı, şifre ve erişim bilgisini net şekilde paylaşsın."},
            {"title": "Session galerisini QR ile aç", "body": "Her müşteri veya etkinlik için ayrı açılan session galerisi, tarayıcıdan QR ile saniyeler içinde açılsın ve seçimler karışmadan ilerlesin."},
            {"title": "Yerel ödeme ve PAC onayı", "body": "İşletme ülkenize göre hazır ödeme yöntemlerini gösterin, seçimi kontrol edin ve PAC doğrulamasını tamamlayın."},
            {"title": "ZIP teslim ve satış raporu", "body": "Onaylanan dosyaları ZIP olarak teslim edin; indirme, satış, dönüşüm ve gelir akışını uygulama içindeki rapor ekranında session mantığını bozmadan izleyin."},
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
        "hero_lead": "Importe fotos desde la galería local o transfiéralas directamente a la app desde una cámara profesional con FTP, abra una session separada para cada trabajo, deje que el cliente entre por QR y entregue los archivos aprobados en ZIP desde el mismo dispositivo.",
        "metrics": [
            {"value": "1 equipo", "label": "Capturar, mostrar y entregar"},
            {"value": "Acceso QR", "label": "El cliente entra en segundos"},
            {"value": "Multi-session", "label": "Cada toma queda separada"},
        ],
        "workflow_title": "QR, sessions y entrega en un solo flujo",
        "workflow_lead": "SnapVend convierte la transferencia directa por FTP desde cámaras profesionales, la gestión por session, el acceso por QR y la entrega en una sola operación de campo.",
        "workflow_cards": [
            {"title": "Importe desde cámara profesional", "body": "Use la galería local o transfiera imágenes directamente a SnapVend desde una cámara profesional compatible con FTP."},
            {"title": "Abra una session separada", "body": "Cree una session distinta para cada cliente, toma o evento para que archivos, elecciones y entregas no se mezclen."},
            {"title": "Abra la galería por QR", "body": "El cliente escanea el QR en la misma red y entra a su propia galería de session en segundos."},
            {"title": "Muestre pago local y confirme PAC", "body": "Enseñe métodos de pago locales según el país del negocio, revise la selección y complete la validación PAC."},
            {"title": "Entregue ZIP y siga la session", "body": "Entregue los archivos aprobados en ZIP y mantenga visible en la app el seguimiento por session y por ingresos."},
        ],
    },
    "fr": {
        "hero_lead": "Importez les photos depuis la galerie locale ou transférez-les directement dans l'app depuis un appareil photo pro compatible FTP, ouvrez une session distincte pour chaque prise de vue, faites entrer le client par QR et livrez les fichiers approuvés en ZIP depuis le même appareil.",
        "metrics": [
            {"value": "1 appareil", "label": "Capturer, montrer, livrer"},
            {"value": "Accès QR", "label": "Le client entre en quelques secondes"},
            {"value": "Multi-session", "label": "Chaque prise reste séparée"},
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
        "hero_lead": "Importieren Sie Fotos aus lokaler Galerie oder uebertragen Sie sie direkt aus einer FTP-faehigen Profikamera in die App, starten Sie fuer jedes Shooting eine eigene Session, lassen Sie Kunden per QR eintreten und liefern Sie freigegebene Dateien als ZIP vom selben Geraet.",
        "metrics": [
            {"value": "1 Geraet", "label": "Aufnehmen, zeigen, liefern"},
            {"value": "QR-Zugang", "label": "Kunden sind in Sekunden drin"},
            {"value": "Multi-Session", "label": "Jedes Shooting bleibt getrennt"},
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
    "pt": {
        "hero_lead": "Importe fotos da galeria local ou transfira direto para o app a partir de uma camera profissional com FTP, abra uma session separada para cada trabalho, deixe o cliente entrar por QR e entregue os arquivos aprovados em ZIP no mesmo dispositivo.",
        "metrics": [
            {"value": "1 aparelho", "label": "Capturar, mostrar e entregar"},
            {"value": "Acesso QR", "label": "Cliente entra em segundos"},
            {"value": "Multi-session", "label": "Cada ensaio fica separado"},
        ],
        "workflow_title": "QR, sessions e entrega no mesmo fluxo",
        "workflow_lead": "SnapVend transforma transferencia FTP direta de camera profissional, gestao por session, acesso por QR e entrega em uma unica operacao de campo.",
        "workflow_cards": [
            {"title": "Importe da camera profissional", "body": "Escolha as fotos na galeria local ou transfira direto para o SnapVend a partir de uma camera profissional com FTP."},
            {"title": "Abra uma session separada", "body": "Crie uma session para cada cliente, ensaio ou evento para manter arquivos, escolhas e entregas organizados."},
            {"title": "Abra a galeria por QR", "body": "O cliente escaneia o QR na mesma rede e entra na propria galeria da session em segundos."},
            {"title": "Mostre pagamento local e confirme PAC", "body": "Exiba metodos locais conforme o pais do negocio, revise a selecao e conclua a validacao do PAC."},
            {"title": "Entregue ZIP e acompanhe a session", "body": "Entregue os arquivos aprovados em ZIP e mantenha visiveis no app o acompanhamento da session e da receita."},
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
        "hero_lead": "استورد الصور من المعرض المحلي او انقلها مباشرة الى التطبيق من كاميرا احترافية تدعم FTP، وافتح session مستقلة لكل جلسة تصوير، ثم دع العميل يدخل عبر QR وسلم الملفات المعتمدة بصيغة ZIP من الجهاز نفسه.",
        "metrics": [
            {"value": "جهاز واحد", "label": "التقاط، عرض، تسليم"},
            {"value": "دخول QR", "label": "العميل يدخل خلال ثوان"},
            {"value": "sessions متعددة", "label": "كل جلسة تبقى منفصلة"},
        ],
        "workflow_title": "QR و sessions والتسليم في تدفق واحد",
        "workflow_lead": "يجمع SnapVend بين النقل المباشر عبر FTP من الكاميرات الاحترافية وادارة sessions ودخول QR والتسليم في عملية ميدانية واحدة.",
        "workflow_cards": [
            {"title": "استيراد من كاميرا احترافية", "body": "اختر الصور من المعرض المحلي او انقل اللقطات مباشرة الى SnapVend من كاميرا احترافية تدعم FTP."},
            {"title": "افتح session مستقلة", "body": "ابدأ session منفصلة لكل عميل او جلسة تصوير او فعالية حتى لا تختلط الملفات والاختيارات وعمليات التسليم."},
            {"title": "افتح المعرض عبر QR", "body": "يمسح العميل QR على الشبكة نفسها ويدخل الى معرض session الخاص به خلال ثوان."},
            {"title": "اعرض الدفع المحلي واكد PAC", "body": "اعرض طرق الدفع المحلية بحسب بلد النشاط وراجع الاختيار ثم اكمل التحقق من PAC."},
            {"title": "سلم ZIP وتابع session", "body": "سلم الملفات المعتمدة بصيغة ZIP وابق تتبع session والايراد ظاهرا داخل التطبيق."},
        ],
    },
    "hi": {
        "hero_lead": "Local gallery se photos lijiye ya professional FTP camera se direct app me transfer kijiye, har shoot ke liye alag session kholiye, client ko QR se andar layein aur approved files ko usi device se ZIP me deliver kijiye.",
        "metrics": [
            {"value": "1 device", "label": "Shoot, show, deliver"},
            {"value": "QR access", "label": "Client seconds me enter kare"},
            {"value": "Multi-session", "label": "Har shoot alag rahe"},
        ],
        "workflow_title": "QR, session aur delivery ek hi flow me",
        "workflow_lead": "SnapVend professional camera se direct FTP intake, session management, QR access aur delivery ko ek hi field workflow me jodta hai.",
        "workflow_cards": [
            {"title": "Professional camera se import karein", "body": "Local gallery se choose karein ya FTP-enabled professional camera se frames direct SnapVend me bhejein."},
            {"title": "Alag session shuru karein", "body": "Har client, shoot ya event ke liye alag session khol kar files, selections aur delivery ko organize rakhein."},
            {"title": "QR se session gallery kholen", "body": "Client usi network par QR scan karke apni session gallery seconds me kholta hai."},
            {"title": "Local payment dikhayein aur PAC confirm karein", "body": "Business country ke hisab se local payment methods dikhayein, selection review karein aur PAC validation complete karein."},
            {"title": "ZIP deliver karein aur session track karein", "body": "Approved files ko ZIP me deliver karein aur app ke andar session-based delivery aur revenue dekhte rahein."},
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
        "hero_lead": "可从本地相册导入照片，也可通过支持 FTP 的专业相机直接传入应用；为每次拍摄建立独立 session，让客户通过 QR 进入，并从同一设备交付已批准的 ZIP 文件。",
        "metrics": [
            {"value": "1 台设备", "label": "拍摄、展示、交付"},
            {"value": "QR 进入", "label": "客户几秒内进入"},
            {"value": "多 session", "label": "每次拍摄独立管理"},
        ],
        "workflow_title": "QR、session 与交付在同一流程中",
        "workflow_lead": "SnapVend 将专业相机的直接 FTP 导入、session 管理、QR 进入和交付整合为一个现场工作流程。",
        "workflow_cards": [
            {"title": "从专业相机导入", "body": "可从本地相册选择，也可通过支持 FTP 的专业相机把照片直接传入 SnapVend。"},
            {"title": "创建独立 session", "body": "为每位客户、每次拍摄或每场活动建立独立 session，让文件、选片和交付互不混淆。"},
            {"title": "通过 QR 打开 session 画廊", "body": "客户在同一网络下扫描 QR，几秒内进入自己的 session 画廊。"},
            {"title": "显示本地支付并确认 PAC", "body": "根据商家所在国家显示本地支付方式，检查所选照片并完成 PAC 验证。"},
            {"title": "交付 ZIP 并追踪 session", "body": "以 ZIP 方式交付已批准文件，并在应用内追踪按 session 区分的交付与收入。"},
        ],
    },
}

FAQ_FLOW_OVERRIDES = {
    "tr": [
        {"q": "SnapVend internetsiz çalışır mı?", "a": "Evet. Ana akış yerel ağ veya hotspot üzerinde çalışabilir. Bulut zorunlu değildir."},
        {"q": "Profesyonel fotoğraf makinesinden doğrudan aktarım yapabilir miyim?", "a": "Evet. FTP destekli profesyonel fotoğraf makinelerinden fotoğrafları aynı ağ veya hotspot üzerinden doğrudan SnapVend uygulamasına aktarabilirsiniz."},
        {"q": "Müşteri fotoğrafları nasıl görür?", "a": "Müşteri önce WiFi ya da hotspot QR bağlantısıyla aynı ağa alınır, ardından session QR kodunu okutup yalnızca kendisine ait galeriyi tarayıcıdan açar."},
        {"q": "Session yapısı ne işe yarar?", "a": "Her müşteri, çekim veya etkinlik ayrı bir session olarak tutulur. Böylece fotoğraflar, seçimler, ödeme akışı ve teslim kayıtları karışmaz; ayrıca her session'ın sonucu daha kontrollü izlenir."},
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
        {"q": "¿SnapVend funciona sin internet?", "a": "Si. El flujo principal puede funcionar con red local o hotspot sin depender de la nube."},
        {"q": "¿Puedo transferir directo desde una camara profesional?", "a": "Si. Puede enviar fotos directamente a SnapVend desde una camara profesional con FTP usando la misma red o hotspot."},
        {"q": "¿Como ve el cliente las fotos?", "a": "El cliente escanea un QR en la misma red, entra a su galeria de session en el navegador y hace alli la seleccion."},
        {"q": "¿Para que sirve la estructura de session?", "a": "Cada cliente, toma o evento puede mantenerse en su propia session para que archivos, selecciones, pago y entrega no se mezclen."},
        {"q": "¿Puedo usar mi propio logo y nombre?", "a": "Si. Los planes Pro desbloquean nombre comercial, logo y entrega con marca propia."},
        {"q": "¿Puedo mostrar metodos de pago segun el pais?", "a": "Si. Al elegir el pais del negocio, los metodos locales configurados aparecen en el popup de pago. Hay metodos listos para Turquia, Espana, India, China y Japon."},
        {"q": "¿Que plan elimina el limite de entrega?", "a": "Los planes Pro mensual y anual eliminan el limite diario."},
    ],
    "fr": [
        {"q": "SnapVend fonctionne t il sans internet ?", "a": "Oui. Le flux principal peut tourner sur reseau local ou hotspot sans cloud obligatoire."},
        {"q": "Puis je transferer directement depuis un appareil photo pro ?", "a": "Oui. Vous pouvez envoyer les photos directement dans SnapVend depuis un appareil photo pro compatible FTP sur le meme reseau ou hotspot."},
        {"q": "Comment le client voit il les photos ?", "a": "Le client scanne un QR sur le meme reseau, ouvre sa galerie de session dans le navigateur et fait ses choix."},
        {"q": "A quoi sert la structure de session ?", "a": "Chaque client, prise de vue ou evenement peut rester dans sa propre session pour que fichiers, choix, paiement et livraison ne se melangent pas."},
        {"q": "Puis je utiliser mon propre logo ?", "a": "Oui. Les plans Pro ouvrent le nom d entreprise, le logo et la livraison personnalisee."},
        {"q": "Puis je afficher des methodes de paiement selon le pays ?", "a": "Oui. Une fois le pays de l entreprise choisi, les methodes locales configurees apparaissent dans la fenetre de paiement. Des ensembles prets existent pour la Turquie, l Espagne, l Inde, la Chine et le Japon."},
        {"q": "Quel plan retire la limite de livraison ?", "a": "Les plans Pro mensuel et annuel retirent la limite quotidienne."},
    ],
    "de": [
        {"q": "Funktioniert SnapVend ohne Internet?", "a": "Ja. Der Hauptablauf kann uber lokales Netzwerk oder Hotspot ohne Cloud laufen."},
        {"q": "Kann ich direkt aus einer Profikamera uebertragen?", "a": "Ja. Fotos koennen ueber dieselbe Netzwerkverbindung oder einen Hotspot direkt aus einer FTP-faehigen Profikamera in SnapVend gehen."},
        {"q": "Wie sehen Kunden die Fotos?", "a": "Kunden scannen im gleichen Netzwerk den QR Code, oeffnen ihre Session-Galerie im Browser und treffen dort die Auswahl."},
        {"q": "Wozu dient die Session-Struktur?", "a": "Jeder Kunde, jedes Shooting oder Event bleibt in einer eigenen Session, damit Dateien, Auswahl, Zahlung und Lieferung nicht vermischt werden."},
        {"q": "Kann ich eigenes Branding nutzen?", "a": "Ja. Pro schaltet Firmenname, Logo und gebrandete Auslieferung frei."},
        {"q": "Kann ich landerspezifische Zahlungsarten zeigen?", "a": "Ja. Sobald das Geschaeftsland gewahlt ist, erscheinen fertig eingerichtete lokale Methoden im Zahlungsfenster. Vorbereitete Sets gibt es fur die Turkei, Spanien, Indien, China und Japan."},
        {"q": "Welcher Plan entfernt das Lieferlimit?", "a": "Sowohl der monatliche als auch der jahrliche Pro Plan entfernen das Tageslimit."},
    ],
    "pt": [
        {"q": "O SnapVend funciona sem internet?", "a": "Sim. O fluxo principal pode rodar em rede local ou hotspot sem depender da nuvem."},
        {"q": "Posso transferir direto de uma camera profissional?", "a": "Sim. As fotos podem entrar direto no SnapVend a partir de uma camera profissional com FTP usando a mesma rede ou hotspot."},
        {"q": "Como o cliente ve as fotos?", "a": "O cliente escaneia um QR na mesma rede, abre sua galeria de session no navegador e faz a selecao ali."},
        {"q": "Para que serve a estrutura de session?", "a": "Cada cliente, ensaio ou evento pode ficar em sua propria session para que arquivos, escolhas, pagamento e entrega nao se misturem."},
        {"q": "Posso usar meu proprio nome e logo?", "a": "Sim. Os planos Pro liberam branding, logo e entrega personalizada."},
        {"q": "Posso mostrar metodos de pagamento por pais?", "a": "Sim. Ao escolher o pais do negocio, os metodos locais configurados aparecem no popup de pagamento. Ha conjuntos prontos para Turquia, Espanha, India, China e Japao."},
        {"q": "Qual plano remove o limite de entrega?", "a": "Os planos Pro mensal e anual removem o limite diario."},
    ],
    "ru": [
        {"q": "Работает ли SnapVend без интернета?", "a": "Да. Основной сценарий может работать через локальную сеть или точку доступа без облака."},
        {"q": "Можно ли передавать напрямую с профессиональной камеры?", "a": "Да. Фото можно отправлять прямо в SnapVend с профессиональной камеры по FTP через ту же сеть или hotspot."},
        {"q": "Как клиент смотрит фотографии?", "a": "Клиент сканирует QR-код в той же сети, открывает свою галерею сессии в браузере и выбирает фотографии там."},
        {"q": "Для чего нужна структура сессий?", "a": "Каждый клиент, съемка или событие могут идти в отдельной сессии, чтобы файлы, выбор, оплата и выдача не смешивались."},
        {"q": "Можно ли использовать свой логотип и бренд?", "a": "Да. Pro открывает фирменное имя, логотип и брендированную выдачу."},
        {"q": "Можно ли показать клиенту способы оплаты по стране?", "a": "Да. После выбора страны бизнеса настроенные локальные методы появляются во всплывающем окне оплаты. Готовые наборы есть для Турции, Испании, Индии, Китая и Японии."},
        {"q": "Какой тариф снимает лимит выдачи?", "a": "И месячный, и годовой Pro снимают ежедневный лимит выдачи."},
    ],
    "ar": [
        {"q": "هل يعمل SnapVend بدون انترنت؟", "a": "نعم. يمكن تشغيل التدفق الرئيسي عبر شبكة محلية او hotspot بدون اعتماد على السحابة."},
        {"q": "هل يمكن النقل مباشرة من كاميرا احترافية؟", "a": "نعم. يمكن نقل الصور مباشرة الى SnapVend من كاميرا احترافية تدعم FTP عبر الشبكة نفسها او hotspot."},
        {"q": "كيف يشاهد العميل الصور؟", "a": "يمسح العميل QR على نفس الشبكة ويدخل الى معرض session الخاص به من المتصفح ويختار الصور هناك."},
        {"q": "ما فائدة بنية sessions؟", "a": "يمكن حفظ كل عميل او جلسة تصوير او فعالية داخل session مستقلة حتى لا تختلط الملفات والاختيارات والدفع والتسليم."},
        {"q": "هل يمكنني استخدام اسمي التجاري وشعاري؟", "a": "نعم. خطط Pro تفتح اسم النشاط والشعار والتسليم بعلامتك الخاصة."},
        {"q": "هل يمكنني عرض طرق دفع حسب البلد للعميل؟", "a": "نعم. عند اختيار بلد النشاط تظهر الطرق المحلية المكتملة في نافذة الدفع. توجد مجموعات جاهزة لتركيا واسبانيا والهند والصين واليابان."},
        {"q": "اي خطة تزيل حد التسليم اليومي؟", "a": "كل من الخطة الشهرية والسنوية Pro يزيلان حد التسليم اليومي."},
    ],
    "hi": [
        {"q": "क्या SnapVend बिना इंटरनेट के काम करता है?", "a": "हाँ। मुख्य workflow लोकल नेटवर्क या hotspot पर चल सकता है, cloud जरूरी नहीं है।"},
        {"q": "क्या मैं professional camera से direct transfer कर सकता हूँ?", "a": "हाँ। FTP-enabled professional camera से photos उसी network या hotspot पर सीधे SnapVend में लाई जा सकती हैं।"},
        {"q": "क्लाइंट फोटो कैसे देखता है?", "a": "क्लाइंट उसी network पर QR scan करके browser में अपनी session gallery खोलता है और वहीं selection करता है।"},
        {"q": "Session structure किस काम आती है?", "a": "हर client, shoot या event को अलग session में रखा जा सकता है ताकि files, selection, payment aur delivery mix न हों।"},
        {"q": "क्या मैं अपना नाम और logo इस्तेमाल कर सकता हूँ?", "a": "हाँ। Pro plans custom branding, logo और branded delivery खोलते हैं।"},
        {"q": "Kya main client ko country-based payment methods dikha sakta hoon?", "a": "Haan. Business country select karne ke baad configured local methods payment popup me dikhte hain. Turkey, Spain, India, China aur Japan ke liye ready method sets maujood hain."},
        {"q": "कौन सा plan delivery limit हटाता है?", "a": "Monthly और yearly दोनों Pro plans daily delivery limit हटाते हैं।"},
    ],
    "ja": [
        {"q": "SnapVend はインターネットなしで使えますか？", "a": "はい。主なフローはローカルネットワークや hotspot 上で動作でき、クラウドは必須ではありません。"},
        {"q": "プロ向けカメラから直接取り込めますか？", "a": "はい。FTP 対応のプロ向けカメラから、同じネットワークや hotspot を通じて SnapVend へ直接取り込めます。"},
        {"q": "クライアントはどうやって写真を見ますか？", "a": "同じネットワーク上で QR を読み取り、自分のセッションギャラリーをブラウザで開いて選択します。"},
        {"q": "セッション構造は何のためにありますか？", "a": "顧客、撮影、イベントごとに個別のセッションで管理できるため、ファイル、選択、支払い、納品が混ざりません。"},
        {"q": "自分のブランド名やロゴを使えますか？", "a": "はい。Pro プランで独自ブランド名、ロゴ、ブランド納品が使えます。"},
        {"q": "国ごとの決済方法をクライアントに表示できますか？", "a": "はい。事業国を選ぶと、設定済みのローカル決済方法が支払いポップアップに表示されます。トルコ、スペイン、インド、中国、日本向けの方法セットが用意されています。"},
        {"q": "どのプランで納品制限がなくなりますか？", "a": "月額 Pro と年額 Pro の両方で日次納品制限が解除されます。"},
    ],
    "zh": [
        {"q": "SnapVend 可以在没有互联网时使用吗？", "a": "可以。主要流程可在本地网络或 hotspot 上运行，不依赖云端。"},
        {"q": "可以直接从专业相机传入吗？", "a": "可以。支持 FTP 的专业相机可通过同一网络或 hotspot 直接把照片传入 SnapVend。"},
        {"q": "客户如何查看照片？", "a": "客户在同一网络中扫描 QR 后，就能在浏览器里打开自己的 session 画廊并完成选片。"},
        {"q": "session 结构有什么作用？", "a": "每位客户、每次拍摄或每场活动都可以放在独立 session 中，这样文件、选片、付款和交付记录不会混在一起。"},
        {"q": "我可以使用自己的品牌名和 logo 吗？", "a": "可以。Pro 计划会开放自定义品牌名、logo 和品牌化交付。"},
        {"q": "可以向客户显示按国家配置的支付方式吗？", "a": "可以。选择商家所在国家后，已完成设置的本地支付方式会显示在支付弹窗中。目前已为土耳其、西班牙、印度、中国和日本准备了现成方式。"},
        {"q": "哪个计划会移除交付限制？", "a": "月度 Pro 和年度 Pro 都会移除每日交付限制。"},
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
        "audience_body": "यह wedding teams के लिए खास तौर पर मजबूत flow है, जहां fast selection, instant delivery aur print list ek hi operation me manage kiye jate hain.",
        "use_case": {
            "title": "Wedding print list",
            "body": "Couple, family aur guest selections collect karte hue print-ready photos ko alag print list me rakhein, taki digital delivery rukhe bina on-site printing chalti rahe.",
        },
        "reference": {
            "title": "Wedding print aur delivery teams",
            "body": "Un wedding photographers ke liye bana hai jo digital delivery aur print preparation ko ek hi operation me chalana chahte hain.",
        },
        "faq": {
            "q": "Print list kya karti hai?",
            "a": "Print list selected photos ko delivery flow tode bina print ke liye ready rakhti hai. Isse wedding teams ko yeh track karna aasaan hota hai ki kaunsi photos print hongi aur print preparation kaise aage badhegi.",
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

for locale_code, overrides in PRINT_QUEUE_OVERRIDES.items():
    COPY[locale_code]["audience_cards"][0]["body"] = overrides["audience_body"]
    PROOF_SECTION[locale_code]["use_cases"].insert(1, overrides["use_case"])
    PROOF_SECTION[locale_code]["references"].insert(0, overrides["reference"])
    FAQ_SECTION[locale_code]["items"].insert(-1, overrides["faq"])

BRAND_MOTTO_BY_LOCALE = {
    "tr": "Çek - Göster - Sat",
    "en": "Shoot - Show - Sell",
    "es": "Captura - Muestra - Vende",
    "fr": "Capture - Montre - Vends",
    "de": "Aufnehmen - Zeigen - Verkaufen",
    "pt": "Capture - Mostre - Venda",
    "ru": "Сними - Покажи - Продай",
    "ar": "التقط - اعرض - بع",
    "hi": "शूट - दिखाओ - बेचो",
    "ja": "撮る - 見せる - 売る",
    "zh": "拍摄 - 展示 - 销售",
}

MARKETING_ASSETS = {
    "hero_main": "assets/marketing/google_play/web/01_gallery_dashboard_web.png",
    "hero_secondary": "assets/marketing/google_play/web/02_session_qr_access_web.png",
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


def flag_emoji(country_code: str) -> str:
    if len(country_code) != 2:
        return ""
    return "".join(chr(127397 + ord(char.upper())) for char in country_code)


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
    for locale_code in LOCALE_ORDER:
        meta = LOCALE_META[locale_code]
        active = " language-option-active" if locale_code == current_code else ""
        flag = flag_emoji(meta["app_store_country"])
        items.append(
            f'              <a class="language-option{active}" href="{relative_page_href(current_code, locale_code)}" lang="{locale_code}" hreflang="{meta["hreflang"][0]}"><span class="language-flag" aria-hidden="true">{flag}</span><span class="language-name">{e(meta["native"])}</span></a>'
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


def build_keyword_string(copy: dict, proof: dict, contact: dict) -> str:
    values = [
        "SnapVend",
        copy["brand_motto"],
        copy["hero_eyebrow"],
        copy["workflow_title"],
        copy["audience_title"],
        proof["title"],
        contact["title"],
        *[card["title"] for card in copy["workflow_cards"]],
        *[card["title"] for card in copy["audience_cards"]],
        *[card["title"] for card in proof["use_cases"]],
        *[card["title"] for card in proof["references"]],
        *copy["monthly_features"],
        *copy["yearly_features"],
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
    country = LOCALE_META[locale_code]["app_store_country"]
    fallback_search = f"https://apps.apple.com/{country}/search?term=SnapVend"
    return f"""
            <div class="store-badges">
              <a class="store-badge store-badge-play" data-store-link="googlePlay" href="https://play.google.com/store/apps/details?id=com.snapvend.gallery" target="_blank" rel="noreferrer">
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

              <a class="store-badge store-badge-apple" data-store-link="appStore" data-app-store-search="{fallback_search}" href="{fallback_search}" target="_blank" rel="noreferrer">
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
            </div>"""


def build_schema(locale_code: str, copy: dict, faq: dict, proof: dict, contact: dict, keywords: str) -> str:
    pricing = SCHEMA_PRICING[locale_code]
    page_url = canonical_url(locale_code)
    logo_url = f"{SITE_URL}{BRAND_MARK_ASSET}"
    contact_point_id = f"{SITE_URL}/#sales-contact"
    screenshot_urls = [
        f"{SITE_URL}/{marketing_asset('hero_main')}",
        f"{SITE_URL}/{marketing_asset('hero_secondary')}",
        f"{SITE_URL}/{marketing_asset('workflow_ftp')}",
        f"{SITE_URL}/{marketing_asset('workflow_dashboard')}",
        f"{SITE_URL}/{marketing_asset('workflow_qr')}",
        f"{SITE_URL}/{marketing_asset('workflow_http_gallery', 'en')}",
        f"{SITE_URL}/{marketing_asset('workflow_payment')}",
        f"{SITE_URL}/{marketing_asset('schema_report')}",
    ]
    audience_list = build_item_list_schema(page_url, "audience", copy["audience_title"], copy["audience_cards"])
    use_case_list = build_item_list_schema(page_url, "use-cases", proof["use_label"], proof["use_cases"])
    reference_profile_list = build_item_list_schema(page_url, "reference-profiles", proof["reference_label"], proof["references"])
    contact_topic_set = build_defined_term_set_schema(page_url, "contact-topics", contact["type_label"], contact["topics"])

    contact_point = {
        "@type": "ContactPoint",
        "@id": contact_point_id,
        "contactType": "sales",
        "email": "snapvendinfo@gmail.com",
        "url": "mailto:snapvendinfo@gmail.com",
        "availableLanguage": [LOCALE_META[code]["native"] for code in LOCALE_ORDER],
    }

    organization = {
        "@type": "Organization",
        "@id": f"{SITE_URL}/#organization",
        "name": "SnapVend",
        "slogan": copy["brand_motto"],
        "url": f"{SITE_URL}/",
        "logo": {
            "@type": "ImageObject",
            "url": logo_url,
        },
        "image": logo_url,
        "contactPoint": [{"@id": contact_point_id}],
    }

    website = {
        "@type": "WebSite",
        "@id": f"{SITE_URL}/#website",
        "url": f"{SITE_URL}/",
        "name": "SnapVend",
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
            {"@id": use_case_list["@id"]},
            {"@id": reference_profile_list["@id"]},
            {"@id": f"{page_url}#faq"},
            {"@id": f"{page_url}#contact-page"},
            {"@id": contact_topic_set["@id"]},
        ],
    }

    software = {
        "@type": "SoftwareApplication",
        "@id": f"{page_url}#app",
        "name": "SnapVend",
        "description": copy["meta_description"],
        "applicationCategory": "BusinessApplication",
        "applicationSubCategory": "Photo workflow, print management and delivery",
        "operatingSystem": "ANDROID, IOS",
        "inLanguage": locale_code,
        "availableLanguage": [LOCALE_META[code]["native"] for code in LOCALE_ORDER],
        "url": page_url,
        "mainEntityOfPage": page_url,
        "image": logo_url,
        "screenshot": screenshot_urls,
        "keywords": keywords,
        "brand": {
            "@type": "Brand",
            "name": "SnapVend",
        },
        "publisher": {"@id": organization["@id"]},
        "isAccessibleForFree": True,
        "featureList": unique_strings(
            [card["title"] for card in copy["workflow_cards"]]
            + copy["monthly_features"]
            + copy["yearly_features"]
            + [card["title"] for card in proof["use_cases"][:2]]
        ),
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
        "downloadUrl": "https://play.google.com/store/apps/details?id=com.snapvend.gallery",
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
            use_case_list,
            reference_profile_list,
            contact_topic_set,
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
    contact_copy = CONTACT_SECTION[locale_code]
    metrics = build_metric_cards(copy)
    demo_steps = build_demo_steps(demo_copy)
    workflow_cards = build_workflow_cards(copy)
    audience_cards = build_audience_cards(copy)
    proof_use_cases = build_proof_cards(proof_copy["use_cases"])
    proof_references = build_proof_cards(proof_copy["references"])
    faq_items = build_faq_items(faq_copy)
    contact_highlights = build_contact_highlights(contact_copy)
    contact_topics = build_contact_topics(contact_copy)
    keyword_string = build_keyword_string(copy, proof_copy, contact_copy)
    schema_json = build_schema(locale_code, copy, faq_copy, proof_copy, contact_copy, keyword_string)
    active_flag = flag_emoji(meta["app_store_country"])
    popular_label = POPULAR_LABELS[locale_code]

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
    <meta name="application-name" content="SnapVend">
    <meta property="og:site_name" content="SnapVend">
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
    <link rel="stylesheet" href="{prefix}/styles.css">
    <script type="application/ld+json">{schema_json}</script>
    <script defer src="{prefix}/site-config.js"></script>
    <script defer src="{prefix}/script.js"></script>
  </head>
  <body>
    <div class="page-aura page-aura-left" aria-hidden="true"></div>
    <div class="page-aura page-aura-right" aria-hidden="true"></div>

    <header class="topbar">
      <div class="container topbar-inner">
        <a class="brand" href="{relative_page_href(locale_code, locale_code)}">
          <img class="brand-mark" src="{prefix}{BRAND_MARK_SITE_ASSET}" alt="SnapVend" width="120" height="120" decoding="async" fetchpriority="high">
          <span class="brand-copy">
            <span class="brand-kicker">Professional Photo Delivery</span>
            <strong>SnapVend</strong>
          </span>
        </a>

        <nav class="topnav" aria-label="Sections">
          <a href="#demo">{e(extra_nav["demo"])}</a>
          <a href="#how-it-works">{e(copy["nav_how"])}</a>
          <a href="#audience">{e(copy["nav_audience"])}</a>
          <a href="#pricing">{e(copy["nav_pricing"])}</a>
          <a href="#faq">{e(extra_nav["faq"])}</a>
        </nav>

        <div class="topbar-actions">
          <a class="pill-link" href="#download">{e(copy["nav_download"])}</a>
          <details class="language-switcher">
            <summary><span class="language-summary"><span class="language-flag" aria-hidden="true">{active_flag}</span><span>{e(copy["language_label"])}</span></span></summary>
            <div class="language-menu">
{language_menu}
            </div>
          </details>
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
            <p class="setup-note" data-setup-note data-nosnippet hidden>{e(copy["setup_note"])}</p>

            <div class="metric-grid">
{metrics}
            </div>
          </div>

          <div class="hero-visual reveal">
            <article class="visual-frame visual-frame-main">
              <img src="{prefix}/{marketing_asset('hero_main', locale_code)}" alt="SnapVend home dashboard with live gallery and session overview" width="324" height="720" loading="eager" decoding="async" fetchpriority="high">
            </article>
            <article class="visual-frame visual-frame-secondary">
              <img src="{prefix}/{marketing_asset('hero_secondary', locale_code)}" alt="SnapVend WiFi and hotspot QR connection screen" width="324" height="720" loading="eager" decoding="async">
            </article>
            <article class="visual-chip">
              <span>SnapVend</span>
              <p class="visual-chip-motto">{e(copy["brand_motto"])}</p>
            </article>
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
                <strong>SnapVend</strong>
              </div>
              <div class="demo-stage-screen">
                <video class="demo-video" data-demo-video playsinline autoplay muted loop controls hidden></video>
                <div class="demo-placeholder" data-demo-fallback>
                  <span class="demo-placeholder-play" aria-hidden="true"></span>
                  <strong>SnapVend</strong>
                  <p>{e(demo_copy["screen_label"])}</p>
                </div>
              </div>
              <p class="demo-stage-note">{e(demo_copy["screen_note"])}</p>
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
                <img src="{prefix}/{marketing_asset('workflow_ftp', locale_code)}" alt="SnapVend FTP server settings for professional cameras" width="324" height="720" loading="lazy" decoding="async">
              </article>
              <article class="shot-card shot-card-dashboard">
                <img src="{prefix}/{marketing_asset('workflow_dashboard', locale_code)}" alt="SnapVend gallery home dashboard" width="324" height="720" loading="lazy" decoding="async">
              </article>
              <article class="shot-card shot-card-qr">
                <img src="{prefix}/{marketing_asset('workflow_qr', locale_code)}" alt="SnapVend QR codes and session access screen" width="324" height="720" loading="lazy" decoding="async">
              </article>
              <article class="shot-card shot-card-http">
                <img src="{prefix}/{marketing_asset('workflow_http_gallery', locale_code)}" alt="SnapVend HTTP gallery with selected photos" width="324" height="720" loading="lazy" decoding="async">
              </article>
              <article class="shot-card shot-card-payment">
                <img src="{prefix}/{marketing_asset('workflow_payment', locale_code)}" alt="SnapVend payment approval and delivery options screen" width="324" height="720" loading="lazy" decoding="async">
              </article>
            </div>
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

          <p class="config-warning reveal" data-config-warning data-nosnippet hidden>{e(copy["config_warning"])}</p>

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


def write_page(locale_code: str) -> None:
    meta = LOCALE_META[locale_code]
    output_dir = ROOT if meta["path"] == "" else ROOT / meta["path"]
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "index.html").write_text(render_page(locale_code), encoding="utf-8")


def write_manifest() -> None:
    manifest = {
        "name": "SnapVend",
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
    write_manifest()
    write_robots()
    write_sitemap()


if __name__ == "__main__":
    main()
