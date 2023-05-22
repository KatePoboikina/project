import random
import turtle

class Trees(object):
    def __init__(self, genom):      # на вход класса поступает только геном дерева
        self.genom = genom      # геном дерева
        self.dl = None      # длина отрезков
        self.itr = None     # количество итераций роста дерева
        self.angl = None        # угол между ветвями дерева
        self.leng_stem = None       # длина ствола дерева в количестве отрезков
        self.leng_leaf = None   # длина листьев
        self.thick = None       # толщина ствола (толщина линии)
        self.leaf_thick = None      # толщина листа (толщина линии)
        self.sp = None      # скорость уменьшения толщины линии на ветках дерева (доля от начальной толщины ствола)
        self.r1 = None      # ниже заданы 3 цвета для листьев по системе RGB
        self.g1 = None
        self.b1 = None
        self.r2 = None
        self.g2 = None
        self.b2 = None
        self.r3 = None
        self.g3 = None
        self.b3 = None
        self.x = random.randint(0, 200)     # место, откуда вырастет дерево по оси х
    def DNK_to_RNK_to_protein(self):
        list_of_nucleotides = []
        list_of_amino_acid = []
        list_of_characteristics = []
        RNK = self.genom.replace('T', 'U')  # по 1 цепи ДНК дерева, создали его РНК

        """создали список всех кодонов в РНК"""
        i = 0
        while i < (len(RNK) - 2):
            k = str(RNK[i] + RNK[i + 1] + RNK[i + 2])
            list_of_nucleotides.append(k)
            i += 3


        rgb_1_1 = [50, 205, 50]
        rgb_2_1 = [255, 255, 0]
        rgb_1_2 = [0, 250, 154]
        rgb_2_2 = [240, 230, 140]
        rgb_1_3 = [0, 128, 0]
        rgb_2_3 = [189, 183, 107]
        """присваиваем каждому кодону РНК числовое значение для перевода его в характеристику дерева (аминокислоту)"""
        translate_nucleotides_to_protein = {
            'UUU': 12, 'UUC': 12,
            'UUA': 7, 'UUG': 7, 'CUU': 7, 'CUC': 7, 'CUA': 7, 'CUG': 7,
            'AUU': 10, 'AUC': 10, 'AUA': 10,
            'GUU': 6, 'GUC': 6, 'GUA': 6, 'GUG': 6,
            'UCU': 3, 'UCC': 3, 'UCA': 3, 'UCG': 3, 'AGU': 3, 'AGC': 3,
            'CCU': 4, 'CCC': 4, 'CCA': 4, 'CCG': 4,
            'ACU': 5, 'ACC': 5, 'ACA': 5, 'ACG': 5,
            'GCU': 20, 'GCC': 20, 'GCA': 20, 'GCG': 20,
            'UAU': 30, 'UAC': 30,
            'CAU': 0.75,
            'CAC': 0.6,
            'CAA': rgb_1_1[0], 'CAG': rgb_2_1[0],
            'AAU': rgb_1_1[1], 'AAC': rgb_2_1[1],
            'AAA': rgb_1_1[2], 'AAG': rgb_2_1[2],
            'GAU': rgb_1_2[0], 'GAC': rgb_2_2[0],
            'GAA': rgb_1_2[1], 'GAG': rgb_2_2[1],
            'UGU': rgb_1_2[2], 'UGC': rgb_2_2[2],
            'UGG': rgb_1_3[0], 'GGG': rgb_2_3[2],
            'CGU': rgb_1_3[1], 'CGC': rgb_1_3[1], 'CGA': rgb_2_3[1],
            'CGG': rgb_1_3[1], 'AGA': rgb_2_3[1], 'AGG': rgb_2_3[1],
            'GGU': rgb_1_3[2], 'GGC': rgb_2_3[2], 'GGA': rgb_1_3[2]
        }
        """переводим все смысловые кодоны (кроме стоп и старт кодонов) в числовые характеристи (аминокислоты) дерева и заносим в список, вместе со старт и стоп кодонами"""
        for i in list_of_nucleotides:
            if i in translate_nucleotides_to_protein:
                k = translate_nucleotides_to_protein[i]
                list_of_amino_acid.append(k)
            else:
                list_of_amino_acid.append(i)

        """переводим список аминокислот в список характеристик дерева"""
        """если несколько кодонов стоят между стоп и старт кодоном, они кодируют один и тот же признак, чья характеристика вычсляется их средним арифметическим"""
        for i in range(0, len(list_of_amino_acid)):
            s = 0
            k = 0
            if list_of_amino_acid[i] == 'AUG':
                i += 1
                while list_of_amino_acid[i] != 'UAA':
                    s += list_of_amino_acid[i]
                    k += 1
                    i += 1
                list_of_characteristics.append(s / k)
                i += 1
        """после у нас остается список из чисел, которые задают параметры дерева"""

        """присваиваем характеристикам дерева их параметры из списка по порядку"""
        self.dl = int(list_of_characteristics[0])
        self.itr = int(list_of_characteristics[1])
        self.angl = int(list_of_characteristics[2])
        self.leng_stem = int(list_of_characteristics[3])
        self.leng_leaf = int(list_of_characteristics[4])
        self.thick = int(list_of_characteristics[5])
        self.leaf_thick = int(list_of_characteristics[6])
        self.sp = list_of_characteristics[7]
        self.r1 = int(list_of_characteristics[8])
        self.g1 = int(list_of_characteristics[9])
        self.b1 = int(list_of_characteristics[10])
        self.r2 = int(list_of_characteristics[11])
        self.g2 = int(list_of_characteristics[12])
        self.b2 = int(list_of_characteristics[13])
        self.r3 = int(list_of_characteristics[14])
        self.g3 = int(list_of_characteristics[15])
        self.b3 = int(list_of_characteristics[16])
    def create_tree_code(self):
        self.axiom = str(self.leng_stem * '2' + '0')
        axmTemp = ""
        translate = {"1": "21", "0": "1[-20]+20"}
        for k in range(self.itr):
            for ch in self.axiom:
                if ch in translate:
                    axmTemp += translate[ch]
                else:
                    axmTemp += ch
            self.axiom = axmTemp
            axmTemp = ""
    def draw_tree(self):
        turtle.hideturtle()
        turtle.tracer(0)
        turtle.penup()
        turtle.setposition(self.x, -300)
        turtle.left(90)
        turtle.pendown()
        turtle.pensize(self.thick)
        stc = []
        for ch in self.axiom:
            if ch == "+":
                turtle.right(self.angl - random.randint(-13, 13))
            elif ch == "-":
                turtle.left(self.angl - random.randint(-13, 13))
            elif ch == "2":
                if random.randint(0, 10) > 4:
                    turtle.forward(self.dl + random.randint(-self.dl // 2, self.dl // 2))
            elif ch == "1":
                if random.randint(0, 10) > 4:
                    turtle.forward(self.dl + random.randint(-self.dl // 2, self.dl // 2))
            elif ch == "0":
                stc.append(turtle.pensize())
                turtle.pensize(self.leaf_thick)
                r = random.randint(1, 3)
                if r == 1:
                    turtle.pencolor('#%02x%02x%02x' % (self.r1, self.g1, self.b1))
                elif r == 2:
                    turtle.pencolor('#%02x%02x%02x' % (self.r2, self.g2, self.b2))
                else:
                    turtle.pencolor('#%02x%02x%02x' % (self.r3, self.g3, self.b3))
                turtle.forward(self.leng_leaf)
                turtle.pensize(stc.pop())
                turtle.pencolor('#000000')
            elif ch == "[":
                self.thick *= self.sp
                turtle.pensize(self.thick)
                stc.append(self.thick)
                stc.append(turtle.xcor())
                stc.append(turtle.ycor())
                stc.append(turtle.heading())
            elif ch == "]":
                turtle.penup()
                turtle.setheading(stc.pop())
                turtle.sety(stc.pop())
                turtle.setx(stc.pop())
                self.thick = stc.pop()
                turtle.pensize(self.thick)
                turtle.pendown()
        turtle.update()
        turtle.mainloop()
def mutation(tree):
    k = random.randint(0, 3)           # случайно выбираем тип мутации, которая произойдет (точковая, вставка или делеция, инверсия)
    tree_gen_list = list(tree.genom)  # создаем список из нуклеотидов по 1
    if k == 0:      # мутация точковая
        i = random.randint(0, len(tree_gen_list)-1)     # случайно выбираем индекс нуклеотида, который собираемся подвергнуть мутации
        tree_gen_list[i] = random.choice(['A', 'T', 'G', 'C'])     # случайно выбираем новое азотистое основания мутировавшего нуклеоида (важно заметить, то нуклеотид может помеься на себя самого, это обозначает процесс репарации)
        print(i)
        print('Точковая')
    elif k == 1:    # вставка
            i = random.randint(0, len(tree_gen_list)-1)  # случайно выбираем индекс нуклеотида, после которого будет вставка
            print(i)
            f = random.randint(0, 3)    # сколько вставим нуклеотидов (если 0 - репарация)
            print(f)
            temp_gen_list = []
            for j in range(0, i+1):     # прописываем начало списка генов до нуклеотида, после которого мутация, во временный список
                temp_gen_list.append(tree_gen_list[j])
            for n in range(1, f+1):    # прописываем мутацию во временный список генов
                g = random.choice(['A', 'T', 'G', 'C'])
                temp_gen_list.append(g)
            for h in range(i+1, len(tree_gen_list)):  # прописываем нуклеотиды после мутации
                temp_gen_list.append(tree_gen_list[h])
            tree_gen_list = temp_gen_list
            print('Вставка')
    elif k == 2:  # если делеция
        i = random.randint(0, len(tree_gen_list)-3)  # случайно выбираем индекс нуклеотида, после которого будет делеция
        print(i)
        k = random.randint(0, 3)    # сколько уберем нуклеотидов (если 0 - репарация)
        print(k)
        del tree_gen_list[i+1:i+k+1]  # удаляем нуклеотиды из списка
        print('Делеция')
    elif k == 3:    # если инверсия
        i = random.randint(0, len(tree_gen_list)-2)  # случайно выбираем индекс нуклеотида, с которого будет инверсия
        print(i)
        k = random.randint(i, len(tree_gen_list)-1)   # случайно выбираем нуклеотид, который будет концом инверсии (если i - репарация)
        print(k)
        temp_invers_list = []       # список, в который потом занесем гены в кусочке для инверсии в обратном порядке
        temp_gen_list = []
        for y in range(k-3, i-2, -1):     # создали кусочек с инверсией
            temp_invers_list.append(tree_gen_list[y])
        for h in range(0, i-1):       # переписали гены до начала инверсии без изменений
            temp_gen_list.append(tree_gen_list[h])
        for h in temp_invers_list:       # подписали во временный список генов инверсию
            temp_gen_list.append(h)
        for h in range(len(temp_gen_list), len(tree_gen_list)):   # прописали гены после инверсии
            temp_gen_list.append(tree_gen_list[h])
        tree_gen_list = temp_gen_list
        print('Инверсия')
    tree.genom = ''  # обнуляем геном дерева
    for i in range(len(tree_gen_list)):  # переписываем геном дерева по списку, в котором содержится мутация
        tree.genom += tree_gen_list[i]
    return tree.genom
def duplicate(tree_1, tree_2):
    tree_1_list_of_nucleotides = []
    tree_2_list_of_nucleotides = []
    result_tree_genom = ''
    tree_1_info_gens_list = []      # список несущих информацию кодонов 1 дерева
    tree_2_info_gens_list = []      # список несущих информацию кодонов 2 дерева
    result_tree_info_gens_list = []
    tree_1_gens = ''      # строка для генов, отвечающих за 1 характеристику
    tree_2_gens = ''

    i = 0
    while i < (len(tree_1.genom) - 2):      # создаем список из кодонов дерева 1
        k = str(tree_1.genom[i] + tree_1.genom[i + 1] + tree_1.genom[i + 2])
        tree_1_list_of_nucleotides.append(k)
        i += 3

    i = 0
    while i < (len(tree_2.genom) - 2):      # создаем список из кодонов дерева 2
        k = str(tree_2.genom[i] + tree_2.genom[i + 1] + tree_2.genom[i + 2])
        tree_2_list_of_nucleotides.append(k)
        i += 3

    for i in range(len(tree_1_list_of_nucleotides)):        # создаем список из кодонов дерева 1, несущих информацию (между ATG и TAA)
        if tree_1_list_of_nucleotides[i] == 'ATG':
            i += 1
            while tree_1_list_of_nucleotides[i] != 'TAA':
                tree_1_gens += tree_1_list_of_nucleotides[i]
                i += 1
            tree_1_info_gens_list.append(tree_1_gens)
            tree_1_gens = ''

    for i in range(len(tree_2_list_of_nucleotides)):        # создаем список из кодонов дерева 2, несущих информацию (между ATG и TAA)
        if tree_2_list_of_nucleotides[i] == 'ATG':
            i += 1
            while tree_2_list_of_nucleotides[i] != 'TAA':
                tree_2_gens += tree_2_list_of_nucleotides[i]
                i += 1
            tree_2_info_gens_list.append(tree_2_gens)
            tree_2_gens = ''


    common_info_gens_list = [tree_1_info_gens_list, tree_2_info_gens_list]      # список несущих информацию кодонов обоих деревьев

    for i in range(8):      # производим скрещивание 2 деревьев по всем признакам, кроме цветов листьев
        k = random.choice([0, 1])
        result_tree_info_gens_list.append(common_info_gens_list[k][i])

    i = 8
    while i < 17:       # производим скрещивание 2 деревьев по цветам листьев
        k = random.choice([0, 1])
        result_tree_info_gens_list.append(common_info_gens_list[k][i])
        result_tree_info_gens_list.append(common_info_gens_list[k][i+1])
        result_tree_info_gens_list.append(common_info_gens_list[k][i+2])
        i += 3


    for i in range(len(result_tree_info_gens_list)):    # из списка несущих информацию кодонов дерева-потомка составляем его геном
        x = 'ATG'+result_tree_info_gens_list[i]+'TAA'
        result_tree_genom += x
    if random.randint(0, 1) == 0:
        return Trees(result_tree_genom)
    else:
        print('Геном до мутации = ', result_tree_genom)
        tree = Trees(result_tree_genom)
        tree_mut = Trees(mutation(tree))
        print('Геном после мутации = ', tree_mut.genom)
        return tree_mut
tree_1 = Trees('ATGTTACTATAAATGATCATTATATAAATGTATTACTACTATTAAATGCCTTAAATGACCTAAATGATATAAATGCTCTAAATGCACTAAATGCAGTAAATGAATTAAATGAAATAAATGGATTAAATGGAGTAAATGTGTTAAATGTGGTAAATGCGTTAAATGGGTTAA')
tree_1.DNK_to_RNK_to_protein()
tree_2 = Trees('ATGTTTTTCTAAATGGTAGTGGTTTAAATGGCATAAATGGTCTAAATGTCCTAAATGATCTAAATGAGCTAAATGCATTAAATGCAGTAAATGAATTAAATGAAATAAATGGATTAAATGGAGTAAATGTGTTAAATGTGGTAAATGCGTTAAATGGGTTAA')
tree_2.DNK_to_RNK_to_protein()
tree_3 = duplicate(tree_1, tree_2)
tree_3.DNK_to_RNK_to_protein()
print('genom =', tree_3.genom)
print('dl =', tree_3.dl)
print('itr =', tree_3.itr)
print('angl =', tree_3.angl)
print('leng_stem =', tree_3.leng_stem)
print('leng_leaf =', tree_3.leng_leaf)
print('thick =', tree_3.thick)
print('leaf_thick =', tree_3.leaf_thick)
print('sp =', tree_3.sp)
print('rgb1 =', tree_3.r1, '-', tree_3.g1, '-', tree_3.b1)
print('rgb2 =', tree_3.r2, '-', tree_3.g2, '-', tree_3.b2)
print('rgb3 =', tree_3.r3, '-', tree_3.g3, '-', tree_3.b3)
tree_3.create_tree_code()
tree_3.draw_tree()


