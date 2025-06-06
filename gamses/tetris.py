import pygame
import random
import time
import sys

# 初始化pygame
pygame.init()

# 游戏常量
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SIDEBAR_WIDTH = 200

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [
    (0, 0, 0),  # 空
    (80, 80, 255),  # I
    (255, 80, 160),  # J
    (80, 255, 160),  # L
    (255, 160, 80),  # O
    (120, 120, 255),  # S
    (255, 80, 80),  # T
    (80, 200, 255)  # Z
]

# 方块形状定义
SHAPES = [
    [],
    [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]],  # I
    [[2, 0, 0], [2, 2, 2], [0, 0, 0]],  # J
    [[0, 0, 3], [3, 3, 3], [0, 0, 0]],  # L
    [[0, 4, 4], [0, 4, 4], [0, 0, 0]],  # O
    [[0, 5, 5], [5, 5, 0], [0, 0, 0]],  # S
    [[0, 6, 0], [6, 6, 6], [0, 0, 0]],  # T
    [[7, 7, 0], [0, 7, 7], [0, 0, 0]]  # Z
]

# 初始化屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("俄罗斯方块")

# 加载字体
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# 游戏状态


class TetrisGame:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.board = [[0 for _ in range(GRID_WIDTH)]
                      for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False
        self.paused = False
        self.last_fall_time = time.time()
        self.fall_speed = 1.0  # 初始下落速度(秒)

    def new_piece(self):
        shape_type = random.randint(1, 7)
        return {
            'shape': SHAPES[shape_type],
            'color': COLORS[shape_type],
            'x': GRID_WIDTH // 2 - len(SHAPES[shape_type][0]) // 2,
            'y': 0
        }

    def rotate_piece(self):
        if self.paused or self.game_over:
            return

        # 获取当前方块的旋转后形状
        old_shape = self.current_piece['shape']
        new_shape = list(map(list, zip(*old_shape[::-1])))  # 转置并反转

        # 检查旋转是否合法
        if not self.check_collision(new_shape, self.current_piece['x'], self.current_piece['y']):
            self.current_piece['shape'] = new_shape

    def move_piece(self, dx, dy):
        if self.paused or self.game_over:
            return

        new_x = self.current_piece['x'] + dx
        new_y = self.current_piece['y'] + dy

        if not self.check_collision(self.current_piece['shape'], new_x, new_y):
            self.current_piece['x'] = new_x
            self.current_piece['y'] = new_y
            return True

        # 如果是向下移动且发生碰撞，锁定方块
        if dy > 0:
            self.lock_piece()
            self.clear_lines()
            self.current_piece = self.next_piece
            self.next_piece = self.new_piece()

            # 检查游戏是否结束
            if self.check_collision(self.current_piece['shape'], self.current_piece['x'], self.current_piece['y']):
                self.game_over = True

        return False

    def hard_drop(self):
        if self.paused or self.game_over:
            return

        while self.move_piece(0, 1):
            self.score += 2  # 硬下落得分

    def check_collision(self, shape, x, y):
        for row_idx, row in enumerate(shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    if (x + col_idx < 0 or
                        x + col_idx >= GRID_WIDTH or
                            y + row_idx >= GRID_HEIGHT):
                        return True

                    if y + row_idx >= 0 and self.board[y + row_idx][x + col_idx]:
                        return True
        return False

    def lock_piece(self):
        shape = self.current_piece['shape']
        x = self.current_piece['x']
        y = self.current_piece['y']

        for row_idx, row in enumerate(shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    if y + row_idx >= 0:  # 确保在网格内
                        self.board[y + row_idx][x + col_idx] = cell

    def clear_lines(self):
        lines_to_clear = []
        for row_idx, row in enumerate(self.board):
            if all(row):
                lines_to_clear.append(row_idx)

        if lines_to_clear:
            # 计算得分
            line_count = len(lines_to_clear)
            line_points = [0, 100, 300, 500, 800]  # 对应1-4行
            self.score += line_points[line_count] * self.level
            self.lines_cleared += line_count

            # 移除已消除的行并在顶部添加新行
            for line in lines_to_clear:
                del self.board[line]
                self.board.insert(0, [0 for _ in range(GRID_WIDTH)])

            # 更新等级
            self.level = self.lines_cleared // 10 + 1
            self.fall_speed = max(0.1, 1.0 - (self.level - 1) * 0.1)

    def update(self):
        if self.paused or self.game_over:
            return

        current_time = time.time()
        if current_time - self.last_fall_time > self.fall_speed:
            self.move_piece(0, 1)
            self.last_fall_time = current_time

    def toggle_pause(self):
        self.paused = not self.paused

    def draw(self, screen):
        # 绘制背景
        screen.fill(BLACK)

        # 绘制游戏区域边框
        pygame.draw.rect(screen, GRAY,
                         (SCREEN_WIDTH // 2 - GRID_WIDTH * GRID_SIZE // 2 - 2,
                          SCREEN_HEIGHT // 2 - GRID_HEIGHT * GRID_SIZE // 2 - 2,
                          GRID_WIDTH * GRID_SIZE + 4,
                          GRID_HEIGHT * GRID_SIZE + 4), 2)

        # 绘制游戏网格
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                cell_value = self.board[row][col]
                if cell_value:
                    self.draw_block(screen, col, row, COLORS[cell_value])

        # 绘制当前方块
        if self.current_piece:
            shape = self.current_piece['shape']
            for row_idx, row in enumerate(shape):
                for col_idx, cell in enumerate(row):
                    if cell:
                        self.draw_block(screen,
                                        self.current_piece['x'] + col_idx,
                                        self.current_piece['y'] + row_idx,
                                        self.current_piece['color'])

        # 绘制侧边栏
        sidebar_x = SCREEN_WIDTH // 2 + GRID_WIDTH * GRID_SIZE // 2 + 20
        sidebar_y = SCREEN_HEIGHT // 2 - GRID_HEIGHT * GRID_SIZE // 2

        # 绘制分数
        score_text = font.render(f"分数: {self.score}", True, WHITE)
        screen.blit(score_text, (sidebar_x, sidebar_y))

        # 绘制等级
        level_text = font.render(f"等级: {self.level}", True, WHITE)
        screen.blit(level_text, (sidebar_x, sidebar_y + 40))

        # 绘制已消除行数
        lines_text = font.render(f"行数: {self.lines_cleared}", True, WHITE)
        screen.blit(lines_text, (sidebar_x, sidebar_y + 80))

        # 绘制下一个方块预览
        next_text = font.render("下一个:", True, WHITE)
        screen.blit(next_text, (sidebar_x, sidebar_y + 140))

        next_shape = self.next_piece['shape']
        for row_idx, row in enumerate(next_shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    block_x = sidebar_x + col_idx * GRID_SIZE
                    block_y = sidebar_y + 180 + row_idx * GRID_SIZE
                    self.draw_block(screen, block_x, block_y,
                                    self.next_piece['color'], False)

        # 绘制游戏状态
        if self.paused:
            pause_text = font.render("暂停", True, WHITE)
            screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2,
                                     SCREEN_HEIGHT // 2 - pause_text.get_height() // 2))
        elif self.game_over:
            game_over_text = font.render("游戏结束", True, WHITE)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2,
                                         SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2 - 30))

            restart_text = small_font.render("按R键重新开始", True, WHITE)
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2,
                                       SCREEN_HEIGHT // 2 - restart_text.get_height() // 2 + 30))

        # 绘制控制说明
        controls_y = SCREEN_HEIGHT - 120
        controls = [
            "方向键: 移动方块",
            "上键: 旋转方块",
            "空格键: 硬下落",
            "P键: 暂停游戏",
            "R键: 重新开始"
        ]

        for i, control in enumerate(controls):
            control_text = small_font.render(control, True, GRAY)
            screen.blit(control_text, (20, controls_y + i * 25))

    def draw_block(self, screen, x, y, color, use_grid=True):
        if use_grid:
            block_x = SCREEN_WIDTH // 2 - GRID_WIDTH * GRID_SIZE // 2 + x * GRID_SIZE
            block_y = SCREEN_HEIGHT // 2 - GRID_HEIGHT * GRID_SIZE // 2 + y * GRID_SIZE
        else:
            block_x = x
            block_y = y

        # 绘制方块主体
        pygame.draw.rect(
            screen, color, (block_x, block_y, GRID_SIZE, GRID_SIZE))

        # 绘制高光效果
        pygame.draw.line(screen, WHITE, (block_x, block_y),
                         (block_x + GRID_SIZE - 1, block_y), 2)
        pygame.draw.line(screen, WHITE, (block_x, block_y),
                         (block_x, block_y + GRID_SIZE - 1), 2)

        # 绘制阴影效果
        pygame.draw.line(screen, BLACK, (block_x + GRID_SIZE - 1, block_y),
                         (block_x + GRID_SIZE - 1, block_y + GRID_SIZE - 1), 2)
        pygame.draw.line(screen, BLACK, (block_x, block_y + GRID_SIZE - 1),
                         (block_x + GRID_SIZE - 1, block_y + GRID_SIZE - 1), 2)

# 主游戏循环


def main():
    game = TetrisGame()
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move_piece(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    game.move_piece(1, 0)
                elif event.key == pygame.K_DOWN:
                    game.move_piece(0, 1)
                elif event.key == pygame.K_UP:
                    game.rotate_piece()
                elif event.key == pygame.K_SPACE:
                    game.hard_drop()
                elif event.key == pygame.K_p:
                    game.toggle_pause()
                elif event.key == pygame.K_r:
                    game.reset_game()

        game.update()
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
