#~PYTHON~
#~~OOP~~
#~~~INHERITAMCE~~~

# class Games():
#     def __init__(self):
#         print("Oyunlar hazırda sistemdə mövcuddur")
    
#     def rules(self):
#         print("Oyunun qaydaları artıq müəyyən edilmişdir") 
    
#     def fee(self, fee = 77):
#         self.fee = fee
#         print(f"Oyunun ödəniş haqqı {fee} azn") 
        
#     def originCountry(self, country):
#         self.country = country
#         print(f"Oyun təqribi 1500 il əvvəl bir qrup 'super-titiz' tərəfindən {country}da ixtira edilib")
        
        
#     def madeinCountry(self, country):
#         self.country = country
#         print(f"Oyun setinin istehsal ölkəsi {country}dir ")
    
    

# class Chess(Games):
#     def __init__(self):
#         super().__init__()
#         print("Şahmat oyunu seçildi")
        
#     def setColor(self):
#         print("Set rəngi yaşıl - krem")
        
#     #OVERWRITE METHOD
#     def rules(self, kefimKok=False):
#         if kefimKok == True:
#             print("Oyunun qaydaları 3-5 saata müəyyən ediləcək")
#         else:
#             print("Zəhmət olacaq amma bir az gözləyin)))")
            
        
        
        
    
        
# chess = Chess()  #Bunu bağlayanda çalışmırmış :O
# chess.rules(True)
# chess.fee(99)
# chess.setColor()
# chess.originCountry(country = "Hindistan")
# chess.madeinCountry(country = "Cənubi Koreya")



#~~~ ENCUPSULATION ~~~
# class ChessPlayer():
#     def __init__(self):
#         self.__playerNation = "AZ"
#         print(f"Inanılmaz yüksək bir məbləğə oyunçu tapıldı")
        
#     def set_playerNation(self, new_nation):
#         if new_nation == "ARM":
#             print("Başqa milliyət seçin")
#         else:
#             self.__playerNation = new_nation
            
        
#     def get_playerNation(self):
#         return self.__playerNation
        
        
# player1 = ChessPlayer()
# print(f"İlkin oyunçunuz => {player1.get_playerNation()}")
# player1.set_playerNation(new_nation = "KR")
# print(f"Yeni {player1.get_playerNation()} milliyətli oyunçu uğurla seçilmişdir!")

#~~~POLYMORPHISIM~~~
class Games():
    def __init__(self):
        print("Oyunlar hazırda sistemdə mövcuddur")
    
    def rules(self):
        print("Oyunun qaydaları artıq müəyyən edilmişdir") 
    
    def fee(self, fee = 77):
        self.fee = fee
        print(f"Oyunun ödəniş haqqı {fee} azn") 
        
    def originCountry(self, country):
        self.country = country
        print(f"Oyun təqribi 1500 il əvvəl bir qrup 'super-titiz' tərəfindən {country}da ixtira edilib")
        
        
    def madeinCountry(self, country):
        self.country = country
        print(f"Oyun setinin istehsal ölkəsi {country}dir ")
    
    

class Chess(Games):
    def __init__(self):
        super().__init__()
        print("Şahmat oyunu seçildi")
        
    def setColor(self):
        print("Set rəngi yaşıl - krem")
        
    #OVERWRITE METHOD
    def rules(self, kefimKok=False):
        if kefimKok == True:
            print("Oyunun qaydaları 3-5 saata müəyyən ediləcək")
        else:
            print("Zəhmət olacaq amma bir az gözləyin)))")
            
class Çövkən(Games):
    def __init__(self):
        super().__init__()
        print("Çövkən oyunu seçildi")
        
    def horseCount(self , horse_numbers):
        self.horse_numbers = horse_numbers
        print(f"Hazırda cari oyun üçün {horse_numbers} ədəd at mövcuddur")
        
            
class Volleyball(Games):
    def __init__(self):
        super().__init__()
        print("Voleybol oyunu seçildi")
        
    def setColor(self):
        print("Set rəngi mavi - sarı")
        
    #OVERWRITE METHOD
    def rules(self, rain=False):
        if rain == True:
            print("Gözləmə zalında dincəlməyiniz tövsiyyə olunur")
        else:
            print("Oyun bir azdan başlayacaq")
            
class Rugby(Games):
    def __init__(self):
        print("Rugby oyunu seçildi")
        
    def setColor(self):
        print("Set rəngi ağ - qırmızı")
        
def strict_rules(strict_game):
    strict_game.rules()
    
strict_rules(Chess())
strict_rules(Çövkən())
strict_rules(Rugby())
strict_rules(Volleyball())
            
            
        
        
        
    



