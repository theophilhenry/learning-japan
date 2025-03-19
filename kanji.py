import os
import random
import time

radicals = {
  # 17 Mar : 10 Radicals
  "一": "ground", "亅": "barb", "ハ": "fins", "丶": "drop", "丿": "slide",
  "二": "two", "亠": "lid", "大": "big", "人": "person", "入": "enter",
  # 18 Mar : 5 Radicals
  '力': 'power', '勹': 'prison', '口': 'mouth', '女': ['woman', 'women'], '七': 'seven',
}

kanji_to_meaning = {
  # 17 Mar
  '人': ['person', 'people'], '太': 'fat', '大': 'big', '六': 'six', '一': 'one', 
  '二': 'two', '三': 'three', '了': 'finish', '久': 'long time', '入': 'enter',
  '才': 'talent', '八': 'eight',
  # 18 Mar
  '力': 'power', '口': 'mouth', '人口': 'population', '女': 'woman', '七': 'seven',
}

kanji_to_hiragana = {
  # 17 Mar : 12 Kanji
  '人': ['じん', 'にん', 'ひと'], '太': 'たい', '大': ['だい', 'たい'], '六': 'ろく', '一': 'いち', 
  '二': 'に', '三': 'さん', '了': 'りょう', '久': ['きゅう', 'く', 'ひさ'], '入': 'にゅう',
  '才': 'さい', '八': 'はち',
  # 18 Mar : 5 Kanji
  '力': ['ちから', 'りょく', 'りき'], '口': ['こう', 'く', 'くち'], '人口': ['じんこう'], '女': ['じょ', 'おんな'], '七': ['なな', 'しち'],
}

false_answer = 0
false_answer_list = {}
correct_answer = 0

items = {}

os.system('clear')
  
while items == {}:
  print("Type of quiz")
  print("[1] Radicals")
  print("[2] Kanji to English")
  print("[3] Kanji To Hiragana")
  print("")
  quiz_type = input('')
  if quiz_type == '1': items = radicals
  elif quiz_type == '2': items = kanji_to_meaning
  elif quiz_type == '3': items = kanji_to_hiragana
  else: print('Invalid type')


while True:
  os.system('clear')

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
    os.system('clear')
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