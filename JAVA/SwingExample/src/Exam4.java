import java.awt.Color;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.util.LinkedList;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;

class Circle4 {
	Point center;
	double r;
	Color color = Color.RED;

	void draw(Graphics g) {
		g.setColor(color);
		g.fillOval((int) (center.x - r), (int) (center.y - r), (int) (2 * r), (int) (2 * r));
		g.setColor(Color.BLACK);
		g.drawOval((int) (center.x - r), (int) (center.y - r), (int) (2 * r), (int) (2 * r));
	}

	boolean isContain(Point p) {
		double d = Math
				.sqrt((p.x - center.getX()) * (p.x - center.getX()) + (p.y - center.getY()) * (p.y - center.getY()));

		if (d < r)
			return true;
		return false;
	}

}

class P4 extends JPanel implements MouseListener, MouseMotionListener {
	LinkedList<Circle4> list = new LinkedList<>();
	boolean select = false;
	Circle4 prev;
	Point p;

	P4() {
		this.addMouseListener(this);
		this.addMouseMotionListener(this);

	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);

		for (Circle4 i : list) {
			i.draw(g);
		}
	}

	@Override
	public void mouseDragged(MouseEvent arg0) {

		if (SwingUtilities.isLeftMouseButton(arg0)) {
			if (select == true) {
				int x = arg0.getX() - p.x;
				int y = arg0.getY() - p.y;
				
				prev.center.translate(x, y);
				p = arg0.getPoint();
			}

			if (select == false) {
				Point p = list.getLast().center;
				double r = Math
						.sqrt((p.x - arg0.getX()) * (p.x - arg0.getX()) + (p.y - arg0.getY()) * (p.y - arg0.getY()));

				list.getLast().r = r;
			}
		}

		repaint();
	}

	@Override
	public void mouseMoved(MouseEvent arg0) {
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

			for (Circle4 i : list) {
				if (i.isContain(e.getPoint())) {
					select = true;
					prev = i;
					p = new Point(e.getPoint());
					break;
				}
			}

			if (select == true) {
				prev.color = Color.YELLOW;
			}

			if (select == false) {
				Circle4 tmp = new Circle4();
				tmp.center = new Point(e.getPoint());
				tmp.color = Color.RED;
				tmp.r = 0;

				list.add(tmp);
			}
		}
		repaint();
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		if (SwingUtilities.isLeftMouseButton(e)) {
			if (select == true) {
				prev.color = Color.RED;
				select = false;
			}
		}
		repaint();
	}

}

public class Exam4 extends JFrame {
	Exam4() {
		this.setSize(500, 500);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setTitle("");

		P4 p = new P4();

		add(p);

		this.setVisible(true);
	}

	public static void main(String[] args) {
		new Exam4();
	}

}
