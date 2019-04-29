import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JFrame;
import javax.swing.JPanel;

class P11 extends JPanel implements KeyListener, Runnable {
	Point p = new Point(0, 0);
	int dx = 0;
	int dy = 0;

	P11() {
		Thread t = new Thread(this);
		t.start();
		setFocusable(true);
		requestFocus();
		this.addKeyListener(this);
	}

	@Override
	protected void paintComponent(Graphics g) {
		// TODO Auto-generated method stub
		super.paintComponent(g);

		g.fillRect(p.x, p.y, 100, 100);
	}

	@Override
	public void keyPressed(KeyEvent e) {

		if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
			dx = 10;
			dy = 0;
		}
		if (e.getKeyCode() == KeyEvent.VK_LEFT) {
			dx = -10;
			dy = 0;
		}
		if (e.getKeyCode() == KeyEvent.VK_UP) {
			dx = 0;
			dy = -10;
		}
		if (e.getKeyCode() == KeyEvent.VK_DOWN) {
			dx = 0;
			dy = 10;
		}
	}

	@Override
	public void keyReleased(KeyEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void keyTyped(KeyEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void run() {
		while (true) {
			try {
				Thread.sleep(50);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

			p.x += dx;
			p.y += dy;

			if (p.x + 100 > this.getWidth() || p.x < 0)
				dx = -dx;

			if (p.y + 100 > this.getHeight() || p.y < 0)
				dy = -dy;

			repaint();
		}
	}

}

public class Exam11 extends JFrame {

	Exam11() {
		this.setSize(600, 600);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);

		add(new P11());

		this.setVisible(true);
	}

	public static void main(String[] args) {
		new Exam11();
	}

}
