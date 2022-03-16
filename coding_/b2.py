def GetInput():
    l = []
    while True:
        s = input()
        if not s:
            break
        t = tuple(s.split(","))
        l.append(t)
    return l

def Qsort(elements):
    for i in range(len(elements) - 1):
        if (elements[i][0] > elements[i+1][0]): 
            elements[i], elements[i+1] = elements[i+1], elements[i]
        elif (int(elements[i][1]) > int(elements[i+1][1])): 
            elements[i], elements[i+1] = elements[i+1], elements[i]
        elif (int(elements[i][2]) > int(elements[i+1][2])): 
            elements[i], elements[i+1] = elements[i+1], elements[i]

def main():
    #elements = GetInput()
    elements = [('Tom', '19', '80'), ('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85')]
    Qsort(elements)
    print(elements)

if __name__ == "__main__":
    main()
