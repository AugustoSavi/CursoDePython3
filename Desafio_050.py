s=0
for c in range(0,6):
    n=int(input('Digite o numero[{}]:'.format(c)))
    if n%2==0:
        s+=n
print('Soma dos numeros pares:{}'.format(s))