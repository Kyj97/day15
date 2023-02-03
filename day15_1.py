pokemon = [['피카츄', 50], ['라이츄', 60], ['파이리', 70],
           ['꼬부기', 60], ['이상해', 40], ['버터플', 10], ['야도란', 35], ['피죤투', 25]]

pokemon.sort(key=lambda x:x[1])
print(pokemon)

def insert_data(po, fr):

     for n in range(0, len(pokemon)-1):
        if po <= pokemon[n][1]:
            pos = n
            print(pos)
            break
        elif po > pokemon[n][1]:
            pos = len(pokemon)



     pokemon.append(None)
     Len = len(pokemon)

     for i in range(Len - 1, pos, -1):
        pokemon[i] = pokemon[i - 1]
        pokemon[i - 1] = None
     print(pos)
     pokemon[pos] = [fr, po]



if __name__ == "__main__":

    while True:
        name = input("포켓몬 이름을 입력하세요 ")
        while True:
            try:
                pow = int(input("포켓몬의 전투력 입력"))
                if pow < 0:
                    print("전투력은 양의 정수로 입력해 주세요.")
                    continue
                else:
                    break
            except:  # 예외가 발생했을 때 실행됨
                print("전투력은 양의 정수로 입력해 주세요.")


        insert_data(pow, name)
        print(pokemon)
