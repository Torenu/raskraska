from manim import *
from some_functions import *


def area(*args, **kwargs):
    p = []
    for k in range(len(args) - 1):
        p.append(get_ic(args[k], args[k + 1]))
    p.append(get_ic(args[0], args[len(args) - 1]))
    return Polygon(*p, color=WHITE, **kwargs)


def line(args):
    return Line(start=args[0:2] + [0], end=args[2:4] + [0])


class Kartinki(Scene):
    def construct(self):
        self.wait(4)
        statement = Text("На плоскости проведено несколько прямых.\n" +
                         "Они делят плоскость на области. Докажите, что\n" +
                         "области можно раскрасить в два цвета, чтобы\n" +
                         "соседние области были покрашены в разные цвета", font_size=20)

        # 1 условие задачи
        self.play(Create(statement), run_time=11)
        self.wait(7)
        self.play(statement.animate.move_to([3.6, 3.2, 0]), run_time=2)
        # statement.move_to([3.6, 3.2, 0])
        statement_box = SurroundingRectangle(statement, buff=0.1)
        self.play(Create(statement_box), run_time=3)
        # self.add(statement, statement_box)

        b1 = area(*BORDER1, stroke_width=0.7)
        b2 = area(*BORDER2, stroke_width=0.7)
        b3 = area(*BORDER3, stroke_width=0.7)
        b4 = area(*BORDER4, stroke_width=0.7)

        l1 = [line(LC[0])]

        p1 = [area(BORDER1[0], BORDER1[1], BORDER1[2], LC[0], fill_color=BLUE, fill_opacity=1),
              area(BORDER1[0], LC[0], BORDER1[2], BORDER1[3], fill_color=RED, fill_opacity=1)]

        l2 = [line(LC[1]),
              line(LC[2])]

        p2 = [area(BORDER2[1], BORDER2[2], LC[2], LC[1], fill_color=BLUE, fill_opacity=1),
              area(BORDER2[0], LC[2], LC[1], BORDER2[3], fill_color=BLUE, fill_opacity=1),
              area(BORDER2[0], BORDER2[1], LC[1], LC[2], fill_color=RED, fill_opacity=1),
              area(BORDER2[3], LC[1], LC[2], BORDER2[2], fill_color=RED, fill_opacity=1)]

        l3 = [line(LC[3]),
              line(LC[4]),
              line(LC[5])]

        p3 = [area(LC[3], LC[5], LC[4], fill_color=BLUE, fill_opacity=1),
              area(LC[3], BORDER3[3], BORDER3[0], LC[4], fill_color=BLUE, fill_opacity=1),
              area(BORDER3[0], BORDER3[1], LC[3], LC[5], fill_color=BLUE, fill_opacity=1),
              area(LC[4], BORDER3[2], LC[5], fill_color=BLUE, fill_opacity=1),
              area(LC[4], BORDER3[0], LC[5], LC[3], fill_color=RED, fill_opacity=1),
              area(LC[5], LC[3], BORDER3[1], BORDER3[2], LC[4], fill_color=RED, fill_opacity=1),
              area(BORDER3[3], LC[3], LC[4], LC[5], BORDER3[2], fill_color=RED, fill_opacity=1)]

        self.wait(3)
        # 2 хочется самому попробовать нарисовать рисунки
        self.play(Create(b1))
        self.wait(1)
        self.play(Create(l1[0]))

        self.play(Create(p1[0]))
        self.play(Create(p1[1]))

        self.wait(2)

        self.play(Create(b2))
        self.wait(1)
        self.play(*[Create(l2[k]) for k in range(len(l2))])

        self.play(Create(p2[0]))
        self.play(Create(p2[2]), Create(p2[3]))
        self.play(Create(p2[1]))

        self.wait(2)

        self.play(Create(b3))
        self.wait(1)
        self.play(*[Create(l3[k]) for k in range(len(l3))])

        self.play(Create(p3[0]))
        self.play(Create(p3[4]), Create(p3[5]), Create(p3[6]))
        self.play(Create(p3[1]), Create(p3[2]), Create(p3[3]))

        self.wait(7)

        # self.add(b1, b2, b3, *p1, *p2, *p3, *l1, *l2, *l3)

        # 3 разобраны не все варианты (для двух прямых)
        self.play(FadeOut(b1, b3, *p1, *p3, *l1, *l3))

        self.wait(3)
        self.play(FadeOut(*p2))

        l4 = [line(LC[6]),
              line(LC[7])]

        self.play(Transform(b2, b4),
                  Transform(l2[0], l4[0]),
                  Transform(l2[1], l4[1]))
        self.wait(2)

        l6 = [line(LC[8]),
              line(LC[9])]

        b5 = b2.copy()
        self.add(l4[0], l4[1])
        self.play(Transform(b5, b3),
                  Transform(l4[0], l6[0]),
                  Transform(l4[1], l6[1]))

        p2 = [p2[k].shift([0, 1.825, 0]) for k in range(len(p2))]
        p4 = [area(BORDER3[0], BORDER3[1], LC[8], fill_color=BLUE, fill_opacity=1),
              area(BORDER3[0], LC[8], BORDER3[1], BORDER3[2], LC[9], BORDER3[3], fill_color=RED, fill_opacity=1),
              area(BORDER3[3], LC[9], BORDER3[2], fill_color=BLUE, fill_opacity=1)]

        self.play(Create(p2[0]), Create(p4[0]))
        self.play(Create(p2[3]), Create(p2[2]), Create(p4[1]))
        self.play(Create(p2[1]), Create(p4[2]))
        self.wait(3)
        self.play(FadeOut(b5, b2, *p2, *l4, *p4, *l2))

        # 4 для трех прямых еще хуже

        self.play(Create(b3))
        self.play(*[Create(l3[k]) for k in range(len(l3))])
        self.wait(2)

        l4 = [line(LC[3]),
              line(LC[4]),
              line(LC[5])]
        l5 = [line(LC[3]),
              line(LC[4]),
              line(LC[5])]
        b4 = b3.copy()
        b5 = b3.copy()
        self.add(*l4, *l5)

        l1 = [line(LC[10]),
              line(LC[11]),
              line(LC[12])]

        self.play(Transform(b4, b1),
                  *[Transform(l4[k], l1[k]) for k in range(len(l4))])

        self.wait(2)

        p1 = [area(BORDER1[0], LC[10], BORDER1[1], LC[11], fill_color=RED, fill_opacity=1),
              area(BORDER1[0], BORDER1[1], LC[10], fill_color=BLUE, fill_opacity=1),
              area(LC[11], BORDER1[2], LC[12], BORDER1[3], fill_color=BLUE, fill_opacity=1),
              area(LC[12], BORDER1[2], BORDER1[3], fill_color=RED, fill_opacity=1)]

        self.play(Create(p1[0]))
        self.play(Create(p1[1]), Create(p1[2]))
        self.play(Create(p1[3]))

        self.wait(2)

        l2 = [line(LC[13]),
              line(LC[14]),
              line(LC[15])]

        b2 = area(*BORDER2, stroke_width=0.7)

        self.play(Transform(b5, b2),
                  *[Transform(l5[k], l2[k]) for k in range(len(l5))])

        self.wait(2)

        p2 = [area(BORDER2[0], LC[13], LC[15], LC[14], BORDER2[3], fill_color=RED, fill_opacity=1),
              area(BORDER2[0], BORDER2[1], LC[15], LC[13], fill_color=BLUE, fill_opacity=1),
              area(BORDER2[3], LC[14], LC[15], fill_color=BLUE, fill_opacity=1),
              area(LC[15], LC[13], BORDER2[1], BORDER2[2], LC[14], fill_color=BLUE, fill_opacity=1),
              area(LC[15], BORDER2[1], LC[13], fill_color=RED, fill_opacity=1),
              area(LC[15], LC[14], BORDER2[2], BORDER2[3], fill_color=RED, fill_opacity=1)]

        self.play(Create(p2[0]))
        self.play(Create(p2[1]), Create(p2[2]), Create(p2[3]))
        self.play(Create(p2[4]), Create(p2[5]))

        self.wait(2)

        l6 = [line(LC[16]),
              line(LC[17]),
              line(LC[18])]

        self.play(*[Transform(l3[k], l6[k]) for k in range(len(l3))])
        self.wait(2)

        p3 = [area(BORDER3[0], BORDER3[1], LC[16], LC[17], fill_color=RED, fill_opacity=1),
              area(BORDER3[0], LC[17], LC[18], fill_color=BLUE, fill_opacity=1),
              area(LC[16], BORDER3[1], BORDER3[2], LC[18], fill_color=BLUE, fill_opacity=1),
              area(LC[18], LC[16], BORDER3[3], BORDER3[0], fill_color=RED, fill_opacity=1),
              area(LC[18], BORDER3[2], LC[17], fill_color=RED, fill_opacity=1),
              area(LC[16], LC[17], BORDER3[2], BORDER3[3], fill_color=BLUE, fill_opacity=1)]

        self.play(Create(p3[0]))
        self.play(Create(p3[1]), Create(p3[2]))
        self.play(Create(p3[4]), Create(p3[3]))
        self.play(Create(p3[5]))
        
        # ADD WAIT BEFORE FADING
        self.wait(10)
        self.play(FadeOut(b5, b3, b4, *p3, *p2, *p1, *l5, *l3, *l4))

        # 5 ( где то в паузе ) перебором не решить(
        self.wait(10)

        b = area(*BORDER5, stroke_width=0.7)

        # SWITCH BEFORE RENDER
        # self.add(b)
        self.play(Create(b))

        # 19 20 21 тут прямые для четвертой картинки + индукции
        # 19 22 23 base
        l = [line(LC[19]),
             line(LC[22]),
             line(LC[23])]

        p = [area(BORDER5[0], BORDER5[1], LC[19], BORDER5[3], fill_color=RED, fill_opacity=1),
             area(BORDER5[1], BORDER5[2], BORDER5[3], LC[19], fill_color=BLUE, fill_opacity=1),
             area(BORDER5[0], BORDER5[1], BORDER5[2], LC[22], fill_color=RED, fill_opacity=1),
             area(BORDER5[0], LC[22], BORDER5[2], BORDER5[3], fill_color=BLUE, fill_opacity=1),
             area(BORDER5[0], BORDER5[1], LC[23], BORDER5[3], fill_color=RED, fill_opacity=1),
             area(BORDER5[1], BORDER5[2], BORDER5[3], LC[23], fill_color=BLUE, fill_opacity=1)]

        # 6 первым шагом проверим, что утверждение задачи верно для 1 прямой
        self.play(Create(l[0]))
        self.play(Create(p[0]))
        self.play(Create(p[1]))
        self.play(FadeOut(p[0], p[1]))
        self.play(Transform(l[0], l[1]))
        self.play(Create(p[2]))
        self.play(Create(p[3]))
        self.play(FadeOut(p[2], p[3]))
        self.play(Transform(l[0], l[2]))
        self.play(Create(p[4]))
        self.play(Create(p[5]))
        self.play(FadeOut(p[4], p[5], l[0]))

        # тут должен быть self.wait
        self.wait(5)

        l = [line(LC[19]),
             line(LC[20]),
             line(LC[21]),
             line(LC[23])]
        l[3].set_color(PURE_GREEN)
        l[3].set(stroke_width=10)

        p = [area(LC[19], LC[20], LC[21], fill_color=BLUE, fill_opacity=1),
             area(BORDER5[0], LC[20], LC[19], LC[21], fill_color=RED, fill_opacity=1),
             area(BORDER5[1], BORDER5[2], LC[21], LC[20], LC[19], fill_color=RED, fill_opacity=1),
             area(LC[21], LC[20], BORDER5[2], BORDER5[3], LC[19], fill_color=RED, fill_opacity=1),
             area(BORDER5[0], BORDER5[1], LC[19], LC[20], fill_color=BLUE, fill_opacity=1),
             area(LC[20], LC[21], BORDER5[2], fill_color=BLUE, fill_opacity=1),
             area(BORDER5[0], LC[21], LC[19], BORDER5[3], fill_color=BLUE, fill_opacity=1),
             area(LC[23], LC[20], LC[21], LC[19], fill_color=RED, fill_opacity=1),
             area(LC[23], LC[19], LC[21], fill_color=BLUE, fill_opacity=1),
             area(LC[23], BORDER5[1], BORDER5[2], LC[21], LC[20], fill_color=BLUE, fill_opacity=1),
             area(LC[23], LC[21], LC[19], BORDER5[3], fill_color=RED, fill_opacity=1)]

        # 7 вторым шагом предположим что есть набор из n прямых
        self.play(Create(l[0]))
        self.play(Create(l[1]))
        self.play(Create(l[2]))
        self.play(Create(p[0]), run_time=2)
        self.play(Create(p[1]), Create(p[2]), Create(p[3]), run_time=2)
        self.play(Create(p[4]), Create(p[5]), Create(p[6]), run_time=2)

        self.wait(5)
        # 8 третьим шагом попробуем понять, что происходит при добавлении 1 прямой
        self.play(Create(l[3]))
        self.play(l[3].animate.set_stroke_width(7))
        self.wait(5)

        # 9 старая раскраска нам уже не годится
        self.play(p[4].animate.set_fill_color(GRAY_D),
                  p[5].animate.set_fill_color(GRAY_D),
                  p[3].animate.set_fill_color(GRAY_D), run_time=4)
        self.wait(5)
        self.play(p[3].animate.set_fill_color(RED),
                  p[4].animate.set_fill_color(BLUE),
                  p[5].animate.set_fill_color(BLUE), run_time=3)

        # TEST 10-13
        # l[3].set(stroke_width=7)
        # self.add(*p[0:7], *l)
        # TEST 10-13

        self.wait(3)

        # 10 поменяли цвет у одной из новых областей, не работает
        self.play(Create(p[7]), run_time=3)
        self.add(l[1], l[3])

        self.wait(15)

        # 11 действуем более глобально
        self.play(Create(p[8]), Create(p[9]), Create(p[10]),
                  p[3].animate.set_fill_color(BLUE),
                  p[5].animate.set_fill_color(RED), run_time=7)
        self.add(l[1], l[3])

        # тут надо реально много
        self.wait(30)

        # TEST 12-13
        # l[3].set(stroke_width=7)
        # p[3].set(fill_color=BLUE)
        # p[5].set(fill_color=RED)
        # self.add(*p, *l)
        # TEST 12-13

        # 12 первый случай мигает
        self.play(l[3].animate.set_stroke_width(10))
        self.play(p[4].animate.set_fill_color(GRAY_D),
                  p[5].animate.set_fill_color(GRAY_D),
                  p[3].animate.set_fill_color(GRAY_D), run_time=4)
        # WAIT НА РАССКАЗ ПОСТАВЬ ПОБОЛЬШЕ
        self.wait(10)
        self.play(p[3].animate.set_fill_color(BLUE),
                  p[4].animate.set_fill_color(BLUE),
                  p[5].animate.set_fill_color(RED), run_time=3)
        self.play(l[3].animate.set_stroke_width(7))

        # self.wait(4)

        # 13 второй случай мигает
        self.play(l[1].animate.set_stroke_width(10))
        self.play(l[1].animate.set_color(YELLOW))
        self.play(p[8].animate.set_fill_color(GRAY_D),
                  p[6].animate.set_fill_color(GRAY_D),
                  p[10].animate.set_fill_color(GRAY_D), run_time=4)
        # WAIT НА РАССКАЗ ПОСТАВЬ ПОБОЛЬШЕ
        self.wait(10)
        self.play(p[8].animate.set_fill_color(BLUE),
                  p[6].animate.set_fill_color(BLUE),
                  p[10].animate.set_fill_color(RED), run_time=3)
        self.play(l[1].animate.set_stroke_width(5))
        self.play(l[1].animate.set_color(WHITE))
        self.add(l[3])
        
        self.play(FadeOut(*p, *l))

        # 14 FINAL

        l = [line(LC[24]),
             line(LC[25]),
             line(LC[26]),
             line(LC[27])]

        p = [area(BORDER5[0], BORDER5[1], BORDER5[2], BORDER5[3], fill_color=BLUE, fill_opacity=1),
             area(LC[24], BORDER5[1], BORDER5[2], BORDER5[3], fill_color=RED, fill_opacity=1),
             area(BORDER5[0], BORDER5[1], LC[25], LC[24], BORDER5[3], fill_color=RED, fill_opacity=1),
             area(LC[24], LC[25], BORDER5[3], fill_color=BLUE, fill_opacity=1),
             area(LC[26], BORDER5[1], BORDER5[2], BORDER5[3], fill_color=BLUE, fill_opacity=1),
             area(BORDER5[0], LC[27], LC[24], BORDER5[3], fill_color=RED, fill_opacity=1),
             area(LC[24], LC[27], LC[26], BORDER5[3], fill_color=BLUE, fill_opacity=1),
             area(LC[26], LC[27], BORDER5[2], BORDER5[3], fill_color=RED, fill_opacity=1)]

        # итак, посмотрим как же работает наш алгоритм раскраски
        self.play(Create(p[0]))

        # для одной прямой условие выполняется
        self.play(Create(l[0]))
        self.play(Create(p[1]), run_time=2)
        self.wait(3)

        # добавив одну прямую получаем решение
        self.play(Create(l[1]))
        self.wait(2)
        self.play(Create(p[2]), Create(p[3]), run_time=2)
        self.wait(2)

        # при этом неважно параллельна или нет
        self.play(FadeOut(l[1], p[2], p[3]))
        self.wait(2)
        self.play(Create(l[2]))
        self.wait(2)
        self.play(Create(p[4]), run_time=2)

        self.wait(3)
        # теперь можно добавить третью прямую
        self.play(Create(l[3]))
        self.wait(2)
        self.play(Create(p[5]), Create(p[6]), Create(p[7]), run_time=2)

        self.wait(10)
