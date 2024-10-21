from datetime import datetime

def calcul_virsta(data_nasterli):
    data_curenta = datetime.now()
    diferenta = data_curenta - data_nasterli
    virsta = diferenta.days //365
    return virsta

def citeste_data_nasterli():
    while True:
        try:
            data= input("(YYYY-MM-DD):")
            data_nasterli= datetime.strptime(data, "%Y-%m-%d")
            return data_nasterli
        except ValueError:
            print("Туған жылыңды нақты жаз")

if __name__ == "__main__":
    data_nasterli=citeste_data_nasterli()
    virsta = calcul_virsta(data_nasterli)
    print(f"Сенің жасың: {virsta} жас")