"""
💡 Boolean 연산자 - 전구 + 성경 이야기
=======================================
전구를 켜고 끄면서 and / or / not 이 어떻게 결과를 만드는지 보고,
아래에서 파이썬 if / else 가 실제로 어느 쪽을 실행하는지 확인해요.

조작법
  1 ~ 6 키 (또는 전구 클릭) : 전구 켜기 / 끄기
  ← → 키 (또는 위쪽 탭 클릭) : 상황 바꾸기
"""

import pygame
import asyncio


# ═══════════════════════════════════════════════════════════════
#  화면 / 색상 설정
# ═══════════════════════════════════════════════════════════════

SCREEN_W = 800
SCREEN_H = 600
FPS = 60

BG = (30, 30, 50)
WHITE = (255, 255, 255)
GRAY = (130, 130, 145)
DARK_GRAY = (60, 60, 75)
YELLOW = (255, 220, 60)
ORANGE = (255, 150, 50)
GREEN = (90, 225, 110)
RED = (235, 85, 95)
CYAN = (100, 200, 240)
CODE_BG = (20, 20, 35)

FONT_NAMES = "malgungothic,applegothic,nanumgothic,notosanscjkkr,arial"
_font_cache = {}


def get_font(size, bold=False):
    key = (size, bold)
    if key not in _font_cache:
        _font_cache[key] = pygame.font.SysFont(FONT_NAMES, size, bold=bold)
    return _font_cache[key]


# ═══════════════════════════════════════════════════════════════
#  📖 성경 상황 목록 (여기에 새 상황을 추가할 수 있어요!)
# ═══════════════════════════════════════════════════════════════
#
#  op      : "AND" / "OR" / "NOT"
#  items   : (화면에 보이는 이름, 코드에 쓰는 변수 이름)
#  start   : 처음 전구 상태
#
# ───────────────────────────────────────────────────────────────

SCENARIOS = [
    {
        "op": "AND",
        "tab": "AND  전신갑주",
        "title": "하나님의 전신갑주 (모두 입어야 해요!)",
        "verse": "에베소서 6:11-17  |  하나님의 전신갑주를 입으라",
        "items": [
            ("진리의 허리띠", "허리띠"),
            ("의의 호심경", "호심경"),
            ("복음의 신", "신발"),
            ("믿음의 방패", "방패"),
            ("구원의 투구", "투구"),
            ("성령의 검", "검"),
        ],
        "start": [True, True, True, True, True, False],
        "msg_true": "마귀의 공격을 이길 수 있어요!",
        "msg_false": "빠진 갑주가 있어요. 약점이 생겨요!",
    },
    {
        "op": "OR",
        "tab": "OR  나아가는 길",
        "title": "하나님께 나아가는 길 (하나만 있어도 돼요!)",
        "verse": "히브리서 4:16  |  은혜의 보좌 앞에 담대히 나아가자",
        "items": [
            ("기도", "기도"),
            ("찬양", "찬양"),
            ("말씀", "말씀"),
        ],
        "start": [False, False, False],
        "msg_true": "하나님과 교제하고 있어요!",
        "msg_false": "아직 하나님께 나아가지 않았어요.",
    },
    {
        "op": "NOT",
        "tab": "NOT  시험",
        "title": "시험에 들지 않기 (반대로 뒤집어요!)",
        "verse": "마태복음 26:41  |  시험에 들지 않게 깨어 기도하라",
        "items": [
            ("시험에 들었음", "시험에_들음"),
        ],
        "start": [True],
        "msg_true": "시험을 이겼어요!",
        "msg_false": "깨어서 기도해야 해요.",
    },
]


# ═══════════════════════════════════════════════════════════════
#  계산 함수
# ═══════════════════════════════════════════════════════════════

def evaluate(op, values):
    if op == "AND":
        return all(values)
    if op == "OR":
        return any(values)
    return not values[0]


def py_op(op):
    return {"AND": " and ", "OR": " or "}.get(op, "")


# ═══════════════════════════════════════════════════════════════
#  그리기 함수
# ═══════════════════════════════════════════════════════════════

def draw_glow(screen, x, y, radius):
    for r in range(radius + 40, radius, -10):
        surf = pygame.Surface((r * 2, r * 2), pygame.SRCALPHA)
        pygame.draw.circle(surf, (255, 240, 100, 35), (r, r), r)
        screen.blit(surf, (x - r, y - r))


def draw_bulb(screen, x, y, radius, is_on, socket=True):
    if is_on:
        draw_glow(screen, x, y, radius)

    color = YELLOW if is_on else DARK_GRAY
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.draw.circle(screen, (40, 40, 50), (x, y), radius, 3)

    if is_on:
        pygame.draw.circle(screen, WHITE, (x - radius // 3, y - radius // 3),
                           max(3, radius // 5))

    # 필라멘트
    fil = ORANGE if is_on else (85, 85, 100)
    s = radius // 3
    pygame.draw.line(screen, fil, (x - s, y + s // 2), (x - s // 3, y - s), 2)
    pygame.draw.line(screen, fil, (x - s // 3, y - s), (x + s // 3, y - s), 2)
    pygame.draw.line(screen, fil, (x + s // 3, y - s), (x + s, y + s // 2), 2)

    if socket:
        w = radius
        pygame.draw.rect(screen, (100, 100, 112),
                         (x - w // 2, y + radius - 4, w, 14))
        pygame.draw.rect(screen, (70, 70, 82),
                         (x - w // 2, y + radius - 4, w, 14), 2)


def draw_text(screen, text, size, color, center=None, left=None, y=None, bold=False):
    surf = get_font(size, bold).render(text, True, color)
    if center is not None:
        rect = surf.get_rect(center=center)
    else:
        rect = surf.get_rect(midleft=(left, y))
    screen.blit(surf, rect)
    return rect


# ═══════════════════════════════════════════════════════════════
#  메인 프로그램
# ═══════════════════════════════════════════════════════════════

class BoolBibleVisualizer:
    BULB_Y = 205
    BULB_R = 28
    RESULT_POS = (400, 385)
    RESULT_R = 36

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        pygame.display.set_caption("Boolean 연산자 - 전구와 성경")
        self.clock = pygame.time.Clock()

        self.mode = 0
        # 상황마다 전구 상태를 따로 기억
        self.states = [list(s["start"]) for s in SCENARIOS]

        # 위쪽 탭 영역
        self.tab_rects = []
        for i in range(len(SCENARIOS)):
            self.tab_rects.append(pygame.Rect(45 + i * 240, 12, 230, 36))

    # ── 현재 상황 도우미 ──
    @property
    def scenario(self):
        return SCENARIOS[self.mode]

    @property
    def values(self):
        return self.states[self.mode]

    def bulb_xs(self):
        n = len(self.values)
        spacing = 120 if n >= 6 else 200
        return [int(400 + (i - (n - 1) / 2) * spacing) for i in range(n)]

    def toggle(self, index):
        if 0 <= index < len(self.values):
            self.values[index] = not self.values[index]

    # ── 메인 루프 ──
    async def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self._on_key(event.key)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self._on_click(event.pos)

            self._draw()
            pygame.display.flip()
            self.clock.tick(FPS)
            await asyncio.sleep(0)

        pygame.quit()

    def _on_key(self, key):
        if key == pygame.K_RIGHT:
            self.mode = (self.mode + 1) % len(SCENARIOS)
        elif key == pygame.K_LEFT:
            self.mode = (self.mode - 1) % len(SCENARIOS)
        elif pygame.K_1 <= key <= pygame.K_6:
            self.toggle(key - pygame.K_1)

    def _on_click(self, pos):
        # 탭 클릭
        for i, rect in enumerate(self.tab_rects):
            if rect.collidepoint(pos):
                self.mode = i
                return
        # 전구 클릭
        for i, x in enumerate(self.bulb_xs()):
            dx = pos[0] - x
            dy = pos[1] - self.BULB_Y
            if dx * dx + dy * dy <= (self.BULB_R + 8) ** 2:
                self.toggle(i)
                return

    # ── 그리기 ──
    def _draw(self):
        self.screen.fill(BG)
        sc = self.scenario
        values = self.values
        result = evaluate(sc["op"], values)

        self._draw_tabs()

        # 제목 / 말씀 / 조작 안내
        draw_text(self.screen, sc["title"], 24, YELLOW,
                  center=(SCREEN_W // 2, 78), bold=True)
        draw_text(self.screen, sc["verse"], 15, CYAN,
                  center=(SCREEN_W // 2, 108))
        draw_text(self.screen, "숫자키 또는 전구 클릭: 켜기/끄기      ← → : 상황 바꾸기",
                  13, GRAY, center=(SCREEN_W // 2, 134))

        # 입력 전구 + 결과로 이어지는 전선
        xs = self.bulb_xs()
        for i, x in enumerate(xs):
            wire_color = YELLOW if values[i] else DARK_GRAY
            pygame.draw.line(self.screen, wire_color,
                             (x, self.BULB_Y + 84),
                             (self.RESULT_POS[0], self.RESULT_POS[1] - self.RESULT_R - 6), 3)

        for i, x in enumerate(xs):
            draw_bulb(self.screen, x, self.BULB_Y, self.BULB_R, values[i])
            name = sc["items"][i][0]
            draw_text(self.screen, name, 15, WHITE,
                      center=(x, self.BULB_Y + 58), bold=True)
            state_text = "True" if values[i] else "False"
            draw_text(self.screen, f"[{i + 1}] {state_text}", 14,
                      GREEN if values[i] else RED,
                      center=(x, self.BULB_Y + 80))

        # 결과 전구 + 메시지
        draw_bulb(self.screen, self.RESULT_POS[0], self.RESULT_POS[1],
                  self.RESULT_R, result, socket=False)
        draw_text(self.screen, "결과: " + ("True" if result else "False"),
                  26, GREEN if result else RED,
                  left=self.RESULT_POS[0] + 70, y=self.RESULT_POS[1] - 12, bold=True)
        msg = sc["msg_true"] if result else sc["msg_false"]
        draw_text(self.screen, msg, 17, WHITE,
                  left=self.RESULT_POS[0] + 70, y=self.RESULT_POS[1] + 20)

        # AND 일 때 빠진 것 알려주기
        if sc["op"] == "AND" and not result:
            missing = [sc["items"][i][0] for i, v in enumerate(values) if not v]
            draw_text(self.screen, "빠진 것: " + ", ".join(missing), 14, ORANGE,
                      center=(SCREEN_W // 2, 432))

        self._draw_code(result)

    def _draw_tabs(self):
        for i, rect in enumerate(self.tab_rects):
            active = (i == self.mode)
            pygame.draw.rect(self.screen, CYAN if active else DARK_GRAY,
                             rect, border_radius=10)
            draw_text(self.screen, SCENARIOS[i]["tab"], 16,
                      (20, 20, 35) if active else GRAY,
                      center=rect.center, bold=True)

    def _draw_code(self, result):
        sc = self.scenario
        values = self.values
        op = sc["op"]

        box = pygame.Rect(40, 448, SCREEN_W - 80, 140)
        pygame.draw.rect(self.screen, CODE_BG, box, border_radius=10)
        pygame.draw.rect(self.screen, CYAN, box, 2, border_radius=10)

        names = [var for _, var in sc["items"]]
        if op == "NOT":
            condition = "not " + names[0]
            substituted = "not " + str(values[0])
        else:
            condition = py_op(op).join(names)
            substituted = py_op(op).join(str(v) for v in values)

        x = box.x + 20
        draw_text(self.screen, "값 대입:  " + substituted, 14, GRAY,
                  left=x, y=box.y + 18)

        lines = [
            (f"if {condition}:", WHITE, 0),
            (f'print("{sc["msg_true"]}")', GREEN if result else GRAY, 1),
            ("else:", WHITE, 0),
            (f'print("{sc["msg_false"]}")', GREEN if not result else GRAY, 1),
        ]
        for i, (text, color, indent) in enumerate(lines):
            line_y = box.y + 46 + i * 24
            draw_text(self.screen, text, 16, color, left=x + indent * 30, y=line_y)
            if color == GREEN:
                draw_text(self.screen, "<- 실행!", 14, GREEN,
                          left=box.right - 90, y=line_y)


# ═══════════════════════════════════════════════════════════════
#  실행!
# ═══════════════════════════════════════════════════════════════

async def main():
    app = BoolBibleVisualizer()
    await app.run()

asyncio.run(main())