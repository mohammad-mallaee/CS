import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Arrays;
import java.util.Random;

public class GamePanel extends JPanel implements ActionListener {
    static final int SCREEN_WIDTH = 1024;
    static final int SCREEN_HEIGHT = 728;
    static final int UNIT_SIZE = 20;
    static final  int PADDING = 2;
    static final int GAME_UNITS = (SCREEN_WIDTH*SCREEN_HEIGHT)/UNIT_SIZE;
    static final int delay = 75;
    final int[] x = new int[GAME_UNITS];
    final int[] y = new int[GAME_UNITS];
    int bodyParts = 6;
    int applesEaten = 0;
    int appleX = 0;
    int appleY = 0;
    char direction = 'R';
    boolean running = false;
    Timer timer;
    Random random;
    GamePanel () {
        random = new Random();
        this.setPreferredSize(new Dimension(SCREEN_WIDTH, SCREEN_HEIGHT));
        this.setBackground(new Color(15, 15, 15));
        this.setFocusable(true);
        this.addKeyListener(new MyKeyAdapter());
        startGame();
    }

    public void startGame() {
        newApple();
        running = true;
        timer = new Timer(delay, this);
        timer.start();
    }

    public void restartGame () {
        bodyParts = 6;
        applesEaten = 0;
        direction = 'R';
        Arrays.fill(x, 0);
        Arrays.fill(y, 0);
        running = true;
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        draw(g);
    }

    public void draw(Graphics g) {
        g.setColor(new Color(70, 200, 255));
        g.setFont(new Font("Ink Free", Font.BOLD, 22));
        FontMetrics metrics = getFontMetrics(g.getFont());
        String scoreString = "Score: " + applesEaten;
        g.drawString(scoreString, (SCREEN_WIDTH - metrics.stringWidth(scoreString))/2, g.getFont().getSize() + 5);

        if (running) {
            g.setColor(new Color(250, 250, 250));
            g.fillRect(appleX - PADDING / 2, appleY - PADDING / 2, UNIT_SIZE - PADDING, UNIT_SIZE - PADDING);

            for (int i = 0; i < bodyParts; i++) {
                g.setColor(Color.white);
                if (i == 0)
                    g.setColor(new Color(150, 150, 150));
                g.fillRect(x[i] - PADDING / 2, y[i] - PADDING / 2, UNIT_SIZE - PADDING, UNIT_SIZE - PADDING);
            }
        } else {
            gameOver(g);
        }
    }

    public void newApple() {
        appleX = random.nextInt(SCREEN_WIDTH / UNIT_SIZE) * UNIT_SIZE;
        appleY = random.nextInt(SCREEN_HEIGHT / UNIT_SIZE) * UNIT_SIZE;
        for (int i = 0; i < bodyParts; i++) {
            if (appleX == x[i] && appleY == y[i]) {
                newApple();
            }
        }
    }

    public void move() {
        for(int i = bodyParts; i > 0; i--) {
            x[i] = x[i - 1];
            y[i] = y[i - 1];
        }

        switch (direction) {
            case 'U':
                y[0] = y[0] - UNIT_SIZE;
                break;
            case 'D':
                y[0] = y[0] + UNIT_SIZE;
                break;
            case 'L':
                x[0] = x[0] - UNIT_SIZE;
                break;
            case 'R':
                x[0] = x[0] + UNIT_SIZE;
                break;
        }
    }

    public void checkApple() {
        if ((x[0] == appleX) && (y[0] == appleY)) {
            bodyParts++;
            applesEaten++;
            newApple();
        }
    }

    public void checkCollisions()  {
        for (int i = bodyParts; i > 0; i--) {
            if ((x[0] == x[i]) && (y[0] == y[i])) {
                running = false;
                break;
            }
        }
        if (x[0] < -PADDING || x[0] > SCREEN_WIDTH - PADDING) {
            running = false;
        }
        if (y[0] < -PADDING || y[0] > SCREEN_HEIGHT - PADDING) {
            running = false;
        }
    }

    public void gameOver(Graphics g) {
        g.setColor(Color.red);
        g.setFont(new Font("Ink Free", Font.BOLD, 75));
        FontMetrics metrics = getFontMetrics(g.getFont());
        g.drawString("Game Over", (SCREEN_WIDTH - metrics.stringWidth("Game Over"))/2, SCREEN_HEIGHT/2);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (running) {
            move();
            checkApple();
            checkCollisions();
        }
        repaint();
    }

    static long startKeyPressTime = System.nanoTime();
    public class MyKeyAdapter extends KeyAdapter {
        @Override
        public void keyPressed(KeyEvent e) {
            long distanceTimeBetweenKeysInMs = (System.nanoTime() - startKeyPressTime) / 1000 / 1000;
            if (distanceTimeBetweenKeysInMs < delay) {
                return;
            }
            startKeyPressTime = System.nanoTime();

            switch (e.getKeyCode()) {
                case KeyEvent.VK_LEFT:
                    direction = direction == 'R' ? 'R' : 'L';
                    break;
                case KeyEvent.VK_RIGHT:
                    direction = direction == 'L' ? 'L' : 'R';
                    break;
                case KeyEvent.VK_UP:
                    direction = direction == 'D' ? 'D' : 'U';
                    break;
                case KeyEvent.VK_DOWN:
                    direction = direction == 'U' ? 'U' : 'D';
                    break;
                case KeyEvent.VK_ENTER:
                    restartGame();
                    break;
            }
        }
    }
}
