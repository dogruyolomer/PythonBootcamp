from datetime import *

birth = datetime.strptime(input("Your birth date (dd.mm.yyyy): "), "%d.%m.%Y")
age = datetime.now() - birth

print(f'You survived {age.total_seconds()} seconds.')
