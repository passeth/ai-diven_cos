# Obsidian 무료 CMS 템플릿

Obsidian → GitHub → Vercel을 연결하는 **완전 무료 CMS**. 마크다운으로 작성하고, 자동으로 배포하세요.

> **[라이브 데모](https://ai-diven-cos.vercel.app)** | **[샘플 아티클](https://ai-diven-cos.vercel.app/articles/niacinamide-complete-guide.html)**

---

## 🚀 시작하기 (템플릿 사용법)

### 1단계: 저장소 생성

위의 녹색 **"Use this template"** 버튼을 클릭하고 **"Create a new repository"**를 선택하세요.

- 저장소 이름 입력 (예: `my-blog`)
- 공개/비공개 선택
- **"Create repository"** 클릭

### 2단계: 새 저장소 Clone

```bash
git clone https://github.com/사용자명/저장소명.git
cd 저장소명
```

### 3단계: 설치 및 실행

```bash
# 의존성 설치
npm install

# 대화형 설정 (선택)
python setup.py

# 개발 서버 시작
npm run dev
```

### 4단계: Vercel 배포

1. [vercel.com/new](https://vercel.com/new) 접속
2. GitHub 저장소 연결
3. 배포 (자동 설정됨)

**완료!** 이제 push할 때마다 자동으로 배포됩니다.

---

## 이 템플릿으로 만들 수 있는 것

블로그, 저널, 문서 사이트 등 콘텐츠 중심 웹사이트를 만들 수 있습니다:

- **Obsidian**에서 콘텐츠 작성 (오프라인, 마크다운)
- **GitHub**에 원클릭 Push
- **Vercel**에 자동 배포 (무료 호스팅, SSL, CDN)
- **월 $0** 인프라 비용

## 💡 무료 CMS 아키텍처

월 $0으로 운영되는 현대적인 **서버리스 CMS**입니다.

```
┌─────────────────────────────────────────────────────────────┐
│                      워크플로우                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Obsidian            Claude Code           Vercel           │
│   ┌─────────┐         ┌───────────┐        ┌─────────┐      │
│   │  작성   │         │   빌드    │        │  배포   │      │
│   │  편집   │ ──────▶ │   자동화  │ ─────▶ │  호스팅 │      │
│   │  이미지 │ GitHub  │   개선    │  자동  │  SSL    │      │
│   └─────────┘  동기화 └───────────┘        └─────────┘      │
│       ▲                                                      │
│       │ Obsidian 플러그인                                    │
│       ├─ Obsidian Git (자동 백업 & 동기화)                   │
│       ├─ Paste Image Rename (자동 이미지 이름 지정)          │
│       ├─ Templater (아티클 템플릿)                           │
│       └─ Linter (YAML 포맷팅)                                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 왜 이 스택인가?

| 기능 | 전통적인 CMS | 이 시스템 |
|------|-------------|----------|
| 호스팅 비용 | $10~50/월 | **무료** (Vercel) |
| 데이터베이스 | MySQL/PostgreSQL | **Git** (무료, 버전 관리) |
| 백업 | 수동 설정 | **자동** (Git 히스토리) |
| 에디터 | 웹 기반만 | **Obsidian** (오프라인 가능) |
| 버전 관리 | 제한적이거나 없음 | **전체 Git 히스토리** |
| 배포 | 수동/복잡함 | **Push = 자동 배포** |
| AI 통합 | 없음 | **Claude Code 내장** |
| 관리자 패널 | 별도 시스템 | **Obsidian이 곧 관리자** |

### 주요 장점

- **Obsidian이 관리자 패널**: 로컬에서 마크다운으로 콘텐츠 작성, 편집, 관리
- **GitHub이 데이터베이스**: 무료 저장소, 자동 버전 관리, 협업 가능
- **Vercel이 호스트**: 자동 SSL, CDN, 설정 없는 배포
- **Claude Code가 개발자**: 기능 구축, 버그 수정, 콘텐츠 생성

## 🧪 개요

화장품 혁신 저널을 위한 정적 사이트 생성기입니다:

- **7개의 AI 저널리스트 페르소나** (각각 고유한 문체)
- **5개 콘텐츠 카테고리**: 개발, 제품, 성분, 트렌드, 팁
- **관리자 대시보드** (콘텐츠 관리용)
- **Obsidian 통합** (Claude Code 스킬 포함)
- **SEO 최적화** 정적 HTML 출력

## 🛠️ 필수 조건

- Python 3.8+
- Node.js 18+
- Git
- [Obsidian](https://obsidian.md/)

## ⚙️ 설정

`setup.py` 스크립트로 설정:
- 사이트 이름 & 설명
- 콘텐츠 카테고리
- Obsidian 플러그인 설정

수동 설정은 **[SETUP.md](SETUP.md)** 참조.

## 📁 프로젝트 구조

```
ai-diven_cos/                   # 루트 = Obsidian Vault
├── content/                    # 마크다운 아티클
│   ├── development/            # AI 화장품 R&D
│   ├── products/               # 제품 리뷰
│   ├── ingredients/            # 성분 과학
│   ├── trends/                 # 업계 트렌드
│   ├── tips/                   # 뷰티 팁
│   ├── videos/                 # YouTube 임베드 + 노트
│   └── _assets/images/         # 아티클 이미지
├── site/
│   ├── public/                 # 정적 자산 (CSS, JS)
│   ├── src/                    # 빌드 스크립트 & 템플릿
│   └── build/                  # 생성된 결과물 (배포용)
├── .obsidian/                  # Obsidian 설정 & 플러그인
├── .claude/skills/             # Claude Code 스킬
├── docs/                       # 문서
├── Home.md                     # Obsidian 홈페이지
└── CLAUDE.md                   # Claude용 프로젝트 가이드라인
```

## ✍️ 콘텐츠 작성

### 1. 템플릿 사용

템플릿은 `.obsidian/templates/`에 위치:

- `template-article.md` - 표준 아티클
- `template-product-review.md` - 제품 리뷰
- `template-research.md` - 과학 아티클
- `template-tutorial.md` - 사용법 가이드

### 2. YAML Frontmatter

모든 아티클에 필수:

```yaml
---
title: "아티클 제목"
slug: "url-친화적-슬러그"
journalist: "dr-sarah-kim"
category: "ingredients"
tags: ["태그1", "태그2"]
date: "2025-01-15"
excerpt: "간단한 요약"
status: "published"
featured: false
homepage_priority: 5
reading_time: "5분"
---
```

전체 스키마는 [docs/YAML_SCHEMA.md](docs/YAML_SCHEMA.md) 참조.

### 3. 저널리스트 페르소나

7개의 페르소나 중 선택:

| 페르소나 | 전문 분야 | 스타일 |
|---------|----------|--------|
| Dr. Sarah Kim | 포뮬레이션 과학 | 과학적이면서 접근 가능 |
| Dr. James Park | 임상 연구 | 증거 기반 |
| Dr. Emily Chen | 생명공학 | 기술 중심 |
| Yuna Lee | 제품 리뷰 | 대화체 |
| Alex Thompson | 시장 트렌드 | 분석적 |
| Min-ji Kang | 라이프스타일 | 우아하고 마음챙김 |
| Dr. David Rodriguez | 지속가능성 | 행동 지향적 |

자세한 내용은 [docs/PERSONAS.md](docs/PERSONAS.md) 참조.

## 🔧 Claude Code 스킬

`.claude/skills/`에 위치:

| 스킬 | 목적 |
|------|------|
| `journalist-writer.md` | 페르소나 목소리로 아티클 생성 |
| `image-generator.md` | 아티클 이미지 생성 |
| `article-publisher.md` | 아티클 검증 및 발행 |
| `yaml-validator.md` | Frontmatter 유효성 검사 |
| `seo-optimizer.md` | 검색 엔진 최적화 |

## 🎛️ 관리자 대시보드

`http://localhost:3000/admin/`에서 접근:

- 아티클 가시성 토글 (초안/발행)
- 추천 아티클 관리
- 홈페이지 우선순위 설정
- 발행 전 미리보기

## 📦 빌드 프로세스

빌드 스크립트 (`site/src/build.js`) 동작:

1. `/content/`에서 마크다운 파일 스캔
2. YAML frontmatter 파싱
3. marked.js로 마크다운 → HTML 변환
4. 생성물:
   - 홈페이지
   - 아티클 페이지
   - 카테고리 페이지
   - 저널리스트 페이지
   - RSS 피드
   - 사이트맵

## 🚢 배포

### Vercel (권장)

**자동 Vercel 배포** 설정됨:

1. GitHub에 Push → Vercel이 자동 빌드
2. 모든 브랜치에 프리뷰 배포
3. `master` 브랜치에 프로덕션 배포

### Obsidian에서 (원클릭)

**Obsidian Git** 플러그인 설치 시:
1. `Cmd+P` → `Obsidian Git: Create backup`
2. 완료! Vercel이 자동 배포

또는 자동 백업 대기 (10분마다 실행)

### 수동

1. `npm run build` 실행
2. `site/build/` 내용을 호스팅에 업로드
3. 도메인/SSL 설정

## 🔌 권장 Obsidian 플러그인

| 플러그인 | 용도 |
|---------|------|
| **Obsidian Git** | GitHub 자동 백업 & 동기화 |
| **Paste Image Rename** | 이미지 자동 이름 지정: `{filename}_{date}_{n}.png` |
| **Templater** | 동적 필드가 있는 아티클 템플릿 |
| **Linter** | YAML frontmatter 자동 포맷 |
| **Homepage** | Vault 열 때 기본 노트 설정 |

### 플러그인 설정 팁

- **Obsidian Git**: 아래 Git Push 관리 섹션 참조
- **Paste Image Rename**: 패턴: `{{fileName}}_{{DATE:YYYYMMDD}}_{{NNNNN}}`
- **이미지 폴더**: `content/_assets/images/`

## 🔄 Git Push 관리

이 프로젝트는 **Obsidian Git** 플러그인으로 자동 백업 및 GitHub 동기화를 사용합니다.

### 기본 설정

| 설정 | 값 | 설명 |
|------|-----|------|
| **Auto backup interval** | 10분 | 10분마다 자동 커밋 + Push |
| **Auto pull on startup** | ✅ ON | Obsidian 시작 시 최신 변경사항 Pull |
| **Push on backup** | ✅ ON | 백업 시 자동 Push |
| **Pull before push** | ✅ ON | 충돌 방지를 위해 Push 전 Pull |
| **Auto backup after file change** | ✅ ON | 파일 저장 시 즉시 Push |

### 자동 Push 동작

기본적으로 **저장 시 즉시 Push**로 설정되어 있습니다:

- 노트 생성/편집 → 저장 → GitHub에 자동 Push → Vercel 배포

**간격 기반 백업** (커밋 수 감소)을 원하면:

1. `.obsidian/plugins/obsidian-git/data.json` 열기
2. `"autoBackupAfterFileChange": false` 설정
3. Obsidian 재시작

이 설정으로 저장할 때마다가 아닌 10분마다 백업됩니다.

### 명령어 (Cmd+P / Ctrl+P)

| 명령어 | 설명 |
|--------|------|
| `Obsidian Git: Create backup` | 즉시 커밋 + Push (가장 많이 사용) |
| `Obsidian Git: Commit all changes` | 변경사항만 커밋 |
| `Obsidian Git: Push` | 원격에 Push |
| `Obsidian Git: Pull` | 원격에서 Pull |

### 커밋 메시지 형식

```
vault backup: 2026-01-16 22:07:32
```

### 상태 바

- Obsidian 하단 상태 바에서 Git 상태 확인
- ✓ = 동기화됨
- 숫자 = 변경된 파일 수

### 수동 Push (터미널)

```bash
cd "프로젝트-폴더"
git add .
git commit -m "메시지"
git push
```

### 플러그인 설정 동기화

플러그인 설정 (`data.json`)이 Git에 포함되어 쉽게 공유됩니다:
- Clone 시 설정 자동 적용
- Push 시 변경사항 함께 동기화

## 📝 문서

- [CLAUDE.md](CLAUDE.md) - Claude Code용 프로젝트 가이드라인
- [WORKFLOW.md](docs/WORKFLOW.md) - 콘텐츠 작성 워크플로우
- [YAML_SCHEMA.md](docs/YAML_SCHEMA.md) - Frontmatter 사양
- [PERSONAS.md](docs/PERSONAS.md) - 저널리스트 페르소나

## 🔗 링크

- **라이브 데모**: https://ai-diven-cos.vercel.app
- **샘플 아티클**: https://ai-diven-cos.vercel.app/articles/niacinamide-complete-guide.html
- **저장소**: https://github.com/passeth/ai-diven_cos
- **빠른 설정 가이드**: [SETUP.md](SETUP.md)

## 📄 라이선스

MIT 라이선스 - 자세한 내용은 LICENSE 파일 참조.

---

Obsidian + Claude Code + Vercel로 제작 | 인프라 비용 무료
