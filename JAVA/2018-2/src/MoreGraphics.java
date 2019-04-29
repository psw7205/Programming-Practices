import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.util.ArrayList;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

abstract class MoreGraphicsShape {

	Color c;

	MoreGraphicsShape() {
		int r = (int) (Math.random() * 255);
		int g = (int) (Math.random() * 255);
		int b = (int) (Math.random() * 255);
		c = new Color(r, g, b);
	}

	void draw(Graphics g) {
		g.setColor(c);
	}

	abstract void setStartPoint(Point p);

	abstract void setEndPoint(Point p);
}

class MoreGraphicsLine extends MoreGraphicsShape {
	Point st = new Point();
	Point ed = new Point();

	@Override
	void draw(Graphics g) {
		super.draw(g);
		g.drawLine(st.x, st.y, ed.x, ed.y);
	}

	@Override
	void setStartPoint(Point p) {
		st = p;
	}

	@Override
	void setEndPoint(Point p) {
		ed = p;
	}
}

class MoreGraphicsRect extends MoreGraphicsShape {
	Point st = new Point();
	int w, h;

	@Override
	void draw(Graphics g) {
		super.draw(g);
		g.fillRect(st.x, st.y, w, h);
	}

	@Override
	void setStartPoint(Point p) {
		st = p;
	}

	@Override
	void setEndPoint(Point p) {
		w = p.x - st.x;
		h = p.y - st.y;
	}
}

class MoreGraphicsCircle extends MoreGraphicsShape {
	Point center = new Point();
	double radius;

	@Override
	void draw(Graphics g) {
		super.draw(g);
		g.fillOval(center.x - (int) radius, center.y - (int) radius, (int) radius * 2, (int) radius * 2);
	}

	@Override
	void setStartPoint(Point p) {
		center = p;
	}

	@Override
	void setEndPoint(Point p) {
		radius = Math.sqrt((p.x - center.x) * (p.x - center.x) + (p.y - center.y) * (p.y - center.y));
	}
}

class MoreGraphicsPanel extends JPanel implements MouseListener, MouseMotionListener {

	static final int LINE = 0;
	static final int RECT = 1;
	static final int CIRCLE = 2;

	// ArrayList<Point> sts = new ArrayList<>();
	// ArrayList<Point> eds = new ArrayList<>();

	int drawMode = LINE;
	ArrayList<MoreGraphicsShape> shapes = new ArrayList<>();

	MoreGraphicsPanel() {
		this.addMouseListener(this); // 마우스리스너를 등록
		this.addMouseMotionListener(this);
	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);

		/*
		 * for (int i = 0; i < sts.size(); i++) { Point st = sts.get(i); Point ed =
		 * eds.get(i); g.drawRect(st.x, st.y, ed.x - st.x, ed.y - st.y);
		 * g.drawOval(st.x, st.y, ed.x - st.x, ed.y - st.y); g.drawLine(st.x, st.y,
		 * ed.x, ed.y); }
		 */

		for (MoreGraphicsShape s : shapes) {
			s.draw(g);
		}
	}

	@Override
	public void mouseDragged(MouseEvent arg0) {
		/*
		 * Point tmp = eds.get(eds.size() - 1); tmp.x = arg0.getX(); tmp.y =
		 * arg0.getY(); this.repaint();
		 */

		shapes.get(shapes.size() - 1).setEndPoint(arg0.getPoint());
		this.repaint();
	}

	@Override
	public void mouseMoved(MouseEvent arg0) {

	}

	@Override
	public void mouseClicked(MouseEvent arg0) {

	}

	@Override
	public void mouseEntered(MouseEvent arg0) {

	}

	@Override
	public void mouseExited(MouseEvent arg0) {

	}

	@Override
	public void mousePressed(MouseEvent arg0) {
		/*
		 * Point p1 = new Point(); Point p2 = new Point(); p1.x = arg0.getX(); p1.y =
		 * arg0.getY(); p2.x = arg0.getX(); p2.y = arg0.getY();
		 * 
		 * sts.add(p1); eds.add(p2);
		 */

		MoreGraphicsShape s;
		switch (drawMode) {
		case LINE:
			s = new MoreGraphicsLine();
			break;
		case RECT:
			s = new MoreGraphicsRect();
			break;
		case CIRCLE:
			s = new MoreGraphicsCircle();
			break;
		default:
			return;
		}

		s.setStartPoint(arg0.getPoint());
		shapes.add(s);
	}

	@Override
	public void mouseReleased(MouseEvent arg0) {
		/*
		 * Point tmp = eds.get(eds.size() - 1); tmp.x = arg0.getX(); tmp.y =
		 * arg0.getY();
		 * 
		 * this.repaint();
		 */

		shapes.get(shapes.size() - 1).setEndPoint(arg0.getPoint());
		this.repaint();
	}
}

class MoreGraphicsMenuPanel extends JPanel implements ActionListener {
	MoreGraphicsPanel gPanel;
	JButton button1, button2, button3;

	MoreGraphicsMenuPanel() {
		button1 = new JButton("Line");
		button2 = new JButton("Rect");
		button3 = new JButton("Circle");
		button1.addActionListener(this);
		button2.addActionListener(this);
		button3.addActionListener(this);
		add(button1);
		add(button2);
		add(button3);
	}

	@Override
	public void actionPerformed(ActionEvent arg0) {
		if (arg0.getSource() == button1)
			gPanel.drawMode = MoreGraphicsPanel.LINE;

		if (arg0.getSource() == button2)
			gPanel.drawMode = MoreGraphicsPanel.RECT;

		if (arg0.getSource() == button3)
			gPanel.drawMode = MoreGraphicsPanel.CIRCLE;
	}
}

public class MoreGraphics extends JFrame {
	MoreGraphics() {
		setTitle("MoreGraphics Practice");
		setSize(500, 500);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		MoreGraphicsPanel p = new MoreGraphicsPanel();
		add(p);

		MoreGraphicsMenuPanel m = new MoreGraphicsMenuPanel();
		m.gPanel = p;
		add(m, BorderLayout.NORTH);

		setVisible(true);
	}

	public static void main(String[] args) {
		new MoreGraphics();
	}

}
