import java.awt.Color;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.Rectangle;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.util.Iterator;
import java.util.LinkedList;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;

class P1 extends JPanel implements MouseListener, MouseMotionListener {
	Point p1 = new Point();
	Point p2 = new Point();
	LinkedList<Point> ar = new LinkedList<>();
	JLabel l = new JLabel("");
	boolean b;

	P1() {
		this.addMouseListener(this);
		this.addMouseMotionListener(this);
		add(l);
	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);

		for (Point p : ar)
			g.fillOval(p.x, p.y, 4, 4);

		l.setText("" + ar.size());

		if (b == true) {
			int x = p1.x;
			int y = p1.y;

			int w = p2.x - p1.x;

			if (w < 0) {
				x = p2.x;
				w = -w;
			}

			int h = p2.y - p1.y;

			if (h < 0) {
				y = p2.y;
				h = -h;
			}

			g.setColor(Color.RED);
			g.drawRect(x, y, w, h);

		}
	}

	@Override
	public void mouseDragged(MouseEvent arg0) {

		if (SwingUtilities.isLeftMouseButton(arg0)) {
			ar.add(new Point(arg0.getX(), arg0.getY()));
		}

		if (SwingUtilities.isRightMouseButton(arg0)) {
			p2.x = arg0.getX();
			p2.y = arg0.getY();
			b = true;
		}

		repaint();
	}

	@Override
	public void mouseMoved(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mousePressed(MouseEvent e) {
		if (SwingUtilities.isLeftMouseButton(e)) {
			ar.add(new Point(e.getX(), e.getY()));
		}

		if (SwingUtilities.isRightMouseButton(e)) {
			p1.x = e.getX();
			p1.y = e.getY();
			p2.x = e.getX();
			p2.y = e.getY();
			b = true;
		}

		repaint();
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		if (SwingUtilities.isRightMouseButton(e)) {
			p2.x = e.getX();
			p2.y = e.getY();

			int x = p1.x;
			int y = p1.y;

			int w = p2.x - p1.x;

			if (w < 0) {
				x = p2.x;
				w = -w;
			}

			int h = p2.y - p1.y;
			
			if (h < 0) {
				y = p2.y;
				h = -h;
			}

			Rectangle rect = new Rectangle();
			rect.setBounds(x, y, w, h);
			Iterator<Point> it = ar.iterator();

			while (it.hasNext()) {
				Point p = it.next();
				if (rect.contains(p))
					it.remove();
			}
			
			repaint();

		}
		b = false;
	}

}

public class Exam1 extends JFrame {
	Exam1() {
		this.setSize(500, 500);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		P1 p = new P1();
		add(p);

		this.setVisible(true);

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		new Exam1();
	}

}
