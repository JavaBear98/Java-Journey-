#Money in original currency
league_of_legends_euro = int(input("How much 'EURO' would you like to convert into RP?"))
#Exchange rate euro to rp
league_of_legends_exchange_rate_euro_RP =  0.0063  #1 RP =0.0063 EURO
#Conversion euro to rp
rp_amount = league_of_legends_euro / league_of_legends_exchange_rate_euro_RP
print(f" Your {league_of_legends_euro} EUR can buy aproximately {int(rp_amount)} RP")