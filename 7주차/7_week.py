import math
import turtle

# 글꼴: 한글이 네모(□)로 보이면 다른 이름으로 바꿔 보세요 (예: "Pretendard", "Arial")
FONT = "맑은 고딕"

sons = ["르우벤", "시므온", "레위", "유다", "단", "납달리",
        "갓", "아셀", "잇사갈", "스불론", "요셉", "베냐민"]

screen = turtle.Screen()
screen.title("이스라엘 12지파")
screen.bgcolor("#FFF4D6")
screen.setup(900, 700)

t = turtle.Turtle()
t.hideturtle()
t.speed(3)

# 제목
t.penup()
t.goto(0, 290)
t.color("#8B4513")
t.write("✡  이스라엘 12지파  ✡",
        align="center", font=(FONT, 26, "bold"))

# 12개의 별을 원형으로 배치
center_x, center_y = 0, -20
radius = 200

colors = ["#E74C3C", "#E67E22", "#F1C40F", "#2ECC71",
          "#1ABC9C", "#3498DB", "#9B59B6", "#E91E63",
          "#795548", "#FF5722", "#16A085", "#C0392B"]

for i in range(12):
    # 12시 방향부터 시계방향으로 배치
    angle = 90 - (360 / 12) * i

    # 별 위치
    x = center_x + radius * math.cos(math.radians(angle))
    y = center_y + radius * math.sin(math.radians(angle))

    # 별 그리기
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color(colors[i], colors[i])
    t.begin_fill()
    for _ in range(5):
        t.forward(30)
        t.right(144)
    t.end_fill()

    # 이름 쓰기 (별 바깥쪽)
    t.penup()
    name_x = center_x + (radius + 60) * math.cos(math.radians(angle))
    name_y = center_y + (radius + 60) * math.sin(math.radians(angle)) - 10
    t.goto(name_x, name_y)
    t.color("#333333")
    t.write(sons[i], align="center", font=(FONT, 14, "bold"))

# 가운데 메시지
t.penup()
t.goto(0, -15)
t.color("#8B4513")
t.write("리스트 마스터!", align="center", font=(FONT, 22, "bold"))

t.goto(0, -50)
t.color("#555555")
t.write("야곱의 12아들 = 이스라엘 12지파",
        align="center", font=(FONT, 14, "normal"))

turtle.done()