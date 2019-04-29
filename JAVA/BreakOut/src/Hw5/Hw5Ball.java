package Hw5;

import java.awt.Color;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.net.URL;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;

class Hw5Ball extends Hw5Object {
	double x, y, r;
	int vx, vy;
	double prex, prey;
	boolean life = true;
	int stage;
	GradientPaint gradient;
	Clip brickBreak;
	Clip bound;
	Clip side;

	public Hw5Ball(int stage) {
		try {
			URL url = this.getClass().getResource("break.wav");
			AudioInputStream audio = AudioSystem.getAudioInputStream(url);

			brickBreak = AudioSystem.getClip();
			brickBreak.open(audio);

			url = this.getClass().getResource("bound.wav");
			audio = AudioSystem.getAudioInputStream(url);
			bound = AudioSystem.getClip();
			bound.open(audio);

			url = this.getClass().getResource("side.wav");
			audio = AudioSystem.getAudioInputStream(url);
			side = AudioSystem.getClip();
			side.open(audio);

		} catch (Exception e) {
			e.printStackTrace();
		}

		vx = stage * 50;
		vy = stage * 50 + 100;
		x = 400;
		y = 639;
		r = 10;
		vx = (int) (Math.random() * 150);
		vy = (int) (Math.random() * 100) + 200;

	}

	Hw5Ball(int _x, int _y, int stage) {
		this(stage);
		x = _x;
		y = _y;
	}

	@Override
	void draw(Graphics g) {
		gradient = new GradientPaint(0, 0, Color.red, 175, 175, Color.yellow, true);
		Graphics2D g2 = (Graphics2D) g;
		g.setColor(Color.black);
		g.fillOval((int) (x - r - 2), (int) (y - r - 2), (int) (2 * r + 4), (int) (2 * r + 4));
		g2.setPaint(gradient);
		g.fillOval((int) (x - r), (int) (y - r), (int) (2 * r), (int) (2 * r));

	}

	@Override
	void update(double dt) {
		
		prex = x;
		prey = y;
		x += vx * dt;
		y += vy * dt;
	}

	@Override
	void resolveCollision(Hw5Object o) {
		if(x > 850 || x < 0 || y < 0 || y > 850)
		{
			 
			life = false;
			return;
		}
		
		
		if (o instanceof Hw5Brick) {
			Hw5Brick brick = (Hw5Brick) o;
			double x1 = brick.x - r;
			double y1 = brick.y - r;
			double x2 = brick.x + brick.w + r;
			double y2 = brick.y + brick.h + r;

			if (x > x1 && x < x2 && y > y1 && y < y2) {

				if (brick.type == 3) {
					life = false;
					return;
				}

				if (prey < y1) {
					y = y1;
					vy = -vy;
				}
				if (prey > y2) {
					y = y2;
					vy = -vy;
				}
				if (prex < x1) {
					x = x1;
					vx = -vx;
				}
				if (prex > x2) {
					x = x2;
					vx = -vx;
				}

				if (brick.type == 0) {
					side.setFramePosition(0);
					side.start();
				}

				if (brick.type == 4) {
					bound.setFramePosition(0);
					bound.start();
					vx = ((int) (Math.random() * 10) - 5) * 30;
				}

				if (brick.type == 1 || brick.type == 2) {
					brickBreak.setFramePosition(0);
					brickBreak.start();

					if (brick.type == 2) {
						brick.collisionX = (int) x;
						brick.collisionY = (int) y;
					}

					brick.detected = true;
				}

			}

		}
	}

}
