import os
import random
import time


def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


radicals = {
    # 17 Mar : 10 Radicals
    "一": "ground", "亅": "barb", "ハ": "fins", "丶": "drop", "丿": "slide",
    "二": "two", "亠": "lid", "大": "big", "人": "person", "入": "enter",
    # 18 Mar : 5 Radicals
    '力': 'power', '勹': 'prison', '口': 'mouth', '女': ['woman', 'women'], '七': 'seven',
    # 19 Mar : 10 Radicals
    '十': 'cross', '山': 'mountain', '川': 'river', '木': 'tree', '工': 'construction',
    '九': 'nine', '𠂉': 'gun', '日': 'sun', 'ト':'toe', '丨':'stick',
}

kanji_to_meaning = {
    # 17 Mar : 12 Kanji
    '人': ['person', 'people'], '太': 'fat', '大': 'big', '六': 'six', '一': 'one',
    '二': 'two', '三': 'three', '了': 'finish', '久': 'long time', '入': 'enter',
    '才': 'talent', '八': 'eight',
    # 18 Mar : 5 Kanji
    '力': 'power', '口': 'mouth', '人口': 'population', '女': 'woman', '七': 'seven',
    # 19 Mar : 12 Kanji 
    '十': 'ten', '山': 'mountain', '出': 'exit', '川': 'river', '木': 'tree', 
    '工': 'construction', '九': 'nine', '丸': 'circle', '日': 'sun', '上':'above', 
    '下':'below', '困': ['distressed', 'troubled', 'annoyed'],
}

kanji_to_hiragana = {
    # 17 Mar : 12 Kanji
    '人': ['じん', 'にん', 'ひと', 'nin', 'jin', 'hito'], '太': ['たい', 'tai'], '大': ['だい', 'たい', 'tai', 'dai'], '大きい': ['おおきい','ookii'], '六': ['ろく', 'roku'], '一': ['いち', 'ichi'],
    '二': ['に', 'ni'], '三': ['さん', 'san'], '了': ['りょう', 'ryou'], '久': ['きゅう', 'く', 'ひさ', 'kyuu', 'ku', 'hisa'], '入': ['にゅう', 'nyuu'],
    '才': ['さい', 'sai'], '八': ['はち', 'hachi'],
    # 18 Mar : 5 Kanji
    '力': ['ちから', 'りょく', 'りき', 'chikara', 'ryoku', 'riki'], '口': ['こう', 'く', 'くち', 'ku', 'kuchi', 'kou'], '人口': ['じんこう', 'jin'], '女': ['じょ', 'おんな', 'onna', 'jyou'], '七': ['なな', 'しち', 'nana', 'shichi'],
    # 19 Mar : 12 Kanji
    '十': ['じゅう', 'jyuu'], '山': ['さん','san'], '出': ['しゅつ', 'shutsu'], '川': ['かわ', 'kawa'], '木': ['もく', 'moku'], 
    '工': ['こう', 'kou'], '九': 'きゅう', '丸': 'まる', '日': ['にち', 'じつ', 'nichi', 'jitsu', 'ひ', 'hi'],  '上': ['じょう','jyou'], 
    '下':['ka', 'か'], '困':['こん', 'kon'],
}

false_answer = 0
false_answer_list = {}
correct_answer = 0
items = {}


clear()

while items == {}:
    print("Type of quiz")
    print("[1] Radicals")
    print("[2] Kanji to English")
    print("[3] Kanji To Hiragana (Or Romanization)")
    print("")
    quiz_type = input('')
    if quiz_type == '1':
        items = radicals
    elif quiz_type == '2':
        items = kanji_to_meaning
    elif quiz_type == '3':
        items = kanji_to_hiragana
    else:
        print('Invalid type')


while True:
    clear()

    if items == {}:
        print('Finished! 🎉')
        print('')
        print('== Result ==')
        print('')
        print(f'Correct: {correct_answer}')
        print(f'Incorrect: {false_answer}')
        print('')
        print(f'Need to study more:')
        print(false_answer_list)
        print('')
        input('Press Enter to exit...')
        clear()
        break

    print("===", quiz_type.capitalize(), "===")
    print("")
    print(f'Incorrect List: {false_answer_list}')
    print(f'Correct: {correct_answer}, Incorrect: {false_answer}')
    print("")

    item, real_answer = random.choice(list(items.items()))
    print(item)
    print("")
    user_answer = input()

    print("")
    if type(real_answer) == list and user_answer in real_answer:
        correct_answer += 1
        print('Correct ✅')

        # Delete the items if already correct
        del items[item]
    elif user_answer == real_answer:
        correct_answer += 1
        print('Correct ✅')

        # Delete the items if already correct
        del items[item]
    else:
        false_answer += 1
        false_answer_list[item] = real_answer
        print('Incorrect ❌')
        print(f'The correct answer is : {real_answer}')
    time.sleep(1)
    # input('Press Enter to continue...')
