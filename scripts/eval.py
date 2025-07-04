from utils.data_preprocess import text_preprocess
from gensim import models
import time
from tensorboardX import SummaryWriter


def main():
    eval_synonym_data = "../data/eval_synonym_data.txt"
    eval_antonym_data = "../data/eval_antonym_data.txt"

    writer = SummaryWriter(logdir="runs/fasttext_eval")

    data_pairs = text_preprocess(eval_synonym_data)

    print("모델을 서버에 업로드 중입니다...")
    start_time = time.time()

    ko_model = models.fasttext.load_facebook_model('cc.ko.300.bin')

    end_time = time.time()
    elapsed = end_time - start_time

    print("모델 업로드 완료!")
    print(f"업로드에 소요된 시간: {elapsed:.3f}초")
    print("=" * 20)
    data_len = len(data_pairs)
    print("총 " + str(data_len) + "개의 데이터로 유의어 평가를 진행합니다.")

    score = 0
    for i, j in enumerate(data_pairs):
        similarity = ko_model.wv.similarity(j[0], j[1])
        print(f"{i}: {j[0]}과 {j[1]}의 코사인 유사도: {similarity:.4f}")
        writer.add_scalar("Similarity/Synonym", similarity, i)
        score += similarity
    synonym_score = score / data_len
    writer.add_scalar("Average_Similarity/Synonym", synonym_score, 0)
    data_pairs.clear()
    print("=" * 20)
    print("유의어 테스트 종료. 반의어 테스트 시작")

    data_pairs = text_preprocess(eval_antonym_data)
    data_len = len(data_pairs)
    print("총 " + str(data_len) + "개의 데이터로 반의어 평가를 진행합니다.")

    score = 0
    for i, j in enumerate(data_pairs):
        similarity = ko_model.wv.similarity(j[0], j[1])
        print(f"{i}: {j[0]}과 {j[1]}의 코사인 유사도: {similarity:.4f}")
        writer.add_scalar("Similarity/Antonym", similarity, i)
        score += similarity
    antonym_score = score / data_len

    print("=" * 20)
    print(f"유의어의 평균 유사도 : {synonym_score:.4f}")
    print(f"반의어의 평균 유사도 : {antonym_score:.4f}")

    writer.close()


if __name__ == "__main__":
    main()
