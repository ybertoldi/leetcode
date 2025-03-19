"""
# uma lista ordenada é do tipo [1,2,3,4,5]
# rotacionada uma vez ela fica [5,1,2,3,4]
# duas vezes: [4,5,1,2,3]
# com cinco vezes ela volta ao estado original

toda lista ordenada rotacionada se encaixa em dois casos:
1 - ela é idêntica a original
2 - ela possui duas partes ordenadas e um trecho de disrupção que separa as duas. 
    A parte ordenada da esquerda tem sempre números maiores que da direita.

Por exemplo:
Lista: [5, 6, 7, 1, 2, 3, 4]
parte ordenada da esquerda (maior): [5, 6, 7]
parte ordenada da direita (menor): [1, 2, 3, 4]
trecho de disrupção: [7, 1]

O trecho de disrupção é o único onde um número é maior que seu sucessor. 
Em todas as outras partes da lista, um número é sempre sucedido por outro maior.

"""



def search(nums, target):
    l, r = 0, len(nums) - 1
    
    while l <= r:
        
        m = (l + r) // 2

        # binary search comum: caso da lista estar ordenada de l à r (ou seja, não possua disrupção)
        if nums[l] < nums[r]:

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1                 
        
        # caso a lista não esteja ordenada de l à r (ou seja, há uma disrupção entre l e r)
        else:
            if target > nums[l]: # caso o alvo esteja na parte esquerda (maior) da lista
                if nums[l] > nums[m]: # caso haja disrupção de entre l e m da lista
                    r = m - 1
                elif l == m: # caso a lista tenha apenas 2 elementos com disrupção
                    r -= 1
                else:  #caso não haja disrupção entre l e m
                    if target < nums[m]:
                        r = m - 1
                    elif target > nums[m]:
                        l = m + 1
                    else:
                        return m
                    
            elif target < nums[l]: # caso o alvo esteja na parte direita (menor) da lista
                if nums[l] < nums[m]: # caso não haja disrupção entre l e m
                    l = m + 1
                elif l == m: # caso a lista tenha 2 elementos
                    l += 1
                else: #caso haja disrupção entre l e m
                    if target > nums[m]:
                        l = m + 1
                    elif target < nums[m]:
                        r = m - 1
                    else:
                        return m
            else:
                return l

    return -1