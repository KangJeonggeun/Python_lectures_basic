height = 200

if height > 190 :
    print('롤러코스터를 못탑니다. 키가 너무 큽니다.')
elif height <= 190 and height > 150:
    print('롤러코스터를 탈수 있습니다.')
elif height > 140 and height <= 150:
    print('어린아이 좌석으로 안내합니다.')
else:
    print('롤러코스터를 못탑니다. 키가 너무 작습니다.')

