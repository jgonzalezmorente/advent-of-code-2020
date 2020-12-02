
with open('input.txt') as input:
    expense_report = [int(m) for m in input]

expense_report.sort()
expense_report = tuple(expense_report)

# Primera parte
print('==================== PRIMERA PARTE ====================')

def search_sum(list, target_sum):

    i = 0
    j = len(list) - 1

    while (i <= j):
        sum = list[i] + list[j]
        if (sum == target_sum):
            print(list[i], list[j])
            return list[i] * list[j]            
        elif (sum < target_sum):
            i+=1
        else:
            j-=1
    return 0

print(search_sum( expense_report, 2020 ))

# Segunda parte
print('==================== SEGUNDA PARTE ====================')

expense_report_list = list(expense_report)

for n in expense_report:

    
    expense_report_list.pop()

    prod2 = search_sum(tuple(expense_report_list), 2020-n )
    if prod2:
        print(n)
        print(n*prod2)
        break
        







