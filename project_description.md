

Простая текстовая игра на Django 4.1.3

Игра построена по принципу простой RPG кликнул -> Подождал -> Собрал награду

Базовый функционал:
- Герои игрока
- Профиль игрока
- Арена для регулярных действий
- Турнир типа ивента (пару раз в сутки) - привязка к классу героя
- Рудник (каждый игрок по умолчанию имеет не прокачанный рудник, который приносит золото раз в сутки)
- Катакомбы для зачистки (По уровням и со своей спицификой)
- Кузня(В кузне можно ковать предметы экипировки)
- Возможность купить валюту за реальные деньги
- Крепость
- Альянсы


Игрок:
  - Общий инвентарь на весь аккаунт (Все предметы хранятся по вкладкам в зависимости от типа)
  - Общий профиль(Аватарка, общая сила всех героев, Крепость, Альянс)
  - Профиль конкретного героя
  - Возможность выбрать определённого героя в качестве текущего




Герои
  Классы героев:
  1. Варвар
  2. Лучник
  3. Паладин
  4. Дворянин

    Герой имеет показатели:
    1. Уровень
    2. Атрибуты (Дворянин имеет одинаковые максимально базовые атрибуты)
    3. Показатель здоровья
    4. Показатель брони
    5. Скорость атаки
    5. Суммарный показатель защиты и урона
    3. Дерево прокачки
    4. Энергия (расходуема взависимости от действий)
    5. Текущую экипировку (отдельная таблица OneToOne)


Бонусы:
 Бонусы можно покупать в магазине и продлевать автоматически(если кликнуть галочку "Автопродление")
 Список бонусов:
    - Боевой раж (даёт +20% к силе на n-часов, покупается за золото)
    - Стойкость в бою (даёт +10% к общей прочности на n-часов, покупается за серебро)
    - Энергия из пустоты (сокращает расход энергии на 30% на n-часов, покупается за золото)







Дерево прокачки:
    Пассивные умения можно сбросить, но стоит дорого.
    Всего имеется 16 пассивных умений 4 больших и 12 маленьких
    Игрок на герое может взять 9 пассивок (7 не взятые это иллюзия вариативнисти)
    Каждый 4й поинт является большой пассивкой
    Напрвляем в сторону 1 из 2 веток(1 ветка защитная, 2 ветка урон)
    Направление ветки круговое, что бы игрок мог взять все большие пассивки


    Варвар:
     Базовая: Сердце война (70 жизни, 30 силы, Ув. жизни 10%)
     Защитная ветка(Правая):
        1. (30 брони, 30 жизни, 10 к силе)
        2. (50 брони, 50 жизни, 8% ув. жизни)
        3. (100 брони, 100 жизни, 14% ув. жизни )
        4. Большая защитная (увеличение брони 20%, + 140 к жизни)
        5. (30 брони, 30 жизни, 10 к силе)
        6. (50 брони, 50 жизни, 8% ув. жизни)
        7. (100 брони, 100 жизни, 14% ув. жизни
        8. Большая защита/урон (Ск. атаки +10%, 20 к силе, 20к интеллекту, +18% урона с оружием ближнего боя)
    Ветка Урона (Левая):
        1. (+30 к урону, +10% ск. атаки)
        2. (+50 к урону, +12% ск. атаки, +12% к общ. урону)
        3. (30% к общ. урону, +18% ск. атаки)
        Большая (+45% общего урона, +20 инт., +20 ловкости)

    





















