from colorama import Fore
import random
import time

def delayed_message(message, delay_seconds):
    time.sleep(delay_seconds)
    print(message)

''' 
Boshlang'ich hikoya. Agar qayta test qilib ko'rmoqchi bo'lsangiz o'chirib qo'yishingiz mumkin '''

# delayed_message(Fore.LIGHTYELLOW_EX + "Qadim zamonlardan beri afsonalar yashirin xazina haqida hikoya qiladi.", 1)
# delayed_message(Fore.LIGHTYELLOW_EX + "Bu xazinani qo'lga kiritish uchun xavfli yo'llardan o'tganlar bor,", 3)
# delayed_message(Fore.LIGHTYELLOW_EX + "lekin hech kim muvaffaqiyatga erishmagan.", 2)
# delayed_message(Fore.LIGHTYELLOW_EX + "Mana, siz — jasur qahramon — ularning izidan borishga va xazinani topishga qaror qildingiz.", 3)
# delayed_message(Fore.LIGHTYELLOW_EX + "Oldinda qanday sarguzashtlar kutayotganini kim biladi?", 4)

player_name = input(Fore.LIGHTWHITE_EX + "Qahramon sizning ismingiz nima? : ").capitalize()

xarita = [
    ['P', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', 'Xazina'],
]
items = ['heal', 'qurol', 'heal', 'qurol', 'heal', 'qurol', 'heal', 'qurol']
def print_xarita():
    for i in xarita:
        print(i)

post = []
for i in range(len(xarita)):
    for j in range(len(xarita[i])):
        if xarita[i][j] == '*':
            post.append((i, j))
random_post = random.sample(post, 8)

for pos, item in zip(random_post, items):
    xarita[pos[0]][pos[1]] = item

last_wish = [9, 9]

class Player_base:
    def __init__(self,x, y ,hp = 50, byte = 20):
        self.x = x
        self.y = y
        self.locator = [0, 0]
        self.hp = hp
        self.byte = byte
        self.bag = []

    def turn(self, go):
        xarita[self.y][self.x] = '*'
        if go == "t" and self.y > 0:
            self.y -= 1
            self.locator[0] -= 1
            print(f"Jasur Qahramon {Fore.LIGHTBLUE_EX + player_name}{Fore.LIGHTCYAN_EX} Shimol{Fore.LIGHTWHITE_EX} tomonga yo'l oldi\n")
        elif go == "p" and self.y < len(xarita) - 1:
            self.y += 1
            self.locator[0] += 1
            print(f"Jasur Qahramon {Fore.LIGHTBLUE_EX + player_name}{Fore.LIGHTYELLOW_EX} Janub{Fore.LIGHTWHITE_EX} tomonga yo'l oldi\n")
        elif go == "c" and self.x > 0:
            self.x -= 1
            self.locator[1] -= 1
            print(f"Jasur Qahramon {Fore.LIGHTBLUE_EX + player_name}{Fore.CYAN} G'arb{Fore.LIGHTWHITE_EX} tomonga yo'l oldi\n")
        elif go == "o" and self.x < len(xarita[1]) - 1:
            self.x += 1
            self.locator[1] += 1
            print(f"Jasur Qahramon {Fore.LIGHTBLUE_EX + player_name}{Fore.LIGHTMAGENTA_EX} Sharq{Fore.LIGHTWHITE_EX} tomonga yo'l oldi\n")
        else:
            print(
                Fore.LIGHTRED_EX + f"Hurmatli Qahramon menimcha u yerda yo'l yo'q!\n")
            pass

    def loot(self, tools):
        print(Fore.LIGHTYELLOW_EX + f"Jasur Qahramon {Fore.LIGHTBLUE_EX + player_name}{Fore.LIGHTCYAN_EX + tools}{Fore.LIGHTWHITE_EX}ni topib oldi")
        self.bag.append(tools)
    def chest(self):
        if self.locator == [9, 9]:
            return Fore.LIGHTWHITE_EX + f"fin - {Fore.LIGHTGREEN_EX}Xazinani ochish"
        else:
            return ''

class Pillager:
    def __init__(self, hp = 75):
        self.byte = 50
        self.hp = hp
        self.locator = [random.randint(0, 9), random.randint(0, 9)]
    def turn(self):
        go = random.choice(['t', 'p', 'c', 'o'])
        if go == 't' and self.locator[0] > 0:
            self.locator[0] -= 1
        elif go == 'p' and self.locator[0] > len(xarita) - 1:
            self.locator[0] += 1
        elif go == 'c' and self.locator[1] > 0:
            self.locator[1] -= 1
        elif go == 'o' and self.locator[1] > len(xarita[1]) - 1:
            self.locator[1] += 1
    def punch(self, player):
        delayed_message(Fore.LIGHTRED_EX + "Jasur Qahramon, yovuz Qaroqchiga duch keldingiz!", 1)
        delayed_message(Fore.LIGHTRED_EX + f"Qahramon, Qaroqchi sizga javob qaytardi va siz 30% joningizni yo'qotdingiz!", 2)
        player.hp -= self.byte

player = Player_base(0, 0)
qaroqchi1 = Pillager()
qaroqchi2 = Pillager()
qaroqchi3 = Pillager()
qaroqchi4 = Pillager()
qaroqchi5 = Pillager()
qaroqchi6 = Pillager()
qaroqchi7 = Pillager()
qaroqchi8 = Pillager()


while True:
    print()
    choice = input(Fore.LIGHTWHITE_EX + f"Qahramon {Fore.LIGHTBLUE_EX + player_name}{Fore.LIGHTWHITE_EX} endi nima qilmoqchisiz? \nx - {Fore.CYAN + 'Xaritaga qarash'}{Fore.LIGHTWHITE_EX} \ny - {Fore.LIGHTYELLOW_EX + 'Yo`lda davom etish'}{Fore.LIGHTWHITE_EX} \ns - {Fore.LIGHTBLUE_EX}Shaxsiy ma'lumot{Fore.LIGHTWHITE_EX}\n{player.chest()}{Fore.LIGHTWHITE_EX}\n >>> ").casefold()

    if choice == 'fin':
        if player.locator == last_wish:
            delayed_message(Fore.LIGHTYELLOW_EX + "Siz sandiqni ochgan zahoti, kimningdir ovozi qulog‘ingizda yangray boshlaydi.",1)
            delayed_message(Fore.LIGHTYELLOW_EX + "Kimdir sizni chaqirayotgandek tuyildi va ovozi tobora kuchayishni boshladi.", 3)
            delayed_message(Fore.LIGHTYELLOW_EX + "Birdan atrofingizdagi hamma narsa yo‘qola boshlaydi, va siz ko‘zlaringizni ochasiz...",4)
            delayed_message(Fore.LIGHTMAGENTA_EX + "haqiqiy hayotga qaytibsiz.", 3)
            delayed_message(Fore.LIGHTYELLOW_EX + "Atrofingizda oilangiz va shifokor turibdi.", 2)
            delayed_message(Fore.LIGHTYELLOW_EX + "Shifokor jilmayib, sizga qarab deydi:", 2)
            delayed_message(Fore.LIGHTBLUE_EX + "Siz kasallikni yengdingiz, endi to‘liq sog‘aydingiz.\n", 3)
            delayed_message(Fore.LIGHTGREEN_EX + "The game is over. Thank you for testing!", 3)
            break

    if player.hp <= 0:
        delayed_message(Fore.LIGHTRED_EX + f"Jasur Qahramon {player_name} qiyinchilikni ko'tara olmadi va yengildi.", 1)
        delayed_message(Fore.LIGHTRED_EX + f"Ax, nega hozirgi qahramonlar bunday kuchsiz.", 3)
        delayed_message(Fore.LIGHTRED_EX + f"Lekin sen xavotir olma.", 2)
        delayed_message(Fore.LIGHTRED_EX + f"Sening ruhing, mening kichkina matritsamda hali kerak bo'ladi", 3)
        delayed_message(Fore.LIGHTRED_EX + f"Men seni tangaga aylantirib, xazinaga qo'shib qo'yaman", 3)
        break

    elif choice == 'x':
        print_xarita()


    elif choice == "y":
        while True:
            turn = input(Fore.LIGHTWHITE_EX + f"Jasur Qahramon {Fore.LIGHTBLUE_EX + player_name}{Fore.LIGHTWHITE_EX} qayerga bormoqchisiz? \n{Fore.LIGHTMAGENTA_EX}t - Tepaga\np - Pastga\nc - chapga\no - o'nga\n\n{Fore.RED}m - bosh menuga qaytish{Fore.LIGHTWHITE_EX}\n{Fore.LIGHTWHITE_EX}>>> ").casefold()

            if turn == 't' or turn == 'p' or turn == 'c' or turn == 'o':

                if xarita[player.y][player.x] == '*' or xarita[player.y][player.x] == 'P':
                    player.turn(turn)
                if xarita[player.locator[0]][player.locator[1]] == 'heal':
                    player.hp += 40
                    print(Fore.LIGHTMAGENTA_EX + "Qahramon siz yo'lda tushirib qoldirilgan giyohni topib oldingiz!")
                    xarita[player.locator[0]][player.locator[1]] = '*'
                if xarita[player.locator[0]][player.locator[1]] == 'qurol':
                    if 'qurol' not in player.bag:
                        player.byte += 60
                        player.bag.append('qurol')
                        print(Fore.BLUE + "Qahramon siz urushda yutgan ritsarning tushirib qoldirgan qilichini topib oldingiz")
                        xarita[player.locator[0]][player.locator[1]] = '*'
                    elif 'qurol' in player.bag:
                        print(Fore.LIGHTRED_EX + "Qahramon, sizga yana bitta qilich shart emas!")
                        xarita[player.locator[0]][player.locator[1]] = '*'

                xarita[player.y][player.x] = 'P'

            elif turn == 'm':
                break
            else:
                print(
                    Fore.LIGHTRED_EX + f"Hurmatli Qahramon iltimos to'rt yo'lakdan birini tanlang!\n")
                pass
    elif choice == "s":
        print(Fore.LIGHTBLUE_EX + f"Qahramonning rezyumesi:\n{Fore.LIGHTWHITE_EX}Ismi: {Fore.LIGHTYELLOW_EX + player_name}\n{Fore.LIGHTWHITE_EX}Familyasi: {Fore.LIGHTYELLOW_EX}Geroyev\n{Fore.LIGHTWHITE_EX}Address: {Fore.LIGHTYELLOW_EX}{player.locator}\n{Fore.LIGHTWHITE_EX}HP: {Fore.LIGHTYELLOW_EX}{player.hp}\n{Fore.LIGHTWHITE_EX}Kuchi (uron): {Fore.LIGHTYELLOW_EX}{player.byte}\n")

    else:
        print(Fore.LIGHTRED_EX + f"Hurmatli Qahramon siz Matritsadasiz va siz men bergan shartlarga amal qilishingiz shart. ltimos men bergan shartlarga amal qiling\n")

    for qaroqchi in [qaroqchi1, qaroqchi2, qaroqchi3, qaroqchi4, qaroqchi5, qaroqchi6, qaroqchi7, qaroqchi8]:
        if player.locator == qaroqchi.locator:
            if 'qurol' in player.bag:
                qaroqchi.hp -= player.byte
                delayed_message(Fore.LIGHTRED_EX + "Jasur Qahramon, yovuz Qaroqchiga duch keldingiz!", 1)
                delayed_message(Fore.LIGHTRED_EX + f"Qahramon qaroqchiga katta zarar yetkazdi. Qaroqchi HP: {qaroqchi.hp}", 2)
                if qaroqchi.hp <= 0:
                    print(Fore.LIGHTBLUE_EX + "Jasur Qahramon, qaroqchi ustidan ustunlik qildi va qaroqchi chekinishga majbur bo'ldi")
                    qaroqchi.locator = [-1, -1]
            else:
                qaroqchi.punch(player)
    for qaroqchi in [qaroqchi1, qaroqchi2, qaroqchi3, qaroqchi4, qaroqchi5, qaroqchi6, qaroqchi7, qaroqchi8]:
        if qaroqchi.hp > 0:
            qaroqchi.turn()
        else:
            qaroqchi.locator = [-1, -1]