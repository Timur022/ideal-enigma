import requests as req
import json
import vk_api
import re
import time
import os
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


vk_session = vk_api.VkApi(token="e2ea1be79721ff8ca20375322c2f996e376a28c0338fc228e64dc8cd2bbdf7cdeaad1ec9428ff0ad10fd6")
i = 0
m = ''
k = 0
ri = 0
error_1 = 0
temp = ''
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
groups = {0: '18ПКС-1', 1: '18ПКС-2', 2: '19КСК-1', 3: '19КСК-2', 4: '19ПКС-1', 5: '19ПКС-1',
          6: '19ИС-1', 7: '19ОИБ-1', 8: '19ОИБ-2', 9: '19ОИБ-3', 10: '19БД-1', 11: '19ЭБУ-1',
          12: '19ПСО-1', 13: '19ПСО-2', 14: '19ПСО-3', 15: '19ПСО-4', 16: '19ЗИО-1', 17: '193ИО-2',
          18: '193ИО-3 (с)', 19: '19ПСО-5 (с)', 20: '19ПСО-6 (с)', 21: '19ОСАТП-1', 22: '19ОСАТП-2', 23: '19ТОРРТ-1',
          24: '19ТОРРТ-2', 25: '19ТМП-1', 26: '19МЭГ-1', 27: '19МТОР-1', 28: '19МТОР-2', 29: '19ПЛ-1',
          30: '19Э-1', 31: '19Э-2', 32: '18КСК-1', 33: '18КСК-2', 34: '18ИС-1', 35: '18ИС-2',
          36: '18ОИБ-1', 37: '18БД-1', 38: '18ЭБУ-1', 39: '18ПСО-1', 40: '18ПСО-2', 41: '18ПСО-3',
          42: '18ЗИО-1', 43: '18ЗИО-2', 44: '18ЗИО-3 (с)', 45: '18ПСО-4 (с)', 46: '18ПСО-5 (с)', 47: '18ЭБУ2-(с)',
          48: '18ПКС-1', 49: '18ПКС-2', 50: '19КСК-1', 51: '19КСК-2', 52: '18КСК-1', 53: '18КСК-2', 54: '18ИС-1', 55: '18ИС-2',
          56: '18ОИБ-1', 57: '18БД-1', 58: '18ЭБУ-1', 59: '18ПСО-1', 60: '18ПСО-2', 61: '18ПСО-3',
          62: '18ЗИО-1', 63: '18ЗИО-2', 64: '18ЗИО-3 (с)', 65: '18ПСО-4 (с)', 66: '18ПСО-5 (с)', 67: '18ЭБУ2-(с)',
          68: '18ОСАТП-1', 69: '18ОСАТП-2', 70: '18ТОРРТ-1', 71: '18ТОРРТ-2', 72: '18ТОРРТ-3', 73: '18ТМ-1',
          74: '18ТМ-2', 75: '18МЭГ-1', 76: '18МТОР-1', 77: '18ПЛ-1', 78: '18Э-1', 79: '17КСК-1',
          80: '17КСК-2', 81: '17ПКС-1', 82: '17ПКС-2', 83: '17ИС-1', 84: '17ИС-2', 85: '17ОИБ-1',
          86: '17БД-1', 87: '17ЭБУ-1', 88: '17ПСО-1', 89: '17ПСО-2', 90: '17ПСО-3', 91: '17ЗИО-1',
          92: '17ЗИО-2', 93: '17АТП-1', 94: '17ТОРРТ-1', 95: '17ТОРРТ-2', 96: '17ТОРРТ-3', 97: '17ТМ-1',
          98: '17ТМ-2', 99: '17МЭГ-1', 100: '17ПЛ-1', 101: '17З-1', 102: '17З-2', 103: '16КСК-1',
          104: '16КСК-2', 105: '16ПКС-1', 106: '16ПКС-2', 107: '16ИС-1', 108: '16АТП-1', 109: '16ТОРРТ-1',
          110: '16ТОРРТ-2', 111: '16ТМ-1', 112: '16ТМ-2', 113: '16МЭГ-1', 114: '16ПЛ-1', 115: '16ПО-1(ТМ)',
          116: '16ПО-2(А)', 117: '16Э-1', 118: '16Э-2', 119: 'З-19ПД-1', 120: 'З-19ПД-2', 121: 'З-19ЭБУ-1',
          122: 'З-19ЭБУ-2(о)', 123: 'З-19ПКС-1', 124: 'З-19ТОРРТ-1', 125: 'З-19Э-1', 126: 'З-19Э-2(0)', 127: 'З-18ПД-1',
          128: 'З-18ПД-2', 129: 'З-18ПД-3(0)', 130: 'З-18ЭБУ-1', 131: 'З-18ЭБУ-2(0)', 132: 'З-18ПКС-1', 133: 'З-18ПКС-2(0)',
          134: 'З-18ТОРРТ-1', 135: 'З-18ТОРРТ-2(0)', 136: 'З-18Э-1', 137: 'З-18Э-2(0)', 138: 'З-17ПД-1', 139: 'З-17ПД-2(0)',
          140: 'З-17ЭБУ-2(0)', 141: 'З-17ПКС-1', 142: 'З-17ТОРРТ-1', 143: 'З-17Э-1', 144: 'З-17Э-2(0)', 145: 'З-17ЭБУ-1',
          146: 'З-16ПД-1', 147: 'З-16ПКС-1', 148: 'З-16ТОРРТ-1', 149: 'З-16Э-1'
          }

button_days = {

}

time_now = time.localtime()

last = 0

month = int(time_now.tm_mon)
if month % 2 == 0 and month != 2 and month != 8 and month != 9 and month != 10 and month != 11 and month != 12:
    last = 30
elif month % 2 != 0 and month != 2 and month != 8 and month != 9 and month != 10 and month != 11 and month != 12:
    last = 31
elif month == 8 or month == 10 or month == 12:
    last = 31
elif month == 9 or month == 11:
    last = 30
elif int(t.tm_year) % 4 == 0:
    last = 29
else:
    last = 28

d = int(time_now.tm_mday)
day2 = 0

for day in range(d, d + 14):
    day2 += 1
    if day == last + 1:
        for day1 in range(1, 14 - (i - d)):
            button_days[day1] = str(day1)
        break
    button_days[day2] = str(day)

data = VkKeyboard(one_time=False)
data.add_button(button_days[1], color=VkKeyboardColor.PRIMARY)
data.add_button(button_days[8], color=VkKeyboardColor.PRIMARY)
data.add_line()
data.add_button(button_days[2], color=VkKeyboardColor.PRIMARY)
data.add_button(button_days[9], color=VkKeyboardColor.PRIMARY)
data.add_line()
data.add_button(button_days[3], color=VkKeyboardColor.PRIMARY)
data.add_button(button_days[10], color=VkKeyboardColor.PRIMARY)
data.add_line()
data.add_button(button_days[4], color=VkKeyboardColor.PRIMARY)
data.add_button(button_days[11], color=VkKeyboardColor.PRIMARY)
data.add_line()
data.add_button(button_days[5], color=VkKeyboardColor.PRIMARY)
data.add_button(button_days[12], color=VkKeyboardColor.PRIMARY)
data.add_line()
data.add_button(button_days[6], color=VkKeyboardColor.PRIMARY)
data.add_button(button_days[13], color=VkKeyboardColor.PRIMARY)
data.add_line()
data.add_button(button_days[7], color=VkKeyboardColor.PRIMARY)
data.add_button(button_days[14], color=VkKeyboardColor.PRIMARY)
data.add_line()
data.add_button('Отмена', color=VkKeyboardColor.DEFAULT)

keyboard1 = VkKeyboard(one_time=True)
keyboard1.add_button(groups[0], color=VkKeyboardColor.PRIMARY)
keyboard1.add_line()
keyboard1.add_button(groups[1], color=VkKeyboardColor.PRIMARY)

# keyboard1.add_button(groups[2], color=VkKeyboardColor.PRIMARY)
# keyboard1.add_button(groups[3], color=VkKeyboardColor.PRIMARY)
# keyboard1.add_line()
# keyboard1.add_button(groups[4], color=VkKeyboardColor.PRIMARY)
# keyboard1.add_button(groups[5], color=VkKeyboardColor.PRIMARY)
# keyboard1.add_line()
# keyboard1.add_button(groups[6], color=VkKeyboardColor.PRIMARY)
# keyboard1.add_button(groups[7], color=VkKeyboardColor.PRIMARY)
# keyboard1.add_line()
# keyboard1.add_button(groups[8], color=VkKeyboardColor.PRIMARY)
# keyboard1.add_button(groups[9], color=VkKeyboardColor.PRIMARY)
# keyboard1.add_line()
# keyboard1.add_button(groups[10], color=VkKeyboardColor.PRIMARY)
# keyboard1.add_button(groups[11], color=VkKeyboardColor.PRIMARY)
# keyboard1.add_line()
# keyboard1.add_button(groups[12], color=VkKeyboardColor.PRIMARY)
# keyboard1.add_button(groups[13], color=VkKeyboardColor.PRIMARY)
# keyboard1.add_line()
# keyboard1.add_button(groups[14], color=VkKeyboardColor.PRIMARY)
# keyboard1.add_button(groups[15], color=VkKeyboardColor.PRIMARY)
# keyboard1.add_line()
# keyboard1.add_button(groups[16], color=VkKeyboardColor.PRIMARY)
# keyboard1.add_button(groups[17], color=VkKeyboardColor.PRIMARY)
# keyboard1.add_line()
# keyboard1.add_button('Вперёд', color=VkKeyboardColor.DEFAULT)

keyboard2 = VkKeyboard(one_time=True)
keyboard2.add_button(groups[18], color=VkKeyboardColor.PRIMARY)
keyboard2.add_button(groups[19], color=VkKeyboardColor.PRIMARY)
keyboard2.add_line()
keyboard2.add_button(groups[20], color=VkKeyboardColor.PRIMARY)
keyboard2.add_button(groups[21], color=VkKeyboardColor.PRIMARY)
keyboard2.add_line()
keyboard2.add_button(groups[22], color=VkKeyboardColor.PRIMARY)
keyboard2.add_button(groups[23], color=VkKeyboardColor.PRIMARY)
keyboard2.add_line()
keyboard2.add_button(groups[24], color=VkKeyboardColor.PRIMARY)
keyboard2.add_button(groups[25], color=VkKeyboardColor.PRIMARY)
keyboard2.add_line()
keyboard2.add_button(groups[26], color=VkKeyboardColor.PRIMARY)
keyboard2.add_button(groups[27], color=VkKeyboardColor.PRIMARY)
keyboard2.add_line()
keyboard2.add_button(groups[28], color=VkKeyboardColor.PRIMARY)
keyboard2.add_button(groups[29], color=VkKeyboardColor.PRIMARY)
keyboard2.add_line()
keyboard2.add_button(groups[30], color=VkKeyboardColor.PRIMARY)
keyboard2.add_button(groups[31], color=VkKeyboardColor.PRIMARY)
keyboard2.add_line()
keyboard2.add_button(groups[32], color=VkKeyboardColor.PRIMARY)
keyboard2.add_button(groups[33], color=VkKeyboardColor.PRIMARY)
keyboard2.add_line()
keyboard2.add_button(groups[34], color=VkKeyboardColor.PRIMARY)
keyboard2.add_button(groups[35], color=VkKeyboardColor.PRIMARY)
keyboard2.add_line()
keyboard2.add_button('Назад', color=VkKeyboardColor.DEFAULT)
keyboard2.add_button('Вперёд', color=VkKeyboardColor.DEFAULT)

keyboard3 = VkKeyboard(one_time=True)
keyboard3.add_button(groups[36], color=VkKeyboardColor.PRIMARY)
keyboard3.add_button(groups[37], color=VkKeyboardColor.PRIMARY)
keyboard3.add_line()
keyboard3.add_button(groups[38], color=VkKeyboardColor.PRIMARY)
keyboard3.add_button(groups[39], color=VkKeyboardColor.PRIMARY)
keyboard3.add_line()
keyboard3.add_button(groups[40], color=VkKeyboardColor.PRIMARY)
keyboard3.add_button(groups[41], color=VkKeyboardColor.PRIMARY)
keyboard3.add_line()
keyboard3.add_button(groups[42], color=VkKeyboardColor.PRIMARY)
keyboard3.add_button(groups[43], color=VkKeyboardColor.PRIMARY)
keyboard3.add_line()
keyboard3.add_button(groups[44], color=VkKeyboardColor.PRIMARY)
keyboard3.add_button(groups[45], color=VkKeyboardColor.PRIMARY)
keyboard3.add_line()
keyboard3.add_button(groups[46], color=VkKeyboardColor.PRIMARY)
keyboard3.add_button(groups[47], color=VkKeyboardColor.PRIMARY)
keyboard3.add_line()
keyboard3.add_button(groups[48], color=VkKeyboardColor.PRIMARY)
keyboard3.add_button(groups[49], color=VkKeyboardColor.PRIMARY)
keyboard3.add_line()
keyboard3.add_button(groups[50], color=VkKeyboardColor.PRIMARY)
keyboard3.add_button(groups[51], color=VkKeyboardColor.PRIMARY)
keyboard3.add_line()
keyboard3.add_button(groups[52], color=VkKeyboardColor.PRIMARY)
keyboard3.add_button(groups[53], color=VkKeyboardColor.PRIMARY)
keyboard3.add_line()
keyboard3.add_button('Назад', color=VkKeyboardColor.DEFAULT)
keyboard3.add_button('Вперёд', color=VkKeyboardColor.DEFAULT)

keyboard4 = VkKeyboard(one_time=True)
keyboard4.add_button(groups[54], color=VkKeyboardColor.PRIMARY)
keyboard4.add_button(groups[55], color=VkKeyboardColor.PRIMARY)
keyboard4.add_line()
keyboard4.add_button(groups[56], color=VkKeyboardColor.PRIMARY)
keyboard4.add_button(groups[57], color=VkKeyboardColor.PRIMARY)
keyboard4.add_line()
keyboard4.add_button(groups[58], color=VkKeyboardColor.PRIMARY)
keyboard4.add_button(groups[59], color=VkKeyboardColor.PRIMARY)
keyboard4.add_line()
keyboard4.add_button(groups[60], color=VkKeyboardColor.PRIMARY)
keyboard4.add_button(groups[61], color=VkKeyboardColor.PRIMARY)
keyboard4.add_line()
keyboard4.add_button(groups[62], color=VkKeyboardColor.PRIMARY)
keyboard4.add_button(groups[63], color=VkKeyboardColor.PRIMARY)
keyboard4.add_line()
keyboard4.add_button(groups[64], color=VkKeyboardColor.PRIMARY)
keyboard4.add_button(groups[65], color=VkKeyboardColor.PRIMARY)
keyboard4.add_line()
keyboard4.add_button(groups[66], color=VkKeyboardColor.PRIMARY)
keyboard4.add_button(groups[67], color=VkKeyboardColor.PRIMARY)
keyboard4.add_line()
keyboard4.add_button(groups[68], color=VkKeyboardColor.PRIMARY)
keyboard4.add_button(groups[69], color=VkKeyboardColor.PRIMARY)
keyboard4.add_line()
keyboard4.add_button(groups[70], color=VkKeyboardColor.PRIMARY)
keyboard4.add_button(groups[71], color=VkKeyboardColor.PRIMARY)
keyboard4.add_line()
keyboard4.add_button('Назад', color=VkKeyboardColor.DEFAULT)
keyboard4.add_button('Вперёд', color=VkKeyboardColor.DEFAULT)

keyboard5 = VkKeyboard(one_time=True)
keyboard5.add_button(groups[72], color=VkKeyboardColor.PRIMARY)
keyboard5.add_button(groups[73], color=VkKeyboardColor.PRIMARY)
keyboard5.add_line()
keyboard5.add_button(groups[74], color=VkKeyboardColor.PRIMARY)
keyboard5.add_button(groups[75], color=VkKeyboardColor.PRIMARY)
keyboard5.add_line()
keyboard5.add_button(groups[76], color=VkKeyboardColor.PRIMARY)
keyboard5.add_button(groups[77], color=VkKeyboardColor.PRIMARY)
keyboard5.add_line()
keyboard5.add_button(groups[78], color=VkKeyboardColor.PRIMARY)
keyboard5.add_button(groups[79], color=VkKeyboardColor.PRIMARY)
keyboard5.add_line()
keyboard5.add_button(groups[80], color=VkKeyboardColor.PRIMARY)
keyboard5.add_button(groups[81], color=VkKeyboardColor.PRIMARY)
keyboard5.add_line()
keyboard5.add_button(groups[82], color=VkKeyboardColor.PRIMARY)
keyboard5.add_button(groups[83], color=VkKeyboardColor.PRIMARY)
keyboard5.add_line()
keyboard5.add_button(groups[84], color=VkKeyboardColor.PRIMARY)
keyboard5.add_button(groups[85], color=VkKeyboardColor.PRIMARY)
keyboard5.add_line()
keyboard5.add_button(groups[86], color=VkKeyboardColor.PRIMARY)
keyboard5.add_button(groups[87], color=VkKeyboardColor.PRIMARY)
keyboard5.add_line()
keyboard5.add_button(groups[88], color=VkKeyboardColor.PRIMARY)
keyboard5.add_button(groups[89], color=VkKeyboardColor.PRIMARY)
keyboard5.add_line()
keyboard5.add_button('Назад', color=VkKeyboardColor.DEFAULT)
keyboard5.add_button('Вперёд', color=VkKeyboardColor.DEFAULT)

keyboard6 = VkKeyboard(one_time=True)
keyboard6.add_button(groups[90], color=VkKeyboardColor.PRIMARY)
keyboard6.add_button(groups[91], color=VkKeyboardColor.PRIMARY)
keyboard6.add_line()
keyboard6.add_button(groups[92], color=VkKeyboardColor.PRIMARY)
keyboard6.add_button(groups[93], color=VkKeyboardColor.PRIMARY)
keyboard6.add_line()
keyboard6.add_button(groups[94], color=VkKeyboardColor.PRIMARY)
keyboard6.add_button(groups[95], color=VkKeyboardColor.PRIMARY)
keyboard6.add_line()
keyboard6.add_button(groups[96], color=VkKeyboardColor.PRIMARY)
keyboard6.add_button(groups[97], color=VkKeyboardColor.PRIMARY)
keyboard6.add_line()
keyboard6.add_button(groups[98], color=VkKeyboardColor.PRIMARY)
keyboard6.add_button(groups[99], color=VkKeyboardColor.PRIMARY)
keyboard6.add_line()
keyboard6.add_button(groups[100], color=VkKeyboardColor.PRIMARY)
keyboard6.add_button(groups[101], color=VkKeyboardColor.PRIMARY)
keyboard6.add_line()
keyboard6.add_button(groups[102], color=VkKeyboardColor.PRIMARY)
keyboard6.add_button(groups[103], color=VkKeyboardColor.PRIMARY)
keyboard6.add_line()
keyboard6.add_button(groups[104], color=VkKeyboardColor.PRIMARY)
keyboard6.add_button(groups[105], color=VkKeyboardColor.PRIMARY)
keyboard6.add_line()
keyboard6.add_button(groups[106], color=VkKeyboardColor.PRIMARY)
keyboard6.add_button(groups[107], color=VkKeyboardColor.PRIMARY)
keyboard6.add_line()
keyboard6.add_button('Назад', color=VkKeyboardColor.DEFAULT)
keyboard6.add_button('Вперёд', color=VkKeyboardColor.DEFAULT)

keyboard7 = VkKeyboard(one_time=True)
keyboard7.add_button(groups[108], color=VkKeyboardColor.PRIMARY)
keyboard7.add_button(groups[109], color=VkKeyboardColor.PRIMARY)
keyboard7.add_line()
keyboard7.add_button(groups[110], color=VkKeyboardColor.PRIMARY)
keyboard7.add_button(groups[111], color=VkKeyboardColor.PRIMARY)
keyboard7.add_line()
keyboard7.add_button(groups[112], color=VkKeyboardColor.PRIMARY)
keyboard7.add_button(groups[113], color=VkKeyboardColor.PRIMARY)
keyboard7.add_line()
keyboard7.add_button(groups[114], color=VkKeyboardColor.PRIMARY)
keyboard7.add_button(groups[115], color=VkKeyboardColor.PRIMARY)
keyboard7.add_line()
keyboard7.add_button(groups[116], color=VkKeyboardColor.PRIMARY)
keyboard7.add_button(groups[117], color=VkKeyboardColor.PRIMARY)
keyboard7.add_line()
keyboard7.add_button(groups[118], color=VkKeyboardColor.PRIMARY)
keyboard7.add_button(groups[119], color=VkKeyboardColor.PRIMARY)
keyboard7.add_line()
keyboard7.add_button(groups[120], color=VkKeyboardColor.PRIMARY)
keyboard7.add_button(groups[121], color=VkKeyboardColor.PRIMARY)
keyboard7.add_line()
keyboard7.add_button(groups[122], color=VkKeyboardColor.PRIMARY)
keyboard7.add_button(groups[123], color=VkKeyboardColor.PRIMARY)
keyboard7.add_line()
keyboard7.add_button(groups[124], color=VkKeyboardColor.PRIMARY)
keyboard7.add_button(groups[125], color=VkKeyboardColor.PRIMARY)
keyboard7.add_line()
keyboard7.add_button('Назад', color=VkKeyboardColor.DEFAULT)
keyboard7.add_button('Вперёд', color=VkKeyboardColor.DEFAULT)

keyboard8 = VkKeyboard(one_time=True)
keyboard8.add_button(groups[126], color=VkKeyboardColor.PRIMARY)
keyboard8.add_button(groups[127], color=VkKeyboardColor.PRIMARY)
keyboard8.add_line()
keyboard8.add_button(groups[128], color=VkKeyboardColor.PRIMARY)
keyboard8.add_button(groups[129], color=VkKeyboardColor.PRIMARY)
keyboard8.add_line()
keyboard8.add_button(groups[130], color=VkKeyboardColor.PRIMARY)
keyboard8.add_button(groups[131], color=VkKeyboardColor.PRIMARY)
keyboard8.add_line()
keyboard8.add_button(groups[132], color=VkKeyboardColor.PRIMARY)
keyboard8.add_button(groups[133], color=VkKeyboardColor.PRIMARY)
keyboard8.add_line()
keyboard8.add_button(groups[134], color=VkKeyboardColor.PRIMARY)
keyboard8.add_button(groups[135], color=VkKeyboardColor.PRIMARY)
keyboard8.add_line()
keyboard8.add_button(groups[136], color=VkKeyboardColor.PRIMARY)
keyboard8.add_button(groups[137], color=VkKeyboardColor.PRIMARY)
keyboard8.add_line()
keyboard8.add_button(groups[138], color=VkKeyboardColor.PRIMARY)
keyboard8.add_button(groups[139], color=VkKeyboardColor.PRIMARY)
keyboard8.add_line()
keyboard8.add_button(groups[140], color=VkKeyboardColor.PRIMARY)
keyboard8.add_button(groups[141], color=VkKeyboardColor.PRIMARY)
keyboard8.add_line()
keyboard8.add_button(groups[142], color=VkKeyboardColor.PRIMARY)
keyboard8.add_button(groups[143], color=VkKeyboardColor.PRIMARY)
keyboard8.add_line()
keyboard8.add_button('Назад', color=VkKeyboardColor.DEFAULT)
keyboard8.add_button('Вперёд', color=VkKeyboardColor.DEFAULT)

keyboard9 = VkKeyboard(one_time=True)
keyboard9.add_button(groups[144], color=VkKeyboardColor.PRIMARY)
keyboard9.add_button(groups[145], color=VkKeyboardColor.PRIMARY)
keyboard9.add_line()
keyboard9.add_button(groups[146], color=VkKeyboardColor.PRIMARY)
keyboard9.add_button(groups[147], color=VkKeyboardColor.PRIMARY)
keyboard9.add_line()
keyboard9.add_button(groups[148], color=VkKeyboardColor.PRIMARY)
keyboard9.add_button(groups[149], color=VkKeyboardColor.PRIMARY)
keyboard9.add_button('Назад', color=VkKeyboardColor.DEFAULT)

t = 0
key = 1
keyboards = {
    1: keyboard1.get_keyboard(),
    2: keyboard2.get_keyboard(),
    3: keyboard3.get_keyboard(),
    4: keyboard4.get_keyboard(),
    5: keyboard5.get_keyboard(),
    6: keyboard6.get_keyboard(),
    7: keyboard7.get_keyboard(),
    8: keyboard8.get_keyboard(),
    9: keyboard9.get_keyboard(),
}

while True:
     try:
          for event in longpoll.listen():
               if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    user = str(event.user_id)
                    if event.text == '!расписание':
                         if event.from_user:
                              vk.messages.send(
                                  user_id=event.user_id,
                                  random_id=0,
                                  message='Введите группу',
                                  keyboard=keyboard1.get_keyboard()
                              )
                    elif event.text == groups[0]:
                             if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[0])
                    elif event.text == groups[1]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[1])
                    elif event.text == groups[2]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[2])
                    elif event.text == groups[3]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[3])
                    elif event.text == groups[4]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[4])
                    elif event.text == groups[5]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[5])
                    elif event.text == groups[6]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[6])
                    elif event.text == groups[7]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[7])
                    elif event.text == groups[8]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[8])
                    elif event.text == groups[9]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[9])
                    elif event.text == groups[10]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[10])
                    elif event.text == groups[11]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[11])
                    elif event.text == groups[12]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[12])
                    elif event.text == groups[13]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[13])
                    elif event.text == groups[14]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[14])
                    elif event.text == groups[15]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[15])
                    elif event.text == groups[16]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[16])
                    elif event.text == groups[17]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[17])
                    elif event.text == groups[18]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[18])
                    elif event.text == groups[19]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[19])
                    elif event.text == groups[20]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[20])
                    elif event.text == groups[21]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[21])
                    elif event.text == groups[22]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[22])
                    elif event.text == groups[23]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[23])
                    elif event.text == groups[24]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[24])
                    elif event.text == groups[25]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[25])
                    elif event.text == groups[26]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[26])
                    elif event.text == groups[27]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[27])
                    elif event.text == groups[28]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[28])
                    elif event.text == groups[29]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[29])
                    elif event.text == groups[30]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[30])
                    elif event.text == groups[31]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[31])
                    elif event.text == groups[32]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[32])
                    elif event.text == groups[33]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[33])
                    elif event.text == groups[34]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[34])
                    elif event.text == groups[35]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[35])
                    elif event.text == groups[36]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[36])
                    elif event.text == groups[37]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[37])
                    elif event.text == groups[38]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[38])
                    elif event.text == groups[39]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[39])
                    elif event.text == groups[40]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[40])
                    elif event.text == groups[41]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[41])
                    elif event.text == groups[42]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[42])
                    elif event.text == groups[43]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[43])
                    elif event.text == groups[44]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[44])
                    elif event.text == groups[45]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[45])
                    elif event.text == groups[46]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[46])
                    elif event.text == groups[47]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[47])
                    elif event.text == groups[48]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[48])
                    elif event.text == groups[49]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[49])
                    elif event.text == groups[50]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[50])
                    elif event.text == groups[51]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[51])
                    elif event.text == groups[52]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[52])
                    elif event.text == groups[53]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[53])
                    elif event.text == groups[54]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[54])
                    elif event.text == groups[55]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[55])
                    elif event.text == groups[56]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[56])
                    elif event.text == groups[57]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[57])
                    elif event.text == groups[58]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[58])
                    elif event.text == groups[59]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[59])
                    elif event.text == groups[60]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[60])
                    elif event.text == groups[61]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[61])
                    elif event.text == groups[62]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[62])
                    elif event.text == groups[63]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[63])
                    elif event.text == groups[64]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[64])
                    elif event.text == groups[65]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[65])
                    elif event.text == groups[66]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[66])
                    elif event.text == groups[67]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[67])
                    elif event.text == groups[68]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[68])
                    elif event.text == groups[69]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[69])
                    elif event.text == groups[70]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[70])
                    elif event.text == groups[71]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[71])
                    elif event.text == groups[72]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[72])
                    elif event.text == groups[73]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[73])
                    elif event.text == groups[74]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[74])
                    elif event.text == groups[75]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[75])
                    elif event.text == groups[76]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[76])
                    elif event.text == groups[77]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[77])
                    elif event.text == groups[78]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[78])
                    elif event.text == groups[79]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[79])
                    elif event.text == groups[80]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[80])
                    elif event.text == groups[81]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[81])
                    elif event.text == groups[82]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[82])
                    elif event.text == groups[83]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[83])
                    elif event.text == groups[84]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[84])
                    elif event.text == groups[85]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[85])
                    elif event.text == groups[86]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[86])
                    elif event.text == groups[87]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[87])
                    elif event.text == groups[88]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[88])
                    elif event.text == groups[89]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[89])
                    elif event.text == groups[90]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[90])
                    elif event.text == groups[91]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[91])
                    elif event.text == groups[92]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[92])
                    elif event.text == groups[93]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[93])
                    elif event.text == groups[94]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[94])
                    elif event.text == groups[95]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[95])
                    elif event.text == groups[96]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[96])
                    elif event.text == groups[97]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[97])
                    elif event.text == groups[98]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[98])
                    elif event.text == groups[99]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[99])
                    elif event.text == groups[100]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[100])
                    elif event.text == groups[101]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[101])
                    elif event.text == groups[102]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[102])
                    elif event.text == groups[103]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[103])
                    elif event.text == groups[104]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[104])
                    elif event.text == groups[105]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[105])
                    elif event.text == groups[106]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[106])
                    elif event.text == groups[107]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[107])
                    elif event.text == groups[108]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[108])
                    elif event.text == groups[109]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[109])
                    elif event.text == groups[110]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[110])
                    elif event.text == groups[111]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[111])
                    elif event.text == groups[112]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[112])
                    elif event.text == groups[113]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[113])
                    elif event.text == groups[114]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[114])
                    elif event.text == groups[115]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[115])
                    elif event.text == groups[116]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[116])
                    elif event.text == groups[117]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[117])
                    elif event.text == groups[118]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[118])
                    elif event.text == groups[119]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[119])
                    elif event.text == groups[120]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[120])
                    elif event.text == groups[121]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[121])
                    elif event.text == groups[122]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[122])
                    elif event.text == groups[123]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[123])
                    elif event.text == groups[124]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[124])
                    elif event.text == groups[125]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[125])
                    elif event.text == groups[126]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[126])
                    elif event.text == groups[127]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[127])
                    elif event.text == groups[128]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[128])
                    elif event.text == groups[129]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[129])
                    elif event.text == groups[130]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[130])
                    elif event.text == groups[131]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[131])
                    elif event.text == groups[132]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[132])
                    elif event.text == groups[133]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[133])
                    elif event.text == groups[134]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[134])
                    elif event.text == groups[135]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[135])
                    elif event.text == groups[136]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[136])
                    elif event.text == groups[137]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[137])
                    elif event.text == groups[138]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[138])
                    elif event.text == groups[139]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[139])
                    elif event.text == groups[140]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[140])
                    elif event.text == groups[141]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[141])
                    elif event.text == groups[142]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[142])
                    elif event.text == groups[143]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[143])
                    elif event.text == groups[144]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[144])
                    elif event.text == groups[145]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[145])
                    elif event.text == groups[146]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[146])
                    elif event.text == groups[147]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[147])
                    elif event.text == groups[148]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[148])
                    elif event.text == groups[149]:
                            if event.from_user:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Выберите день',
                                            keyboard=data.get_keyboard()
                                    )
                                    with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'w') as f:
                                            f.write(groups[149])
                    elif event.text == button_days[1]:
                      try:
                          dat = button_days[1]
                          for ri in range(0, 149):
                               with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'r') as f:
                                     if f.readline() == groups[ri]:
                                             temp = groups[ri]
                                             break
                      except FileNotFoundError:
                               vk.messages.send(
                                       user_id=event.user_id,
                                       random_id=0,
                                       message='Для начала введите группу',
                                       keyboard=keyboard1.get_keyboard()
                               )
                               i = 1
                      if event.from_user:
                          try:
                              with open("//home//ubuntu//bot1//bo1//Rasp//" + dat + "_" + temp + ".txt", "r") as f:
                                  m = f.readlines()
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message=m,
                                   keyboard=data.get_keyboard()
                              )
                              m = ''
                          except FileNotFoundError:
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message='Расписание не доступно',
                              )
                      temp = ''
                    elif event.text == button_days[2]:
                      try:
                                    dat = button_days[2]
                                    for ri in range(0, 149):
                                        with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'r') as f:
                                               if f.readline() == groups[ri]:
                                                       temp = groups[ri]
                                                       break
                      except FileNotFoundError:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Для начала введите группу',
                                            keyboard=keyboard1.get_keyboard()
                                    )
                                    i = 1
                      if event.from_user:
                          try:
                              with open("//home//ubuntu//bot1//bo1//Rasp//" + dat + "_" + temp + ".txt", "r") as f:
                                  m = f.readlines()
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message=m,
                                   keyboard=data.get_keyboard()
                              )
                              m = ''
                          except FileNotFoundError:
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message='Расписание не доступно',
                              )
                      temp = ''
                    elif event.text == button_days[3]:
                      try:
                                    dat = button_days[3]
                                    for ri in range(0, 149):
                                        with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'r') as f:
                                               if f.readline() == groups[ri]:
                                                       temp = groups[ri]
                                                       break
                      except FileNotFoundError:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Для начала введите группу',
                                            keyboard=keyboard1.get_keyboard()
                                    )
                                    i = 1
                      if event.from_user:
                          try:
                              with open("//home//ubuntu//bot1//bo1//Rasp//" + dat + "_" + temp + ".txt", "r") as f:
                                  m = f.readlines()
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message=m,
                                   keyboard=data.get_keyboard()
                              )
                              m = ''
                          except FileNotFoundError:
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message='Расписание не доступно',
                              )
                      temp = ''
                    elif event.text == button_days[4]:
                      try:
                                    dat = button_days[4]
                                    for ri in range(0, 149):
                                        with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'r') as f:
                                               if f.readline() == groups[ri]:
                                                       temp = groups[ri]
                                                       break
                      except FileNotFoundError:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Для начала введите группу',
                                            keyboard=keyboard1.get_keyboard()
                                    )
                                    i = 1
                      if event.from_user:
                          try:
                              with open("//home//ubuntu//bot1//bo1//Rasp//" + dat + "_" + temp + ".txt", "r") as f:
                                  m = f.readlines()
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message=m,
                                   keyboard=data.get_keyboard()
                              )
                              m = ''
                          except FileNotFoundError:
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message='Расписание не доступно',
                              )
                      temp = ''
                    elif event.text == button_days[5]:
                      try:
                                    dat = button_days[5]
                                    for ri in range(0, 149):
                                        with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'r') as f:
                                               if f.readline() == groups[ri]:
                                                       temp = groups[ri]
                                                       break
                      except FileNotFoundError:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Для начала введите группу',
                                            keyboard=keyboard1.get_keyboard()
                                    )
                                    i = 1
                      if event.from_user:
                          try:
                              with open("//home//ubuntu//bot1//bo1//Rasp//" + dat + "_" + temp + ".txt", "r") as f:
                                  m = f.readlines()
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message=m,
                                   keyboard=data.get_keyboard()
                              )
                              m = ''
                          except FileNotFoundError:
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message='Расписание не доступно',
                              )
                      temp = ''
                    elif event.text == button_days[6]:
                      try:
                                    dat = button_days[6]
                                    for ri in range(0, 149):
                                        with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'r') as f:
                                               if f.readline() == groups[ri]:
                                                       temp = groups[ri]
                                                       break
                      except FileNotFoundError:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Для начала введите группу',
                                            keyboard=keyboard1.get_keyboard()
                                    )
                                    i = 1
                      if event.from_user:
                          try:
                              with open("//home//ubuntu//bot1//bo1//Rasp//" + dat + "_" + temp + ".txt", "r") as f:
                                  m = f.readlines()
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message=m,
                                   keyboard=data.get_keyboard()
                              )
                              m = ''
                          except FileNotFoundError:
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message='Расписание не доступно',
                              )
                      temp = ''
                    elif event.text == button_days[7]:
                      try:
                                    dat = button_days[7]
                                    for ri in range(0, 149):
                                        with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'r') as f:
                                               if f.readline() == groups[ri]:
                                                       temp = groups[ri]
                                                       break
                      except FileNotFoundError:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Для начала введите группу',
                                            keyboard=keyboard1.get_keyboard()
                                    )
                                    i = 1
                      if event.from_user:
                         try:
                              with open("//home//ubuntu//bot1//bo1//Rasp//" + dat + "_" + temp + ".txt", "r") as f:
                                  m = f.readlines()
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message=m,
                                   keyboard=data.get_keyboard()
                              )
                              m = ''
                         except FileNotFoundError:
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message='Расписание не доступно',
                              )
                      temp = ''
                    elif event.text == button_days[8]:
                      try:
                                    dat = button_days[8]
                                    for ri in range(0, 149):
                                        with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'r') as f:
                                               if f.readline() == groups[ri]:
                                                       temp = groups[ri]
                                                       break
                      except FileNotFoundError:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Для начала введите группу',
                                            keyboard=keyboard1.get_keyboard()
                                    )
                                    i = 1
                      if event.from_user:
                          try:
                              with open("//home//ubuntu//bot1//bo1//Rasp//" + dat + "_" + temp + ".txt", "r") as f:
                                  m = f.readlines()
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message=m,
                                   keyboard=data.get_keyboard()
                              )
                              m = ''
                          except FileNotFoundError:
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message='Расписание не доступно',
                              )
                      temp = ''
                    elif event.text == button_days[9]:
                      try:
                                    dat = button_days[9]
                                    for ri in range(0, 149):
                                        with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'r') as f:
                                               if f.readline() == groups[ri]:
                                                       temp = groups[ri]
                                                       break
                      except FileNotFoundError:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Для начала введите группу',
                                            keyboard=keyboard1.get_keyboard()
                                    )
                                    i = 1
                      if event.from_user:
                          try:
                              with open("//home//ubuntu//bot1//bo1//Rasp//" + dat + "_" + temp + ".txt", "r") as f:
                                  m = f.readlines()
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message=m,
                                   keyboard=data.get_keyboard()
                              )
                              m = ''
                          except FileNotFoundError:
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message='Расписание не доступно',
                              )
                      temp = ''
                    elif event.text == button_days[10]:
                      try:
                                    dat = button_days[10]
                                    for ri in range(0, 149):
                                        with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'r') as f:
                                               if f.readline() == groups[ri]:
                                                       temp = groups[ri]
                                                       break
                      except FileNotFoundError:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Для начала введите группу',
                                            keyboard=keyboard1.get_keyboard()
                                    )
                                    i = 1
                      if event.from_user:
                          try:
                              with open("//home//ubuntu//bot1//bo1//Rasp//" + dat + "_" + temp + ".txt", "r") as f:
                                  m = f.readlines()
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message=m,
                                   keyboard=data.get_keyboard()
                              )
                              m = ''
                          except FileNotFoundError:
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message='Расписание не доступно',
                              )
                      temp = ''
                    elif event.text == button_days[11]:
                      try:
                                    dat = button_days[11]
                                    for ri in range(0, 149):
                                        with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'r') as f:
                                               if f.readline() == groups[ri]:
                                                       temp = groups[ri]
                                                       break
                      except FileNotFoundError:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Для начала введите группу',
                                            keyboard=keyboard1.get_keyboard()
                                    )
                                    i = 1
                      if event.from_user:
                          try:
                              with open("//home//ubuntu//bot1//bo1//Rasp//" + dat + "_" + temp + ".txt", "r") as f:
                                  m = f.readlines()
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message=m,
                                   keyboard=data.get_keyboard()
                              )
                              m = ''
                          except FileNotFoundError:
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message='Расписание не доступно',
                              )
                      temp = ''
                    elif event.text == button_days[12]:
                      try:
                                    dat = button_days[12]
                                    for ri in range(0, 149):
                                        with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'r') as f:
                                               if f.readline() == groups[ri]:
                                                       temp = groups[ri]
                                                       break
                      except FileNotFoundError:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Для начала введите группу',
                                            keyboard=keyboard1.get_keyboard()
                                    )
                                    i = 1
                      if event.from_user:
                          try:
                              with open("//home//ubuntu//bot1//bo1//Rasp//" + dat + "_" + temp + ".txt", "r") as f:
                                  m = f.readlines()
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message=m,
                                   keyboard=data.get_keyboard()
                              )
                              m = ''
                          except FileNotFoundError:
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message='Расписание не доступно',
                              )
                      temp = ''
                    elif event.text == button_days[13]:
                      try:
                                    dat = button_days[13]
                                    for ri in range(0, 149):
                                        with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'r') as f:
                                               if f.readline() == groups[ri]:
                                                       temp = groups[ri]
                                                       break
                      except FileNotFoundError:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Для начала введите группу',
                                            keyboard=keyboard1.get_keyboard()
                                    )
                                    i = 1
                      if event.from_user:
                          try:
                              with open("//home//ubuntu//bot1//bo1//Rasp//" + dat + "_" + temp + ".txt", "r") as f:
                                  m = f.readlines()
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message=m,
                                   keyboard=data.get_keyboard()
                              )
                              m = ''
                          except FileNotFoundError:
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message='Расписание не доступно',
                              )
                      temp = ''
                    elif event.text == button_days[14]:
                      try:
                                    dat = button_days[14]
                                    for ri in range(0, 149):
                                        with open('//home//ubuntu//bot1//bo1//jsn//groups//' + user + '.txt', 'r') as f:
                                               if f.readline() == groups[ri]:
                                                       temp = groups[ri]
                                                       break
                      except FileNotFoundError:
                                    vk.messages.send(
                                            user_id=event.user_id,
                                            random_id=0,
                                            message='Для начала введите группу',
                                            keyboard=keyboard1.get_keyboard()
                                    )
                                    i = 1
                      if event.from_user:
                          try:
                              with open("//home//ubuntu//bot1//bo1//Rasp//" + dat + "_" + temp + ".txt", "r") as f:
                                  m = f.readlines()
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message=m,
                                   keyboard=data.get_keyboard()
                              )
                              m = ''
                          except FileNotFoundError:
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message='Расписание не доступно',
                              )
                      temp = ''
                    elif event.text == 'Отмена':
                         if event.from_user:
                              vk.messages.send(
                                   user_id=event.user_id,
                                   random_id=0,
                                   message='Введите группу',
                                   keyboard=keyboard1.get_keyboard()
                              )
     except:
          error_1 = 1