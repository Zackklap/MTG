# mtg deck comparison
import ast
import pprint

def readFile(fileName):
    fileName = fileName + '.txt'
    file = open(fileName, "r")
    dict = {}
    content_list = file.readlines()
    for i in range(len(content_list)):
        content_list[i] = content_list[i][:-1]
    for y in content_list:
        dict[y[2:]] = int(y[0])
    return dict

def dict_keys_to_array(dict):
    ret_array = []
    for key in dict.keys():
        ret_array .append(key)
    return ret_array


def compare_decks(deck1, deck2):
    deck1_dic = readFile(deck1)
    deck2_dic = readFile(deck2)
    removed = {}
    replace={}
    for key in deck1_dic.keys():
        if key not in deck2_dic:
            removed[key] = 1
    for key in deck2_dic.keys():
        if key not in deck1_dic:
            replace[key] = 1
    replce_arr = dict_keys_to_array(replace)
    remove_arr = dict_keys_to_array(removed)

    replce_file = open("replace.txt", "x")
    replce_file.write('\n'.join(map(str, replce_arr)))
    replce_file.close()
    remove_file = open("remove.txt", "x")
    remove_file.write('\n'.join(map(str, remove_arr)))
    remove_file.close()
    return "poggies"

compare_decks('precon','upgraded')
