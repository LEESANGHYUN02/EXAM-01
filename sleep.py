for i in range(int(input())):
    n = int(input())
    s = set() 
    cnt = 1
    while True:
        for k in list(str(n)):
            s.add(k)
        if len(s) == 10: 
            break
        n //= cnt 
        cnt += 1 
        n *= cnt 
    
    print("#{} {}".format(i+1, n))
#중복제거 집함 선언
    ##집합 s의 길이가 0~9까지의 길이,총 10이 되면 break
    #n이 1295를 값을 유지하기 위해 1295/1,2590/2 ``` 등등
    #cnt 값 + 1
    #마지막 숫자 출력