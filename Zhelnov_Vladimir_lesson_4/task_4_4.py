import utils

'''
<Valute ID="R01235">
<NumCode>840</NumCode>
<CharCode>USD</CharCode>
<Nominal>1</Nominal>
<Name>Доллар США</Name>
<Value>74,8355</Value>
</Valute>
'''
print(utils.currency_rates("USD"))

'''
<Valute ID="R01200">
<NumCode>344</NumCode>
<CharCode>HKD</CharCode>
<Nominal>10</Nominal>
<Name>Гонконгских долларов</Name>
<Value>95,9860</Value>
</Valute>
'''
print(utils.currency_rates("HKD"))

print(utils.currency_rates("noname"))

'''
    74.8355
    95.986
    None
'''