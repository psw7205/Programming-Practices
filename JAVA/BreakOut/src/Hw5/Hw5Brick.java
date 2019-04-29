package Hw5;

import java.awt.Color;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.PaintContext;
import java.awt.TexturePaint;

class Hw5Brick extends Hw5Object {

	int x, y, w, h;
	int type = 0;
	Color color = Color.RED;
	public boolean detected = false;
	int collisionX, collisionY;
	GradientPaint gradient;

	Hw5Brick(int _x, int _y, int _w, int _h) {
		x = _x;
		y = _y;
		w = _w;
		h = _h;
	}

	@Override
	void draw(Graphics g) {
		if (!detected) {
			g.setColor(Color.black);
			g.fillRect(x, y, w, h);

			Graphics2D g2 = (Graphics2D) g;
			gradient = new GradientPaint(x / 2, y, color, x / 2, y + h, Color.white, false);
			g2.setPaint(gradient);
			g.fillRect(x + 4, y + 4, w - 8, h - 8);
		}
	}
}
