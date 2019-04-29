import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.util.ArrayList;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;

class Point2 {
	float x, y;

	Point2() {
	}

	Point2(float _x, float _y) {
		x = _x;
		y = _y;
	}

	Point2(Point in) {
		x = in.x;
		y = in.y;
	}
}

class Curve2 {
	ArrayList<Point2> ar = new ArrayList<>();

	void draw(Graphics g, Dimension d) {
		int w = d.width;
		int h = d.height;
		for (int i = 0; i < ar.size() - 1; i++) {
			Point2 p1 = ar.get(i);
			Point2 p2 = ar.get(i + 1);
			g.drawLine((int)( p1.x * w), (int) (p1.y * h), (int) (p2.x * w), (int) (p2.y * h));
		}
	}

	void add(Point2 p) {
		ar.add(p);
	}

}

class P2 extends JPanel implements MouseListener, MouseMotionListener {

	ArrayList<Curve2> ar = new ArrayList<>();
	JLabel l = new JLabel();

	P2() {
		add(l);
		this.addMouseListener(this);
		this.addMouseMotionListener(this);
	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);
		l.setText("" + ar.size());

		Dimension d = getSize();

		g.setColor(Color.BLACK);
		for (Curve2 i : ar)
			i.draw(g, d);
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
			Dimension d = getSize();
			ar.add(new Curve2());
			ar.get(ar.size()-1).add(new Point2(e.getX()/(float)d.width, e.getY()/(float)d.height));
		}

		repaint();
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mouseDragged(MouseEvent e) {
		if (SwingUtilities.isLeftMouseButton(e)) {
			Dimension d = getSize();
			ar.get(ar.size()-1).add(new Point2(e.getX()/(float)d.width, e.getY()/(float)d.height));
		}
		repaint();
	}

	@Override
	public void mouseMoved(MouseEvent e) {
		// TODO Auto-generated method stub

	}

}

public class Exam2 extends JFrame {

	Exam2() {
		this.setSize(500, 500);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		P2 p = new P2();
		add(p);

		this.setVisible(true);
	}

	public static void main(String[] args) {
		new Exam2();
	}
}
