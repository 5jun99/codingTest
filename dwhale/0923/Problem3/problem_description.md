# 문제: 성과 관리 시스템 – 상시 피드백 및 캘리브레이션

## 문제 설명

당신은 성과 관리 SaaS(클랩) 팀에 합류한 백엔드 개발자입니다.
기업 고객들이 사용하는 **상시 피드백 + 캘리브레이션** 기능을 구현해야 합니다.

이 기능은 다음 요구사항을 만족해야 합니다.

1. 여러 직원(`Employee`)이 있고, 각 직원은 다수의 피드백(`Feedback`)을 가진다.
2. 하나의 피드백은 다음 정보로 구성된다.
   * `evaluatorId`: 평가자 ID
   * `text`: 피드백 내용
   * `score`: 0~100 사이의 정수 점수 (없을 수도 있음)
3. 여러 스레드가 동시에 피드백을 추가할 수 있다.
   * 동시성 문제 없이 안전해야 한다.
4. 모든 피드백이 입력된 후 **캘리브레이션**을 수행한다.
   * 평가자별 평균 점수를 계산한다.
   * 전체 평균보다 특정 평가자의 평균이 높으면, 그 평가자의 모든 점수를 `(전체평균 / 평가자평균)` 비율로 조정한다.
   * 낮은 경우에는 조정하지 않는다.
   * 조정 결과는 소수점 둘째 자리까지 반올림한다.
5. 각 직원에 대한 리포트를 생성해야 한다. 리포트는 다음을 포함한다.
   * 원본 점수 평균 (score 없는 피드백은 제외)
   * 조정된 점수 평균
   * 모든 피드백 텍스트 목록

---

## 입력 형식

표준 입력으로 다음이 주어진다.

* 첫 줄: 직원 수 `N` (1 ≤ N ≤ 100)
* 둘째 줄: 직원들의 ID와 이름 (공백 구분)
* 셋째 줄: 피드백 수 `M` (1 ≤ M ≤ 1000)
* 이후 M줄: 각 피드백 정보 (직원ID evaluatorID text score)
  * score가 `-1`이면 점수가 없는 피드백으로 처리한다.
  * text는 공백 없는 문자열이라고 가정한다.

---

## 출력 형식

N명의 직원별로 리포트를 출력한다.

형식:
```
[직원이름]
원본 평균: X
조정 평균: Y
피드백: text1, text2, ...
```

X, Y는 소수점 둘째 자리까지 출력.

---

## 입력 예시

```
2
E1 Alice
E2 Bob
5
E1 A1 GoodJob 80
E2 A2 NeedsImprovement 60
E1 A3 KeepGoing -1
E2 A1 SolidWork 90
E1 A2 Excellent 100
```

---

## 출력 예시

```
[Alice]
원본 평균: 90.00
조정 평균: 85.00
피드백: GoodJob, KeepGoing, Excellent

[Bob]
원본 평균: 75.00
조정 평균: 72.50
피드백: NeedsImprovement, SolidWork
```

---

## 구현 조건

* `Employee`, `Feedback`, `FeedbackService`, `CalibrationModule`, `Report` 클래스를 정의할 것.
* `FeedbackService.addFeedback(Employee e, Feedback f)`는 **동시성 안전**하게 작성할 것.
* `CalibrationModule.calibrate(List<Employee> employees)`에서 조정 로직을 구현할 것.
* `Report`는 직원별로 생성되어 출력까지 담당할 것.

---

## MVC 패턴 적용

현재 `src/main/java/original_state/` 폴더에 기본 뼈대가 있습니다:

* **Model**: `Employee`, `Feedback`, `FeedbackService`, `CalibrationModule` 클래스들
* **View**: 입출력을 담당할 클래스 (생성 필요)
* **Controller**: `EvaluationController` 클래스
* **Main**: 애플리케이션 진입점

### 다음 단계로 구현하세요:

1. **View 클래스 생성**: 입력 읽기와 결과 출력을 담당
2. **Model 클래스들 완성**: 필요한 메소드들 추가
3. **Controller 로직 구현**: View와 Model을 연결
4. **Main에서 MVC 조립**: Controller에 실행 위임