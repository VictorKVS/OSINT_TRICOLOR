# RP-002 · Протокол исследования и ответственного тестирования
## Исследовательская карточка
- ID / дата / исследователь / роли reviewer
- цель и business/FR trace
- утверждённый scope и источник права на исследование
- версия исследуемого компонента и методики
- входные данные и их класс (synthetic/public/authorized/internal)
- ожидаемый результат, измеримые метрики, критерии прекращения
- ход эксперимента (воспроизводимо), журналы, hash и provenance
- полученные факты, интерпретации, неопределённости и ограничения
- security/privacy/legal review, риски и отклонения
- решение: approve/retest/reject, upstream CORE / PROFILE / EXPERIMENT
## Research Security
Не обходить авторизацию/защиту, не применять активные проверки к чужим системам, не собирать избыточные ПД; контролировать rate limits, секреты и журналирование. Все adversarial тесты выполнять на собственном полигоне либо с явным разрешением. Исключить автоматическую атрибуцию физических лиц или отправку претензий.
## QA
Research reproducibility, peer-review, negative tests, false-positive accounting, protocol version, evidence of manual approval. До воспроизводимого теста и независимой проверки результат имеет статус hypothesis/experiment.
