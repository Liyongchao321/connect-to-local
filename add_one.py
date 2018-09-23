
class solution:

    @staticmethod  
    def add_one(A):
        print(A)
        temp = 10
        i = 1
        while len(A) != 1:
            temp = A[-i]+1
            print(temp)
            A[-i] = temp%10
            if temp != 10:
                break
            if i < len(A):
                i = i+1
                print('zizi')
            else:
                A.append(1)
                A.reverse()
                print('sisi') 
                break 

        if len(A) == 1:
            if A[0] !=9:
                A[0] = A[0]+1
                print('haha')
            else:
                A[0] = 0
                A.append(1)
                A.reverse()
                print('hehe')

        return A


if __name__ == '__main__':
    solu = solution()
    A=[9]
    solu.add_one(A)
    print(A)

