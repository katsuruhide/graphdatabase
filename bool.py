import random
import logical_operation as LO

class Atom:

    def __init__(self, k, name):
        """単語に設定するアトムの初期化。
        アトムの名前の設定、論理変数は0～(2^k)-1 の範囲で乱数を格納、k桁のbitの並置で表現"""
        self.NUMBER_OF_BIT = k
        self.name=name
        self.logical_variable = random.getrandbits(k)

    def print_atom(self):
        print(self.name + " : "+ str(self.logical_variable))

    def set_lv_random(self):
        self.logical_variable = random.getrandbits(self.NUMBER_OF_BIT)

def make_list_from_file(filename):
    with open(filename) as f:
        tmp=f.read()
    return tmp.split("\n")

def init_atom(number_of_bit):
    atomlist0 = []
    name_list = make_list_from_file('atomname.dat')

    for name in name_list:
        atomlist0.append(Atom(number_of_bit,name))

    return atomlist0

def atomlist_to_atomdict(l):
    atomlist1 = []
    for a in l:
        atomlist1.append((a.name, a.logical_variable))
    return dict(atomlist1)

def truth_function_for_predicate_logic(x, y):
    """述語論理の真理値関数
    denominatorは分母"""
    denominator = bin(x).count("1")
    if denominator == 0 :
        return 1
    else:
        return bin(x & y).count("1") / denominator

def make_knowledge_list():
    """(y → L)[x] = T
    [[y ,L , x, T], [y1, ...],.. ]"""
    knowledgelist=[]
    for knowledge in make_list_from_file("knowledge.dat"):
        knowledgelist.append(knowledge.split())
    return knowledgelist

def calculate_residual_error(atomdict,knowledgelist,number_of_bit):
    warning_threshold = 0.15 #警告の閾値
    count=0
    residual_error_list = []
    for knowledge in knowledgelist:
        while True:
            y_to_L = LO.implication_operation(atomdict[knowledge[0]], atomdict[knowledge[1]])
            truth_value = truth_function_for_predicate_logic(atomdict[knowledge[2]], y_to_L)
            residual_error = float(knowledge[3]) - truth_value
            if abs(residual_error) < warning_threshold:
                residual_error_list.append(residual_error)
                break
            elif count > 100:
                residual_error_list.append(residual_error)
                break
            else:
                atomdict[knowledge[0]] = random.getrandbits(number_of_bit)
                count+=1
    print(atomdict.values)
    print(residual_error_list)
    return atomdict

#def print_result(atomdict, knowledgelist):

def optimize_logical_variable():
    """論理変数の最適化"""
    number_of_bit = 8
    atom_list = init_atom(number_of_bit)
    atom_dict = atomlist_to_atomdict(atom_list)
    knowledge_list = make_knowledge_list()
    atom_dict = calculate_residual_error(atom_dict, knowledge_list,number_of_bit)



if __name__ == '__main__':

   optimize_logical_variable()


