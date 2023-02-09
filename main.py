datalist = []


class Cell:
    def __init__(self, data, nextCell):
        self.data = data
        self.nextCell = nextCell

    def __str__(self):
        if self is None:
            return 'None'
        else:
            return str(self.data)

    def addCell(self, cell):
        self.nextCell = cell


def addData(data):
    cell = Cell(data, None)
    row = data % 10
    if datalist[row] is None:
        datalist[row] = cell
    else:
        lastCell = datalist[row]
        while lastCell.nextCell is not None:
            lastCell = lastCell.nextCell
        lastCell.addCell(cell)


def findData(data):
    row = data % 10
    cell = datalist[row]
    found = False
    while cell is not None:
        if cell.data == data:
            found = True
            break
        cell = cell.nextCell
    if found:
        print("Data found !")
    else:
        print("Data NOT found !")


def deleteData(data):
    row = data % 10
    cell = datalist[row]
    found = False
    if cell is not None:
        if cell.data == data:
            datalist[row] = cell.nextCell
            found = True
        else:
            while not found:
                nextCell = cell.nextCell
                if nextCell.data == data:
                    cell.addCell(nextCell.nextCell)
                    del nextCell
                    found = True
                cell = cell.nextCell
    if found:
        print('Data found and deleted.')
    else:
        print('Data NOT found, nothing deleted.')


def printList():
    for i in range(len(datalist)):
        cell = datalist[i]
        if cell is not None:
            while cell.nextCell is not None:
                print(cell, end=' ')
                cell = cell.nextCell
        print(cell)


def menu():
    print('1-Adding new data')
    print('2-Searching for a data')
    print('3-Deleting a data')
    print('4-Print list')
    print('5-Exit')
    ch = input("Your choice:")

    if ch == '1':
        data = input('Enter value to add:')
        addData(int(data))
    elif ch == '2':
        data = input('Enter data to be searched:')
        findData(int(data))
    elif ch == '3':
        data = input('Enter data to be deleted:')
        deleteData(int(data))
    elif ch == '4':
        printList()
    elif ch == '5':
        return
    menu()


if __name__ == '__main__':
    for i in range(0, 10):
        datalist.append(None)
    menu()
