# ═══════════════════════════════════════════════════════════════
#  🚶‍♂️ 물 위를 걷는 베드로 - Step 2 (웹 버전, 한 파일)
# ═══════════════════════════════════════════════════════════════
#  📖 마태복음 14:22-33
#  🎮 마우스를 노란 범위 안에 유지하고, 돌풍 🌬️ 과 파도 🌊 를 피하세요!
#     시간이 지나면 예수님이 나타나요. 예수님을 클릭하면 승리!
# ═══════════════════════════════════════════════════════════════

import pygame
import random
import math
import asyncio


# ┌─────────────────────────────────────────────────────────────┐
# │  [A] 준비 코드  ※ 수정하지 마세요! 아래 [B]로 내려가세요       │
# └─────────────────────────────────────────────────────────────┘

W, H = 900, 600
_만든_게임들 = []


def _is_num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


class _GameSettings:
    def __init__(self, name):
        self.name = name
        self.safe_height = 100
        self.game_time = 30
        self.winds = []
        self.waves = []
        self.zone_moves = []
        self.zone_shrinks = []
        self.blackouts = []
        self.lightning_count = 0
        self.started = False

    def set_safe_zone(self, 높이=100):
        if not _is_num(높이) or not 50 <= 높이 <= 300:
            print(f"⚠️ 높이는 50~300 사이여야 해요 (입력값: {높이}) → 기본값 100으로 설정")
            높이 = 100
        self.safe_height = int(높이)
        return self

    def set_time(self, 시간=30):
        if not _is_num(시간) or not 10 <= 시간 <= 120:
            print(f"⚠️ 시간은 10~120초 사이여야 해요 (입력값: {시간}) → 기본값 30초로 설정")
            시간 = 30
        self.game_time = int(시간)
        return self

    def _check_time(self, kind, t):
        if not _is_num(t) or t < 0 or t > self.game_time:
            print(f"⚠️ {kind} 등장_시간은 0~{self.game_time}초 사이여야 해요 (입력값: {t}) → 이 {kind}은(는) 추가하지 않아요")
            return False
        return True

    def add_wind(self, 등장_시간, x좌표):
        if not self._check_time("돌풍", 등장_시간):
            return self
        if not _is_num(x좌표) or not 0 <= x좌표 <= W:
            print(f"⚠️ 돌풍 x좌표는 0~{W} 사이여야 해요 (입력값: {x좌표}) → 이 돌풍은 추가하지 않아요")
            return self
        self.winds.append((등장_시간, x좌표))
        return self

    def add_wave(self, 등장_시간, 방향):
        if not self._check_time("파도", 등장_시간):
            return self
        if 방향 not in ("오른쪽", "왼쪽"):
            print(f'⚠️ 파도 방향은 "오른쪽" 또는 "왼쪽"이어야 해요 (입력값: {방향}) → 이 파도는 추가하지 않아요')
            return self
        self.waves.append((등장_시간, 방향))
        return self

    def start(self):
        self.started = True


def create_game(이름="베드로"):
    if not isinstance(이름, str) or not 이름.strip():
        print("⚠️ 이름은 글자(문자열)여야 해요 → '베드로'로 설정")
        이름 = "베드로"
    game = _GameSettings(이름)
    _만든_게임들.append(game)
    return game


class _EngineName:
    pass


# peter_engine2.create_game(...) 처럼 써도 되게 (import 는 쓰지 않아요)
peter_engine2 = _EngineName()
peter_engine2.create_game = create_game


# ┌─────────────────────────────────────────────────────────────┐
# │  [B] 🧑‍💻 학생이 작성하는 부분                                  │
# └─────────────────────────────────────────────────────────────┘

# 이름 정의                    (글자)



# 게임 만들기



# 안전 범위 설정               (높이: 50 ~ 300)



# 게임 시간 설정               (시간: 10 ~ 120초)



# 돌풍 리스트 만들기
#   등장 시간 리스트           (0 ~ 게임 시간)
#   x좌표 리스트               (0 ~ 900)



# 돌풍 추가하기



# 파도 리스트 만들기
#   등장 시간 리스트           (0 ~ 게임 시간)
#   방향 리스트                ("오른쪽" 또는 "왼쪽")



# 파도 추가하기



# 시작!                        (항상 마지막 줄)



# ┌─────────────────────────────────────────────────────────────┐
# │  [C] 게임 엔진  ※ 수정하지 마세요!                             │
# └─────────────────────────────────────────────────────────────┘

# 선생님 설정: 한글이 네모(□)로 보이면 글꼴 파일 경로를 넣어주세요
#   예) FONT_FILE = "Pretendard-Bold.otf"
FONT_FILE = None

GRACE_MS = 500            # 시작 직후 보호 시간
SINK_MS = 1500            # 가라앉는 시간
VERSE_MS = 700            # 말씀 한 줄 간격

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
GOLD_LIGHT = (255, 233, 120)
RED = (231, 76, 60)
SKY_BLUE = (135, 206, 235)
SKIN = (245, 222, 179)
ROBE = (139, 69, 19)
HAIR = (61, 40, 23)

VERSES = [
    ("31절", GOLD, 18, True),
    ("예수께서 즉시 손을 내밀어 베드로를 붙잡으시며 이르시되", WHITE, 16, False),
    ("믿음이 작은 자여 왜 의심하였느냐 하시고", SKY_BLUE, 18, True),
    ("32절", GOLD, 18, True),
    ("배에 함께 오르매 바람이 그치는지라", WHITE, 16, False),
    ("33절", GOLD, 18, True),
    ("배에 있는 사람들이 예수께 절하며 이르되", WHITE, 16, False),
    ("진실로 하나님의 아들이로소이다 하더라", SKY_BLUE, 18, True),
]

_fonts = {}


def _font(size, bold=False):
    key = (size, bold)
    if key not in _fonts:
        font = None
        if FONT_FILE:
            try:
                font = pygame.font.Font(FONT_FILE, size)
            except Exception:
                font = None
        if font is None:
            font = pygame.font.SysFont(
                "malgungothic,applegothic,nanumgothic,notosanscjkkr,arial",
                size, bold=bold)
        _fonts[key] = font
    return _fonts[key]


def _text(s, msg, size, color, center, bold=False):
    surf = _font(size, bold).render(msg, True, color)
    s.blit(surf, surf.get_rect(center=center))


async def _call(func, *args):
    # 웹 IDE가 함수를 자동으로 async로 바꿔도 동작하도록 처리
    result = func(*args)
    if asyncio.iscoroutine(result):
        result = await result
    return result


def _cursor(visible):
    try:
        pygame.mouse.set_visible(visible)
    except Exception:
        pass


class _Wind:
    """돌풍: 위에서 아래로 떨어짐"""
    def __init__(self, t, x):
        self.t, self.x, self.y = t, x, -40
        self.spawned = False
        self.active = False

    def update(self, elapsed):
        if not self.spawned and elapsed >= self.t:
            self.spawned = self.active = True
        if self.active:
            self.y += 6
            if self.y > H + 50:
                self.active = False

    def hits(self, mx, my):
        return self.active and abs(mx - self.x) < 15 and abs(my - (self.y - 10)) < 25

    def draw(self, s):
        if not self.active:
            return
        x, y = int(self.x), int(self.y)
        for dx in (-8, 0, 8):
            pygame.draw.line(s, (136, 136, 136), (x + dx, y - 25), (x + dx, y + 5), 2)
        pygame.draw.polygon(s, (102, 102, 102), [(x - 12, y + 5), (x + 12, y + 5), (x, y + 25)])
        pygame.draw.arc(s, (170, 170, 170), (x - 15, y - 35, 30, 20), 0, math.pi, 2)


class _Wave:
    """파도: 좌우로 이동 + 위아래로 흔들림"""
    def __init__(self, t, direction):
        self.t = t
        self.vx = 5 if direction == "오른쪽" else -5
        self.x = -50 if direction == "오른쪽" else W + 50
        self.base_y = self.y = H / 2
        self.frame = 0
        self.spawned = False
        self.active = False

    def update(self, elapsed, base_y):
        if not self.spawned and elapsed >= self.t:
            self.spawned = self.active = True
        if self.active:
            self.x += self.vx
            self.frame += 1
            self.y = base_y + math.sin(self.frame * 0.05) * 25
            if self.x < -100 or self.x > W + 100:
                self.active = False

    def hits(self, mx, my):
        return self.active and abs(mx - self.x) < 30 and abs(my - self.y) < 12

    def draw(self, s):
        if not self.active:
            return
        x, y = int(self.x), int(self.y)
        pygame.draw.ellipse(s, (78, 205, 196), (x - 30, y - 12, 60, 24))
        pygame.draw.ellipse(s, (42, 157, 143), (x - 30, y - 12, 60, 24), 2)
        for dx in (-15, 0, 15):
            pygame.draw.arc(s, WHITE, (x + dx - 8, y - 6, 16, 12), 0, math.pi, 2)
        pygame.draw.circle(s, (170, 255, 255), (x - 30, y), 5)
        pygame.draw.circle(s, (170, 255, 255), (x + 30, y), 5)


class _PeterWalk:
    def __init__(self, cfg):
        pygame.init()
        self.screen = pygame.display.set_mode((W, H))
        pygame.display.set_caption(f"{cfg.name}, 물 위를 걷다")
        self.clock = pygame.time.Clock()
        self.cfg = cfg
        self.mouse = (W // 2, H // 2)
        self.frame = 0
        self.reset()
        self.state = "ready"

    # ── 상태 초기화 ──
    def reset(self, start_y=None):
        c = self.cfg
        self.state = "playing"
        # 버튼을 누른 위치를 안전 범위 한가운데로 → 시작하자마자 죽지 않아요
        half = c.safe_height / 2
        y = H / 2 if start_y is None else start_y
        self.zone_cy = min(max(y, half + 10), H - half - 10)
        self.zone_target = self.zone_cy
        self.zone_h = float(c.safe_height)
        self.start_ms = pygame.time.get_ticks()
        self.elapsed = 0.0
        self.jesus = False
        self.jesus_pos = (W - 80, 90)
        self.winds = [_Wind(t, x) for t, x in c.winds]
        self.waves = [_Wave(t, d) for t, d in c.waves]
        self.moves = sorted(c.zone_moves)
        self.shrinks = sorted(c.zone_shrinks)
        self.blackouts = sorted(c.blackouts)
        n = c.lightning_count
        self.lightnings = [c.game_time * (i + 1) / (n + 1) for i in range(n)]
        self.used_moves = set()
        self.used_shrinks = set()
        self.used_blackouts = set()
        self.used_lightnings = set()
        self.shrink_target = None
        self.shrink_end = 0
        self.invisible_end = 0
        self.lightning_end = 0
        self.lightning_x = W // 2
        self.victory = False
        self.end_ms = 0
        self.sink_pos = None

    def zone_rect(self):
        return pygame.Rect(0, int(self.zone_cy - self.zone_h / 2), W, int(self.zone_h))

    def button_rect(self):
        # 버튼 높이 = 안전 범위 높이, 위치 = 안전 범위 한가운데
        # → 버튼을 누르는 순간 마우스가 이미 안전 범위 안에 있어요
        r = self.zone_rect()
        return pygame.Rect(W // 2 - 130, r.top, 260, r.height)

    # ── 메인 루프 ──
    async def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEMOTION:
                    self.mouse = event.pos
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = event.pos
                    await _call(self._on_click, event.pos)
            if self.state == "playing":
                await _call(self._update)
            elif self.state == "sinking" and pygame.time.get_ticks() - self.end_ms > SINK_MS:
                self.state = "over"
                self.end_ms = pygame.time.get_ticks()
            self.frame += 1
            await _call(self._draw)
            pygame.display.flip()
            self.clock.tick(60)
            await asyncio.sleep(0)     # 웹 환경 필수!
        pygame.quit()

    def _on_click(self, pos):
        if self.state == "ready" and self.button_rect().collidepoint(pos):
            self.reset(pos[1])
            _cursor(False)
        elif self.state == "over" and self._retry_ready() and self._retry_rect().collidepoint(pos):
            self.reset(pos[1])
            _cursor(False)
        elif self.state == "playing" and self.jesus:
            jx, jy = self.jesus_pos
            if (pos[0] - jx) ** 2 + (pos[1] - jy) ** 2 < 40 ** 2:
                self.victory = True
                self.state = "over"
                self.end_ms = pygame.time.get_ticks()
                _cursor(True)

    # ── 업데이트 ──
    def _update(self):
        c = self.cfg
        now = pygame.time.get_ticks()
        self.elapsed = (now - self.start_ms) / 1000
        e = self.elapsed

        if e >= c.game_time:
            self.jesus = True
            self.zone_target = self.jesus_pos[1]
        else:
            for i, (t, y) in enumerate(self.moves):
                if i not in self.used_moves and e >= t:
                    self.used_moves.add(i)
                    self.zone_target = y
            for i, (t, h) in enumerate(self.shrinks):
                if i not in self.used_shrinks and e >= t:
                    self.used_shrinks.add(i)
                    self.shrink_target = h
                    self.shrink_end = e + 3
            for i, (t, d) in enumerate(self.blackouts):
                if i not in self.used_blackouts and e >= t:
                    self.used_blackouts.add(i)
                    self.invisible_end = e + d
            for i, t in enumerate(self.lightnings):
                if i not in self.used_lightnings and e >= t:
                    self.used_lightnings.add(i)
                    self.lightning_end = e + 3

        # 범위 이동 (천천히)
        self.zone_cy += (self.zone_target - self.zone_cy) * 0.02
        # 범위 축소 → 3초 뒤 복귀
        if self.shrink_target is not None and e < self.shrink_end:
            self.zone_h += (self.shrink_target - self.zone_h) * 0.15
        else:
            self.shrink_target = None
            self.zone_h += (c.safe_height - self.zone_h) * 0.1

        for w in self.winds:
            w.update(e)
        for w in self.waves:
            w.update(e, self.zone_cy)

        if now - self.start_ms < GRACE_MS:
            return

        mx, my = self.mouse
        out = not self.zone_rect().collidepoint(W // 2, my)
        hit = any(w.hits(mx, my) for w in self.winds) or any(w.hits(mx, my) for w in self.waves)
        if out or hit:
            self.state = "sinking"
            self.sink_pos = (mx, my)
            self.end_ms = now
            _cursor(True)

    # ── 그리기 ──
    def _draw(self):
        s = self.screen
        # 바다
        for i in range(20):
            r = i / 19
            color = (int(30 - 20 * r), int(95 - 34 * r), int(138 - 46 * r))
            pygame.draw.rect(s, color, (0, i * H // 20, W, H // 20 + 1))
        for y in range(20, H, 40):
            for x in range(0, W + 60, 60):
                off = math.sin(self.frame * 0.05 + x * 0.02 + y * 0.03) * 3
                pygame.draw.ellipse(s, (58, 124, 168), (x + off - 8, y - 1, 16, 3))

        playing = self.state == "playing"
        e = self.elapsed
        lightning = playing and e < self.lightning_end
        shrinking = playing and self.shrink_target is not None

        if lightning:
            flash = (self.frame // 6) % 2 == 0
            shade = pygame.Surface((W, H), pygame.SRCALPHA)
            shade.fill((255, 255, 255, 140) if flash else (0, 0, 40, 120))
            s.blit(shade, (0, 0))
            if flash and self.frame % 12 < 3:
                if self.frame % 12 == 0:
                    self.lightning_x = random.randint(100, W - 100)
                x = self.lightning_x
                pts = [(x, 0), (x - 15, 80), (x + 10, 100), (x - 20, 180), (x + 5, 220), (x - 25, 320)]
                pygame.draw.lines(s, (255, 255, 0), False, pts, 5)
                pygame.draw.lines(s, WHITE, False, pts, 2)

        # 안전 범위
        zr = self.zone_rect()
        color = GOLD
        if shrinking and (self.frame // 8) % 2 == 0:
            color = (255, 107, 107)
        pygame.draw.line(s, color, (0, zr.top), (W, zr.top), 3)
        pygame.draw.line(s, color, (0, zr.bottom), (W, zr.bottom), 3)

        for w in self.winds:
            w.draw(s)
        for w in self.waves:
            w.draw(s)

        if self.jesus:
            self._draw_jesus(s)

        if playing:
            if e >= self.invisible_end:
                self._draw_peter(s, *self.mouse)
            else:
                _text(s, "베드로가 보이지 않아요... 흔들리지 마세요!", 15, (255, 170, 170), (W // 2, 62))
        elif self.state == "sinking":
            self._draw_sinking(s)

        if playing:
            if self.jesus:
                _text(s, "예수님께 가세요!", 20, GOLD, (W // 2, 28), True)
            else:
                remain = max(0, self.cfg.game_time - e)
                _text(s, f"남은 시간  {remain:.1f}초", 20, WHITE, (W // 2, 28), True)
            if pygame.time.get_ticks() - self.start_ms < GRACE_MS:
                _text(s, "준비하세요...", 24, WHITE, (W // 2, zr.top - 30), True)

        if self.state == "ready":
            self._draw_ready(s)
        elif self.state == "over":
            self._draw_over(s)

    def _draw_peter(self, s, x, y):
        pygame.draw.ellipse(s, (20, 40, 60), (x - 16, y + 18, 32, 6))
        pygame.draw.ellipse(s, ROBE, (x - 14, y - 4, 28, 26))
        pygame.draw.circle(s, SKIN, (x, y - 12), 10)
        pygame.draw.arc(s, HAIR, (x - 10, y - 22, 20, 14), 0, math.pi, 4)
        pygame.draw.circle(s, BLACK, (x - 4, y - 13), 2)
        pygame.draw.circle(s, BLACK, (x + 4, y - 13), 2)

    def _draw_jesus(self, s):
        x, y = self.jesus_pos
        glow = pygame.Surface((120, 120), pygame.SRCALPHA)
        pygame.draw.circle(glow, (255, 230, 120, 70), (60, 60), 55)
        s.blit(glow, (x - 60, y - 60))
        pygame.draw.ellipse(s, WHITE, (x - 18, y - 5, 36, 35))
        pygame.draw.circle(s, SKIN, (x, y - 14), 11)
        pygame.draw.ellipse(s, GOLD, (x - 15, y - 34, 30, 8), 2)
        if self.state == "playing":
            size = 14 + int((math.sin(self.frame * 0.15) + 1) * 2)
            _text(s, "클릭하세요!", size, GOLD, (x - 10, y + 50), True)

    def _draw_sinking(self, s):
        t = (pygame.time.get_ticks() - self.end_ms) / SINK_MS
        x, y = self.sink_pos
        y = int(y + t * 90)
        if t < 0.8:
            self._draw_peter(s, x, y)
            cover = pygame.Surface((40, 50), pygame.SRCALPHA)
            cover.fill((30, 95, 138, int(255 * min(1, t * 1.3))))
            s.blit(cover, (x - 20, y - 25))
        for _ in range(4):
            pygame.draw.circle(s, (170, 204, 238),
                               (x + random.randint(-20, 20), y + random.randint(-12, 12)), 3)

    def _dim(self, s, alpha, keep_zone=False):
        shade = pygame.Surface((W, H), pygame.SRCALPHA)
        shade.fill((0, 0, 0, alpha))
        if keep_zone:
            shade.fill((0, 0, 0, 0), self.zone_rect())
        s.blit(shade, (0, 0))

    def _draw_button(self, s, rect, label):
        hover = rect.collidepoint(self.mouse)
        pygame.draw.rect(s, GOLD_LIGHT if hover else GOLD, rect, border_radius=12)
        pygame.draw.rect(s, (160, 120, 0), rect, 3, border_radius=12)
        _text(s, label, 22, BLACK, rect.center, True)

    def _draw_ready(self, s):
        self._dim(s, 150, keep_zone=True)
        zr = self.zone_rect()
        _text(s, f"{self.cfg.name}, 물 위를 걷다", 32, GOLD, (W // 2, zr.top - 110), True)
        _text(s, "마우스로 베드로를 노란 범위 안에 두세요. 벗어나면 가라앉아요!", 16, WHITE, (W // 2, zr.top - 65))
        _text(s, f"{self.cfg.game_time}초를 버티면 예수님이 나타나요", 16, WHITE, (W // 2, zr.top - 38))
        self._draw_button(s, self.button_rect(), "시작하기")

    def _retry_rect(self):
        if self.victory:
            return pygame.Rect(W // 2 - 110, H - 75, 220, 50)
        return self.button_rect()

    def _retry_ready(self):
        if not self.victory:
            return True
        shown = (pygame.time.get_ticks() - self.end_ms) // VERSE_MS
        return shown >= len(VERSES) + 1

    def _draw_over(self, s):
        if self.victory:
            self._dim(s, 200)
            _text(s, "예수님께 도달했어요!", 30, GOLD, (W // 2, 60), True)
            _text(s, "마태복음 14장 31-33절", 18, GOLD, (W // 2, 100), True)
            shown = (pygame.time.get_ticks() - self.end_ms) // VERSE_MS
            y = 150
            for text, color, size, bold in VERSES[:shown]:
                _text(s, text, size, color, (W // 2, y), bold)
                y += 44 if text.endswith("절") else 36 if bold else 32
        else:
            self._dim(s, 170, keep_zone=True)
            zr = self.zone_rect()
            if zr.top > 120:      # 범위 위쪽에 글자 공간이 있으면 위에
                y1, y2, y3 = zr.top - 75, zr.top - 35, zr.bottom + 30
            else:                 # 범위가 화면 위쪽에 붙어 있으면 아래에
                y1, y2, y3 = zr.bottom + 50, zr.bottom + 90, zr.bottom + 125
            _text(s, "마음이 흔들렸습니다", 30, RED, (W // 2, y1), True)
            _text(s, "믿음이 작은 자여 왜 의심하였느냐  (마태복음 14:31)", 16, (220, 220, 220), (W // 2, y2))
            _text(s, "버튼을 누르면 그 자리에서 다시 시작해요", 14, (180, 180, 180), (W // 2, y3))
        if self._retry_ready():
            self._draw_button(s, self._retry_rect(), "다시하기")


# ┌─────────────────────────────────────────────────────────────┐
# │  [D] 실행  ※ 수정하지 마세요!                                  │
# └─────────────────────────────────────────────────────────────┘

async def _실행():
    준비된_게임 = [g for g in _만든_게임들 if g.started]
    if not 준비된_게임:
        print("⚠️ 게임이 시작되지 않았어요. [B] 맨 마지막 줄에 game.start() 가 있는지 확인해 주세요!")
        return
    await _PeterWalk(준비된_게임[-1]).run()

asyncio.run(_실행())
