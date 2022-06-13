# Given an array of arrays, implement an iterator class to allow the client to
# traverse and remove elements in the array list. This iterator should provide
# three public class member functions:
# def hasNext()
#    return true or false if there is another element in the set
#  def next()
#    return the value of the next element in the array
# def remove()
#    remove the last element returned by the iterator.
#    That is, remove the element that the previous next() returned
#
# The code should be well structured, and robust enough to handle any access
# pattern. Additionally, write code to demonstrate that the class can be used for
# the following basic scenarios:
# Print elements
#   Given:  [[],[1,2,3],[4,5],[],[],[6],[7,8],[],[9],[10],[]]
#   Print:  1 2 3 4 5 6 7 8 9 10
# Remove multiplies of 3
#   Given:  [[],[1,2,3],[4,5],[],[],[6],[7,8],[],[9],[10],[]]
#   Should result in:  [[],[1,2],[4,5],[],[],[],[7,8],[],[],[10],[]]

# array_list = [[1,2,3],[7,6]]
# iter = Iterator(array_list)
# iter.next() # return 1
# iter.next() # return 2
# iter.hasNext() # return True
# 1, 2, 3, 7 , 6


'''

for i in Outer
    for j in Inner
        if typeof(arr[i][j]) is list:


'''


class Iterator():

    def __init__(self, arrList):
        self.arr = arrList
        self.curr_i = 0
        self.curr_j = 0

    def next(self):

        while self.hasNext():
            print("Ith value: ", self.curr_i, "jth value: ", self.curr_j)

            print(self.arr)
            val = self.arr[self.curr_i][self.curr_j]
            self.curr_j += 1
            return val
        return

    # [[],[1,2,3],[4,5],[],[],[6],[7,8],[],[9],[10],[]]
    def hasNext(self):

        while True:
            if self.curr_i > len(self.arr) - 1:
                return False

            if len(self.arr[self.curr_i]) == 0:
                self.curr_i += 1
                self.curr_j = 0

            elif len(self.arr[self.curr_i]) - 1 < self.curr_j:
                self.curr_i = 1
                self.curr_j = 0

            else:
                print("Ith value: ", self.curr_i, "jth value: ", self.curr_j)
                return True

        return False


def testCase1(arrayList):
    it = Iterator(arrayList)
    while (it.hasNext()):
        print(it.next())


def testCase2(arrayList):
    it = Iterator(arrayList)
    while (it.hasNext()):
        it.hasNext()
        print(it.next())


def testCase3(arrayList):
    it = Iterator(arrayList)
    for i in range(20):
        print(it.next())


def testCase4(arrayList):
    it = Iterator(arrayList)
    while (it.hasNext()):
        x = it.next()
        if (x % 4 == 0):
            it.remove()
    print(arrayList)


def testCase5(arrayList):
    '''Remove everything from the list'''
    it = Iterator(arrayList)
    while it.hasNext():
        it.next()
        it.remove()
    print(arrayList)


arrayList = [[], [1, 2, 3], [4, 5], [], [], [6], [7, 8], [], [9], [10], []]
if __name__ == '__main__':
    # Scenario 1
    # testCase1(arrayList)
    # testCase2(arrayList)
    # testCase3(arrayList)
    it = Iterator(arrayList)
    print(it.next())
    print(it.hasNext())
    # Scenario 2
    # testCase4(arrayList)
    # testCase5(arrayList)
