##Birthday Finder
import os
#Neil Cole
def findBirthday():
	print("Hey! Whose birthday do you want to know? (Write her/his name and surname with one space)")
	name = input("> ")
	file = open("birthdays.txt", "r")
	lines = file.readlines()
	for person in lines:
		splitted = person.split("|")
		nameinfile = splitted[0]
		birthday = splitted[1]
		if name == nameinfile:
			print(f"{name}'s birthday is {birthday}")
			break
		else:
			print(f"There is noone named {name}")
			break
	file.close()
	input("Press any key to continue...")

def addBirthday():
	print("Please write someone's name and surname which you want to add, with one space.")
	name = input("> ")
	print("Please write birthday date with \"/\" between numbers. (e.g. 12/02/2002)")
	birthday = input("> ")
	file = open("birthdays.txt", "a")
	file.write("\n")
	file.write(name)
	file.write("|")
	file.write(birthday)
	file.close()
	print("Birthday has been succesfully added!")
	input("Press any key to continue...")

def allBirthdays():
	file = open("birthdays.txt", "r")
	lines = file.readlines()
	for person in lines:
		splitted = person.split("|")
		nameinfile = splitted[0]
		birthday = splitted[1]
		print("#"*50)
		print("{nameinfile}, {birthday}\n".format(nameinfile=nameinfile.upper(),birthday=birthday))
	input("Press any key to continue...")




clean = ("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
	while True:
		os.system(clean)
		print("""


			[1] Find someone's birthday
			[2] Add someone's birthday
			[3] See all the birthdays


			""")

		choice = int(input("Make your choice: "))
		if choice == 1:
			os.system(clean)
			findBirthday()
		elif choice == 2:
			os.system(clean)
			addBirthday()
		elif choice == 3:
			os.system(clean)
			allBirthdays()