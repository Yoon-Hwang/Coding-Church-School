import pygame
import math

# ============================================
# 1주차: 기본 설정 및 연산자
# ============================================

# Pygame 초기화
pygame.init()

# 화면 크기 설정 (산술 연산자 사용)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("아브라함과 이삭 이야기")

# 색상 정의 (튜플 사용)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
SKY_BLUE = (135, 206, 235)
BROWN = (139, 69, 19)

# 시계 설정 (FPS 조절용)
clock = pygame.time.Clock()

# ============================================
# 이미지 로드 함수 (학생들이 직접 치지 않을 부분)
# ============================================
import os


def load_images():
    """이미지를 불러오는 함수"""
    #base_path = os.path.join(os.path.dirname(__file__), "images")
    try:
        abraham ="이미지-세종꿈의교회-아브라함 이미지의 '복사'-붙여넣기"
        isaac = ""
        angel = ""
        sheep = ""
        altar = ""
        bush = ""
        abraham = pygame.image.load(abraham)
        isaac = pygame.image.load(isaac)
        angel = pygame.image.load(angel)
        sheep = pygame.image.load(sheep)
        altar = pygame.image.load(altar)  # 번제단
        bush = pygame.image.load(bush)    # 수풀
        
        # 이미지 크기 조절 (산술 연산자 활용)
        abraham = pygame.transform.scale(abraham, (100, 150))
        isaac = pygame.transform.scale(isaac, (80, 120))
        angel = pygame.transform.scale(angel, (120, 120))
        sheep = pygame.transform.scale(sheep, (60, 60))
        altar = pygame.transform.scale(altar, (150, 120))   # 번제단 크기
        bush = pygame.transform.scale(bush, (120, 100))     # 수풀 크기
        
        return abraham, isaac, angel, sheep, altar, bush

    except Exception as e:
        print(f"이미지 로드 실패: {e}")
        # 이미지가 없을 경우 기본 사각형 반환
        abraham = pygame.Surface((100, 150))
        abraham.fill((100, 50, 0))
        isaac = pygame.Surface((80, 120))
        isaac.fill((150, 100, 50))
        angel = pygame.Surface((120, 120))
        angel.fill((255, 255, 200))
        sheep = pygame.Surface((60, 60))
        sheep.fill((200, 200, 200))
        altar = pygame.Surface((150, 120))
        altar.fill((80, 80, 80))  # 회색 (돌)
        bush = pygame.Surface((120, 100))
        bush.fill((34, 139, 34))  # 초록색
        return abraham, isaac, angel, sheep, altar, bush

# 이미지 불러오기
abraham_img, isaac_img, angel_img, sheep_img, altar_img, bush_img = load_images()

# ============================================
# 위치 상수 정의 (산술 연산자 사용)
# ============================================
# 번제단 위치 (화면 중앙)
ALTAR_X = 325
ALTAR_Y = 330

# 수풀 위치 (화면 오른쪽)
BUSH_X = 600
BUSH_Y = 350

# 아브라함 기본 위치 (번제단 왼쪽)
ABRAHAM_X = 150
ABRAHAM_Y = 300

# 이삭 기본 위치 (아브라함 옆)
ISAAC_BESIDE_X = ABRAHAM_X + 120  # 산술 연산자: 아브라함 옆
ISAAC_BESIDE_Y = 330

# 이삭이 번제단 위에 있을 때 위치
ISAAC_ON_ALTAR_X = ALTAR_X + 10  # 산술 연산자: 번제단 중앙
ISAAC_ON_ALTAR_Y = ALTAR_Y - 30  # 산술 연산자: 번제단 위

# 양이 수풀에서 나올 때 위치
SHEEP_IN_BUSH_X = BUSH_X + 20
SHEEP_IN_BUSH_Y = BUSH_Y + 10

# 양이 번제단으로 갈 때 위치
SHEEP_ON_ALTAR_X = ALTAR_X + 40
SHEEP_ON_ALTAR_Y = ALTAR_Y - 20

# ============================================
# 텍스트 출력 함수 (학생들이 직접 치지 않을 부분)
# ============================================
def draw_text(text, x, y, size=30, color=BLACK):
    """화면에 텍스트를 그리는 함수 (한글 지원)"""
    # 한글 폰트 사용 (Windows 기준)
    try:
        # Windows: 맑은 고딕
        font = pygame.font.SysFont('malgungothic', size)
    except:
        try:
            # Mac: Apple SD Gothic Neo
            font = pygame.font.SysFont('applegothic', size)
        except:
            # 그래도 안 되면 기본 폰트 (영어만 가능)
            font = pygame.font.Font(None, size)
    
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# ============================================
# 별 그리기 함수 (for 반복문 + 산술 연산자)
# ============================================
def draw_stars(center_x, center_y, num_stars, radius, angle_offset):
    """
    원형으로 별을 그리는 함수
    - center_x, center_y: 중심 좌표
    - num_stars: 별의 개수
    - radius: 반지름
    - angle_offset: 회전 각도
    """
    # 2주차: for 반복문 배우기
    for i in range(num_stars):
        # 산술 연산자: 각도 계산
        angle = (360 / num_stars) * i + angle_offset
        # 산술 연산자: 라디안 변환
        radian = angle * (math.pi / 180)
        
        # 산술 연산자: x, y 좌표 계산
        star_x = center_x + radius * math.cos(radian)
        star_y = center_y + radius * math.sin(radian)
        
        # 별 그리기 (노란색 원)
        pygame.draw.circle(screen, YELLOW, (int(star_x), int(star_y)), 5)

# ============================================
# 메인 게임 로직
# ============================================

# 게임 상태 변수
scene = 1  # 현재 장면 번호
running = True
star_angle = 0  # 별의 회전 각도
star_radius = 50  # 별의 초기 반지름

# 2주차: while 반복문으로 게임 루프 만들기
while running:
    # 배경색 채우기
    screen.fill(SKY_BLUE)
    
    # 땅 그리기
    pygame.draw.rect(screen, BROWN, (0, 450, SCREEN_WIDTH, 150))
    
    # ============================================
    # 배경 요소 그리기 (번제단, 수풀은 항상 표시)
    # ============================================
    screen.blit(altar_img, (ALTAR_X, ALTAR_Y))  # 번제단
    screen.blit(bush_img, (BUSH_X, BUSH_Y))     # 수풀
    
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 3주차: if문으로 키 입력 처리
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # 스페이스바를 누르면
                # 산술 연산자: 장면 번호 증가
                scene = scene + 1
                
                # 관계 연산자: 장면이 마지막을 넘어가면 처음으로
                if scene > 7:  # 장면이 7개로 늘어남
                    scene = 1
    
    # ============================================
    # 3주차: if문으로 장면 전환하기
    # ============================================
    
    # 장면 1: 이삭이 질문
    if scene == 1:
        screen.blit(abraham_img, (ABRAHAM_X, ABRAHAM_Y))
        screen.blit(isaac_img, (ISAAC_BESIDE_X, ISAAC_BESIDE_Y))
        draw_text("이삭: 번제할 어린 양은 어디 있나이까?", 120, 50, 35, BLACK)
        draw_text("[스페이스바를 눌러 계속하기]", 250, 550, 25, WHITE)
    
    # 장면 2: 아브라함이 이삭을 번제단으로 데려감
    elif scene == 2:
        screen.blit(abraham_img, (ABRAHAM_X, ABRAHAM_Y))
        screen.blit(isaac_img, (ISAAC_ON_ALTAR_X, ISAAC_ON_ALTAR_Y))  # 이삭을 번제단 위로
        draw_text("아브라함이 이삭을 제단에 눕히고...", 180, 50, 35, BLACK)
        draw_text("[스페이스바]", 350, 550, 25, WHITE)
    
    # 장면 3: 이삭의 외침
    elif scene == 3:
        screen.blit(abraham_img, (ABRAHAM_X, ABRAHAM_Y))
        screen.blit(isaac_img, (ISAAC_ON_ALTAR_X, ISAAC_ON_ALTAR_Y))
        draw_text("이삭: 앗, 아버지!", 300, 100, 40, (255, 0, 0))
        draw_text("[스페이스바]", 350, 550, 25, WHITE)
    
    # 장면 4: 천사 등장
    elif scene == 4:
        screen.blit(abraham_img, (ABRAHAM_X, ABRAHAM_Y))
        screen.blit(isaac_img, (ISAAC_ON_ALTAR_X, ISAAC_ON_ALTAR_Y))
        screen.blit(angel_img, (500, 200))
        draw_text("천사: 아브라함아! 그 아이에게 손을 대지 말라!", 80, 50, 32, (255, 100, 0))
        draw_text("[스페이스바]", 350, 550, 25, WHITE)
    
    # 장면 5: 천사의 축복 (별 애니메이션)
    elif scene == 5:
        screen.blit(abraham_img, (ABRAHAM_X, ABRAHAM_Y))
        screen.blit(isaac_img, (ISAAC_ON_ALTAR_X, ISAAC_ON_ALTAR_Y))
        screen.blit(angel_img, (500, 150))
        
        draw_text("천사: 네가 하나님을 경외하는 줄 아노라!", 150, 30, 32, (255, 100, 0))
        draw_text("네 자손이 하늘의 별처럼", 230, 70, 32, (255, 100, 0))
        draw_text("많아질 것이니라!", 280, 110, 32, (255, 100, 0))
        
        # 2주차: for 반복문으로 여러 개의 별 그리기
        # 3개의 원형 패턴으로 별 그리기
        for circle_num in range(3):
            # 산술 연산자: 반지름 계산
            current_radius = star_radius + (circle_num * 60)
            # 산술 연산자: 별 개수 계산
            num_stars = 8 + (circle_num * 4)
            
            # 별 그리기 함수 호출
            draw_stars(550, 200, num_stars, current_radius, star_angle + (circle_num * 30))
        
        # 산술 연산자: 별 회전 각도 증가
        star_angle = star_angle + 2
        
        # 관계 연산자: 각도가 360도를 넘으면 0으로 리셋
        if star_angle >= 360:
            star_angle = 0
        
        # 산술 연산자: 별 반지름 증가
        star_radius = star_radius + 0.5
        
        # 관계 연산자: 반지름이 너무 커지면 리셋
        if star_radius > 100:
            star_radius = 50
        
        draw_text("[스페이스바]", 350, 550, 25, WHITE)
    
    # 장면 6: 양이 수풀에서 뿅! 나타남
    elif scene == 6:
        screen.blit(abraham_img, (ABRAHAM_X, ABRAHAM_Y))
        screen.blit(isaac_img, (ISAAC_ON_ALTAR_X, ISAAC_ON_ALTAR_Y))
        screen.blit(sheep_img, (SHEEP_IN_BUSH_X, SHEEP_IN_BUSH_Y))  # 양이 수풀 위에!
        draw_text("수풀에서 숫양이 나타났다!", 250, 50, 40, (0, 150, 0))
        draw_text("[스페이스바]", 350, 550, 25, WHITE)
    
    # 장면 7: 양이 번제단으로, 이삭은 아브라함 옆으로
    elif scene == 7:
        screen.blit(abraham_img, (ABRAHAM_X, ABRAHAM_Y))
        screen.blit(isaac_img, (ISAAC_BESIDE_X, ISAAC_BESIDE_Y))  # 이삭 다시 옆으로
        screen.blit(sheep_img, (SHEEP_ON_ALTAR_X, SHEEP_ON_ALTAR_Y))  # 양이 번제단 위로
        draw_text("하나님께서 준비하셨도다!", 220, 50, 40, (0, 150, 0))
        draw_text("이삭 대신 숫양을 번제로 드렸습니다!", 170, 100, 35, (0, 150, 0))
        draw_text("[스페이스바를 눌러 처음으로]", 250, 550, 25, WHITE)
    
    # 화면 업데이트
    pygame.display.flip()
    
    # FPS 설정 (60fps)
    clock.tick(60)

# 게임 종료
pygame.quit()