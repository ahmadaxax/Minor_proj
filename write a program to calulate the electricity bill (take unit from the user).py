unit=int(input("enter the number of units: "))
if unit<=100:
    print("no charges applied")
if 100<unit<200:
    unit=(unit-100)*5
    print("the charges applied will be ",unit)
if unit>200:
    unit=500+(unit-200)*10
    print("the charges applied will be ",unit)
