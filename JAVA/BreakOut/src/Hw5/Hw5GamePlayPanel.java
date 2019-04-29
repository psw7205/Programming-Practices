package Hw5;

import java.awt.Color;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.net.URL;
import java.util.Iterator;
import java.util.LinkedList;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.swing.JPanel;

class Hw5GamePlayPanel extends JPanel implements KeyListener, Runnable {
	Hw5Panel parent;
	boolean play = false;
	int score = 0;
	int ballCnt = 1;
	int stage = 1;
	int brickCnt;
	static final double dt = 0.017;

	Clip gameOver;

	Hw5Paddle paddle = new Hw5Paddle();

	LinkedList<Hw5Object> list = new LinkedList<>();

	Hw5GamePlayPanel() {

		try {
			URL url = this.getClass().getResource("GameOver.wav");
			AudioInputStream audio = AudioSystem.getAudioInputStream(url);
			gameOver = AudioSystem.getClip();
			gameOver.open(audio);

		} catch (Exception e) {
			e.printStackTrace();
		}

		addKeyListener(this);
		requestFocus();
		setFocusable(true);
		Thread t = new Thread(this);
		t.start();
	}

	boolean isGameOver() {
		if (ballCnt > 0)
			return false;
		return true;
	}

	void init() {
		stage = 1;
		score = 0;
		initStage();
		list.add(paddle);
		list.add(new Hw5Brick(0, -100, 1000, 100));
		list.add(new Hw5Brick(-100, 0, 100, 1000));
		list.add(new Hw5Brick(790, 0, 100, 1000));
		Hw5Brick b = new Hw5Brick(0, 800, 1000, 100);
		b.type = 3;
		list.add(b);
	}

	void initStage() {
		Iterator<Hw5Object> it = list.iterator();
		while (it.hasNext()) {
			Hw5Object o = it.next();
			if (o instanceof Hw5Ball) {
				it.remove();
			}
		}

		list.add(new Hw5Ball(stage));
		ballCnt = 1;
		paddle.x = 325;
		paddle.y = 650;
		paddle.move = 0;

		int offset = 20;
		int div = stage + 2;
		int dw = 700 / div;
		int dh = 300 / div;
		int initX = (int) ((800 - (dw + offset) * div) / 2);

		brickCnt = div * div;

		for (int i = 0; i < div; ++i) {
			for (int j = 0; j < div; ++j) {
				int dx = initX + (dw + offset) * i;
				int dy = offset + (dh + offset) * j;

				Hw5Brick b = new Hw5Brick(dx, dy, dw, dh);

				int tmp = (int) (Math.random() * 10);

				if (tmp % 4 == 0)
					b.type = 2;
				else
					b.type = 1;

				if (b.type == 2)
					b.color = Color.YELLOW;

				list.add(b);
			}
		}

	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);

		Graphics2D g2 = (Graphics2D) g;
		g2.setPaint(new GradientPaint(0.0f, 0.0f, Color.darkGray, 0.0f, getHeight(), Color.gray));
		g2.fillRect(0, 0, getWidth(), getHeight());

		int cx = 0, cy = 0;
		boolean multi = false;

		for (Hw5Object o : list)
			if (o instanceof Hw5Ball)
				for (Hw5Object b : list)
					o.resolveCollision(b);

		for (Hw5Object o : list) {
			if (o instanceof Hw5Ball)
				o.update(dt * 2);
		}

		paddle.update(dt);

		Iterator<Hw5Object> it = list.iterator();
		while (it.hasNext()) {
			Hw5Object o = it.next();
			if (o instanceof Hw5Ball) {
				Hw5Ball b = (Hw5Ball) o;
				if (!b.life) {
					it.remove();
					ballCnt--;
				}
			}

			if (o instanceof Hw5Brick) {
				Hw5Brick b = (Hw5Brick) o;
				if (b.detected) {
					it.remove();
					score += 100;
					brickCnt--;

					if (b.type == 2) {
						cx = b.collisionX;
						cy = b.collisionY;
						multi = true;
					}
				}
			}
			o.draw(g);
		}

		if (multi) {
			list.add(new Hw5Ball(cx, cy, stage));
			list.add(new Hw5Ball(cx, cy, stage));
			ballCnt += 2;
		}

		if (isGameOver()) {
			it = list.iterator();
			while (it.hasNext()) {
				Hw5Object o = it.next();
				if (o instanceof Hw5Brick) {
					it.remove();
				}
			}

			gameOver.setFramePosition(0);
			gameOver.start();

			parent.requestFocus();
			parent.setFocusable(true);
			parent.end.score = score;
			parent.idx = 2;
			parent.card.show(parent, "end");
		}

		if (brickCnt == 0) {
			stage++;
			initStage();
		}
	}

	@Override
	public void keyTyped(KeyEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void keyPressed(KeyEvent e) {

		if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
			paddle.move = 300;
		}

		if (e.getKeyCode() == KeyEvent.VK_LEFT) {
			paddle.move = -300;
		}

		repaint();
	}

	@Override
	public void keyReleased(KeyEvent e) {
		if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
			paddle.move = 0;
		}

		if (e.getKeyCode() == KeyEvent.VK_LEFT) {
			paddle.move = 0;
		}
	}

	@Override
	public void run() {
		while (true) {

			try {
				Thread.sleep((int) (dt * 1000));
			} catch (InterruptedException e) {
				e.printStackTrace();
			}

			repaint();
		}
	}

}
