import sys

# cat $raw | openssl aes-256-cbc -pbkdf2 | xxd -p -
# cat $cst | xxd -r -p - | openssl aes-256-cbc -d -pbkdf2

class TraRenkchalCalendar:
	def __init__(self, Suns):
		self.__suns = Suns
		self.__decades = ["Плуг", "Согхо", "Лук", "Большая Капля", "Карп", "Оцелот", "Тростник", "Змея", "Малая Капля", "Пирог"]
		self.__rains_long = {(False, False): "полновесный", (True, False): "малый високосный", (False, True): "большой високосный", (True, True): "двойной високосный", True: "високосный", False: "полновесный"}
		self.__rains_even = {False: "нёчетный", True: "чётный"}
	def CurrentDate(self):
		Rain = 1
		CurrentRain = {"Minor": False, "Major": False, "Even": False}
		CurrentSuns = int(self.__suns)
		while 1:
			SunsInRain = 80
			CurrentRain = {"Minor": False, "Major": False, "Even": False}
			if (Rain % 16) == 0:
				SunsInRain -= 1
				CurrentRain["Minor"] = True
			if (Rain % 450) == 0:
				SunsInRain -= 1
				CurrentRain["Major"] = True
			if CurrentSuns < SunsInRain: break
			CurrentSuns -= SunsInRain
			Rain += 1
		Decade = CurrentSuns // 16
		if (Rain % 2) == 0:
			CurrentRain["Even"] = True
			Decade += 5
		Sunset = (CurrentSuns % 16) + 1
		
		CurrentYear = 0
		CurrentSuns = int(self.__suns) + 402536
		YearLength = False
		while 1:
			SunsInYear = 288
			YearLength = False
			if (CurrentYear % 41) == 0: 
				SunsInYear -= 3
				YearLength = True
			if CurrentSuns < SunsInYear: break
			CurrentSuns -= SunsInYear
			CurrentYear += 1
		#if ((Decade == 0) or (Decade == 5)) and (Sunset == 1) and (CurrentSuns == 0): print(f"{self.__decades[Decade]} {Sunset} дождя {Rain} ({self.__rains_even[CurrentRain['Even']]}, {self.__rains_long[CurrentRain['Minor'], CurrentRain['Major']]}), рассвет {CurrentSuns + 1} Года Церемонии {CurrentYear} ({self.__rains_long[YearLength]})")
		return f"{self.__decades[Decade]} {Sunset} дождя {Rain}, {self.__rains_even[CurrentRain['Even']]}, {self.__rains_long[CurrentRain['Minor'], CurrentRain['Major']]}, рассвет {CurrentSuns + 1} Года Церемонии {CurrentYear % 41 + 1} ({CurrentYear + 1}), {self.__rains_long[YearLength]}"

print(TraRenkchalCalendar(sys.argv[1]).CurrentDate())
