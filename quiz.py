question1 = "1. 우리나라의 수도는 서울입니까? (O/X) "
question2 = "2. 대한민국의 국기 색상은 빨강, 흰색, 청색입니다. (O/X) "
question3 = "3. 지구에서 가장 큰 대륙은 아시아입니다. (O/X) "
question4 = "4. 백두산은 한반도의 북부에 위치한 산맥입니다. (O/X) "
question5 = "5. 아프리카 대륙에서는 펭귄이 서식합니다. (O/X) "
correct_msg = "정답입니다!"
wrong_msg = "오답입니다."

def ox_quiz():
    score = 0
    
    answer1 = input(question1).lower()
    if answer1 == 'o':
        print(correct_msg)
        score += 1
    else:
        print(wrong_msg)

    answer2 = input(question2).lower()
    if answer2 == 'o':
        print(correct_msg)
        score += 1
    else:
        print(wrong_msg)

    answer3 = input(question3).lower()
    if answer3 == 'x':
        print(correct_msg)
        score += 1
    else:
        print(wrong_msg)

    answer4 = input(question4).lower()
    if answer4 == 'o':
        print(correct_msg)
        score += 1
    else:
        print(wrong_msg)

    answer5 = input(question5).lower()
    if answer5 == 'x':
        print(correct_msg)
        score += 1
    else:
        print(wrong_msg)

    print(f"최종 점수는 {score}점입니다.")

if __name__ == "__main__":
    ox_quiz()

    ### GUI 프로그램으로 만들어보기. _main_ 사용해 보기
    