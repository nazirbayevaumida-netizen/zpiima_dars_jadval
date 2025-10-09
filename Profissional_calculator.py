# 💥 3 tilli Kalkulyator Dasturi: Daraja, Oddiy, Kredit/Omonat 💥

til = input("Tilni tanlang/Выберите язык/Choose language (ozb/rus/eng): ").lower()

while True:
    # -------- O'ZBEK TILI --------
    if til == "ozb":
        print("\n--- Asosiy menyu ---")
        print("1 - Sonning darajasini topish")
        print("2 - Oddiy kalkulyator")
        print("3 - Kredit/Omonat kalkulyatori")

        tanlov = input("Tanlovingizni kiriting (1-3): ")

        # 1) Sonning darajasi
        if tanlov == "1":
            a, b = map(float, input("Son va darajasini kiriting (masalan: 2 3): ").split())
            print(f"Natija: {a ** b}")

        # 2) Oddiy kalkulyator
        elif tanlov == "2":
            print("\nAmalni tanlang:")
            print("1 - Qo‘shish\n2 - Ayirish\n3 - Ko‘paytirish\n4 - Bo‘lish\n5 - Qoldiq (%)")
            amal = input("Tanlov (1-5): ")

            a, b = map(float, input("Ikkita son kiriting (masalan: 5 2): ").split())

            if amal == "1":
                print(f"Natija: {a + b}")
            elif amal == "2":
                print(f"Natija: {a - b}")
            elif amal == "3":
                print(f"Natija: {a * b}")
            elif amal == "4":
                if b == 0:
                    print("0 ga bo‘lish mumkin emas!")
                else:
                    print(f"Natija: {a / b}")
            elif amal == "5":
                print(f"Natija: {a % b}")
            else:
                print("Noto‘g‘ri tanlov!")

        # 3) Kredit/Omonat kalkulyatori
        elif tanlov == "3":
            print("\n💡 Kredit/Omonat Kalkulyatori bo‘limiga xush kelibsiz!")
            print("⚠️ Eslatma bilan tanishib chiqing:")
            print("Kredit formulasi annuitet to‘lov usulida hisoblaydi (ya’ni har oy to‘lov bir xil).")

            tanishuv = input("\n1 - Tanishib chiqdim\n2 - Yo‘q, rahmat, shart emas\nTanlov: ")

            if tanishuv == "1":
                asosiy_pul = float(input("\n1. Qancha pul kredit oldingiz (so‘mda): "))
                tolov_soni = int(input("2. 1 yilda necha marta to‘lov qilasiz: "))
                muddat = int(input("3. Necha yilga kredit oldingiz: "))
                foiz = float(input("4. Yillik foiz stavkasi (%), masalan 24 kiriting: "))

                # Hisoblash
                oy_soni = muddat * tolov_soni
                oy_foiz = foiz / 100 / tolov_soni
                if oy_foiz == 0:
                    tolov = asosiy_pul / oy_soni
                else:
                    tolov = asosiy_pul * (oy_foiz * (1 + oy_foiz)**oy_soni) / ((1 + oy_foiz)**oy_soni - 1)
                jami = tolov * oy_soni

                print(f"\nHar bir to‘lov: {tolov:,.2f} so‘m")
                print(f"Umumiy to‘lov: {jami:,.2f} so‘m")
                print(f"Foiz bo‘yicha ortiqcha to‘lov: {jami - asosiy_pul:,.2f} so‘m")
            else:
                print("Tushunarli, qaytib menyuga o‘tasiz 😊")

        else:
            print("Noto‘g‘ri tanlov!")

        davom = input("\nYana davom etasizmi? (ha/yo‘q): ").lower()
        if davom != "ha":
            print("Dastur tugadi!")
            break


    # -------- RUS TILI --------
    elif til == "rus":
        print("\n--- Главное меню ---")
        print("1 - Степень числа")
        print("2 - Обычный калькулятор")
        print("3 - Кредит/Депозит калькулятор")

        choice = input("Ваш выбор (1-3): ")

        if choice == "1":
            a, b = map(float, input("Введите число и степень (например: 2 3): ").split())
            print(f"Результат: {a ** b}")

        elif choice == "2":
            print("\nВыберите операцию:")
            print("1 - Сложение\n2 - Вычитание\n3 - Умножение\n4 - Деление\n5 - Остаток (%)")
            op = input("Ваш выбор (1-5): ")

            a, b = map(float, input("Введите два числа (например: 5 2): ").split())

            if op == "1":
                print(f"Результат: {a + b}")
            elif op == "2":
                print(f"Результат: {a - b}")
            elif op == "3":
                print(f"Результат: {a * b}")
            elif op == "4":
                if b == 0:
                    print("На ноль делить нельзя!")
                else:
                    print(f"Результат: {a / b}")
            elif op == "5":
                print(f"Результат: {a % b}")
            else:
                print("Неверный выбор!")

        elif choice == "3":
            print("\n💡 Добро пожаловать в раздел Кредит/Депозит!")
            print("⚠️ Ознакомьтесь с примечанием:")
            print("Формула кредита использует аннуитетные платежи (то есть ежемесячный платеж одинаковый).")

            read = input("\n1 - Ознакомился\n2 - Нет, спасибо\nВыбор: ")

            if read == "1":
                amount = float(input("\n1. Какую сумму кредита вы взяли (в сумах): "))
                payments_per_year = int(input("2. Сколько раз в год вы платите: "))
                years = int(input("3. На сколько лет кредит: "))
                rate = float(input("4. Годовая процентная ставка (%), например 24: "))

                n = payments_per_year * years
                i = rate / 100 / payments_per_year
                if i == 0:
                    payment = amount / n
                else:
                    payment = amount * (i * (1 + i)**n) / ((1 + i)**n - 1)
                total = payment * n

                print(f"\nПлатеж каждый раз: {payment:,.2f} сум")
                print(f"Общая сумма выплат: {total:,.2f} сум")
                print(f"Переплата по процентам: {total - amount:,.2f} сум")
            else:
                print("Хорошо, возвращаемся в меню 😊")

        again = input("\nПродолжить? (да/нет): ").lower()
        if again != "да":
            print("Программа завершена!")
            break


    # -------- ENGLISH --------
    elif til == "eng":
        print("\n--- Main Menu ---")
        print("1 - Power of a number")
        print("2 - Simple calculator")
        print("3 - Loan/Savings calculator")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            a, b = map(float, input("Enter number and power (e.g., 2 3): ").split())
            print(f"Result: {a ** b}")

        elif choice == "2":
            print("\nChoose operation:")
            print("1 - Add\n2 - Subtract\n3 - Multiply\n4 - Divide\n5 - Modulo (%)")
            op = input("Choice (1-5): ")

            a, b = map(float, input("Enter two numbers (e.g., 5 2): ").split())

            if op == "1":
                print(f"Result: {a + b}")
            elif op == "2":
                print(f"Result: {a - b}")
            elif op == "3":
                print(f"Result: {a * b}")
            elif op == "4":
                if b == 0:
                    print("Cannot divide by zero!")
                else:
                    print(f"Result: {a / b}")
            elif op == "5":
                print(f"Result: {a % b}")
            else:
                print("Invalid choice!")

        elif choice == "3":
            print("\n💡 Welcome to the Loan/Savings Calculator!")
            print("⚠️ Please read the note before continuing:")
            print("This calculator uses the annuity payment formula (equal monthly payments).")

            read = input("\n1 - I have read the note\n2 - No, thanks\nChoice: ")

            if read == "1":
                amount = float(input("\n1. How much money did you borrow (in sum): "))
                payments_per_year = int(input("2. How many payments per year: "))
                years = int(input("3. For how many years: "))
                rate = float(input("4. Annual interest rate (%), e.g. enter 24 for 24%: "))

                n = payments_per_year * years
                i = rate / 100 / payments_per_year
                if i == 0:
                    payment = amount / n
                else:
                    payment = amount * (i * (1 + i)**n) / ((1 + i)**n - 1)
                total = payment * n

                print(f"\nEach payment: {payment:,.2f} sum")
                print(f"Total payment: {total:,.2f} sum")
                print(f"Total interest paid: {total - amount:,.2f} sum")
            else:
                print("Alright, returning to menu 😊")

        again = input("\nContinue? (yes/no): ").lower()
        if again != "yes":
            print("Program ended!")
            break


    else:
        print("Noto‘g‘ri til tanlandi! / Неверный язык! / Invalid language!")
        til = input("Tilni tanlang / Выберите язык / Choose language (ozb/rus/eng): ").lower()
