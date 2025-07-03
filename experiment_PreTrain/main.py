from gensim import models
import time

print("모델을 서버에 업로드 중입니다...")
start_time = time.time()

ko_model = models.fasttext.load_facebook_model('cc.ko.300.bin')

end_time = time.time()
elapsed = end_time - start_time

print("모델 업로드 완료!")
print(f"업로드에 소요된 시간: {elapsed:.3f}초")

print("=" * 20)
while True:
    word1 = input("1번째 단어를 입력해주세요: ")
    word2 = input("2번째 단어를 입력해주세요: ")

    if word1 in ko_model.wv and word2 in ko_model.wv:
        similarity = ko_model.wv.similarity(word1, word2)
        print(f"'{word1}' 와 '{word2}' 의 코사인 유사도: {similarity:.4f}")
    else:
        print(f"둘 중 하나 이상의 단어가 vocab에 없어 유사도를 계산할 수 없습니다.")
    print("-" * 10)

    if word1 in ko_model.wv:
        print(f"'{word1}' 과 유사한 단어들 입니다.")
        for w, sim in ko_model.wv.similar_by_word(word1, topn=10):
            print(f'{w}: {sim}')
    else:
        print(f"'{word1}' 단어가 vocab에 없습니다.")
    print("-" * 10)

    if word2 in ko_model.wv:
        print(f"'{word2}' 과 유사한 단어들 입니다.")
        for w, sim in ko_model.wv.similar_by_word(word2, topn=10):
            print(f'{w}: {sim}')
    else:
        print(f"'{word2}' 단어가 vocab에 없습니다.")
    print("=" * 20)
