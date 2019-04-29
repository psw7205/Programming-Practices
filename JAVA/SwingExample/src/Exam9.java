import java.awt.Color;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JPanel;

class P9 extends JPanel implements Runnable {
	Point p = new Point();
	int dt = 1;
	int r = 1;
	Color color;
	
	P9() {
		Thread t = new Thread(this);
		t.start();
		this.addMouseMotionListener(new MouseAdapter() {
			@Override
			public void mouseMoved(MouseEvent e) {
				super.mouseMoved(e);

				p = e.getPoint();
			}

		});
	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);
		
		g.setColor(color);
		g.fillOval(p.x-r, p.y-r, 2*r, 2*r);
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
			
			color = new Color(r*5, r*5, r*5);
			
			if (r > 25 || r < 1)
				dt = -dt;

			r += dt;

			repaint();
		}
	}
}

public class Exam9 extends JFrame {
	
	public Exam9() {
	this.setSize(600,600);
	this.setDefaultCloseOperation(EXIT_ON_CLOSE);
	
	P9 p = new P9();
	add(p);
	
	this.setVisible(true);
	}
	
	public static void main(String[] args) {
		new Exam9();
	}

}
