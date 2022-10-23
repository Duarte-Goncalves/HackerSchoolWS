from pydoc import classname
from random import choices
from time import pthread_getcpuclockid, sleep

class Slot:
    simbolos = ['#','$','%','&','@','£','€']
    slotf = []
    def rodar(self):
        self.slotf.clear()
        for c in range(3):
            escolha = choices(self.simbolos, weights=(50/156,40/156,30/156,20/156,10/156,5/156,1/156))
            self.slotf.append(escolha[0])

        return self.slotf

money = ''
while not isinstance(money,int):
    try: money = int(input('Quanto crédito social deseja depositar: '))
    except ValueError:
        print('Tente de novo')

bet = 0
vezes = 0
vontade = True
while vontade:
    while True:
        bet = ''
        while not isinstance(bet,int):
            try: 
                bet = int(input('Quanto crédito social deseja apostar: '))
            except ValueError:
                print('Tente de novo')
        vezes = ''
        while not isinstance(vezes,int):
            try:
                vezes = int(input('Muito bem, e quantas vezes de seguida deseja apostar esse valor? '))
            except ValueError:
                print('Tente de novo')
        if bet*vezes <= money:
            break
        print('Não tens créditos suficientes para jogares assim.')
    
    print('May the wheels spin...')
    slot = Slot()
    for i in range(vezes):
        if money < 0:
            break
        if money < bet:
            bet = money
        money-= bet
        sleep(.33)
        slot.rodar()
        print(slot.slotf)
        if slot.slotf[0] == slot.slotf[1] == slot.slotf[2]:
            print('Parabéns, ganhaste ', end='')
            if slot.slotf[0] == '#':
                money+= bet*5
                print(f'{bet*5} créditos')
            if slot.slotf[0] == '$':
                money+= bet*10
                print(f'{bet*10} créditos')
            if slot.slotf[0] == '%':
                money+= bet*20
                print(f'{bet*20} créditos')
            if slot.slotf[0] == '&':
                money+= bet*70
                print(f'{bet*70} créditos')
            if slot.slotf[0] == '@':
                money+= bet*200
                print(f'{bet*200} créditos')
            if slot.slotf[0] == '£':
                money+= bet*1000
                print(f'{bet*1000} créditos')
            if slot.slotf[0] == '€':
                money+= bet*100000
                print(f'{bet*100000} créditos')
    if money <= 0:
        print('Ficaste sem créditos camarada, vais reconstruir a muralha. >:(')
        sleep(5)
        quit
    else:
        vontade = False if input('Deseja continuar a jogar? ').upper() == 'N' else True
        print(f'Ficaste com {money} creditos')
        #print('Não tens crédito social suficiente, vou te meter a reconstruir a muralha')