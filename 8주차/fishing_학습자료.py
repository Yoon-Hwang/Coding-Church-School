# ═══════════════════════════════════════════════════════════════
#  🎣 베드로의 그물 낚시 게임 (웹 버전, 한 파일)
# ═══════════════════════════════════════════════════════════════
#  조작법:  ← → 배 이동  |  Space 그물 던지기 / 한 번 더 누르면 회수
#  📖 누가복음 5:1-11
# ═══════════════════════════════════════════════════════════════

import pygame
import random
import asyncio


# ┌─────────────────────────────────────────────────────────────┐
# │  [A] 준비 코드  ※ 수정하지 마세요! 아래 [B]로 내려가세요       │
# └─────────────────────────────────────────────────────────────┘

_만든_게임들 = []


def _check_range(value, low, high):
    return isinstance(value, (int, float)) and low <= value <= high


class _GameSettings:
    def __init__(self, name, game_time):
        self.name = name
        self.game_time = game_time
        self.boat_speed = 15
        self.net_speed = 10
        self.net_size = 40
        self.zones = []
        self.started = False

    def set_boat(self, 속도=15):
        if not _check_range(속도, 5, 30):
            print(f"⚠️ 배 속도는 5~30 사이여야 해요 (입력값: {속도}) → 기본값 15로 설정")
            속도 = 15
        self.boat_speed = 속도
        return self

    def set_net(self, 속도=10, 크기=40):
        if not _check_range(속도, 3, 20):
            print(f"⚠️ 그물 속도는 3~20 사이여야 해요 (입력값: {속도}) → 기본값 10으로 설정")
            속도 = 10
        if not _check_range(크기, 20, 80):
            print(f"⚠️ 그물 크기는 20~80 사이여야 해요 (입력값: {크기}) → 기본값 40으로 설정")
            크기 = 40
        self.net_speed = 속도
        self.net_size = int(크기)
        return self

    def add_fish_zone(self, 구간_번호, 색상, 속도, 생성_확률):
        if not _check_range(속도, 1, 15):
            print(f"⚠️ 구간 {구간_번호}: 속도는 1~15 사이여야 해요 (입력값: {속도}) → 이 구간은 만들지 않아요")
            return self
        if not _check_range(생성_확률, 0.01, 0.15):
            print(f"⚠️ 구간 {구간_번호}: 생성_확률은 0.01~0.15 사이여야 해요 (입력값: {생성_확률}) → 이 구간은 만들지 않아요")
            return self
        try:
            pygame.Color(색상)
        except (ValueError, TypeError):
            print(f"⚠️ 구간 {구간_번호}: '{색상}' 은(는) 알 수 없는 색이에요 → 이 구간은 만들지 않아요")
            return self
        self.zones.append({"번호": 구간_번호, "색상": 색상, "속도": 속도, "확률": 생성_확률})
        return self

    def start(self):
        if not self.zones:
            print("⚠️ 물고기 구간이 하나도 없어요! game.add_fish_zone(...) 으로 추가해 주세요.")
            return
        self.started = True


def create_game(이름="베드로", 시간=30):
    if not isinstance(이름, str) or not 이름.strip():
        print("⚠️ 이름은 글자(문자열)여야 해요 → '베드로'로 설정")
        이름 = "베드로"
    if not _check_range(시간, 10, 120):
        print(f"⚠️ 시간은 10~120초 사이여야 해요 (입력값: {시간}) → 기본값 30초로 설정")
        시간 = 30
    game = _GameSettings(이름, int(시간))
    _만든_게임들.append(game)
    return game


class fishing_engine:
    # fishing_engine.create_game(...) 처럼 써도 되게 (import 는 쓰지 않아요)
    create_game = staticmethod(create_game)


# ┌─────────────────────────────────────────────────────────────┐
# │  [B] 🧑‍💻 학생이 작성하는 부분                                  │
# └─────────────────────────────────────────────────────────────┘

'''
색상_리스트 = [
    "red",        # 🔴 빨강
    "orange",     # 🟠 주황
    "yellow",     # 🟡 노랑
    "green",      # 🟢 초록
    "blue",       # 🔵 파랑
    "purple",     # 🟣 보라
    "pink",       # 🌸 분홍
    "cyan",       # 🩵 청록
    "magenta",    # 💗 자홍
    "gold",       # ✨ 금색
]
'''


# step 1  색상 리스트          (위 색 이름 중에서 골라요)



# step 2  속력 리스트          (1 ~ 15)



# step 3  확률 리스트          (0.01 ~ 0.15)



# 이름 / 게임 시간 정의        (이름: 글자,  게임 시간: 10 ~ 120초)



# 게임 설정



# 배 설정                      (속도: 5 ~ 30)



# 그물 설정                    (속도: 3 ~ 20,  크기: 20 ~ 80)



# 물고기 추가



# 시작!                        (항상 마지막 줄)



# ┌─────────────────────────────────────────────────────────────┐
# │  [C] 게임 엔진  ※ 수정하지 마세요!                             │
# └─────────────────────────────────────────────────────────────┘

# 선생님 설정: 한글이 네모(□)로 보이면 글꼴 파일 경로를 넣어주세요
#   예) FONT_FILE = "Pretendard-Bold.otf"
FONT_FILE = None

W, H = 800, 600
FPS = 60
SEA_Y = 150                 # 수면 높이
ZONE_TOP = SEA_Y + 30       # 물고기가 다니는 영역 위쪽
ZONE_BOTTOM = H - 20        # 물고기가 다니는 영역 아래쪽
FRAME_SCALE = 0.55          # 예전 turtle 버전과 같은 체감 속도로 맞추는 값

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY = (135, 206, 235)
GOLD = (255, 215, 0)
SKY_BLUE = (135, 206, 250)
RED = (230, 70, 70)

VERSES = [
    ("누가복음 5장 9-11절", GOLD, 22, True),
    ("9절", GOLD, 16, True),
    ("이는 자기 및 자기와 함께 있는 모든 사람이 고기 잡힌 것으로 말미암아 놀라고", WHITE, 15, False),
    ("10절", GOLD, 16, True),
    ("세베대의 아들로서 시몬의 동업자인 야고보와 요한도 놀랐음이라", WHITE, 15, False),
    ("예수께서 시몬에게 이르시되", WHITE, 15, False),
    ("무서워하지 말라 이제 후로는 네가 사람을 취하리라 하시니", SKY_BLUE, 17, True),
    ("11절", GOLD, 16, True),
    ("그들이 배들을 육지에 대고 모든 것을 버려 두고", WHITE, 15, False),
    ("예수를 따르니라", SKY_BLUE, 18, True),
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


def _text(screen, msg, size, color, center=None, topleft=None, topright=None, bold=False):
    surf = _font(size, bold).render(msg, True, color)
    if center:
        rect = surf.get_rect(center=center)
    elif topright:
        rect = surf.get_rect(topright=topright)
    else:
        rect = surf.get_rect(topleft=topleft)
    screen.blit(surf, rect)


def _zone_color(i, count):
    ratio = 0 if count <= 1 else i / (count - 1)
    return (int(30 - 20 * ratio), int(144 - 83 * ratio), int(255 - 148 * ratio))


async def _call(func, *args):
    # 웹 IDE가 함수를 자동으로 async로 바꿔도 동작하도록 처리
    result = func(*args)
    if asyncio.iscoroutine(result):
        result = await result
    return result


class _Boat:
    def __init__(self, speed):
        self.x = W // 2
        self.y = SEA_Y
        self.speed = speed * 0.4

    def move(self, direction):
        self.x = max(60, min(W - 60, self.x + direction * self.speed))

    def draw(self, s):
        x, y = int(self.x), self.y
        # 배
        hull = [(x - 50, y - 14), (x + 50, y - 14), (x + 38, y + 12), (x - 38, y + 12)]
        pygame.draw.polygon(s, (139, 69, 19), hull)
        pygame.draw.polygon(s, (93, 46, 12), hull, 2)
        pygame.draw.line(s, (107, 62, 29), (x - 46, y - 8), (x + 46, y - 8), 2)
        # 돛대 + 돛
        pygame.draw.line(s, (74, 44, 13), (x + 8, y - 14), (x + 8, y - 90), 4)
        sail = [(x + 12, y - 86), (x + 50, y - 30), (x + 12, y - 30)]
        pygame.draw.polygon(s, (245, 245, 220), sail)
        pygame.draw.polygon(s, (139, 115, 85), sail, 2)
        # 베드로
        px = x - 24
        robe = [(px - 9, y - 14), (px + 9, y - 14), (px + 6, y - 40), (px - 6, y - 40)]
        pygame.draw.polygon(s, (160, 82, 45), robe)
        pygame.draw.line(s, (160, 82, 45), (px + 5, y - 34), (px + 17, y - 46), 4)
        pygame.draw.circle(s, (245, 222, 179), (px, y - 48), 8)
        pygame.draw.ellipse(s, (61, 40, 23), (px - 8, y - 57, 16, 8))
        pygame.draw.circle(s, BLACK, (px + 3, y - 48), 1)


class _Net:
    def __init__(self, x, speed, size):
        self.x = x
        self.start_y = SEA_Y + 12
        self.y = self.start_y
        self.w = size
        self.h = size + 10
        self.speed = speed * FRAME_SCALE
        self.going_down = True
        self.active = True

    @property
    def rect(self):
        return pygame.Rect(int(self.x - self.w / 2), int(self.y), self.w, self.h)

    def pull_back(self):
        self.going_down = False

    def update(self):
        if self.going_down:
            self.y += self.speed
            if self.y + self.h >= H - 5:      # 바닥에 닿으면 자동 회수
                self.going_down = False
        else:
            self.y -= self.speed
            if self.y <= self.start_y:
                self.active = False

    def draw(self, s):
        r = self.rect
        pygame.draw.line(s, (90, 70, 50), (int(self.x), self.start_y), (int(self.x), r.top), 2)
        mesh = pygame.Surface((r.w, r.h), pygame.SRCALPHA)
        mesh.fill((220, 220, 220, 70))
        line = (70, 70, 70) if self.going_down else (170, 170, 170)
        for gx in range(0, r.w, 8):
            pygame.draw.line(mesh, line, (gx, 0), (gx, r.h), 1)
        for gy in range(0, r.h, 8):
            pygame.draw.line(mesh, line, (0, gy), (r.w, gy), 1)
        s.blit(mesh, r.topleft)
        pygame.draw.rect(s, line, r, 2)


class _Fish:
    def __init__(self, zone_pos, zone_count, color, speed):
        direction = random.choice([-1, 1])
        self.x = -30 if direction == 1 else W + 30
        self.vx = direction * speed * FRAME_SCALE
        band = (ZONE_BOTTOM - ZONE_TOP) / zone_count
        top = ZONE_TOP + zone_pos * band
        self.y = random.uniform(top + 12, top + band - 12)
        c = pygame.Color(color)
        self.color = (c.r, c.g, c.b)
        self.dark = (int(c.r * 0.6), int(c.g * 0.6), int(c.b * 0.6))
        self.active = True

    @property
    def rect(self):
        return pygame.Rect(int(self.x - 20), int(self.y - 9), 40, 18)

    def update(self):
        self.x += self.vx
        if self.x < -60 or self.x > W + 60:
            self.active = False

    def draw(self, s):
        x, y = int(self.x), int(self.y)
        d = 1 if self.vx > 0 else -1
        tail = x - d * 18
        pygame.draw.polygon(s, self.dark, [(tail + d * 4, y), (tail - d * 12, y - 10), (tail - d * 12, y + 10)])
        pygame.draw.ellipse(s, self.color, (x - 22, y - 10, 44, 20))
        pygame.draw.ellipse(s, self.dark, (x - 22, y - 10, 44, 20), 2)
        eye = x + d * 11
        pygame.draw.circle(s, WHITE, (eye, y - 3), 4)
        pygame.draw.circle(s, BLACK, (eye + d, y - 3), 2)


class _FishingGame:
    def __init__(self, settings):
        pygame.init()
        self.screen = pygame.display.set_mode((W, H))
        pygame.display.set_caption(f"{settings.name}의 그물 낚시")
        self.clock = pygame.time.Clock()
        self.s = settings
        self.zones = sorted(settings.zones, key=lambda z: z["번호"])
        self.reset()

    def reset(self):
        self.state = "ready"          # ready → playing → over
        self.boat = _Boat(self.s.boat_speed)
        self.net = None
        self.fishes = []
        self.popups = []              # [x, y, 남은 프레임]
        self.score = 0
        self.time_up = False
        self.buzzer = False
        self.start_ms = 0
        self.over_ms = 0
        self.wave_t = 0
        self.left_held = False
        self.right_held = False

    # ── 메인 루프 ──
    async def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.left_held = True
                    elif event.key == pygame.K_RIGHT:
                        self.right_held = True
                    await _call(self._on_key, event.key)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.left_held = False
                    elif event.key == pygame.K_RIGHT:
                        self.right_held = False
                elif event.type == pygame.MOUSEBUTTONDOWN and self.state == "ready":
                    await _call(self._begin)
            if self.state == "playing":
                await _call(self._update)
            self.wave_t += 1
            await _call(self._draw)
            pygame.display.flip()
            self.clock.tick(FPS)
            await asyncio.sleep(0)     # 웹 환경 필수!
        pygame.quit()

    def _begin(self):
        self.state = "playing"
        self.start_ms = pygame.time.get_ticks()

    def _on_key(self, key):
        if self.state == "ready" and key == pygame.K_SPACE:
            self._begin()
        elif self.state == "playing" and key == pygame.K_SPACE:
            if self.net is None:
                if not self.time_up:
                    self.net = _Net(self.boat.x, self.s.net_speed, self.s.net_size)
            elif self.net.going_down:
                self.net.pull_back()
        elif self.state == "over" and key == pygame.K_r:
            self.reset()

    # ── 업데이트 ──
    def _remaining(self):
        elapsed = (pygame.time.get_ticks() - self.start_ms) / 1000
        return max(0, self.s.game_time - elapsed)

    def _update(self):
        # 배 이동 (그물이 나가 있으면 못 움직임)
        if self.net is None:
            if self.left_held:
                self.boat.move(-1)
            if self.right_held:
                self.boat.move(1)

        # 물고기 생성 (구간마다 따로)
        if not self.time_up:
            for pos, zone in enumerate(self.zones):
                if random.random() < zone["확률"] * FRAME_SCALE:
                    self.fishes.append(_Fish(pos, len(self.zones), zone["색상"], zone["속도"]))

        for fish in self.fishes:
            fish.update()

        # 그물: 내려갈 때도, 올라올 때도 잡힘
        if self.net:
            self.net.update()
            net_rect = self.net.rect
            for fish in self.fishes:
                if fish.active and net_rect.colliderect(fish.rect):
                    fish.active = False
                    self.score += 1
                    self.popups.append([fish.x, fish.y, 40])
            if not self.net.active:
                self.net = None

        self.fishes = [f for f in self.fishes if f.active]
        for p in self.popups:
            p[1] -= 1
            p[2] -= 1
        self.popups = [p for p in self.popups if p[2] > 0]

        # 시간 종료 + 버저비터
        if not self.time_up and self._remaining() <= 0:
            self.time_up = True
            if self.net is None:
                self._finish()
            else:
                self.buzzer = True
        elif self.buzzer and self.net is None:
            self._finish()

    def _finish(self):
        self.state = "over"
        self.over_ms = pygame.time.get_ticks()

    # ── 그리기 ──
    def _draw(self):
        s = self.screen
        s.fill(SKY)
        pygame.draw.circle(s, (255, 223, 90), (560, 60), 28)

        # 바다 (구간별 색)
        count = max(1, len(self.zones))
        band = (ZONE_BOTTOM - ZONE_TOP) / count
        pygame.draw.rect(s, _zone_color(0, count), (0, SEA_Y, W, ZONE_TOP - SEA_Y + 1))
        for i in range(count):
            top = int(ZONE_TOP + i * band)
            pygame.draw.rect(s, _zone_color(i, count), (0, top, W, int(band) + 2))
        pygame.draw.rect(s, _zone_color(count - 1, count), (0, ZONE_BOTTOM, W, H - ZONE_BOTTOM))
        for x in range(-40, W + 40, 40):
            offset = (self.wave_t // 3) % 40
            pygame.draw.arc(s, WHITE, (x + offset, SEA_Y - 5, 40, 12), 0, 3.14, 2)

        for fish in self.fishes:
            fish.draw(s)
        if self.net:
            self.net.draw(s)
        self.boat.draw(s)

        for x, y, life in self.popups:
            _text(s, "+1", 20, GOLD, center=(int(x), int(y) - 15), bold=True)

        # 시간 / 점수
        if self.state == "playing":
            if self.buzzer:
                _text(s, "버저비터! 그물 회수 중", 20, RED, topleft=(20, 15), bold=True)
            else:
                _text(s, f"남은 시간: {int(self._remaining())}초", 20, BLACK, topleft=(20, 15), bold=True)
            _text(s, f"잡은 물고기: {self.score}마리", 20, BLACK, topright=(W - 20, 15), bold=True)

        if self.state == "ready":
            self._draw_overlay(150)
            _text(s, f"{self.s.name}의 그물 낚시", 36, GOLD, center=(W // 2, 220), bold=True)
            _text(s, "← → : 배 이동     Space : 그물 던지기 / 회수", 18, WHITE, center=(W // 2, 280))
            _text(s, f"제한 시간 {self.s.game_time}초", 18, WHITE, center=(W // 2, 315))
            _text(s, "스페이스바를 누르거나 화면을 클릭하면 시작!", 20, SKY_BLUE, center=(W // 2, 380), bold=True)
        elif self.state == "over":
            self._draw_ending()

    def _draw_overlay(self, alpha):
        shade = pygame.Surface((W, H), pygame.SRCALPHA)
        shade.fill((0, 0, 0, alpha))
        self.screen.blit(shade, (0, 0))

    def _draw_ending(self):
        s = self.screen
        self._draw_overlay(190)
        _text(s, "게임 종료!", 34, GOLD, center=(W // 2, 60), bold=True)
        _text(s, f"총 {self.score}마리를 잡았어요!", 24, WHITE, center=(W // 2, 105), bold=True)

        # 말씀을 0.7초마다 한 줄씩
        elapsed = pygame.time.get_ticks() - self.over_ms - 1200
        shown = 0 if elapsed < 0 else min(len(VERSES), elapsed // 700 + 1)
        y = 165
        for text, color, size, bold in VERSES[:shown]:
            _text(s, text, size, color, center=(W // 2, y), bold=bold)
            y += 34 if text.endswith("절") or text.startswith("누가") else 30

        if shown == len(VERSES):
            _text(s, "R 키를 누르면 다시 시작해요", 16, (200, 200, 200), center=(W // 2, H - 30))


# ┌─────────────────────────────────────────────────────────────┐
# │  [D] 실행  ※ 수정하지 마세요!                                  │
# └─────────────────────────────────────────────────────────────┘

async def _실행():
    준비된_게임 = [g for g in _만든_게임들 if g.started]
    if not 준비된_게임:
        print("⚠️ 게임이 시작되지 않았어요. [B] 에 game.start() 를 마지막 줄에 썼는지 확인해 주세요!")
        return
    await _FishingGame(준비된_게임[-1]).run()

asyncio.run(_실행())
