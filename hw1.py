question = ['\"이화여대 멋사 대표님\"', '\"멋사 창립자\"', '\"파이썬 세션 튜터\"', '\"야옹\"']      #문제를 저장한 리스트
ans = { 0: '현숙', 1: '두희', 2:'세은', 3:'마루'}       #정답 딕셔너리
 
for i in range(4):
    print('다음은 누구에 대한 설명일까요?\n' + str(question[i])) 
    x = input('1.현숙 2.세은 3.두희 4.마루\n')

    if( x == ans[i] ):      #사용자의 입력값과 정답 딕셔너리의 키를 비교
        print('정답입니다!\n\n')
    else:
        print('오답입니다!\n\n')
