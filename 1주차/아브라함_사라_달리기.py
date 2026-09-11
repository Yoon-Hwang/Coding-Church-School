"""
🏁 캐릭터 입장 레이스
=====================
두 캐릭터가 랜덤 속도로 달려 결승선(하늘색 선)에 먼저 도착하는 사람이 승리!
"""

import pygame
import random
import asyncio


# ═══════════════════════════════════════════════════════════════
#  🎯 [1] 캐릭터 이름 설정
# ═══════════════════════════════════════════════════════════════

player1 = "아브라함"
player2 = "사라"


# ═══════════════════════════════════════════════════════════════
#  🎨 [2] 캐릭터 이미지 (없으면 None으로!)
# ═══════════════════════════════════════════════════════════════

player1_image = None   # 예) "abraham.png"
player2_image = None   # 예) "sarah.png"


# ═══════════════════════════════════════════════════════════════
#  📍 [3] 캐릭터 시작 위치 (좌우 위치를 조절해요!)
# ═══════════════════════════════════════════════════════════════
#
#  💡 x좌표: 화면 좌우 위치 (0 ~ 500, 가운데는 250)
#     y좌표: 화면 위아래 위치 (작을수록 위쪽)
#
# ───────────────────────────────────────────────────────────────

player1_x = 195   # 아브라함 왼쪽
player1_y = 80    # 상단

player2_x = 305   # 사라 오른쪽
player2_y = 80    # 상단


# ═══════════════════════════════════════════════════════════════
#  ⚡ [4] 캐릭터 속력 설정
# ═══════════════════════════════════════════════════════════════
#
#  💡 속력을 직접 정하면 그 속도로 달려요!
#     None으로 두면 랜덤 속도가 부여돼요 (0.5 ~ 2.5)
#
#  예시) player1_speed = 2.0   ← 직접 지정
#       player1_speed = None  ← 랜덤
#
# ───────────────────────────────────────────────────────────────

player1_speed = None    # 아브라함 속력 (None = 랜덤)
player2_speed = None    # 사라 속력 (None = 랜덤)


# ═══════════════════════════════════════════════════════════════
#  🎨 [5] 캐릭터 색상 (이미지 없을 때)
# ═══════════════════════════════════════════════════════════════

player1_color = (230, 80, 90)      # 빨강 (R, G, B)
player2_color = (80, 130, 220)     # 파랑


# ═══════════════════════════════════════════════════════════════
#  🖥️ 게임 화면 설정 (수정 필요 없음)
# ═══════════════════════════════════════════════════════════════

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
FPS = 60

COLOR_BG_TOP = (255, 235, 200)
COLOR_BG_MID = (245, 220, 130)
COLOR_BG_SIDE = (140, 200, 130)
COLOR_FINISH = (100, 200, 240)
COLOR_TEXT = (40, 40, 40)
COLOR_WHITE = (255, 255, 255)
COLOR_GOLD = (255, 200, 40)

CHAR_SIZE = 50
FINISH_Y = SCREEN_HEIGHT - 100


# ═══════════════════════════════════════════════════════════════
#  캐릭터 클래스
# ═══════════════════════════════════════════════════════════════

class Character:
    def __init__(self, name, x, y, color, speed, image_path=None):
        self.name = name
        self.x = x
        self.y = y
        self.start_y = y
        self.color = color
        
        # 속력 설정 (None이면 랜덤)
        if speed is None:
            self.speed = random.uniform(0.5, 2.5)
        else:
            self.speed = speed
        
        self.finished = False
        self.finish_time = 0
        
        # 이미지 로드
        self.image = None
        if image_path:
            try:
                img = pygame.image.load(image_path)
                self.image = pygame.transform.scale(img, (CHAR_SIZE, CHAR_SIZE))
            except Exception as e:
                print(f"⚠️ 이미지 로드 실패 ({image_path}): {e}")
                print(f"   → 기본 캐릭터로 대체합니다.")
    
    def update(self):
        if not self.finished:
            self.y += self.speed
            if self.y + CHAR_SIZE//2 >= FINISH_Y:
                self.y = FINISH_Y - CHAR_SIZE//2
                self.finished = True
                self.finish_time = pygame.time.get_ticks()
    
    def draw(self, screen):
        if self.image:
            rect = self.image.get_rect(center=(self.x, self.y))
            screen.blit(self.image, rect)
        else:
            self._draw_default_character(screen)
        
        # 이름 표시
        font = pygame.font.SysFont("malgungothic", 18, bold=True)
        text = font.render(self.name, True, COLOR_TEXT)
        text_rect = text.get_rect(center=(self.x, self.y - CHAR_SIZE//2 - 15))
        bg_rect = text_rect.inflate(10, 4)
        pygame.draw.rect(screen, COLOR_WHITE, bg_rect, border_radius=4)
        pygame.draw.rect(screen, self.color, bg_rect, 2, border_radius=4)
        screen.blit(text, text_rect)
    
    def _draw_default_character(self, screen):
        cx, cy = int(self.x), int(self.y)
        pygame.draw.ellipse(screen, (0, 0, 0, 80),
                            (cx - 20, cy + 20, 40, 8))
        pygame.draw.rect(screen, self.color,
                         (cx - 18, cy - 5, 36, 30), border_radius=4)
        pygame.draw.circle(screen, (245, 220, 180), (cx, cy - 15), 14)
        pygame.draw.circle(screen, (100, 70, 50), (cx, cy - 15), 14, 2)
        pygame.draw.arc(screen, (80, 50, 30),
                        (cx - 14, cy - 30, 28, 20),
                        0, 3.14, 6)
        pygame.draw.circle(screen, (0, 0, 0), (cx - 5, cy - 15), 2)
        pygame.draw.circle(screen, (0, 0, 0), (cx + 5, cy - 15), 2)


# ═══════════════════════════════════════════════════════════════
#  게임 클래스
# ═══════════════════════════════════════════════════════════════

class RaceGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(f"🏁 {player1} vs {player2} 레이스")
        self.clock = pygame.time.Clock()
        
        # 캐릭터 생성 (위에서 지정한 변수들 사용!)
        self.p1 = Character(player1, player1_x, player1_y,
                            player1_color, player1_speed, player1_image)
        self.p2 = Character(player2, player2_x, player2_y,
                            player2_color, player2_speed, player2_image)
        
        self.winner = None
        self.game_over = False
        self.countdown_start = pygame.time.get_ticks()
        self.started = False
        
        print(f"\n🏁 레이스 시작!")
        print(f"   {player1} 위치: ({player1_x}, {player1_y}), 속도: {self.p1.speed:.2f}")
        print(f"   {player2} 위치: ({player2_x}, {player2_y}), 속도: {self.p2.speed:.2f}")
    
    async def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and self.game_over:
                        self._reset()
            
            self._update()
            self._draw()
            
            pygame.display.flip()
            self.clock.tick(FPS)
            
            await asyncio.sleep(0)
        
        pygame.quit()
    
    def _update(self):
        if not self.started:
            elapsed = (pygame.time.get_ticks() - self.countdown_start) / 1000
            if 3 - int(elapsed) <= 0:
                self.started = True
            return
        
        if self.game_over:
            return
        
        self.p1.update()
        self.p2.update()
        
        # 승자 결정
        if self.p1.finished and self.p2.finished and self.winner is None:
            if self.p1.finish_time < self.p2.finish_time:
                self.winner = self.p1
            elif self.p2.finish_time < self.p1.finish_time:
                self.winner = self.p2
            else:
                self.winner = "무승부"
            self.game_over = True
        elif self.p1.finished and not self.winner:
            self.winner = self.p1
            self.game_over = True
        elif self.p2.finished and not self.winner:
            self.winner = self.p2
            self.game_over = True
    
    def _draw(self):
        self._draw_track()
        self._draw_finish_line()
        self.p1.draw(self.screen)
        self.p2.draw(self.screen)
        
        if not self.started:
            self._draw_countdown()
        elif self.game_over:
            self._draw_winner()
    
    def _draw_track(self):
        self.screen.fill(COLOR_BG_SIDE)
        track_x = SCREEN_WIDTH // 2 - 110
        track_w = 220
        pygame.draw.rect(self.screen, COLOR_BG_MID,
                         (track_x, 0, track_w, SCREEN_HEIGHT))
        pygame.draw.rect(self.screen, (80, 140, 70),
                         (track_x, 0, track_w, SCREEN_HEIGHT), 3)
        pygame.draw.ellipse(self.screen, COLOR_BG_TOP,
                            (track_x + 20, 0, track_w - 40, 100))
        door_w = 50
        door_h = 60
        door_x = SCREEN_WIDTH // 2 - door_w // 2
        pygame.draw.rect(self.screen, (140, 100, 70),
                         (door_x, 20, door_w, door_h),
                         border_radius=10)
        pygame.draw.circle(self.screen, (200, 170, 100),
                           (door_x + door_w - 8, 20 + door_h // 2), 3)
    
    def _draw_finish_line(self):
        pygame.draw.rect(self.screen, COLOR_FINISH,
                         (SCREEN_WIDTH // 2 - 110, FINISH_Y, 220, 15))
        pygame.draw.rect(self.screen, (60, 150, 200),
                         (SCREEN_WIDTH // 2 - 110, FINISH_Y, 220, 15), 2)
        font = pygame.font.SysFont("arial", 16, bold=True)
        text = font.render("FINISH", True, COLOR_WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, FINISH_Y + 7))
        self.screen.blit(text, text_rect)
    
    def _draw_countdown(self):
        elapsed = (pygame.time.get_ticks() - self.countdown_start) / 1000
        remaining = 3 - int(elapsed)
        
        if remaining > 0:
            text = str(remaining)
            color = player1_color if remaining == 1 else COLOR_TEXT
        else:
            text = "GO!"
            color = (50, 200, 80)
        
        font = pygame.font.SysFont("arial", 120, bold=True)
        rendered = font.render(text, True, color)
        rect = rendered.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        
        s = pygame.Surface((200, 200), pygame.SRCALPHA)
        s.fill((255, 255, 255, 180))
        self.screen.blit(s, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 100))
        self.screen.blit(rendered, rect)
    
    def _draw_winner(self):
        s = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        s.fill((0, 0, 0, 150))
        self.screen.blit(s, (0, 0))
        
        box_w, box_h = 400, 200
        box_x = (SCREEN_WIDTH - box_w) // 2
        box_y = (SCREEN_HEIGHT - box_h) // 2
        
        pygame.draw.rect(self.screen, COLOR_WHITE,
                         (box_x, box_y, box_w, box_h),
                         border_radius=15)
        pygame.draw.rect(self.screen, COLOR_GOLD,
                         (box_x, box_y, box_w, box_h),
                         5, border_radius=15)
        
        if self.winner == "무승부":
            title_text = "무승부!"
            winner_msg = f"{player1}, {player2} 동시 도착!"
            title_color = COLOR_TEXT
        else:
            title_text = "🏆 승리! 🏆"
            winner_msg = f"{self.winner.name} 승리!"
            title_color = COLOR_GOLD
        
        font_title = pygame.font.SysFont("malgungothic", 32, bold=True)
        title_rendered = font_title.render(title_text, True, title_color)
        title_rect = title_rendered.get_rect(center=(SCREEN_WIDTH // 2, box_y + 60))
        self.screen.blit(title_rendered, title_rect)
        
        font_winner = pygame.font.SysFont("malgungothic", 28, bold=True)
        winner_rendered = font_winner.render(winner_msg, True, COLOR_TEXT)
        winner_rect = winner_rendered.get_rect(center=(SCREEN_WIDTH // 2, box_y + 110))
        self.screen.blit(winner_rendered, winner_rect)
        
        font_hint = pygame.font.SysFont("malgungothic", 14)
        hint_rendered = font_hint.render("R 키를 눌러 다시 시작", True, (100, 100, 100))
        hint_rect = hint_rendered.get_rect(center=(SCREEN_WIDTH // 2, box_y + 160))
        self.screen.blit(hint_rendered, hint_rect)
    
    def _reset(self):
        self.p1 = Character(player1, player1_x, player1_y,
                            player1_color, player1_speed, player1_image)
        self.p2 = Character(player2, player2_x, player2_y,
                            player2_color, player2_speed, player2_image)
        self.winner = None
        self.game_over = False
        self.countdown_start = pygame.time.get_ticks()
        self.started = False
        
        print(f"\n🔄 재시작!")
        print(f"   {player1} 속도: {self.p1.speed:.2f}")
        print(f"   {player2} 속도: {self.p2.speed:.2f}")


# ═══════════════════════════════════════════════════════════════
#  실행!
# ═══════════════════════════════════════════════════════════════

async def main():
    game = RaceGame()
    await game.run()

asyncio.run(main())