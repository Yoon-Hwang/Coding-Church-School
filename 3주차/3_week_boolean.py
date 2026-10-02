"""
💡 Boolean 연산자 시각화 (전구 비유)
=====================================
AND, OR, NOT을 전구로 쉽게 이해해보기!

📋 조작법:
   A 키 : 전구 A 토글 (켜기/끄기)
   B 키 : 전구 B 토글
   1,2,3 : 연산자 선택 (1=AND, 2=OR, 3=NOT)
"""

import pygame
import asyncio


# ═══════════════════════════════════════════════════════════════
#  화면 설정
# ═══════════════════════════════════════════════════════════════

SCREEN_W = 800
SCREEN_H = 600
FPS = 60

# 색상
BG = (30, 30, 50)
WHITE = (255, 255, 255)
GRAY = (120, 120, 130)
DARK_GRAY = (60, 60, 70)
YELLOW = (255, 220, 60)
YELLOW_GLOW = (255, 240, 150)
ORANGE = (255, 150, 50)
GREEN = (80, 220, 100)
RED = (230, 80, 90)
CYAN = (100, 200, 240)


# ═══════════════════════════════════════════════════════════════
#  전구 그리기 함수
# ═══════════════════════════════════════════════════════════════

def draw_bulb(screen, x, y, is_on, label):
    """전구 하나 그리기"""
    # 전구 몸체 색상
    if is_on:
        # 켜진 상태: 노란색 + 빛나는 효과
        glow_color = YELLOW_GLOW
        bulb_color = YELLOW
        # 빛 효과 (여러 겹 원)
        for radius in range(80, 50, -10):
            alpha_surface = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
            alpha = 30 if radius > 60 else 50
            pygame.draw.circle(alpha_surface, (255, 240, 100, alpha),
                               (radius, radius), radius)
            screen.blit(alpha_surface, (x - radius, y - radius))
    else:
        # 꺼진 상태: 회색
        bulb_color = DARK_GRAY
        glow_color = GRAY

    # 전구 유리 (큰 원)
    pygame.draw.circle(screen, bulb_color, (x, y), 45)
    pygame.draw.circle(screen, (40, 40, 50), (x, y), 45, 3)

    # 전구 하이라이트 (반짝임)
    if is_on:
        pygame.draw.circle(screen, WHITE, (x - 15, y - 15), 10)

    # 필라멘트 (전구 내부 선)
    if is_on:
        filament_color = ORANGE
    else:
        filament_color = (80, 80, 90)
    pygame.draw.line(screen, filament_color, (x - 15, y + 5), (x - 5, y - 10), 2)
    pygame.draw.line(screen, filament_color, (x - 5, y - 10), (x + 5, y - 10), 2)
    pygame.draw.line(screen, filament_color, (x + 5, y - 10), (x + 15, y + 5), 2)

    # 전구 아래 소켓 (사각형)
    pygame.draw.rect(screen, (100, 100, 110), (x - 20, y + 40, 40, 20))
    pygame.draw.rect(screen, (70, 70, 80), (x - 20, y + 40, 40, 20), 2)

    # 소켓 선
    for i in range(3):
        pygame.draw.line(screen, (70, 70, 80),
                         (x - 20, y + 45 + i*5),
                         (x + 20, y + 45 + i*5), 1)

    # 라벨 (A, B 등)
    font = pygame.font.SysFont("arial", 32, bold=True)
    text = font.render(label, True, WHITE)
    text_rect = text.get_rect(center=(x, y + 90))
    screen.blit(text, text_rect)

    # True/False 표시
    status_text = "True ✓" if is_on else "False ✗"
    status_color = GREEN if is_on else RED
    font_status = pygame.font.SysFont("arial", 20, bold=True)
    status = font_status.render(status_text, True, status_color)
    status_rect = status.get_rect(center=(x, y + 125))
    screen.blit(status, status_rect)


def draw_result_bulb(screen, x, y, is_on, label):
    """결과 전구 (더 크게)"""
    # 빛 효과
    if is_on:
        for radius in range(120, 70, -15):
            alpha_surface = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
            alpha = 20 if radius > 90 else 40
            pygame.draw.circle(alpha_surface, (255, 240, 100, alpha),
                               (radius, radius), radius)
            screen.blit(alpha_surface, (x - radius, y - radius))

    # 전구 색상
    bulb_color = YELLOW if is_on else DARK_GRAY

    # 큰 전구
    pygame.draw.circle(screen, bulb_color, (x, y), 65)
    pygame.draw.circle(screen, (40, 40, 50), (x, y), 65, 4)

    # 하이라이트
    if is_on:
        pygame.draw.circle(screen, WHITE, (x - 22, y - 22), 15)

    # 필라멘트
    filament_color = ORANGE if is_on else (80, 80, 90)
    pygame.draw.line(screen, filament_color, (x - 20, y + 10), (x - 8, y - 15), 3)
    pygame.draw.line(screen, filament_color, (x - 8, y - 15), (x + 8, y - 15), 3)
    pygame.draw.line(screen, filament_color, (x + 8, y - 15), (x + 20, y + 10), 3)

    # 소켓
    pygame.draw.rect(screen, (100, 100, 110), (x - 28, y + 58, 56, 28))
    pygame.draw.rect(screen, (70, 70, 80), (x - 28, y + 58, 56, 28), 2)
    for i in range(4):
        pygame.draw.line(screen, (70, 70, 80),
                         (x - 28, y + 63 + i*6),
                         (x + 28, y + 63 + i*6), 1)

    # 라벨
    font = pygame.font.SysFont("arial", 24, bold=True)
    text = font.render(label, True, CYAN)
    text_rect = text.get_rect(center=(x, y + 115))
    screen.blit(text, text_rect)

    # 결과
    status_text = "True ✓" if is_on else "False ✗"
    status_color = GREEN if is_on else RED
    font_status = pygame.font.SysFont("arial", 26, bold=True)
    status = font_status.render(status_text, True, status_color)
    status_rect = status.get_rect(center=(x, y + 150))
    screen.blit(status, status_rect)


# ═══════════════════════════════════════════════════════════════
#  연산자 계산
# ═══════════════════════════════════════════════════════════════

def calculate(op, a, b):
    """연산자 결과 계산"""
    if op == "AND":
        return a and b
    elif op == "OR":
        return a or b
    elif op == "NOT":
        return not a
    return False


# ═══════════════════════════════════════════════════════════════
#  메인 게임
# ═══════════════════════════════════════════════════════════════

class BoolVisualizer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        pygame.display.set_caption("💡 Boolean 연산자 - 전구 비유")
        self.clock = pygame.time.Clock()

        # 전구 상태
        self.a = True
        self.b = False
        self.operator = "AND"   # AND / OR / NOT

    async def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.a = not self.a
                    elif event.key == pygame.K_b:
                        self.b = not self.b
                    elif event.key == pygame.K_1:
                        self.operator = "AND"
                    elif event.key == pygame.K_2:
                        self.operator = "OR"
                    elif event.key == pygame.K_3:
                        self.operator = "NOT"

            self._draw()
            pygame.display.flip()
            self.clock.tick(FPS)
            await asyncio.sleep(0)

        pygame.quit()

    def _draw(self):
        self.screen.fill(BG)

        # 타이틀
        font_title = pygame.font.SysFont("malgungothic", 32, bold=True)
        title = font_title.render(f"💡 Boolean 연산자: {self.operator}", True, YELLOW)
        title_rect = title.get_rect(center=(SCREEN_W // 2, 40))
        self.screen.blit(title, title_rect)

        # 조작 안내
        font_hint = pygame.font.SysFont("malgungothic", 14)
        hints = [
            "[A] 전구 A 토글   [B] 전구 B 토글",
            "[1] AND   [2] OR   [3] NOT",
        ]
        for i, h in enumerate(hints):
            text = font_hint.render(h, True, GRAY)
            text_rect = text.get_rect(center=(SCREEN_W // 2, 75 + i * 20))
            self.screen.blit(text, text_rect)

        # 입력 전구 그리기
        if self.operator == "NOT":
            # NOT은 A만 사용
            draw_bulb(self.screen, 200, 250, self.a, "A")
        else:
            # AND, OR는 둘 다
            draw_bulb(self.screen, 130, 250, self.a, "A")
            draw_bulb(self.screen, 330, 250, self.b, "B")

        # 연산자 표시 (가운데)
        font_op = pygame.font.SysFont("arial", 48, bold=True)
        if self.operator != "NOT":
            op_text = font_op.render(self.operator, True, CYAN)
            op_rect = op_text.get_rect(center=(230, 250))
            # 배경 박스
            bg_rect = op_rect.inflate(30, 15)
            pygame.draw.rect(self.screen, DARK_GRAY, bg_rect, border_radius=10)
            pygame.draw.rect(self.screen, CYAN, bg_rect, 2, border_radius=10)
            self.screen.blit(op_text, op_rect)
        else:
            op_text = font_op.render("NOT", True, CYAN)
            op_rect = op_text.get_rect(center=(200, 150))
            bg_rect = op_rect.inflate(30, 15)
            pygame.draw.rect(self.screen, DARK_GRAY, bg_rect, border_radius=10)
            pygame.draw.rect(self.screen, CYAN, bg_rect, 2, border_radius=10)
            self.screen.blit(op_text, op_rect)

        # = 표시
        font_eq = pygame.font.SysFont("arial", 50, bold=True)
        eq_text = font_eq.render("=", True, WHITE)
        if self.operator == "NOT":
            eq_rect = eq_text.get_rect(center=(430, 250))
        else:
            eq_rect = eq_text.get_rect(center=(500, 250))
        self.screen.blit(eq_text, eq_rect)

        # 결과 전구 (큰 전구)
        result = calculate(self.operator, self.a, self.b)
        if self.operator == "NOT":
            draw_result_bulb(self.screen, 600, 250, result, f"NOT A")
        else:
            draw_result_bulb(self.screen, 650, 250, result, f"A {self.operator} B")

        # 하단: 코드 표시
        self._draw_code(result)

    def _draw_code(self, result):
        """하단에 Python 코드 표시"""
        box_y = 480
        box_h = 100
        pygame.draw.rect(self.screen, (20, 20, 35),
                         (50, box_y, SCREEN_W - 100, box_h), border_radius=10)
        pygame.draw.rect(self.screen, CYAN,
                         (50, box_y, SCREEN_W - 100, box_h), 2, border_radius=10)

        font_code = pygame.font.SysFont("consolas", 18)

        # 변수 할당
        a_str = "True" if self.a else "False"
        b_str = "True" if self.b else "False"
        result_str = "True" if result else "False"

        if self.operator == "NOT":
            lines = [
                f"A = {a_str}",
                f"not A = {result_str}",
            ]
        else:
            op_py = "and" if self.operator == "AND" else "or"
            lines = [
                f"A = {a_str}      B = {b_str}",
                f"A {op_py} B = {result_str}",
            ]

        for i, line in enumerate(lines):
            color = GREEN if "True" in line.split("=")[-1] else WHITE
            if i == 0:
                color = WHITE
            text = font_code.render(line, True, color)
            self.screen.blit(text, (80, box_y + 15 + i * 35))


# ═══════════════════════════════════════════════════════════════
#  실행!
# ═══════════════════════════════════════════════════════════════

async def main():
    app = BoolVisualizer()
    await app.run()

asyncio.run(main())