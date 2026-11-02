# -*- coding: utf-8 -*-
"""Контент сайта KAPM — русская версия. Тексты согласованы в документе «KAPM — карта сайта и тексты (RU)»."""
import datetime

SITE = dict(site="https://kapm.uz", langs=["ru", "en", "uz"], build=datetime.date.today().strftime("%Y%m%d"),
            legal_name="ООО «KAPM»", inn="313 133 475", email="ceo@acre.estate",
            address_short="Ташкент, Мирзо-Улугбекский р-н,<br>1-й пр. Дархан, 7",
            address_legal="г. Ташкент, Шайхантахурский район, махалля «Yangishahar», ул. Ko'kcha Darvoza, д. 314",
            linkedin="https://www.linkedin.com/in/artem-kudriashov-4591772a1/",
            form_action="https://formspree.io/f/REPLACE_ME")  # TODO: вставить реальный endpoint формы

L = dict(locale="ru_RU", skip="К содержанию", nav_label="Главное меню", menu="Меню", cta_short="Обсудить проект",
         nav=[("services", "/services/", "Услуги"), ("sectors", "/sectors/", "Секторы"), ("projects", "/projects/", "Проекты"),
              ("about", "/about/", "О компании"), ("insights", "/insights/", "Экспертиза"), ("contact", "/contact/", "Контакты")],
         cta_h="Нужен ответственный за ваш объект?", cta_p="Напишите нам о проекте — предложим формат участия и стоимость услуг в течение одного рабочего дня.", cta_btn="Обсудить проект",
         foot_tag="Управление строительством на стороне заказчика. When you need to be sure.",
         foot_services_h="УСЛУГИ", foot_company_h="КОМПАНИЯ", foot_contact_h="СВЯЗЬ",
         foot_services=[("/services/technical-customer/", "Технический заказчик"), ("/services/project-management/", "Управление проектом и строительством"), ("/services/construction-supervision/", "Строительный контроль и технадзор"), ("/services/cost-management/", "Контроль стоимости")],
         foot_company=[("/about/", "О компании"), ("/about/#leadership", "Руководство"), ("/projects/", "Проекты"), ("/insights/", "Экспертиза"), ("/contact/", "Контакты")],
         inn="ИНН", privacy="Политика конфиденциальности",
         cookie="Сайт использует файлы cookie для аналитики. Продолжая, вы соглашаетесь с политикой:", cookie_ok="Принять", cookie_no="Отклонить")

IMG = dict(hero="/assets/img/img_5100.jpg", nature="/assets/img/img_4850.jpg", robotis="/assets/img/img_4972.jpg", robotis_hero="/assets/img/img_5101.jpg",
           wh1370="/assets/img/img_1370.jpg", wh1318="/assets/img/img_1318.jpg", bonded="/assets/img/img_9078.jpg", wh8290="/assets/img/img_8290.jpg",
           toyota="/assets/img/img_9780.jpg", toyota_off="/assets/img/img_9563.jpg", sbi="/assets/img/img_8435.jpg", griffin="/assets/img/img_7123.jpg",
           service="/assets/img/img_5237.jpg", about="/assets/img/img_5303.jpg", portrait="/assets/img/portrait.jpg",
           g1="/assets/img/img_5068.jpg", g2="/assets/img/img_5106.jpg", g3="/assets/img/img_5110.jpg", g4="/assets/img/img_5035.jpg", g5="/assets/img/img_5111.jpg")

CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="#0F57D8" stroke-width="2.2" aria-hidden="true"><path d="M5 12l5 5 9-10"/></svg>'
ICONS = {
 "tc": '<svg viewBox="0 0 24 24" fill="none" stroke="#0A1F44" stroke-width="1.6" aria-hidden="true"><path d="M9 4h6v3H9zM6 7h12v13H6zM9 12h6M9 16h4"/></svg>',
 "pm": '<svg viewBox="0 0 24 24" fill="none" stroke="#0A1F44" stroke-width="1.6" aria-hidden="true"><path d="M4 19h16M6 19V9l6-5 6 5v10M10 19v-5h4v5"/></svg>',
 "cs": '<svg viewBox="0 0 24 24" fill="none" stroke="#0A1F44" stroke-width="1.6" aria-hidden="true"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6l8-3zM8.5 12l2.5 2.5 4.5-5"/></svg>',
 "cm": '<svg viewBox="0 0 24 24" fill="none" stroke="#0A1F44" stroke-width="1.6" aria-hidden="true"><path d="M4 20V10M10 20V4M16 20v-8M22 20H2M19 7l-5 5-3-3-5 5"/></svg>'}

def ph(src, alt="", h=None, cls=""):
    st = f' style="height:{h}px"' if h else ""
    if src: return f'<div class="ph {cls}"{st}><img src="{src}" alt="{alt}" loading="lazy"></div>'
    return f'<div class="ph ph-e {cls}"{st}>Фото скоро</div>'

def li(items): return "".join(f'<div class="li">{CHECK}<span>{t}</span></div>' for t in items)

# ---------- данные ----------
SERVICES = [
 dict(slug="technical-customer", icon="tc", name="Технический заказчик", short="Все функции заказчика по закону и по сути: ИРД, экспертиза, согласования, разрешение на строительство, ввод в эксплуатацию.",
      eyebrow="Услуга · Owner's Representative",
      lead="Выполняем все функции заказчика по объекту — от получения исходно-разрешительной документации до акта ввода в эксплуатацию. Вы принимаете решения, мы обеспечиваем их исполнение и отвечаем за соответствие нормам Узбекистана.",
      task="Получить готовый объект с полным комплектом документов, не создавая собственную строительную дирекцию и не разбираясь в ШНК, экспертизе и порядке ввода.",
      who="Частные инвесторы, иностранные компании, открывающие производство или офис в Узбекистане, девелоперы без собственного ОКСа.",
      do=["Исходно-разрешительная документация: АПЗ, техусловия, согласования с сетевыми организациями", "Сопровождение проектирования: задание на проектирование, контроль проектировщика, проверка решений на стоимость и реализуемость", "Экспертиза проекта и получение разрешения на строительство", "Выбор подрядчиков, подготовка и сопровождение договоров", "Контроль строительства по срокам, бюджету и качеству", "Авторский и технический надзор, исполнительная документация", "Приёмка объекта, заключение о соответствии, ввод в эксплуатацию и передача службе эксплуатации"],
      get="Объект, введённый в эксплуатацию с полным комплектом исполнительной и разрешительной документации; одного ответственного вместо десяти.",
      projects=["robotis", "wh7500"], photo="service",
      faq=[("Чем технический заказчик отличается от генподрядчика?", "Генподрядчик строит и отвечает за работы; технический заказчик представляет инвестора, контролирует генподрядчика и отвечает за объект в целом."), ("Сколько стоят услуги технического заказчика?", "Вознаграждение считается как процент от бюджета строительства или как ежемесячный фикс на период проекта — формат согласуем под объект. Стоимость окупается за счёт проверенных актов и исключения переделок."), ("Можно ли подключить KAPM на уже идущей стройке?", "Да. Начинаем с двухнедельного аудита состояния проекта: сроки, деньги, риски, план действий."), ("Работаете ли с иностранными инвесторами?", "Да. Отчётность на английском, знание требований международных операторов и банков.")],
      title="Технический заказчик в Узбекистане — KAPM", desc="Функции технического заказчика по полному циклу: ИРД, экспертиза, разрешение, контроль, ввод в эксплуатацию. Ташкент, Узбекистан."),
 dict(slug="project-management", icon="pm", name="Управление проектом и строительством", short="График, бюджет, тендеры, контракты, координация участников и отчётность инвестору — один ответственный за весь процесс.",
      eyebrow="Услуга · Project & Construction Management",
      lead="Один руководитель проекта от KAPM отвечает за то, чтобы проект шёл по графику, укладывался в бюджет и был прозрачен для инвестора. Project Management, Construction Management и представительство интересов заказчика в одном пакете.",
      task="У проекта много участников — проектировщик, подрядчики, поставщики, банк, госорганы — и никто не отвечает за целое.",
      who="Инвесторы с несколькими проектами, компании с ОКСом, которому не хватает рук, банки и фонды, финансирующие строительство.",
      do=["Структура проекта: этапы, график, бюджет, матрица ответственности", "Тендеры и контрактация: пакеты работ, квалификация подрядчиков, сравнение предложений, переговоры, договоры с защитой интересов заказчика", "Координация участников: еженедельные совещания, протоколы, контроль исполнения решений", "Управление сроками и бюджетом: план-факт, прогноз завершения, управление изменениями", "Управление рисками: реестр рисков, меры реагирования, резервы", "Отчётность инвестору и банку: еженедельный и ежемесячный отчёт по срокам, деньгам, качеству и рискам", "Представительство заказчика на площадке, перед подрядчиками, оператором и госорганами"],
      get="Проект под контролем с первого дня, понятные отчёты и ранние предупреждения вместо сюрпризов на финише.",
      projects=["toyota", "hotel"], photo="g4",
      faq=[("Чем управление проектом отличается от генподряда?", "Генподрядчик выполняет работы и заинтересован в их объёме и цене. Управляющий проектом работает на стороне заказчика, не строит сам и отвечает за срок, бюджет и качество в целом."), ("В каком формате вы отчитываетесь?", "Еженедельный отчёт по графику, деньгам, качеству и рискам; ежемесячный — для инвестора и банка, при необходимости на английском."), ("Можно ли подключиться на этапе проектирования?", "Да, и это лучший момент: большинство проблем стройки закладывается в проекте и договорах с подрядчиками.")],
      title="Управление строительными проектами — KAPM, Ташкент", desc="Project & Construction Management на стороне инвестора: график, бюджет, тендеры, координация, отчётность. Узбекистан."),
 dict(slug="construction-supervision", icon="cs", name="Строительный контроль и технический надзор", short="Качество работ и материалов, объёмы, скрытые работы, охрана труда, приёмка — каждый этап проверен до оплаты.",
      eyebrow="Услуга · Construction Supervision",
      lead="Независимые инженеры KAPM на площадке проверяют каждый этап работ до того, как заказчик за него заплатит. Качество, объёмы, материалы, скрытые работы, охрана труда — по проекту и нормам, а не по словам подрядчика.",
      task="Подрядчик отчитывается сам за себя; ошибки обнаруживаются после оплаты, когда исправлять дорого или поздно.",
      who="Заказчики с действующим генподрядом, собственники помещений при ремонте и реконструкции, операторы отелей и производств.",
      do=["Входной контроль проектной документации и материалов", "Освидетельствование скрытых работ и ответственных конструкций", "Контроль качества работ по ШНК и проекту, предписания подрядчику", "Проверка объёмов и актов выполненных работ перед оплатой", "Контроль графика производства работ", "Контроль охраны труда и безопасности на площадке (HSE)", "Ведение журналов, исполнительной документации, фотофиксация", "Участие в приёмке и передаче объекта"],
      get="Оплаченные работы равны выполненным; дефекты найдены до закрытия, а не после заселения.",
      projects=["hotel", "eventhall"], photo="g2",
      faq=[("Сколько инженеров будет на площадке?", "Зависит от объёма и интенсивности работ: от одного инженера с регулярными выездами до постоянной группы на крупном объекте."), ("Что происходит, когда вы находите нарушение?", "Выдаём подрядчику предписание с фотофиксацией и сроком устранения, не подписываем акт до исправления и информируем заказчика."), ("Нужен ли технадзор, если есть авторский надзор проектировщика?", "Да. Авторский надзор следит за соответствием проекту, технадзор — за качеством, объёмами, безопасностью и деньгами заказчика.")],
      title="Строительный контроль и технадзор — KAPM", desc="Независимый строительный контроль и технический надзор заказчика в Узбекистане: качество, объёмы, скрытые работы, HSE, приёмка."),
 dict(slug="cost-management", icon="cm", name="Контроль стоимости", short="Проверка смет и актов, протоколы цен, управление изменениями и претензиями — вы платите только за то, что сделано.",
      eyebrow="Услуга · Cost Management",
      lead="Проверяем каждую цифру, которую вам предъявляют к оплате: сметы, акты, протоколы цен, дополнительные работы. Завышения в актах подрядчиков — обычная практика, и их стоимость многократно превышает стоимость контроля.",
      task="Сметы и акты подрядчика сложно проверить без собственного сметчика и инженера; разногласия превращаются в претензии и остановку работ.",
      who="Инвесторы и банки, финансирующие строительство; заказчики с действующим договором генподряда; компании, которым нужна независимая проверка смет.",
      do=["Бюджет проекта и проверка сметной документации до договора", "Проверка актов выполненных работ, форм Ф-2 и Ф-3 до оплаты", "Протоколы согласования цен на материалы и оборудование", "Управление изменениями: оценка дополнительных работ, согласование стоимости и сроков", "Претензионная работа и защита позиции заказчика при разногласиях с подрядчиком", "Ежемесячный отчёт план-факт по бюджету и прогноз итоговой стоимости"],
      get="Подтверждённая стоимость каждого платежа и прогноз итоговой стоимости объекта, которому можно верить.",
      projects=["hotel", "robotis"], photo="g3",
      faq=[("Как считается вознаграждение за контроль стоимости?", "Процент от проверяемого объёма или фиксированная ставка за документ — выбираем формат под поток актов на объекте."), ("Можно ли проверить сметы до подписания договора с подрядчиком?", "Да, это самый выгодный момент: правки в смете до договора стоят ничего, после — становятся претензией."), ("Что вы делаете при споре с подрядчиком?", "Готовим обоснованную позицию заказчика с расчётами и ссылками на нормы, участвуем в переговорах и при необходимости — в претензионной работе.")],
      title="Контроль стоимости строительства, проверка смет — KAPM", desc="Проверка смет и актов, протоколы цен, управление изменениями и претензиями в интересах заказчика. Ташкент.")]

SECTORS = [
 dict(slug="industrial-logistics", name="Промышленность и логистика", photo="wh1370",
      short="Заводы, склады, логистические парки — объекты, где цена ошибки измеряется простоем производства. Опыт: 115 000+ м² в Узбекистане и Казахстане.",
      lead="Заводы, склады и логистические парки — объекты, где срок ввода напрямую равен деньгам: каждый месяц задержки — это простой производства, невыполненные контракты и аренда временных площадей. Команда KAPM построила и запустила более 115 000 м² промышленной и складской недвижимости в Узбекистане и Казахстане.",
      points=["Технология первична: планировка, нагрузки на полы, инженерные мощности и логистика потоков задаются процессом, а не наоборот", "Монтаж оборудования идёт параллельно со строительством — нужна координация строителей, поставщиков оборудования и пусконаладки в одном графике", "Требования к полам, кровле, воротам и инженерии складов класса A отличаются от обычной стройки и редко знакомы местным подрядчикам", "Иностранный инвестор ждёт отчётность и стандарты своей страны, а разрешения и экспертиза — узбекские"],
      how="Начинаем с технологической схемы и логистики потоков, закладываем монтаж оборудования в график с первого дня, ведём единый реестр интерфейсов между строителями и поставщиками оборудования.",
      projects=["robotis", "wh25000", "bonded", "wh7500", "griffin", "magnit"],
      title="Строительство заводов и складов: управление проектом — KAPM", desc="Техзаказчик, управление проектом и контроль для промышленных и логистических объектов в Узбекистане: 115 000+ м² опыта."),
 dict(slug="hospitality", name="Гостиницы и HoReCa", photo=None,
      short="Отели международных брендов строятся по стандартам оператора, и мы знаем, как провести объект через их приёмку. Опыт: Hilton Garden Inn, Hyatt.",
      lead="Отель международного бренда принимает не заказчик, а оператор — по своим стандартам, со своими инспекциями и правом не открыть объект. KAPM знает эти стандарты изнутри и ведёт объект так, чтобы приёмка оператора прошла с первого раза.",
      points=["Бренд-стандарты оператора (Hilton, Hyatt и др.) определяют материалы, инженерию, безопасность и отделку — отклонения выявляются на инспекциях и останавливают открытие", "Инженерные системы отеля сложнее, чем в офисе или жилье: вентиляция номеров, пожарная безопасность, кухни, прачечные, слаботочные системы", "Сроки открытия привязаны к сезону и маркетингу оператора; сдвиг даты стоит дороже, чем в любом другом секторе", "Финансирование часто банковское — нужна отчётность в формате кредитора"],
      how="Проверяем проект на соответствие бренд-стандартам до строительства, ведём реестр замечаний оператора как часть графика, сопровождаем все инспекции бренда и готовим объект к ним.",
      projects=["hotel", "eventhall", "hyatt"],
      title="Строительство отелей под брендом: контроль заказчика — KAPM", desc="Управление строительством и строительный контроль отелей международных брендов в Узбекистане: Hilton Garden Inn, Hyatt.")]

# проекты: key -> dict; sector keys: ind, hosp, office, resid, eng; country: uz, kz, ru, cy, tr
PROJECTS = {
 "robotis": dict(name="Завод по производству робототехники в Ташкенте", place="Ташкент", sector="ind", sec_label="Промышленность", country="uz", role="Представитель заказчика", num="22 000", unit="м²", photo="robotis", kapm=True, page=True),
 "hotel": dict(name="Отель международного бренда, 212 номеров", place="Бухара", sector="hosp", sec_label="Гостиницы", country="uz", role="Строительный контроль заказчика", num="20 700", unit="м²", photo=None, kapm=True),
 "eventhall": dict(name="Event Hall Бухара", place="Бухара", sector="hosp", sec_label="Гостиницы", country="uz", role="Строительный контроль заказчика", num=None, photo=None, kapm=True),
 "toyota": dict(name="Toyota Motors Central Asia / Toyota Academy", place="Ташкент", sector="office", sec_label="Офисы", country="uz", role="Управление проектом", num="2 500", unit="м²", photo="toyota", kapm=True),
 "sbi": dict(name="SBI Group: офис, торговая зона Uzum + Ucell, капремонт офиса", place="Ташкент", sector="office", sec_label="Офисы, ритейл", country="uz", role="Управление и производство работ", num=None, photo="sbi", kapm=True),
 "wh25000": dict(name="Склад с монтажом промышленного оборудования", place="Ташкент", sector="ind", sec_label="Логистика", country="uz", role="Технический заказчик", num="25 000", unit="м²", photo="wh1318", kapm=True),
 "wh7500": dict(name="Склад 7 500 м²", place="Ташкент", sector="ind", sec_label="Логистика", country="uz", role="Технический заказчик", num="7 500", unit="м²", photo="wh1370", kapm=True),
 "bonded": dict(name="Bonded-склад с монтажом оборудования", place="Ташкент", sector="ind", sec_label="Логистика", country="uz", role="Технический заказчик", num="7 000", unit="м²", photo="bonded", kapm=True),
 "griffin": dict(name="Логистический парк 64 000 м²", place="Алматы", sector="ind", sec_label="Логистика", country="kz", role="Опыт команды", photo="griffin"),
 "magnit": dict(name="Склад Магнит Маркет 25 000 м²", place="Казань", sector="ind", sec_label="Логистика", country="ru", role="Опыт команды", photo=None),
 "hyatt": dict(name="Hyatt: инфраструктура и гидроизоляция", place="Ташкент", sector="hosp", sec_label="Гостиницы", country="uz", role="Опыт команды", photo=None),
 "hills": dict(name="ЖК Hills Blue, Юнусабад", place="Ташкент", sector="resid", sec_label="Жильё", country="uz", role="Опыт команды", photo=None),
 "nirvana": dict(name="Жилой комплекс, Яккасарай", place="Ташкент", sector="resid", sec_label="Жильё", country="uz", role="Опыт команды", photo=None),
 "moscow": dict(name="Moscow City", place="Москва", sector="office", sec_label="Коммерческая", country="ru", role="Опыт команды", photo=None),
 "bridge": dict(name="Большепролётный вантовый мост", place="Санкт-Петербург", sector="eng", sec_label="Инфраструктура", country="ru", role="Опыт команды", photo=None),
 "istanbul": dict(name="ЖК и коммерческие объекты", place="Стамбул", sector="resid", sec_label="Жильё, коммерческая", country="tr", role="Опыт команды", photo=None),
 "cic": dict(name="Центр исламской цивилизации", place="Ташкент", sector="eng", sec_label="Конструктор", country="uz", role="Конструкторские работы", photo=None),
 "peugeot": dict(name="Завод Peugeot-Citroën (ныне BYD)", place="Джизак", sector="eng", sec_label="Конструктор", country="uz", role="Конструкторские работы", photo=None),
 "pvc": dict(name="Завод ПВХ-труб", place="Ахангаран", sector="eng", sec_label="Конструктор", country="uz", role="Конструкторские работы", photo=None),
 "aybek": dict(name="24-этажный жилой дом, ул. Айбека", place="Ташкент", sector="eng", sec_label="Конструктор", country="uz", role="Конструкторские работы", photo=None),
 "uzbum": dict(name="Многоуровневый паркинг «Узбум»", place="Ташкент", sector="eng", sec_label="Конструктор", country="uz", role="Конструкторские работы", photo=None)}

INSIGHTS = [
 dict(d="Октябрь 2026", h="Технический заказчик в Узбекистане: функции, ответственность, стоимость услуги", p="Что входит в договор, за что отвечает техзаказчик и как считается вознаграждение."),
 dict(d="Октябрь 2026", h="Склад класса A: требования к полам, кровле и инженерии", p="Что нужно заложить в договор с подрядчиком, чтобы склад приняли арендатор и оператор."),
 dict(d="Сентябрь 2026", h="Где теряются деньги на стройке: шесть типовых завышений в актах", p="Разбор реальных актов: объёмы, коэффициенты, материалы и «дополнительные» работы.")]

ORG_LD = {"@context": "https://schema.org", "@type": "ProfessionalService", "name": "KAPM", "legalName": "ООО «KAPM»", "url": "https://kapm.uz", "logo": "https://kapm.uz/assets/logo/kapm-logo-primary.svg",
          "description": "Независимое управление строительством на стороне заказчика в Узбекистане: технический заказчик, управление проектом, строительный контроль, контроль стоимости.",
          "telephone": "+998910040152", "email": "ceo@acre.estate", "address": {"@type": "PostalAddress", "streetAddress": "1-й проезд Дархан, 7", "addressLocality": "Ташкент", "addressCountry": "UZ"},
          "areaServed": "UZ", "founder": {"@type": "Person", "name": "Артём Кудряшов"}, "sameAs": [SITE["linkedin"]]}

# ---------- блоки ----------
def proj_card(key, small=False, href=True):
    p = PROJECTS[key]
    link = "/projects/robotis/" if p.get("page") else "/projects/"
    meta = ""
    if p.get("num"): meta = f'<div class="meta"><span><b>{p["num"]}</b> {p["unit"]}</span><span>{p["role"]}</span></div>'
    elif not small: meta = f'<div class="meta"><span>{p["role"]}</span></div>'
    return (f'<a class="pc{" pc-s" if small else ""}" href="{link}" data-sector="{p["sector"]}" data-country="{p["country"]}">{ph(IMG.get(p["photo"]) if p["photo"] else None, p["name"])}'
            f'<div class="b"><div class="eyebrow">{p["sec_label"]} · {p["place"]}</div><h3>{p["name"]}</h3>{meta}</div></a>')

def service_cards():
    return "".join(f'<a class="card" href="/services/{s["slug"]}/">{ICONS[s["icon"]]}<h3>{s["name"]}</h3><p>{s["short"]}</p></a>' for s in SERVICES)

def faq_block(items):
    return '<div class="faq">' + "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + "</div>"

def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

# ---------- страницы ----------
def home():
    body = f'''
<section class="hero"><img src="{IMG["hero"]}" alt="" fetchpriority="high"><div class="ov"></div><div class="wrap on-dark">
<div class="eyebrow">When you need to be sure</div>
<h1>Управление строительством на&nbsp;стороне заказчика</h1>
<p class="lead">Берём на себя ответственность за бюджет и качество вашего объекта — от разрешения на строительство до ввода в эксплуатацию.</p>
<div class="acts"><a class="btn" href="/contact/">Обсудить проект</a><a class="btn btn-o" href="/services/">Наши услуги</a></div>
</div></section>

<section class="sec"><div class="wrap">
<p class="pos">KAPM — независимая компания по управлению строительством. Мы не проектируем и не строим сами, поэтому у нас нет конфликта интересов: единственная сторона, чьи интересы мы представляем, — заказчик и инвестор.</p>
<div class="stats">
<div><div class="n">5</div><p>стран, где команда реализовала проекты</p></div>
<div><div class="n">20+</div><p>объектов в портфолио команды</p></div>
<div><div class="n">115 000<small>&nbsp;м²</small></div><p>промышленной и складской недвижимости</p></div>
<div><div class="n">$270<small>&nbsp;млн</small></div><p>CAPEX-портфель под управлением руководителей</p></div>
</div></div></section>

<section class="sec" style="padding-top:0" id="services"><div class="wrap">
<div class="sec-h"><div class="t"><div class="eyebrow">Услуги</div><h2>Четыре направления —<br>одна ответственность за результат</h2></div><a class="more" href="/services/">Все услуги →</a></div>
<div class="grid4">{service_cards()}</div>
</div></section>

<section class="sec" style="padding-top:0" id="sectors"><div class="wrap">
<div class="sec-h"><div class="t"><div class="eyebrow">Секторы</div><h2>Где у нас больше всего опыта</h2></div></div>
<div class="grid2">{"".join(f'<a class="sector" href="/sectors/{s["slug"]}/">{ph(IMG.get(s["photo"]) if s["photo"] else None, s["name"])}<div class="b"><h3>{s["name"]}</h3><p>{s["short"]}</p><span class="more">Подробнее →</span></div></a>' for s in SECTORS)}</div>
</div></section>

<section class="sec sec-cloud"><div class="wrap">
<div class="sec-h"><div class="t"><div class="eyebrow">Проекты</div><h2>Объекты, за которые мы отвечали</h2></div><a class="more" href="/projects/">Все проекты →</a></div>
<div class="grid3">{proj_card("robotis")}{proj_card("hotel")}{proj_card("toyota").replace(IMG["toyota"], IMG["toyota_off"])}</div>
</div></section>

<section class="band"><img src="{IMG["nature"]}" alt="" loading="lazy"><div class="ov"></div><div class="wrap on-dark">
<div class="eyebrow">When you need to be sure</div>
<h2>Когда нужна уверенность в результате</h2>
<p>Проекты в Узбекистане, Казахстане, России, Турции и на Кипре. Одна команда, которая отвечает за объект от первого согласования до передачи ключей.</p>
</div></section>

<section class="sec sec-dark"><div class="wrap why">
<div class="intro"><div class="eyebrow">Почему KAPM</div><h2>Заказчик покупает не стройку, а уверенность в результате</h2><p>Когда нужна уверенность — на площадке работает команда, у которой нет другого интереса, кроме вашего.</p></div>
<div>
<div class="why-i"><span class="n">01</span><div><h3>Без конфликта интересов</h3><p>Не проектируем, не строим, не поставляем — только управляем в интересах заказчика.</p></div></div>
<div class="why-i"><span class="n">02</span><div><h3>Один договор — один ответственный</h3><p>Вместо десятка подрядчиков и согласований у вас одна точка ответственности за результат.</p></div></div>
<div class="why-i"><span class="n">03</span><div><h3>Международные стандарты, местная практика</h3><p>Опыт команды в проектах Узбекистана, Казахстана, России, Турции и Кипра и знание требований ШНК, экспертизы и ввода в Узбекистане.</p></div></div>
<div class="why-i"><span class="n">04</span><div><h3>Прозрачность для инвестора</h3><p>Еженедельная отчётность по графику, бюджету и рискам в формате, понятном банку и акционерам.</p></div></div>
</div></div></section>

<section class="sec"><div class="wrap">
<div class="sec-h"><div class="t"><div class="eyebrow">Как мы работаем</div><h2>Пять этапов — от идеи до передачи объекта</h2></div></div>
<ol class="steps grid5">
<li><span class="k">ЭТАП 1</span><h3>Предпроект</h3><p>ТЭО, бюджет, график, ИРД</p></li>
<li><span class="k">ЭТАП 2</span><h3>Проектирование и экспертиза</h3><p>Задание, контроль проектировщика, экспертиза</p></li>
<li><span class="k">ЭТАП 3</span><h3>Тендеры и контрактация</h3><p>Пакеты работ, выбор подрядчиков, договоры</p></li>
<li><span class="k">ЭТАП 4</span><h3>Строительство</h3><p>Контроль качества, стоимости и сроков</p></li>
<li><span class="k">ЭТАП 5</span><h3>Ввод и передача</h3><p>Приёмка, ЗОС, передача службе эксплуатации</p></li>
</ol></div></section>

<section class="sec" style="padding-top:0" id="insights"><div class="wrap">
<div class="sec-h"><div class="t"><div class="eyebrow">Экспертиза</div><h2>Что спрашивают инвесторы перед стройкой</h2></div><a class="more" href="/insights/">Все материалы →</a></div>
<div class="grid3">{"".join(f'<a class="ins" href="/insights/"><span class="d">{i["d"]}</span><h3>{i["h"]}</h3><p>{i["p"]}</p></a>' for i in INSIGHTS)}</div>
</div></section>'''
    return dict(path="/", nav="", title="KAPM — технический заказчик и управление строительством, Ташкент",
                desc="Независимое управление строительством на стороне заказчика в Узбекистане: технический заказчик, строительный контроль, контроль стоимости. Ответ в течение рабочего дня.",
                body=body, cta_h="Обсудим ваш проект", ld=[ORG_LD])

def services_index():
    rows = [("Полный цикл техзаказчика", "Инвестор без собственной строительной дирекции", "% от бюджета строительства или ежемесячный фикс"),
            ("Управление проектом", "Есть ОКС, нужен ответственный за срок и бюджет", "Ежемесячный фикс на период строительства"),
            ("Строительный контроль", "Есть генподрядчик и проект, нужен независимый контроль", "Ежемесячный фикс или % от стоимости СМР"),
            ("Контроль стоимости", "Нужна проверка смет и актов перед оплатой", "% от проверяемого объёма или за документ"),
            ("Аудит проекта", "Проект уже идёт, нужна независимая оценка состояния", "Фиксированная стоимость за аудит")]
    body = f'''
<section class="pagehead"><div class="wrap"><nav class="crumbs" aria-label="Хлебные крошки"><a href="/">Главная</a><span>/</span><span>Услуги</span></nav>
<div class="eyebrow">Услуги</div><h1>Услуги на стороне заказчика</h1>
<p class="lead" style="max-width:820px">Инвестор и заказчик редко строят каждый день. Мы — да. KAPM берёт на себя функции, которые обычно размазаны между штатным ОКСом, проектировщиком и генподрядчиком, и отвечает за результат одним договором.</p></div></section>
<section class="sec"><div class="wrap"><div class="grid4">{service_cards()}</div>
<p class="lead" style="margin-top:64px;max-width:900px"><b style="color:var(--navy)">Что мы не делаем:</b> не проектируем, не строим, не поставляем материалы. Это принцип, а не ограничение — только так можно объективно контролировать тех, кто проектирует, строит и поставляет.</p></div></section>
<section class="sec sec-cloud"><div class="wrap"><div class="sec-h"><div class="t"><div class="eyebrow">Формат и оплата</div><h2>Модели сотрудничества</h2></div></div>
<div class="tbl"><table><thead><tr><th>МОДЕЛЬ</th><th>КОГДА ПОДХОДИТ</th><th>ВОЗНАГРАЖДЕНИЕ</th></tr></thead><tbody>{"".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a,b,c in rows)}</tbody></table></div></div></section>'''
    return dict(path="/services/", nav="services", title="Услуги KAPM: техзаказчик, управление проектом, строительный контроль", desc="Четыре направления услуг на стороне заказчика в Узбекистане и модели сотрудничества: полный цикл, управление проектом, контроль, аудит.", body=body)

def service_page(s):
    others = "".join(f'<a href="/services/{o["slug"]}/">{o["name"]} →</a>' for o in SERVICES if o["slug"] != s["slug"])
    body = f'''
<section class="pagehead"><div class="wrap"><nav class="crumbs" aria-label="Хлебные крошки"><a href="/">Главная</a><span>/</span><a href="/services/">Услуги</a><span>/</span><span>{s["name"]}</span></nav>
<div class="eyebrow">{s["eyebrow"]}</div><h1>{s["name"]}</h1><p class="lead" style="max-width:820px">{s["lead"]}</p></div></section>
{ph(IMG[s["photo"]], s["name"], 480)}
<section class="sec"><div class="wrap split">
<aside class="stack" style="gap:40px"><div class="stack"><div class="eyebrow">Задача заказчика</div><p style="font-size:20px">{s["task"]}</p></div>
<div class="stack"><div class="eyebrow">Для кого</div><p class="muted">{s["who"]}</p></div>
<div class="sub"><span class="ftr-h">ДРУГИЕ УСЛУГИ</span>{others}</div></aside>
<div class="stack" style="gap:28px"><h2>Что мы делаем</h2><div>{li(s["do"])}</div>
<div class="box dk"><div class="eyebrow">Что получаете</div><p>{s["get"]}</p></div></div>
</div></section>
<section class="sec sec-cloud"><div class="wrap"><div class="sec-h"><div class="t"><div class="eyebrow">Проекты</div><h2>Где мы это делали</h2></div><a class="more" href="/projects/">Все проекты →</a></div>
<div class="grid2">{"".join(proj_card(k) for k in s["projects"])}</div></div></section>
<section class="sec"><div class="wrap split split-4"><div class="stack"><div class="eyebrow">Вопросы</div><h2>Что спрашивают чаще всего</h2></div>{faq_block(s["faq"])}</div></section>'''
    return dict(path=f'/services/{s["slug"]}/', nav="services", title=s["title"], desc=s["desc"], body=body, ld=[faq_ld(s["faq"])])

def sectors_index():
    body = f'''<section class="pagehead"><div class="wrap"><nav class="crumbs" aria-label="Хлебные крошки"><a href="/">Главная</a><span>/</span><span>Секторы</span></nav><div class="eyebrow">Секторы</div><h1>Где у нас больше всего опыта</h1><p class="lead" style="max-width:820px">Два сектора, в которых команда KAPM знает требования заказчиков, операторов и подрядчиков изнутри. Офисы, жильё и инфраструктуру смотрите в разделе проектов.</p></div></section>
<section class="sec"><div class="wrap grid2">{"".join(f'<a class="sector" href="/sectors/{s["slug"]}/">{ph(IMG.get(s["photo"]) if s["photo"] else None, s["name"])}<div class="b"><h3>{s["name"]}</h3><p>{s["short"]}</p><span class="more">Подробнее →</span></div></a>' for s in SECTORS)}</div></section>'''
    return dict(path="/sectors/", nav="sectors", title="Секторы — KAPM", desc="Промышленность и логистика, гостиницы и HoReCa: специфика объектов и опыт KAPM в Узбекистане и Казахстане.", body=body)

def sector_page(s):
    body = f'''
<section class="pagehead"><div class="wrap"><nav class="crumbs" aria-label="Хлебные крошки"><a href="/">Главная</a><span>/</span><a href="/sectors/">Секторы</a><span>/</span><span>{s["name"]}</span></nav>
<div class="eyebrow">Сектор</div><h1>{s["name"]}</h1><p class="lead" style="max-width:820px">{s["lead"]}</p></div></section>
{ph(IMG.get(s["photo"]) if s["photo"] else None, s["name"], 480)}
<section class="sec"><div class="wrap split">
<div class="stack"><div class="eyebrow">Что важно в этом секторе</div><h2>Особенности объектов</h2></div>
<div class="stack" style="gap:28px"><div>{li(s["points"])}</div><div class="box dk"><div class="eyebrow">Что делаем иначе</div><p>{s["how"]}</p></div></div></div></section>
<section class="sec sec-cloud"><div class="wrap"><div class="sec-h"><div class="t"><div class="eyebrow">Проекты</div><h2>Проекты сектора</h2></div><a class="more" href="/projects/">Все проекты →</a></div>
<div class="grid3">{"".join(proj_card(k) for k in s["projects"])}</div></div></section>'''
    return dict(path=f'/sectors/{s["slug"]}/', nav="sectors", title=s["title"], desc=s["desc"], body=body)

def projects_index():
    kapm = [k for k, p in PROJECTS.items() if p.get("kapm")]; team = [k for k, p in PROJECTS.items() if not p.get("kapm")]
    sect = [("all", "Все"), ("ind", "Промышленность и логистика"), ("hosp", "Гостиницы"), ("office", "Офисы и коммерческая"), ("resid", "Жильё"), ("eng", "Конструкторские работы")]
    ctry = [("all", "Все страны"), ("uz", "Узбекистан"), ("kz", "Казахстан"), ("ru", "Россия"), ("tr", "Турция")]
    chips = lambda items, key: f'<div class="chips" data-filter="{key}">' + "".join(f'<button class="chip{" on" if v=="all" else ""}" type="button" data-v="{v}">{t}</button>' for v, t in items) + "</div>"
    body = f'''
<section class="pagehead" style="padding-bottom:56px"><div class="wrap"><nav class="crumbs" aria-label="Хлебные крошки"><a href="/">Главная</a><span>/</span><span>Проекты</span></nav>
<div class="eyebrow">Проекты</div><h1>Объекты</h1><p class="lead" style="max-width:760px">Проекты KAPM и опыт команды в пяти странах — от заводов и складов до отелей международных брендов.</p>
{chips(sect, "sector")}{chips(ctry, "country")}</div></section>
<section class="sec sec-sm"><div class="wrap stack" style="gap:64px">
<div><h2 style="font-size:28px;margin-bottom:28px">Проекты KAPM, 2024–2026</h2><div class="grid3">{"".join(proj_card(k).replace('class="pc"', 'class="pc c"') for k in kapm)}</div></div>
<div><h2 style="font-size:28px">Опыт команды</h2><p class="muted" style="max-width:760px;margin:10px 0 28px">Проекты, реализованные руководителями и инженерами KAPM до создания компании — в роли заказчика, управляющего и конструктора.</p><div class="grid4">{"".join(proj_card(k, small=True).replace('class="pc pc-s"', 'class="pc pc-s c"') for k in team)}</div></div>
</div></section>'''
    return dict(path="/projects/", nav="projects", title="Проекты KAPM — заводы, склады, отели, офисы", desc="Объекты, за которые отвечала KAPM, и опыт команды в Узбекистане, Казахстане, России и Турции: ROBOTIS, Hilton Garden Inn, Toyota Academy, склады класса A.", body=body)

def project_robotis():
    body = f'''
<section class="hero hero-sm"><img src="{IMG["robotis_hero"]}" alt=""><div class="ov"></div><div class="wrap on-dark">
<nav class="crumbs" aria-label="Хлебные крошки"><a href="/">Главная</a><span>/</span><a href="/projects/">Проекты</a><span>/</span><span>ROBOTIS</span></nav>
<div class="eyebrow">Промышленность · Узбекистан · 2026–2027</div><h1 style="font-size:clamp(34px,4.4vw,60px)">Завод по производству робототехники в Ташкенте</h1></div></section>
<section class="sec-sm sec-cloud" style="padding:56px 0"><div class="wrap grid4">
<div class="stat"><span class="v">22 000 м²</span><span class="l">Общая площадь</span></div><div class="stat"><span class="v">2026–2027</span><span class="l">Срок строительства</span></div>
<div class="stat"><span class="v">Представитель заказчика</span><span class="l">Роль KAPM</span></div><div class="stat"><span class="v">Монтаж оборудования</span><span class="l">В объёме проекта</span></div></div></section>
<section class="sec"><div class="wrap split split-4">
<aside class="stack" style="gap:36px"><div class="stack"><div class="eyebrow">Заказчик</div><p>ROBOTIS, Южная Корея — производитель робототехники; первый завод компании в Узбекистане</p></div>
<div class="sub"><span class="ftr-h">УСЛУГИ НА ПРОЕКТЕ</span><a href="/services/project-management/">Управление проектом и строительством →</a><a href="/services/construction-supervision/">Строительный контроль →</a></div>
<div class="stack"><div class="eyebrow">Сектор</div><a href="/sectors/industrial-logistics/" style="font-weight:600">Промышленность и логистика →</a></div></aside>
<div class="stack" style="gap:56px">
<div class="stack" style="gap:18px"><h2>Задача</h2><p class="lead">Корейский производитель робототехники строит первый завод в Узбекистане. Заказчику нужны были глаза и руки на площадке: контроль генподрядчика, соответствие корейским стандартам производства и узбекским нормам, координация поставок оборудования со строительной готовностью.</p></div>
<div class="stack" style="gap:18px"><h2>Что делает KAPM</h2><div>{li(["Проверка проектных решений на соответствие технологии и нормам", "Контроль графика и качества работ генподрядчика, приёмка скрытых работ", "Проверка актов выполненных работ перед оплатой", "Координация строительной готовности с поставкой и монтажом оборудования", "Еженедельная отчётность инвестору"])}</div></div>
<div class="box dk"><div class="eyebrow">Статус</div><p>Проект в работе: строительство каркаса завершено, идёт монтаж инженерных систем и подготовка к поставке оборудования.</p></div>
</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap gal">{ph(IMG["g1"],"Площадка завода ROBOTIS",cls="w")}{ph(IMG["g2"],"Металлокаркас")}{ph(IMG["g3"],"Монтаж ферм")}{ph(IMG["g4"],"Колонны и команда на площадке")}{ph(IMG["g5"],"Монтаж конструкций")}</div></section>
<section class="sec sec-cloud"><div class="wrap"><div class="sec-h"><h2>Другие проекты</h2><a class="more" href="/projects/">Все проекты →</a></div><div class="grid3">{proj_card("hotel")}{proj_card("wh25000")}{proj_card("toyota")}</div></div></section>'''
    return dict(path="/projects/robotis/", nav="projects", title="Завод ROBOTIS в Ташкенте — представитель заказчика KAPM", desc="22 000 м², 2026–2027. KAPM — представитель заказчика и строительный контроль на строительстве завода робототехники ROBOTIS в Ташкенте.", body=body, cta_h="Похожая задача?")

def about():
    body = f'''
<section class="sec" style="padding-bottom:80px"><div class="wrap split" style="align-items:end;gap:80px"><div class="stack" style="gap:24px"><div class="eyebrow">О компании</div><h1 style="font-size:clamp(34px,4.4vw,60px)">Независимое управление строительством в интересах заказчика</h1></div>
<p class="lead">KAPM — Kudryashov Architecture Project Management — ташкентская компания по управлению строительством на стороне заказчика. Мы выполняем функции технического заказчика, управляем проектами и ведём строительный контроль для частных инвесторов, международных компаний и девелоперов в Узбекистане.</p></div></section>
{ph(IMG["about"], "Объект KAPM", 520)}
<section class="sec"><div class="wrap split split-4"><div class="stack"><div class="eyebrow">Принципы</div><h2>На чём стоит компания</h2></div>
<div class="grid2" style="gap:0 48px">
<div class="pr"><h3>Независимость</h3><p>Мы не проектируем, не строим и не поставляем. У нас нет мотива скрыть ошибку проектировщика или завысить акт подрядчика.</p></div>
<div class="pr"><h3>Полный цикл</h3><p>Сопровождаем проект на каждом этапе — от идеи и проектирования до ввода и эксплуатации.</p></div>
<div class="pr"><h3>Прозрачность</h3><p>Заказчик видит план-факт по графику и деньгам каждую неделю и узнаёт о проблеме раньше, чем она станет дорогой.</p></div>
<div class="pr"><h3>Мультидисциплинарность</h3><p>В одной команде — инженеры-строители, конструкторы, сметчики и руководители проектов; заказчик получает ответ по любому аспекту объекта из одного окна.</p></div>
<div class="pr" style="grid-column:span 2"><h3>Стандарты</h3><p>Международные практики управления проектами (PMI, FIDIC) в сочетании с требованиями ШНК, экспертизы и порядка ввода в Узбекистане.</p></div>
</div></div></section>
<section class="sec sec-cloud"><div class="wrap grid2" style="gap:96px"><div class="stack" style="gap:20px"><div class="eyebrow">Подход</div><h2>Заходим на любом этапе</h2><p class="lead" style="font-size:18px">Мы подключаемся к проекту на любой стадии — от идеи до незавершённого строительства — и за две недели даём заказчику картину: где проект находится по срокам и деньгам, какие риски впереди и что нужно сделать. Дальше работаем по одной из моделей: полный цикл техзаказчика, управление проектом, строительный контроль или контроль стоимости.</p><a class="btn btn-dark" href="/services/" style="align-self:flex-start;margin-top:12px">Услуги и модели сотрудничества</a></div>
<div><div class="eyebrow" style="padding-bottom:20px">Факты и цифры</div>
<div class="fact"><span>Страны реализации проектов команды</span><b>5</b></div><div class="fact"><span>Объектов в портфолио команды</span><b>20+</b></div><div class="fact"><span>Промышленной и складской недвижимости</span><b>115 000+ м²</b></div><div class="fact"><span>CAPEX-портфель под управлением руководителей</span><b>$270 млн</b></div><div class="fact"><span>Год основания</span><b>2024</b></div><div class="fact"><span>Секторы</span><b style="max-width:320px">Промышленность и логистика, гостиницы, офисы, жильё</b></div></div></div></section>
<section class="sec" id="leadership"><div class="wrap"><div class="sec-h"><div class="t"><div class="eyebrow">Руководство</div></div></div>
<div class="split" style="gap:80px">{ph(IMG["portrait"], "Артём Кудряшов", 640)}
<div class="stack" style="gap:32px"><div><h3 style="font-size:36px">Артём Кудряшов</h3><p class="muted" style="font-weight:600;font-size:17px;margin-top:8px">Основатель и генеральный директор KAPM</p></div>
<div class="prose">
<p>Инженер-строитель, в капитальном строительстве и управлении инвестиционными проектами с начала карьеры. Прошёл путь от инженера на международных стройках атомной отрасли до директора департамента капитального строительства одной из крупнейших e-commerce компаний Центральной Азии.</p>
<p>В 2024 году основал KAPM, чтобы дать инвесторам и заказчикам в Узбекистане то, чего не хватало ему самому на стороне заказчика: независимую команду, которая отвечает за бюджет и качество одним договором.</p>
<p>География опыта — пять стран. В Узбекистане — директор департамента капитального строительства крупнейшей e-commerce компании страны: CAPEX-портфель $77 млн, 255 объектов логистической инфраструктуры. В России — четыре склада класса A в Казани площадью от 8 000 до 25 000 м² и проекты жилой и коммерческой недвижимости; участие в проектах атомной отрасли на площадках в Турции и Китае.</p></div>
<p class="muted" style="font-size:15px"><b style="color:var(--navy)">Образование:</b> магистр гражданского строительства, KSUAE · инфраструктурные финансы, Bocconi University</p><a href="{SITE["linkedin"]}" rel="noopener" style="font-weight:700">LinkedIn →</a></div></div></div></section>
<section class="sec sec-dark"><div class="wrap split split-4 on-dark"><div class="stack"><div class="eyebrow">Реквизиты</div><h2 style="font-size:32px">ООО «KAPM»</h2></div>
<div class="stack" style="gap:24px"><div class="req"><div><span>ИНН</span><br>313 133 475</div><div><span>Юридический адрес</span><br>{SITE["address_legal"]}</div><div><span>Телефон</span><br>+998 91 004 0152</div><div><span>E-mail</span><br>{SITE["email"]}</div></div></div></div></section>'''
    ld = [dict(ORG_LD), {"@context": "https://schema.org", "@type": "Person", "name": "Артём Кудряшов", "jobTitle": "Основатель и генеральный директор", "worksFor": {"@type": "Organization", "name": "KAPM"}, "sameAs": [SITE["linkedin"]]}]
    return dict(path="/about/", nav="about", title="О компании KAPM — управление строительством, Ташкент", desc="Независимая компания по управлению строительством на стороне заказчика. Основана инженером с опытом управления CAPEX-портфелем $77 млн. Принципы, подход, руководство, реквизиты.", body=body, ld=ld)

def insights():
    body = f'''<section class="pagehead"><div class="wrap"><nav class="crumbs" aria-label="Хлебные крошки"><a href="/">Главная</a><span>/</span><span>Экспертиза</span></nav><div class="eyebrow">Экспертиза</div><h1>Что спрашивают инвесторы перед стройкой</h1><p class="lead" style="max-width:820px">Разбираем вопросы, которые инвесторы и заказчики задают перед стартом и во время строительства в Узбекистане: сколько стоит, сколько длится, кто за что отвечает и где теряются деньги.</p></div></section>
<section class="sec"><div class="wrap"><div class="grid3">{"".join(f'<div class="ins"><span class="d">{i["d"]} · готовится к публикации</span><h3>{i["h"]}</h3><p>{i["p"]}</p></div>' for i in INSIGHTS)}</div>
<p class="muted" style="margin-top:48px;max-width:720px">Первые материалы выйдут в ближайшие недели. Если у вас есть вопрос, на который вы не нашли ответа, — напишите нам, и мы ответим лично, а тему возьмём в работу.</p></div></section>'''
    return dict(path="/insights/", nav="insights", title="Экспертиза KAPM — статьи о строительстве в Узбекистане", desc="Экспертные материалы для инвесторов и заказчиков: технический заказчик, разрешение на строительство, проверка актов, склады класса A, отели под брендом.", body=body)

def contact():
    body = f'''
<section class="sec"><div class="wrap split">
<div class="stack" style="gap:32px"><div class="stack" style="gap:20px"><div class="eyebrow">Контакты</div><h1 style="font-size:clamp(34px,4vw,56px)">Обсудим ваш проект</h1><p class="lead" style="font-size:18px">Расскажите о задаче — объект, стадия, что нужно от нас. В течение одного рабочего дня ответим, в каком формате KAPM может участвовать, и назовём ориентировочную стоимость услуг.</p></div>
<div><div class="ct"><span>ТЕЛЕФОН</span><a href="tel:+998910040152">+998 91 004 0152</a><div class="pills"><a href="https://t.me/+998910040152" rel="noopener">Telegram</a><a href="https://wa.me/998910040152" rel="noopener">WhatsApp</a></div></div>
<div class="ct"><span>E-MAIL</span><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></div>
<div class="ct"><span>ОФИС</span><p>Ташкент, Мирзо-Улугбекский район,<br>1-й проезд Дархан, 7</p></div>
<div class="ct"><span>ЧАСЫ РАБОТЫ</span><p>Пн–пт, 9:00–18:00 (Ташкент, UTC+5)</p></div></div></div>
<form class="form" id="lead" action="{SITE["form_action"]}" method="POST" data-err="Не удалось отправить. Позвоните или напишите нам напрямую.">
<h2>Заявка на проект</h2>
<div class="grid2">
<div class="f"><label for="name">ИМЯ *</label><input id="name" name="name" type="text" required autocomplete="name"></div>
<div class="f"><label for="company">КОМПАНИЯ</label><input id="company" name="company" type="text" autocomplete="organization"></div>
<div class="f"><label for="contact">ТЕЛЕФОН ИЛИ E-MAIL *</label><input id="contact" name="contact" type="text" required placeholder="+998 … или name@company.uz"></div>
<div class="f"><label for="type">ТИП ОБЪЕКТА</label><select id="type" name="type"><option value="">Выберите</option><option>Завод</option><option>Склад</option><option>Отель</option><option>Офис</option><option>Жильё</option><option>Другое</option></select></div>
<div class="f f2"><label for="stage">СТАДИЯ</label><select id="stage" name="stage"><option value="">Выберите</option><option>Идея</option><option>Есть участок</option><option>Есть проект</option><option>Идёт стройка</option></select></div>
<div class="f f2"><label for="msg">СООБЩЕНИЕ</label><textarea id="msg" name="message" placeholder="Коротко о задаче: объект, площадь, сроки, что нужно от KAPM"></textarea></div>
</div>
<div class="hp" aria-hidden="true"><input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></div>
<label class="chk"><input type="checkbox" required name="consent"><span>Согласен на обработку персональных данных в соответствии с <a href="/privacy/">политикой конфиденциальности</a> *</span></label>
<div class="form-foot"><button class="btn" type="submit">Отправить заявку</button><span>Отвечаем в течение одного рабочего дня. Данные используются только для ответа на запрос.</span></div>
<div class="form-ok">Спасибо, запрос получен. Свяжемся с вами в течение рабочего дня. Если срочно — звоните +998 91 004 0152.</div>
</form></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><iframe class="map" title="Офис KAPM на карте" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=1-%D0%B9+%D0%BF%D1%80%D0%BE%D0%B5%D0%B7%D0%B4+%D0%94%D0%B0%D1%80%D1%85%D0%B0%D0%BD+7,+%D0%A2%D0%B0%D1%88%D0%BA%D0%B5%D0%BD%D1%82&output=embed"></iframe></div></section>
<section class="sec sec-dark" style="padding:64px 0"><div class="wrap grid3 on-dark" style="gap:48px;font-size:15px"><div><div class="eyebrow" style="margin-bottom:12px">Реквизиты</div>ООО «KAPM»<br>ИНН 313 133 475</div><div><div class="eyebrow" style="margin-bottom:12px">Юридический адрес</div>{SITE["address_legal"]}</div><div><div class="eyebrow" style="margin-bottom:12px">Часы работы</div>Пн–пт, 9:00–18:00<br>Ташкент, UTC+5</div></div></section>'''
    return dict(path="/contact/", nav="contact", title="Контакты KAPM — Ташкент", desc="Телефон, e-mail, адрес и форма заявки KAPM. Ответ в течение одного рабочего дня.", body=body, nocta=True, ld=[ORG_LD])

def privacy():
    body = f'''<section class="pagehead"><div class="wrap"><div class="eyebrow">Документы</div><h1 style="font-size:clamp(30px,3.6vw,48px)">Политика конфиденциальности</h1></div></section>
<section class="sec"><div class="wrap prose">
<p>Настоящая политика описывает, какие данные собирает сайт kapm.uz, принадлежащий ООО «KAPM» (ИНН 313 133 475, г. Ташкент), и как они используются.</p>
<h2>Какие данные мы получаем</h2><p>Через форму заявки — имя, компания, телефон или e-mail и текст сообщения, которые вы вводите сами. Через системы аналитики — обезличенные данные о посещении: страницы, время, тип устройства, регион.</p>
<h2>Зачем</h2><p>Данные из формы используются только для ответа на ваш запрос и подготовки предложения. Данные аналитики — для улучшения сайта. Мы не передаём данные третьим лицам, кроме сервисов, которые технически обеспечивают отправку формы и аналитику, и не используем их для рассылок без вашего согласия.</p>
<h2>Хранение и удаление</h2><p>Данные из заявок хранятся не дольше, чем нужно для работы с запросом и выполнения требований законодательства Республики Узбекистан. Вы можете запросить удаление своих данных письмом на {SITE["email"]}.</p>
<h2>Cookie</h2><p>Сайт использует файлы cookie для аналитики. Вы можете отклонить их в уведомлении на сайте или в настройках браузера — сайт продолжит работать.</p>
<h2>Контакты</h2><p>По вопросам, связанным с персональными данными: {SITE["email"]}, +998 91 004 0152.</p>
</div></section>'''
    return dict(path="/privacy/", nav="", title="Политика конфиденциальности — KAPM", desc="Какие данные собирает сайт KAPM и как они используются.", body=body, nocta=True)

def pages():
    out = [home(), services_index()] + [service_page(s) for s in SERVICES] + [sectors_index()] + [sector_page(s) for s in SECTORS] + [projects_index(), project_robotis(), about(), insights(), contact(), privacy()]
    return out
