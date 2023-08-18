import random
import pandas as pd
import numpy as np
# グラフ可視化
import plotly.graph_objects as go
import pprint
import copy
#~.iat[列,行]




def GA(number_of_party, number_of_element, min_rand, max_rand, a_times, b_add_and_sub, point, lower_limit, probability, party):
    ####評価関数の下準備####
    #各要素ごとに固めて、配列化
    party_element_list = []
    for i in range(number_of_element):
        party_element = []
        for j in range(number_of_party):
            party_element.append(party[j][i])
        party_element_list.append(party_element)

    print("Elemented ([[No.0 elements][No.1 elements]...])")
    print(party_element_list)

    #平均値取る
    average_list = []
    for i in range(number_of_element):
        average = np.average(party_element_list[i])
        average_list.append(average)

    print("Average list (average_list)")
    print(average_list)

    ####スケーリング####
    #平均値のx倍させる
    times_evaluation_value_list = []
    for i in range(number_of_element):
        times_evaluation_value = average_list[i] * a_times[i]
        times_evaluation_value_list.append(times_evaluation_value)

    #平均値をb増やす
    evaluation_value_list = []
    for i in range(number_of_element):
        evaluation_value = times_evaluation_value_list[i] + b_add_and_sub[i]
        evaluation_value_list.append(evaluation_value)

    print("Scaled (evaluation_value_list)")
    print(evaluation_value_list)

    ####評価関数####
    #評価
    indices_list = []
    for i in range(number_of_element):
        #絶対値 <-np.abs
        distance = np.abs(party_element_list[i] - evaluation_value_list[i])
        indices = np.where(distance == np.min(distance))[0]
        indices_list.append(indices)

    print("Indices List")
    pprint.pprint(indices_list)

    #得点の付与
    party_changed = copy.deepcopy(party)
    party_access = copy.deepcopy(party)
    for i in range(number_of_element):
        for j in range(len(indices_list[i])):
            party_address = indices_list[i][j]
            party_changed[party_address][i] = [party_access[party_address][i], point]

    print("Result")
    pprint.pprint(party_changed)

    #得点の集計
    party_point_list = []
    for i in range(number_of_party):
        party_point = 0
        for j in range(number_of_element):
            if type(party_changed[i][j]) is list:
                party_point = party_point + point
            else:
                pass
        party_point_list.append(party_point)
    #パーティ番号の付与
    for i in range(number_of_party):
        party_point = party_point_list[i]
        party_point_list[i] = [party_point, i]

    print("Molded Party Point (party_point_list)")
    print(party_point_list)

    #ソートする
    sorted_data = sorted(party_point_list, reverse=True)

    print("Sorted Data")
    print(sorted_data)

    #選択 (エリート戦略)
    selected_data = sorted_data[:lower_limit]

    print("Selected Data")
    print(selected_data)

    selected_party_list = []
    for i in range(lower_limit):
        for j in range(2):
            if j==0:
                pass
            elif j==1:
                selected_party = party[selected_data[i][j]]
        selected_party_list.append(selected_party)

    print("Selected Party list")
    pprint.pprint(selected_party_list)

    #交叉 (1点交叉)
    child = []
    child_list = []
    for i in range(number_of_party - lower_limit):
        number_of_element_molded = number_of_element - 1
        random_choice_1_list = selected_party_list[random.randint(0, lower_limit - 1)]
        random_choice_2_list = selected_party_list[random.randint(0, lower_limit - 1)]
        print("Parents")
        print(random_choice_1_list)
        print(random_choice_2_list)
        random_cut = random.randint(0, number_of_element_molded)
        random_cut_list = random_choice_1_list[:random_cut]
        random_cut_2_list = random_choice_2_list[random_cut:number_of_element]
        print("The parts of Children")
        print(random_cut_list)
        print(random_cut_2_list)
        child = random_cut_list + random_cut_2_list
        child_list.append(child)

    print("赤ちゃん爆誕")
    print(child_list)

    #突然変異
    rest_of_probability = 1 - probability
    for i in range(number_of_party - lower_limit):
        mutation_party = child_list[i]
        flag = np.random.choice([0,1], p=[probability, rest_of_probability])
        if flag==0:
            change_child_part = random.randint(0, number_of_element_molded)
            choice_element_number = random.randint(min_rand, max_rand)
            mutation_party[change_child_part] = choice_element_number
        elif flag==1:
            pass

    print("赤ちゃんの突然変異")
    print(child_list)

    #合体(新しい母集団の完成)
    result = selected_party_list + child_list
    print("合体（新しい母集団の完成）")
    print(result)
    return result








######################初期設定######################
#number_of_party
number_of_party = 10
#number_of_element
number_of_element = 10
#the range of rand
min_rand = 0
max_rand = 5
#平均値のx倍 <-今回は十個
a_times = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#平均値の加減算 <-今回は十個
b_add_and_sub = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#得点の設定
point=1
#エリート選択時の下限順位
lower_limit = 5
#突然変異の発生割合 (0~1)
probability = 0
#世代
generation = 1000

######################初期集団の生成######################
#[x_1, x_2, x_3]
party = [[random.randint(min_rand,max_rand) for _ in range(number_of_element)] for _ in range(number_of_party)]

print("Party (This is a original data)")
print(party)


######################実行######################
gen=1
while gen <= generation:
    print(f"第{gen}世代")
    result = GA(number_of_party, number_of_element, min_rand, max_rand, a_times, b_add_and_sub, point, lower_limit, probability, party)
    gen = gen + 1