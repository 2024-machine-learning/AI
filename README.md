## 🎵 Pen to Tone - 텍스트 분위기에 따른 음악 추천 서비스 

24-2 기계학습 Term Project Pen to Tone의 AI 레포입니다.

---

### 📂 폴더 구조

1. **핵심 노트북 및 스크립트**
   - `cover.ipynb`: 주어진 쿼리의 RGB 값을 예측하는 회귀 모델 구현
   - `dl_sbert.ipynb`: SBERT 임베딩을 활용한 딥러닝 기반 색상 예측 모델
   - `lyrics.ipynb`: 가사 데이터를 활용한 노래 추천 모델 구현
   - `preprocessing.ipynb`: 가사 크롤링 및 앨범 색상 추출 등의 전처리 작업 수행
   - `lyrics.py`: 노래 추천 기능을 Python 스크립트로 분리

2. **데이터 및 모델**
   - `merged.csv`: 전처리된 노래 메타데이터 및 가사, 앨범 커버 RGB 데이터 파일
   - `sbert_embeddings.pt`: SBERT로 생성된 가사 임베딩 데이터
   - `dl_sbert.pth`: SBERT 기반 딥러닝 모델의 학습 완료된 가중치 파일

3. **기타**
   - `.gitignore`: Git에서 제외할 파일/디렉토리 설정
   - `README.md`: 현재 파일 (설명 문서)

---

### 🛠️ 실행 방법

1. **전처리**
   - `preprocessing.ipynb`를 실행하여 데이터를 정리 및 전처리합니다.
   - 결과를 `merged.csv` 파일로 저장합니다.

2. **모델 학습**
   - 가사 기반 추천:

   - 색상 분석:
     - `cover.ipynb`를 실행하여 주어진 쿼리의 RGB 값을 예측하는 회귀 모델을 학습합니다. (Pycaret 기반)
     - `dl_sbert.ipynb`를 실행하여 SBERT로 임베딩된 벡터에 대해 RGB 값을 예측하는 회귀 모델을 딥러닝으로 학습합니다.
3. **추천 모델 실행**
   - `lyrics.py`를 사용하여 애플리케이션에 통합합니다.
