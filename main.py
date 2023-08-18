import random
import pandas as pd
import numpy as np
# グラフ可視化
import plotly.graph_objects as go
#~.iat[列,行]

#number_of_party
number_of_party = 10
#number_of_element
number_of_element = 10
#the range of rand
min_rand = 0
max_rand = 5
#独立関数の設定

#平均値のx倍 <-今回は十個
a_times = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#平均値の加減算 <-今回は十個
b_add_and_sub = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


#初期集団の生成
#[x_1, x_2, x_3]
party = [[random.randint(min_rand,max_rand) for _ in range(number_of_element)] for _ in range(number_of_party)]

####評価関数の下準備####
#各要素ごとに固めて、配列化
party_element_list = []
for i in range(number_of_party):
    party_element = []
    for j in range(number_of_element):
        party_element.append(party[i][j])
    party_element_list.append(party_element)

print(party_element_list)

#平均値取る
average_list = []
for i in range(number_of_element):
    average = np.average(party_element_list[i])
    average_list.append(average)

print(average_list)

####スケーリング####
#平均値のx倍させる
times_evaluation_value_list = []
for i in range(number_of_element):
    times_evaluation_value = average_list[i] * a_times[i]
    times_evaluation_value_list.append(times_evaluation_value)
    # if times_evaluation_value <= np.max(party_element_list[i]) and times_evaluation_value >= np.min(party_element_list[i]):
    #     times_evaluation_value_list.append(times_evaluation_value)
    # else:
    #     #Errorハンドラーを作る
    #     #切り捨て処理の簡略化として (max-0.01), (min + 0.01) としている。
    #     print("An error has occurred.")
    #     err_min = (np.min(party_element_list[i]) / average_list[i]) - 0.01
    #     err_max = (np.max(party_element_list[i]) / average_list[i]) + 0.01
    #     print(f"You should change the {i} a_times number in the range from {err_min} to {err_max}")

print(times_evaluation_value_list)

#平均値をb増やす
evaluation_value_list = []
for i in range(number_of_element):
    evaluation_value = times_evaluation_value_list[i] + b_add_and_sub[i]
    evaluation_value_list.append(evaluation_value)
    # if evaluation_value <= np.max(party_element_list[i]) and evaluation_value >= np.min(party_element_list[i]):
    #     evaluation_value_list.append(evaluation_value)
    # else:
    #     #Errorハンドラーを作る
    #     #切り捨て処理の簡略化として (max-0.01), (min + 0.01) としている。
    #     print("An error has occurred.")
    #     err_min = (np.min(party_element_list[i]) / average_list[i]) - 0.01
    #     err_max = (np.max(party_element_list[i]) / average_list[i]) + 0.01
    #     print(f"You should change the {i} b_add_and_sub number in the range from {err_min} to {err_max}")

print(evaluation_value_list)

####評価関数####
indices_list = []
for i in range(number_of_element):
    #絶対値 <-np.abs
    distance = np.abs(party_element_list[i] - evaluation_value_list[i])
    indices = np.where(distance == np.min(distance))[0]
    indices_list.append(indices)

print(indices_list)
#配列番号の付与
# for i in range(number_of_element):
#     party[i].insert(0, i)