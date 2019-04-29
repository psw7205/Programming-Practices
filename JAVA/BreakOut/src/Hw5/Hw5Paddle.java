package Hw5;

import java.awt.Color;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;

class Hw5Paddle extends Hw5Brick {
	public int move;
	
	Hw5Paddle() {
		super(325, 650, 150, 20);
		type = 4;
	}

	@Override
	void draw(Graphics g) {
		gradient = new GradientPaint(400, 650, Color.white, 400, 670, Color.black, true);
		Graphics2D g2 = (Graphics2D) g;
		g2.setPaint(gradient);
		
		g.fillRoundRect(x, y, w, h, 10, 10);
		g.setColor(Color.black);
		g.fillRoundRect(x+2, y+2, w-4, h-4, 10, 10);
	}

	@Override
	void update(double dt) {
		x += move * dt;

		if (x < 0)
			x = 0;

		if (x + w > 780)
			x = 785  -   w;
		
	}
}
