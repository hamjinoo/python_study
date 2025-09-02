# 파이썬 RAG 학습 메모리

## 학습 목표

**파이썬 기초 → 파일·웹 → 임베딩·검색(FAISS/pgvector) → 간단 생성 → 평가(ragas)·보안(OWASP) → FastAPI 서비스** 순서로, 10주 안에 "출처 달린 RAG 미니앱"까지 완성하는 것이 목표입니다.

## 현재 단계

- **0단계**: 파이썬 설치 및 첫 실행 (오늘 30분)
- **목표**: `input()` 받아서 "이름-인사" 출력 프로그램 작성

## 10주 커리큘럼 요약

### Week 1 — 파이썬 기초(문법의 뼈대)

- 변수·숫자·문자열·리스트/딕셔너리·조건/반복·함수·모듈 기초
- **과제**: 텍스트 파일에서 단어 수 세고, 상위 10개 단어 출력 스크립트

### Week 2 — 파일·에러·테스트·타입

- 파일 입출력(JSON), 예외 처리, 로깅 기초
- 타입힌트·`dataclass`와 `pydantic`으로 입력 검증
- `pytest`로 첫 유닛 테스트
- **과제**: "할 일 목록" CLI (추가/목록/저장 JSON)

### Week 3 — 웹 기초 & 비동기 맛보기

- `httpx`로 HTTP GET/POST, `asyncio` 기초
- **과제**: 뉴스/위키 API에서 JSON 받아 요약 텍스트 출력

### Week 4 — 텍스트 전처리 & 청킹

- 문단/문장 청킹, 오버랩(stride), 메타데이터 보존
- **과제**: 폴더 안 문서들을 `chunks.jsonl`로 저장

### Week 5 — 임베딩 & FAISS로 벡터 검색(로컬)

- `sentence-transformers`로 임베딩 → FAISS 인덱스 구축/쿼리
- **과제**: "내 문서 검색기" CLI — 질문 입력→상위 k개 문서 조각 반환

### Week 6 — pgvector(PostgreSQL)로 DB 기반 검색

- Postgres + pgvector 설치, HNSW/IVFFlat 인덱스 비교
- **과제**: `faiss` vs `pgvector` 검색 지연·리콜 간단 비교표

### Week 7 — 재순위(rerank)로 정밀도 올리기

- 후보 top-k를 Cross-Encoder로 재점수화하여 상위 N 재선택
- **과제**: 재순위 전/후 정답률 비교 로그

### Week 8 — "출처 달린 답변" 생성(라이트)

- LLM 호출 구조화 출력(JSON), 프롬프트에 각주 필드 강제
- **과제**: 상위 문서조각을 주입해 [1][2] 각주 포함 답변 생성

### Week 9 — 평가(ragas·HELM 관점) & 보안(OWASP)

- ragas로 answer relevancy / faithfulness 측정
- OWASP LLM Top 10 체크리스트로 프롬프트 인젝션·민감정보 노출 방어
- **과제**: 공격 프롬프트 5개에 대해 차단/완화 테스트 통과

### Week 10 — FastAPI로 서비스화

- `/ask` POST: {query} → (검색→재순위→생성→JSON 응답)
- **최종 과제**: 단일 페이지 데모(파일 업로드→질문→각주·하이라이트)

## 학습 루틴

- **45분** 강의/문서 읽고 따라 치기 → **30분** 실습(작동하는 코드 1개) → **15분** 기록(실패/깨달음 3줄)

## 핵심 코드 조각들

### ① 입력 검증(Python 기초+Pydantic)

```python
from pydantic import BaseModel, Field

class Query(BaseModel):
    q: str = Field(min_length=3)
```

### ② FAISS top-k 검색(임베딩은 sbert)

```python
import faiss, numpy as np
# dim = 임베딩 차원 (예: 384 또는 768)
index = faiss.IndexFlatIP(dim)
index.add(np.array(doc_embs, dtype="float32"))
D, I = index.search(np.array([q_emb], dtype="float32"), k=5)
```

### ③ FastAPI 서비스 뼈대

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True}
```

## 주차별 산출물 체크리스트

- [ ] W1-2: 기초 문제 모음 + `pytest` 5개
- [ ] W3: API 호출 유틸 + 타임아웃/재시도
- [ ] W4: `chunks.jsonl`(텍스트+출처+오프셋)
- [ ] W5: FAISS 검색기(질문→top-k 반환)
- [ ] W6: pgvector 검색 API + 리콜/지연 비교표
- [ ] W7: 재순위 모듈 + 정밀도 개선(+5pt 목표)
- [ ] W8: 구조화 JSON 응답(각주 필드 필수)
- [ ] W9: ragas 리포트 + OWASP 테스트 케이스 10개
- [ ] W10: FastAPI `/ask` 배포(로컬 OK)

## 참고 자료

- Python 공식 튜토리얼/문서
- FastAPI 문서
- FAISS 문서/깃허브
- pgvector 깃허브
- Sentence-Transformers 문서/깃허브
- HELM 논문(평가 프레임)
- ragas 문서(평가지표)
- OWASP LLM Top 10(최신)
- OpenAI Structured Outputs(스키마 강제)

## 현재 진행 상황

- **시작일**: 오늘
- **현재 단계**: 0단계 (파이썬 설치 및 첫 실행)
- **다음 목표**: `input()` 받아서 "이름-인사" 출력 프로그램 작성
