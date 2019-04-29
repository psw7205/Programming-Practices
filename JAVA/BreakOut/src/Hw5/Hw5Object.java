package Hw5;

import java.awt.Graphics;

abstract class Hw5Object {
	abstract void draw(Graphics g);
	void update(double dt) {};
	void resolveCollision(Hw5Object o) {};
}
