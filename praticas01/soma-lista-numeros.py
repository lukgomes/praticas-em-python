nums = []
soma = 0

while True:
    nums.append(int(input("Informe um número a ser somado (Digite 0 para sair): ")))
    if (nums[len(nums) - 1] == 0):
        break


for num in nums:
    soma += num


print(f"A soma de todos os numeros informados é igual a {soma}.")