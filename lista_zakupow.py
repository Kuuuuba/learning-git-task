lista_zakupow = {'PIEKARNIA': ('CHLEB', 'BUŁKI', 'PĄCZKI'),
'WARZYWNIALK': ('MARCHEW', 'SELER','RUKOLA')}
for sklep, produkty in lista_zakupow.items():
    print('Idę do', sklep, 'i kupuję tam', produkty)
for produkty in lista_zakupow.values():
    print('W sumie kupuję', len(produkty), 'produktów') 
