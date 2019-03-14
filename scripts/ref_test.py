def main():
    lst = []
    for x in range(1, 10):
        appnd(lst, x)

    print(lst)



def appnd(lst, x):
    lst.append(x)


if __name__ == '__main__':
    main()
