from datascience import *
import collections as cl

class naive_bayes:
    def __init__(self):
        self.reader = None
        self.reader2 = None
        self.class_name = None
        self.dict_input = {}
        self.class_same_elements = []
        self.class_same_elements_count = []
        self.class_probabilities = []

    def input_from_user(self):
        flag = False

        self.reader = Table.read_table('dataMain.csv')

        column_names = self.reader.take(0)
        print(column_names)

        self.class_name = input('Enter Class Name : ')
        print()
        for i in column_names:
            if self.class_name == i:
                flag = True
        if flag is False:
            print('Class Name Not Present in File...')
            return

        for i in column_names:
            if self.class_name != i:
                self.dict_input[i] = input('Enter Value of {} : '.format(i))
        print()

        # print(self.dict_input)
        return

    def find_class_probabilities(self):
        class_contents = self.reader.column(self.class_name)

        for k, v in cl.Counter(class_contents).items():
            self.class_same_elements.append(k)
            self.class_same_elements_count.append(v)
            self.class_probabilities.append(v / len(class_contents))

        # print(self.class_same_elements)
        # print(self.class_same_elements_count)
        # print(self.class_probabilities)
        return

    def find_user_input_probabilities(self):
        for k, v in self.dict_input.items():
            self.reader2 = self.reader.groups([k, self.class_name]).where(k, v)

            for i in range(len(self.class_same_elements)):
                self.class_probabilities[i] = self.class_probabilities[i] * (self.reader2.where(self.class_name, self.class_same_elements[i]).column('count') / self.class_same_elements_count[i])

        # print(self.class_probabilities)
        return

    def final_answer(self):
        index = self.class_probabilities.index(max(self.class_probabilities))

        print('-------------------------------------------------------------------------------------------------------')
        print()
        print('The Point -->')
        for k, v in self.dict_input.items():
            print(k, ' : ', v)
        print()
        print('Belongs to the Class ', self.class_name, ' : ', self.class_same_elements[index])
        print()
        print('-------------------------------------------------------------------------------------------------------')
        return


if __name__ == '__main__':
    nb = naive_bayes()
    nb.input_from_user()
    nb.find_class_probabilities()
    nb.find_user_input_probabilities()
    nb.final_answer()
