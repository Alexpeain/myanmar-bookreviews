# Path: <your_project>/<your_app>/management/commands/load_genres.py

import json
from django.core.management.base import BaseCommand
from books.models import Genre # သင့် app name ကို ပြောင်းလဲရန် မမေ့ပါနှင့်

class Command(BaseCommand):
    help = 'ဒေတာဘေ့စ်ထဲသို့ JSON အချက်အလက်များနှင့်အတူ စာအုပ်အမျိုးအစားများကို ထည့်သွင်းပေးခြင်း။'

    def handle(self, *args, **kwargs):
        """
        Main function to handle the command logic.
        """
 
        # description များကို ဖြည့်သွင်းရန် လိုအပ်ပါသည်။
        genres_data = [
          {"name": "လစဉ်ထုတ်မဂ္ဂဇင်းများ", "description": "လစဉ် ထုတ်ဝေသော မဂ္ဂဇင်းနှင့် စာအုပ်များကို စုစည်းဖော်ပြခြင်း။"},
          {"name": "ပညာရေးစာအုပ်များ", "description": "ကျောင်းသုံးစာအုပ်များ၊ ကျောင်းပြင်ပ ပညာရေးနှင့် ဘာသာစကားဆိုင်ရာစာအုပ်များ။"},
          {"name": "အသစ်ထွက်စာအုပ်များ New Releases!", "description": "အသစ်ဆုံးနှင့် ရောင်းအားအကောင်းဆုံး စာအုပ်များ။"},
          {"name": "အရောင်းရဆုံးစာအုပ်များ", "description": "အချိန်တိုင်း ရောင်းအားအကောင်းဆုံး စာအုပ်များ။"},
          {"name": "အယ်ဒီတာအဖွဲ့ စိတ်ကြိုက်စာအုပ်များ", "description": "အယ်ဒီတာအဖွဲ့မှ ရွေးချယ်ထားသော စာအုပ်များ။"},
          {"name": "စာပေဆုရစာအုပ်များ", "description": "နိုင်ငံတကာနှင့် ပြည်တွင်း စာပေဆုများရရှိထားသော စာအုပ်များ။"},
          {"name": "မြန်မာစာပေ ဂန္ထဝင်စာအုပ်များ", "description": "မြန်မာ့စာပေ သမိုင်းတွင် ထင်ရှားကျော်ကြားခဲ့သော ဂန္ထဝင် စာအုပ်များ။"},
          {"name": "စာအုပ်အမျိုးအစား", "description": None},
          {"name": "ကလေးစာပေ", "description": None},
          {"name": "ပုံပြင်နှင့်ကဗျာစာအုပ်များ", "description": None},
          {"name": "သုတရဖွယ်စာအုပ်များ", "description": None},
          {"name": "ကာတွန်းနှင့်ရုပ်ပြများ", "description": None},
          {"name": "ဉာဏ်စမ်းနှင့်အထွေထွေစာအုပ်များ", "description": None},
          {"name": "ကျန်းမာရေး စာအုပ်များ", "description": None},
          {"name": "အထွေထွေကျန်းမာရေး", "description": None},
          {"name": "ကိုယ်ဝန်ဆောင်နှင့်အမျိုးသမီးကျန်းမာရေး", "description": None},
          {"name": "ကလေးပြုစုပျိုးထောင်ရေး၊ မိဘ-ဆရာလက်စွဲ", "description": None},
          {"name": "စိတ်ပညာစာအုပ်များ", "description": None},
          {"name": "ရသစာပေ", "description": None},
          {"name": "မြန်မာဝတ္ထုများ", "description": None},
          {"name": "၀တ္ထုတိုနှင့် ရသဆောင်းပါးစာအုပ်များ", "description": None},
          {"name": "ကဗျာနှင့်အက်ဆေးစာအုပ်များ", "description": None},
          {"name": "ဘာသာပြန်ဝတ္ထုများ", "description": None},
          {"name": "LGBT ရသဝတ္ထုများ", "description": None},
          {"name": "ပရလောက စိတ်ဝိဉာဉ်ဝတ္ထုများ", "description": None},
          {"name": "စိတ်ကူးယဉ် စွန့်စားခန်းဝတ္ထုများ", "description": None},
          {"name": "လျှို့ဝှက်ဆန်းကြယ်၊ သည်းထိတ်ရင်ဖိုဝတ္ထုများ", "description": None},
          {"name": "ပန်းချီ ဂီတအနုပညာ စာအုပ်များ", "description": None},
          {"name": "ပြဇာတ်နှင့် ဇာတ်ညွှန်းစာအုပ်များ", "description": None},
          {"name": "ဟာသဝတ္ထုများနှင့် သရော်စာများ", "description": None},
          {"name": "စိတ်ခွန်အားနှင့် ဘ၀လမ်းညွှန်မှု", "description": None},
          {"name": "အောင်မြင်ရေးနှင့်စိတ်ခွန်အား", "description": None},
          {"name": "စီးပွားရေးနှင့် ငွေကြေး", "description": None},
          {"name": "ခေါင်းဆောင်မှုနှင့် စီမံခန့်ခွဲမှု", "description": None},
          {"name": "လူမှုဆက်ဆံရေး", "description": None},
          {"name": "အတ္ထုပ္ပတ္တိ မှတ်တမ်းနှင့် ခရီးသွား", "description": None},
          {"name": "အတ္ထုပ္ပတ္တိ စာအုပ်များ", "description": None},
          {"name": "ကိုယ်တွေ့မှတ်တမ်း နှင့် ခရီးသွားမှတ်တမ်းစာအုပ်များ", "description": None},
          {"name": "သမိုင်းနှင့် နိုင်ငံရေး", "description": None},
          {"name": "မြန်မာ့သမိုင်းစာအုပ်များ", "description": None},
          {"name": "မြန်မာ့နိုင်ငံရေးစာအုပ်များ", "description": None},
          {"name": "ကမ္ဘာ့သမိုင်းစာအုပ်များ", "description": None},
          {"name": "ကမ္ဘာ့နိုင်ငံရေးစာအုပ်များ", "description": None},
          {"name": "အတွေးအမြင်၊ လူမှုဒဿန၊ သိပ္ပံ", "description": None},
          {"name": "နိုင်ငံရေးအတွေးအခေါ်စာအုပ်များ", "description": None},
          {"name": "လူမှုသိပ္ပံ၊ ဒဿနစာအုပ်များ", "description": None},
          {"name": "အတွေးအမြင်နှင့် ဆောင်းပါးစာအုပ်များ", "description": None},
          {"name": "ဘာသာရေးနှင့် တရားဓမ္မ", "description": None},
          {"name": "ဗုဒ္ဓဓမ္မ စာအုပ်များ", "description": None},
          {"name": "ဘာသာရေးကျမ်းဂန်များ", "description": None},
          {"name": "ဆရာတော်ကြီးများ အတ္ထုပ္ပတ္တိ", "description": None},
          {"name": "တရားဒေသနာနှင့် ဝတ်ရွတ်စဉ်စာအုပ်များ", "description": None},
          {"name": "ဘာသာရေးသမိုင်းစာအုပ်များ", "description": None},
          {"name": "အခြားဘာသာ စာအုပ်များ", "description": None},
          {"name": "သင်ကြားလေ့လာမှုနှင့် စာပေဆိုင်ရာ", "description": None},
          {"name": "ပညာရေးနှင့် သင်ကြားပို့ချမှုစာအုပ်များ", "description": None},
          {"name": "မြန်မာဘာသာစကားနှင့် မြန်မာစာပေ", "description": None},
          {"name": "အင်္ဂလိပ်ဘာသာ လေ့လာမှုစာအုပ်များ", "description": None},
          {"name": "ဘာသာစကား လေ့လာမှုစာအုပ်များ", "description": None},
          {"name": "စာအုပ်စုစည်းမှု", "description": None},
          {"name": "အင်္ဂလိပ်-မြန်မာနှစ်ဘာသာ စာအုပ်များ", "description": None},
          {"name": "ဂျွန်စီမက်ဝဲလ် စာအုပ်များ", "description": None},
          {"name": "တစ်နာရီသမိုင်းဖတ်စာ", "description": None},
          {"name": "ရောဘတ်ကီယိုဆာကီ စာအုပ်များ", "description": None},
          {"name": "ပုဂံပုံရိပ်များ", "description": None},
          {"name": "ပြင်သစ်ဝတ္ထုများ", "description": None},
          {"name": "တက္ကသိုလ်နောက်ခံဝတ္ထုများ", "description": None},
          {"name": "ပညာရပ်နယ်ပယ် ကဏ္ဍစုံ", "description": None},
          {"name": "ကွန်ပြူတာနည်းပညာစာအုပ်များ", "description": None},
          {"name": "သက်မွေးပညာနှင့် ကျွမ်းကျင်မှုဆိုင်ရာ", "description": None},
          {"name": "အားကစားနှင့် ဝါသနာဆိုင်ရာ", "description": None},
          {"name": "ဥပဒေစာအုပ်များ", "description": None},
          {"name": "ဗေဒင်၊ လက္ခဏာ၊ မျက်လှည့်", "description": None},
          {"name": "ရည်ညွှန်းကိုးကားခြင်းဆိုင်ရာ", "description": None},
          {"name": "စွယ်စုံကျမ်းနှင့် အဘိဓာန်များ", "description": None},
          {"name": "သုတေသနနှင့် ကျမ်းစာအုပ်များ", "description": None},
          {"name": "အညွှန်းစာအုပ်များ", "description": None},
          {"name": "စာနယ်ဇင်း စာအုပ်များ", "description": None},
          {"name": "မဂ္ဂဇင်း စာအုပ်များ", "description": None},
          {"name": "လစဉ်/အပတ်စဉ်ထုတ်စာအုပ်များ", "description": None},
          {"name": "English Version Books", "description": None},
          {"name": "Children & Kid Books", "description": None},
          {"name": "English Version Books", "description": None},
          {"name": "Stories Books", "description": None},
          {"name": "Educational Books", "description": None}
        ]
        
        # Check if the genre data list is empty.
        if not genres_data:
            self.stdout.write(self.style.WARNING('Genres data list is empty. No genres to import.'))
            return

        # ရှိပြီးသားအမျိုးအစားများကို ရှာဖွေပြီး ထပ်မံထည့်သွင်းခြင်းမှ ကာကွယ်ခြင်း
        existing_genres = set(Genre.objects.values_list('name', flat=True))

        # အသစ်ဖန်တီးမည့် အမျိုးအစားစာရင်းကို ပြင်ဆင်ခြင်း
        genres_to_create = []
        for genre_data in genres_data:
            genre_name = genre_data.get('name')
            if genre_name and genre_name not in existing_genres:
                genres_to_create.append(Genre(name=genre_name, description=genre_data.get('description')))

        # bulk_create ကို အသုံးပြု၍ အကျိုးရှိစွာ ထည့်သွင်းခြင်း
        if genres_to_create:
            Genre.objects.bulk_create(genres_to_create)
            self.stdout.write(self.style.SUCCESS(f'အမျိုးအစားအသစ် {len(genres_to_create)} ခုကို အောင်မြင်စွာထည့်သွင်းပြီးပါပြီ။'))
        else:
            self.stdout.write(self.style.WARNING('အသစ်ထည့်ရန် အမျိုးအစားမရှိပါ။'))
