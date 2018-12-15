#ESTOQUE em litros--------------------------------------
arm_gc = 2000 #gasolina comum
arm_ga = 2000 #gasolina adtivada
arm_et = 2000 #etanol
arm_die = 2000 #diesel


#Compra combustivel-------------------------------------
c_gc = 2.19 #gasolina comum
c_ga = 2.29 #gasolina adtivada
c_et = 1.19 #etanol
c_die = 1.39 #diesel

#Venda--------------------------------------------------
v_gc = 3.49 #gasolina comum
v_ga = 3.69 #gasolina adtivada
v_et = 2.39 #etanol
v_die = 2.89 #diesel
v_ducha = 8.00
v_to = 50.00 #troca de oléo
v_balan = 35.00 #balanceamento
v_cafe = 2.00
#Contadores----------------------------------------------
lts_gc = 0
lts_ga = 0
lts_et = 0
lts_die = 0
ab_gc = 0
ab_ga = 0
ab_et = 0
ab_die = 0
tv_ducha = 0
tv_to = 0
tv_balan = 0
tv_cafe = 0
lts_gc_v = 0
lts_ga_v = 0
lts_et_v = 0
lts_die_v = 0
lts_gc_c = 0
lts_ga_c = 0
lts_et_c = 0
lts_die_c = 0




#------------- ínicio ----------------------------------
print('=' * 40)
print('{:^50}'.format(' \033[32mBem-Vindo ao AUTOPOSTO\033[m ' ))
print('=' * 40)
menu0 = 0
while menu0 != 4:
    print(''' [1] Abastecimentos
 [2] Serviços adcionais
 [3] Estoque
 [4] Financeiro''')
    menu0 = int(input('Escolha a opção desejada: '))
    if menu0 == 1:
        menu1 = 0
        while menu1 != 5:
            print('''[1] Gasolina Comum
[2] Gasolina Adtivada
[3] Etanol
[4] Diesel
[5] voltar''')
            menu1 = int(input('Escolha o combustivel: '))


            if menu1 == 1:
                venda = float(input('Digite o valor a ser abastecido: '))
                lts_gc = venda / v_gc
                arm_gc = arm_gc - lts_gc
                lts_gc_v = lts_gc_v + lts_gc

                print ('\033[4;32mFoi abastecido {:.2f} Litros de gasolina comum\033[m'.format(lts_gc))

            if menu1 == 2:
                 venda = float(input('digite o valor a ser abastecido: '))
                 lts_ga = venda / v_ga
                 arm_ga = arm_ga - lts_ga
                 lts_ga_v = lts_ga_v + lts_ga

                 print('\033[4;32mFoi abastecido {:.2f} litros de gasolina adtivada\033[m'.format(lts_ga))
            if menu1 == 3:
                venda = float(input('Digite o valor a ser abastecido: '))
                lts_et = venda / v_et
                arm_et = arm_et - lts_et
                lts_et_v = lts_et_v + lts_et
                print('\033[4;32mFoi abastecido {:.2f} litros de etanol\033[m'.format(lts_et))
            if menu1 == 4:
                venda = float(input('Digite o valor a ser abastecido: '))
                lts_die = venda / v_die
                arm_die = arm_die - lts_die
                lts_die_v = lts_die_v + lts_die
                print('\033[4;32mFoi abastecido {:.2f} litros de diesel\033[m'.format(lts_die))
            if arm_gc < 300:
                print('\033[31mNivel do resservatório de gasolina comum está baixo\033[m')
            if arm_ga < 300:
                print('\033[31mNivel do resservatório de gasolina aditivada está baixo\033[m')
            if arm_et < 300:
                print('\033[31mNivel do resservatório de etanol está baixo\033[m')
            if arm_die < 300:
                print('\033[31mNivel do resservatório de diesel está baixo\033[m')


            if menu1 == 5:
                break
    if menu0 == 2:
         menu2 = 0
         while menu2 != 5:
             print('''[1] Ducha eco
[2] Troca de oléo
[3] Balanceamento
[4] Café
[5] Voltar''')
             menu2 = int(input('Escolha a opção desejada: '))
             if menu2 == 1:
                 print('\033[4;32mValor R$ {:.2f}\033[m'.format(v_ducha))
                 tv_ducha = tv_ducha + v_ducha
             if menu2 == 2:
                 print('\033[4;32mValor R$ {:.2f}\033[m'.format(v_to))
                 tv_to = tv_to + v_to
             if menu2 == 3:
                 print('\033[4;32mValor R$ {:.2f}\033[m'.format(v_balan))
                 tv_balan = tv_balan + v_balan
             if menu2 == 4:
                 print('\033[4;32mValor R% {:.2f}\033[m'.format(v_cafe))
                 tv_cafe = tv_cafe + v_cafe
             if menu2 == 5:
                 break

    if menu0 == 3:
        menu3 = 0
        while menu3 != 3:
            print('''[1] Abastecimento estoque
[2] Relatório estoque
[3] Voltar''')
            menu3 = int(input('Escolha a opção: '))

            if menu3 == 1:
                ab_gc = float(input('Quantos litros de gasolina comum foi abastecido ? '))
                if arm_gc + ab_gc <= 2000:
                    arm_gc = arm_gc + ab_gc
                    lts_gc_c = lts_gc_c + ab_gc
                else:
                    print('capacidade excedida')
                ab_ga = float(input('Quantos litros de gasolina aditivada foi abastecido? '))
                if arm_ga + ab_ga <= 2000:
                    arm_ga = arm_ga + ab_ga
                    lts_ga_c = lts_ga_c + ab_ga
                else:
                    print('capacidade excedida')
                ab_et = float(input('Quantos litros de etanol foi abastecido? '))
                if arm_et + ab_et <= 2000:
                    arm_et = arm_et + ab_et
                    lts_et_c = lts_et_c +ab_et
                else:
                    print('capacidade excedida')

                ab_die = float(input('Quantos litros de diesel foi abastecido? '))
                if arm_die + ab_die<= 2000:
                    arm_die = arm_die + ab_die
                    lts_die_c = lts_die_c + ab_die
                else:
                    print('capacidade excedida')



            if menu3 == 2:

                print('=' * 50)
                print('Há {:.2f} litros de gasolina comum'.format(arm_gc))
                print('Há {:.2f} litros de gasolina aftivada'.format(arm_ga))
                print('Há {:.2f} litros de etanol'.format(arm_et))
                print('Há {:.2f} litros de diesel'.format(arm_die))
                print('=' * 50)

            

            if menu3 == 3:
                break

    if menu0 == 4:
        vtotal_c_gc = lts_gc_c * c_gc #valor total de combustivel comprado
        vtotal_c_ga = lts_ga_c * v_ga
        vtotal_c_et = lts_et_c * v_et
        vtotal_c_die = lts_die_c * v_die


        #valor total vendido
        vtotal_v_gc = lts_gc_v * v_gc
        vtotal_v_ga = lts_ga_v * v_ga
        vtotal_v_et = lts_et_v * v_et
        vtotal_v_die = lts_die_v * v_die

        lucro_gc = vtotal_v_gc - (lts_gc_v * c_gc)
        lucro_ga = vtotal_v_ga - (lts_ga_v * c_ga)
        lucro_et = vtotal_v_et - (lts_et_v * c_et)
        lucro_die = vtotal_v_die - (lts_die_v * c_die)

        fechlucro = lucro_gc + lucro_ga + lucro_et + lucro_die + tv_ducha + tv_cafe + tv_to + tv_balan
        fechcomb = vtotal_v_gc + vtotal_v_ga + vtotal_v_et + vtotal_c_die

        print('{:=^90}'.format(' \033[33mRelatório venda de combustiveis\033[m '))
        print(f'Gasolina comum - Compra: R${vtotal_c_gc} ({lts_gc_c} lts.) Venda: R${vtotal_v_gc} ({lts_gc_v} lts.) Lucro total: R${lucro_gc}')
        print(f'Gasolina adtivada - Compra: R${vtotal_c_ga} ({lts_ga_c} lts.) Venda: R${vtotal_v_ga} ({lts_ga_v} lts.) Lucro total: R${lucro_ga}')
        print(f'Etanol - Compra: R${vtotal_c_et} ({lts_et_c} lts.) Venda: R${vtotal_v_et} ({lts_et_v} lts.) Lucro total: R${lucro_et}')
        print(f'Diesel - Compra: R${vtotal_c_die} ({lts_die_c} lts.) Venda: R${vtotal_v_die} ({lts_die_v} lts.) Lucro total: R${lucro_die}')

        print('{:=^90}'.format(' \033[33mRelatório de serviços adicionais\033[m '))
        print(f'Total Ducha: R${tv_ducha}')
        print(f'Total Troca de óleo: R${tv_to}')
        print(f'Total Balanceamento: R${tv_balan}')
        print(f'Total Café: R${tv_cafe}')

        print('{:=^90}'.format(' \033[33mGanhos Totais\033[m '))
        print('Valor total referente a venda de combustivel: R${:.2f}'.format(fechcomb))
        print('Total de Lucro: R${:.2f}'.format(fechlucro))