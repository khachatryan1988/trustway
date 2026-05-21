from django.core.management.base import BaseCommand
from core.models import SiteSettings, PageContent, Stat, Service, RoutePoint, Partner, ValueItem, WorkStep, FooterLink

class Command(BaseCommand):
    help = "Seed Trust Way default editable content"

    def handle(self, *args, **kwargs):
        SiteSettings.objects.get_or_create(id=1)

        pages = [
            ("home", "Գլխավոր", "Главная", "Home", "Միջազգային լոգիստիկ լուծումներ", "Международные логистические решения", "International logistics solutions"),
            ("about", "Մեր մասին", "О нас", "About us", "Trust Way-ի մասին", "О компании Trust Way", "About Trust Way"),
            ("services", "Ծառայություններ", "Услуги", "Services", "Լոգիստիկ ծառայություններ", "Логистические услуги", "Logistics services"),
            ("contacts", "Կապ", "Контакты", "Contacts", "Կապվեք մեզ հետ", "Свяжитесь с нами", "Contact us"),
        ]
        for key, hy, ru, en, shy, sru, sen in pages:
            PageContent.objects.get_or_create(key=key, defaults={
                "title_hy": hy, "title_ru": ru, "title_en": en,
                "subtitle_hy": shy, "subtitle_ru": sru, "subtitle_en": sen,
                "body_hy": "Մենք առաջարկում ենք վստահելի և արագ լոգիստիկ լուծումներ։",
                "body_ru": "Мы предлагаем надёжные и быстрые логистические решения.",
                "body_en": "We provide reliable and fast logistics solutions.",
            })

        stats = [("12+","ուղղություններ","направлений","routes","ti-map-pin"),("15+","գործընկերներ","партнёров","partners","ti-users"),("3","փոխադրում","вида перевозок","transport types","ti-truck"),("24/7","աջակցություն","поддержка","support","ti-headset")]
        for i, s in enumerate(stats):
            Stat.objects.get_or_create(number=s[0], defaults={"label_hy":s[1],"label_ru":s[2],"label_en":s[3],"icon":s[4],"sort_order":i})

        services = [
            ("ti-truck-delivery","Ցամաքային փոխադրում","Автоперевозки","Road freight"),
            ("ti-plane","Օդային փոխադրում","Авиаперевозки","Air freight"),
            ("ti-ship","Ծովային փոխադրում","Морские перевозки","Sea freight"),
            ("ti-file-certificate","Մաքսային ձևակերպում","Таможенное оформление","Customs clearance"),
            ("ti-package","Պահեստավորում","Складские услуги","Warehousing"),
            ("ti-route","Մուլտիմոդալ լուծումներ","Мультимодальные решения","Multimodal solutions"),
        ]
        for i, (icon, hy, ru, en) in enumerate(services):
            Service.objects.get_or_create(name_ru=ru, defaults={
                "icon": icon, "name_hy": hy, "name_en": en,
                "desc_hy": "Արագ և վերահսկվող ծառայություն ձեր բեռների համար։",
                "desc_ru": "Быстрая и контролируемая услуга для ваших грузов.",
                "desc_en": "Fast and controlled service for your cargo.",
                "tags_hy": "արագ,վստահելի,հսկվող", "tags_ru": "быстро,надёжно,контроль", "tags_en": "fast,reliable,tracked",
                "sort_order": i
            })

        routes = [("Հայաստան","Армения","Armenia",500,260),("Ռուսաստան","Россия","Russia",610,150),("Եվրոպա","Европа","Europe",360,180),("Չինաստան","Китай","China",780,260),("Վրաստան","Грузия","Georgia",530,210)]
        for i, (hy, ru, en, x, y) in enumerate(routes):
            RoutePoint.objects.get_or_create(name_ru=ru, defaults={"name_hy":hy,"name_en":en,"x":x,"y":y,"size":8,"sort_order":i})

        for i in range(1,16):
            Partner.objects.get_or_create(name=f"Partner {i}", defaults={"icon":"ti-building","color":"#f59e0b","sort_order":i})

        values = [("ti-shield-check","Վստահություն","Надёжность","Reliability"),("ti-clock","Արագություն","Скорость","Speed"),("ti-eye","Թափանցիկություն","Прозрачность","Transparency"),("ti-users","Գործընկերություն","Партнёрство","Partnership")]
        for i, (icon, hy, ru, en) in enumerate(values):
            ValueItem.objects.get_or_create(title_ru=ru, defaults={"icon":icon,"title_hy":hy,"title_en":en,"desc_hy":"Մեր աշխատանքի հիմնական արժեքներից մեկը։","desc_ru":"Одна из ключевых ценностей нашей работы.","desc_en":"One of the key values of our work.","sort_order":i})

        steps = [("01","Հարցում","Заявка","Request"),("02","Հաշվարկ","Расчёт","Calculation"),("03","Փոխադրում","Перевозка","Shipping"),("04","Առաքում","Доставка","Delivery")]
        for i, (num, hy, ru, en) in enumerate(steps):
            WorkStep.objects.get_or_create(num=num, defaults={"name_hy":hy,"name_ru":ru,"name_en":en,"desc_hy":"Մենք կատարում ենք փուլը վերահսկմամբ։","desc_ru":"Мы выполняем этап с контролем.","desc_en":"We complete the step with control.","sort_order":i})


        footer_links = [
            ("Մեր մասին", "О нас", "About us", "/about/"),
            ("Ծառայություններ", "Услуги", "Services", "/services/"),
            ("Կապ", "Контакты", "Contacts", "/contacts/"),
            ("Գաղտնիության քաղաքականություն", "Политика конфиденциальности", "Privacy Policy", "#"),
        ]

        for i, (hy, ru, en, url) in enumerate(footer_links):
            FooterLink.objects.get_or_create(
                title_ru=ru,
                defaults={
                    "title_hy": hy,
                    "title_en": en,
                    "url": url,
                    "sort_order": i,
                }
            )
        self.stdout.write(self.style.SUCCESS("Trust Way content seeded."))
